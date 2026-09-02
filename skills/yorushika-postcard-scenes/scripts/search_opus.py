#!/usr/bin/env python3
"""Recall diverse bilingual lyric candidates from the bundled opus.md.

This script performs literal full-corpus retrieval only.  It deliberately does
not choose the final lyric or infer emotion; the calling skill reranks the
returned candidates against the actual MV artwork.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


ALBUM_RE = re.compile(r"^## ■ (.+?)\s*$")
SONG_RE = re.compile(r"^### ◆ (.+?)\s*$")
TRANSLATOR_RE = re.compile(r"^\*译：(.+?)\*\s*$")
JAPANESE_RE = re.compile(r"^\*\*(.+)\*\*\s*$")
CHINESE_RE = re.compile(r"^>\s?(.*)$")


@dataclass(frozen=True)
class Pair:
    ja: str
    zh: str
    ja_line: int
    zh_line: int


@dataclass
class Entry:
    release_group: str
    title: str
    translator: str | None
    line: int
    ordinal: int
    pairs: list[Pair] = field(default_factory=list)


def normalize(text: str) -> str:
    return unicodedata.normalize("NFKC", text).casefold()


def stable_key(*parts: str) -> str:
    payload = "\u241f".join(parts).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def parse_counts(raw: str) -> list[int]:
    counts: list[int] = []
    for value in raw.split(","):
        value = value.strip()
        if not value:
            continue
        count = int(value)
        if count < 1 or count > 4:
            raise argparse.ArgumentTypeError("--counts values must be between 1 and 4")
        if count not in counts:
            counts.append(count)
    if not counts:
        raise argparse.ArgumentTypeError("--counts must contain at least one value")
    return counts


def clean_terms(values: Iterable[str]) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for value in values:
        for term in value.split("|"):
            term = term.strip()
            normalized = normalize(term)
            if term and normalized not in seen:
                seen.add(normalized)
                result.append(term)
    return result


def parse_corpus(path: Path) -> tuple[list[str], list[Entry]]:
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    entries: list[Entry] = []
    current_group = ""
    current_entry: Entry | None = None
    index = 0

    while index < len(lines):
        line = lines[index]
        line_number = index + 1

        album_match = ALBUM_RE.match(line)
        if album_match:
            current_group = album_match.group(1).strip()
            current_entry = None
            index += 1
            continue

        song_match = SONG_RE.match(line)
        if song_match:
            current_entry = Entry(
                release_group=current_group,
                title=song_match.group(1).strip(),
                translator=None,
                line=line_number,
                ordinal=len(entries),
            )
            entries.append(current_entry)
            index += 1
            continue

        if current_entry is not None:
            translator_match = TRANSLATOR_RE.match(line)
            if translator_match:
                current_entry.translator = translator_match.group(1).strip()
                index += 1
                continue

            japanese_match = JAPANESE_RE.match(line)
            if japanese_match:
                next_index = index + 1
                while next_index < len(lines) and not lines[next_index].strip():
                    next_index += 1
                if next_index < len(lines):
                    chinese_match = CHINESE_RE.match(lines[next_index])
                    if chinese_match:
                        current_entry.pairs.append(
                            Pair(
                                ja=japanese_match.group(1),
                                zh=chinese_match.group(1),
                                ja_line=line_number,
                                zh_line=next_index + 1,
                            )
                        )
                        index = next_index + 1
                        continue

        index += 1

    return lines, entries


def score_window(
    pairs: list[Pair],
    term_groups: dict[str, list[str]],
) -> tuple[int, dict[str, list[str]]]:
    text = normalize("\n".join(item for pair in pairs for item in (pair.ja, pair.zh)))
    weights = {"motif": 1, "relation": 2, "affect": 2}
    matched: dict[str, list[str]] = {name: [] for name in term_groups}
    score = 0

    for name, terms in term_groups.items():
        for term in terms:
            normalized = normalize(term)
            occurrences = text.count(normalized)
            if occurrences:
                matched[name].append(term)
                score += weights[name] * min(occurrences, 3)

    return score, matched


def build_candidates(
    entries: list[Entry],
    corpus_line_count: int,
    counts: list[int],
    term_groups: dict[str, list[str]],
) -> list[dict[str, object]]:
    total_entries = max(len(entries), 1)
    candidates: list[dict[str, object]] = []

    for entry in entries:
        for count in counts:
            if len(entry.pairs) < count:
                continue
            for start in range(0, len(entry.pairs) - count + 1):
                pairs = entry.pairs[start : start + count]
                score, matched = score_window(pairs, term_groups)
                if score <= 0:
                    continue
                combined = [item for pair in pairs for item in (pair.ja, pair.zh)]
                position = entry.ordinal / total_entries
                bucket_index = min(int(position * 4), 3)
                candidate_id = stable_key(
                    entry.release_group,
                    entry.title,
                    *(pair.ja for pair in pairs),
                    *(pair.zh for pair in pairs),
                )[:16]
                candidates.append(
                    {
                        "id": candidate_id,
                        "release_group": entry.release_group,
                        "song_title": entry.title,
                        "translator": entry.translator,
                        "entry_line": entry.line,
                        "entry_ordinal": entry.ordinal + 1,
                        "corpus_position": round(entry.line / max(corpus_line_count, 1), 4),
                        "corpus_bucket": f"Q{bucket_index + 1}",
                        "pair_count": count,
                        "pairs": [
                            {
                                "ja": pair.ja,
                                "zh": pair.zh,
                                "ja_line": pair.ja_line,
                                "zh_line": pair.zh_line,
                            }
                            for pair in pairs
                        ],
                        "matched_terms": matched,
                        "lexical_score": score,
                        "character_count": sum(len(item) for item in combined),
                        "stable_tiebreaker": stable_key(entry.title, *combined),
                    }
                )

    return candidates


def candidate_rank(candidate: dict[str, object]) -> tuple[object, ...]:
    return (
        -int(candidate["lexical_score"]),
        int(candidate["character_count"]),
        str(candidate["stable_tiebreaker"]),
    )


def deduplicate_titles(candidates: list[dict[str, object]]) -> list[dict[str, object]]:
    best_by_title: dict[str, dict[str, object]] = {}
    for candidate in sorted(candidates, key=candidate_rank):
        title_key = normalize(str(candidate["song_title"]))
        if title_key not in best_by_title:
            best_by_title[title_key] = candidate
    return list(best_by_title.values())


def diversified_selection(
    candidates: list[dict[str, object]],
    limit: int,
    seed_text: str,
) -> list[dict[str, object]]:
    if limit <= 0:
        return []

    ranked = sorted(candidates, key=candidate_rank)
    by_bucket: dict[str, list[dict[str, object]]] = {
        f"Q{index}": [] for index in range(1, 5)
    }
    for candidate in ranked:
        by_bucket[str(candidate["corpus_bucket"])].append(candidate)

    start = int(stable_key(seed_text)[:8], 16) % 4
    bucket_order = [f"Q{((start + offset) % 4) + 1}" for offset in range(4)]
    selected: list[dict[str, object]] = []
    selected_ids: set[str] = set()
    album_counts: dict[str, int] = {}

    def take(require_new_album: bool, max_per_album: int | None) -> bool:
        progress = False
        for bucket in bucket_order:
            for candidate in by_bucket[bucket]:
                candidate_id = str(candidate["id"])
                album = str(candidate["release_group"])
                if candidate_id in selected_ids:
                    continue
                if require_new_album and album_counts.get(album, 0) > 0:
                    continue
                if max_per_album is not None and album_counts.get(album, 0) >= max_per_album:
                    continue
                selected.append(candidate)
                selected_ids.add(candidate_id)
                album_counts[album] = album_counts.get(album, 0) + 1
                progress = True
                break
            if len(selected) >= limit:
                break
        return progress

    diversity_target = min(limit, 8)
    while len(selected) < diversity_target and take(require_new_album=True, max_per_album=1):
        pass
    while len(selected) < limit and take(require_new_album=False, max_per_album=2):
        pass
    while len(selected) < limit and take(require_new_album=False, max_per_album=None):
        pass

    for candidate in selected:
        candidate.pop("stable_tiebreaker", None)
    return selected


def build_parser() -> argparse.ArgumentParser:
    default_corpus = Path(__file__).resolve().parents[1] / "references" / "opus.md"
    parser = argparse.ArgumentParser(
        description="Recall diverse bilingual lyric windows from the full opus corpus."
    )
    parser.add_argument("--corpus", type=Path, default=default_corpus)
    parser.add_argument("--motif", action="append", default=[], help="Visible motif term; repeatable or pipe-separated.")
    parser.add_argument("--relation", action="append", default=[], help="Action or spatial-relation term; repeatable or pipe-separated.")
    parser.add_argument("--affect", action="append", default=[], help="Emotion or sensory term; repeatable or pipe-separated.")
    parser.add_argument("--counts", type=parse_counts, default=parse_counts("1,2"), help="Comma-separated consecutive pair counts, 1-4.")
    parser.add_argument("--limit", type=int, default=12, help="Maximum number of diversified candidates (default: 12).")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    term_groups = {
        "motif": clean_terms(args.motif),
        "relation": clean_terms(args.relation),
        "affect": clean_terms(args.affect),
    }
    if not any(term_groups.values()):
        parser.error("provide at least one --motif, --relation, or --affect term")
    if args.limit < 1:
        parser.error("--limit must be at least 1")
    if not args.corpus.is_file():
        parser.error(f"corpus not found: {args.corpus}")

    lines, entries = parse_corpus(args.corpus)
    all_candidates = build_candidates(entries, len(lines), args.counts, term_groups)
    unique_candidates = deduplicate_titles(all_candidates)
    seed_text = json.dumps(term_groups, ensure_ascii=False, sort_keys=True)
    selected = diversified_selection(unique_candidates, args.limit, seed_text)
    returned_buckets = sorted({item["corpus_bucket"] for item in selected})
    returned_release_groups = len({item["release_group"] for item in selected})
    returned_song_titles = len({item["song_title"] for item in selected})

    # Keep corpus-position fields internal to diversification.  The caller only
    # needs compact evidence for emotional reranking and source verification.
    for item in selected:
        item.pop("entry_line", None)
        item.pop("entry_ordinal", None)
        item.pop("corpus_position", None)
        item.pop("corpus_bucket", None)

    complete_pairs = sum(len(entry.pairs) for entry in entries)
    result = {
        "corpus": str(args.corpus.resolve()),
        "query": term_groups,
        "counts": args.counts,
        "coverage": {
            "corpus_lines": len(lines),
            "release_groups": len({entry.release_group for entry in entries}),
            "song_entries": len(entries),
            "unique_song_titles": len({normalize(entry.title) for entry in entries}),
            "complete_pairs": complete_pairs,
            "matched_windows": len(all_candidates),
            "matched_unique_titles": len(unique_candidates),
            "returned_candidates": len(selected),
            "returned_release_groups": returned_release_groups,
            "returned_song_titles": returned_song_titles,
            "returned_buckets": returned_buckets,
        },
        "candidates": selected,
    }
    # ASCII escapes keep the JSON transport stable across Windows console code
    # pages.  JSON consumers recover the exact Japanese and Chinese strings.
    json.dump(result, sys.stdout, ensure_ascii=True, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
