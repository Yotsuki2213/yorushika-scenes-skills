# Yorushika Scenes Skills

Two complementary Codex skills for transforming a supplied photograph into a scene-led MV artwork and a tactile landscape postcard.

[中文](README.md) · [MV scene skill](skills/yorushika-mv-scenes/SKILL.md) · [Postcard skill](skills/yorushika-postcard-scenes/SKILL.md) · [Examples](examples/README.md)

## The two skills

| | MV scene | Postcard |
| --- | --- | --- |
| Invocation | `$yorushika-mv-scenes` | `$yorushika-postcard-scenes` |
| Input | One user-supplied photograph | A photograph or an existing MV artwork |
| Target | Landscape about 16:9; portrait about 3:4; square defaults to about 16:9 | Landscape 4:3 postcard front |
| Treatment | Composition analysis, source preservation, white line figures, ink and controlled print fractures | Scene-derived paper color, light aging, edge integration, signature and 1–4 Chinese lyric lines matched to the scene |
| Dependency | Built-in ImageGen and local image viewing | The sibling MV scene skill and the same image tools |

```text
Photo → MV scene generation → saved artwork ─┐
                                            ├→ postcard composition → inspection
Existing MV artwork → inspect and reuse ────┘
```

Read the source composition before styling. The default `preserve-edit` mode keeps the main subject, geometry and lighting. Full re-authoring requires an explicit `redraw` request. Available routes are `graphic-soliloquy`, `sunlit-memory`, `nocturnal-material`, and a weighted `fusion`. The route name does not authorize changing the photograph's actual weather.

If no human subject exists, add one readable white sketched protagonist whose action and contact fit the scene. If human subjects already exist, preserve their bodies, clothing, poses and positions while covering visible heads with dense white hatching and horizontal scribbles. Body strokes retain transparent gaps; head coverage may be dense. Incidental background passers-by alone do not count as a primary subject, and off-frame heads are not invented.

Use approximately landscape 16:9 or portrait 3:4 framing from EXIF-oriented input dimensions, accepting nearby native output dimensions and naturally extending edges when composition benefits while preserving body proportions and spatial anchors. The skill bundles three selected [line references](skills/yorushika-mv-scenes/references/human-treatment.md). Postcard composition preserves the resulting artwork's aspect and human treatment inside its landscape 4:3 paper canvas.

## Install

Use Codex with built-in ImageGen and local image inspection. This repository contains instructions, references and assets; it does not provide an image service, credentials or model weights.

The repository is private. Authenticate with a GitHub account that has access, then clone it:

```text
gh repo clone Yotsuki2213/yorushika-scenes-skills
```

Copy both folders from `skills/` into the target project's `.agents/skills/`, or into a personal skill directory. Keep them as siblings: the postcard skill resolves its MV dependency through a relative path. Compare and back up an existing installation before replacing it. A PowerShell installation example with overwrite checks is available in the [Chinese README](README.md#开始使用).

The MV skill may be installed alone. The postcard skill requires both folders.

## Use

Attach an image and request:

```text
Use $yorushika-mv-scenes on this photo.
Preserve the composition, choose graphic-soliloquy, and add no text.
```

```text
Use $yorushika-postcard-scenes to make a postcard from this image.
Choose paper from the scene's colors, light aging, and 1–4 Chinese lyric lines matching its visible elements and mood.
```

See [scene examples](examples/mv-scene.md) and [postcard examples](examples/postcard.md) for controls and inspection expectations.

## Chinese lyric selection

The bundled user-provided [geci.md](skills/yorushika-postcard-scenes/references/geci.md) contains Japanese lyrics and Chinese translations. With `lyrics=auto`, follow the [selection guide](skills/yorushika-postcard-scenes/references/lyric-selection.md) to choose 1–4 Chinese translation lines from one song entry according to visible motifs and emotional tone. Preserve wording and punctuation, and record the song, translator when present, source line numbers and matching reason.

User-designated text takes precedence; `lyrics=none` disables added lyrics, with legacy `poem=auto|none` aliases supported. Newly generated MV artwork uses `text=none` for added microcopy; existing MV text remains. The historical [Japanese expression analysis](skills/yorushika-postcard-scenes/references/japanese-verse-corpus.md) is retained. Lyrics and translations remain subject to third-party rights; source metadata is supplied by the user and has not been independently verified.

## Layout

```text
yorushika-scenes-skills/
├── README.md
├── README.en.md
├── NOTICE.md
├── .gitignore
├── .gitattributes
├── assets/brand/README.md
├── examples/
│   ├── README.md
│   ├── mv-scene.md
│   └── postcard.md
└── skills/
    ├── yorushika-mv-scenes/
    │   ├── SKILL.md
    │   ├── agents/openai.yaml
    │   ├── references/ (including human-treatment.md)
    │   └── assets/line-figures/ (three reference PNGs and SOURCES.md)
    └── yorushika-postcard-scenes/
        ├── SKILL.md
        ├── agents/openai.yaml
        ├── references/ (including lyric-selection.md and geci.md)
        └── assets/
```

The repository layout follows the two-skill and bilingual-documentation organization of [gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill). Documentation here is written for this package. Its example images, brand assets and license have not been copied.

## Output and verification

Save newly generated MV artwork and postcards in `output/` directly under the active workspace root. Use `YYYYMMDD-title.png` with a short scene title and the actual file extension, such as `20260831-autumn-path.png`. Choose a distinct short title on a naming collision; preserve original inputs and historical outputs in place. Detailed prompts and inspection notes stay with the generated project.

Inspect actual dimensions, orientation, composition and glyph accuracy. MV 16:9 and 3:4 are approximate framing preferences: small deviations are acceptable and require no cropping, resampling or regeneration. Postcards retain their own landscape 4:3 canvas and native-artwork-scale checks. Prompt instructions alone do not prove compliance; report genuine concerns in the handoff.

Three user-selected line-figure references are bundled with the MV skill, and the user-provided geci.md lyric collection is bundled with the postcard skill. Historical MV research screenshot collections, other personal photographs, generated projects, credentials and local backups are not bundled. The examples directory currently contains invocation and acceptance guides rather than an image gallery.

## Rights

This is an unofficial private project. No open-source license is granted by this repository. Third-party marks and creative works remain subject to their respective rights. Read [NOTICE.md](NOTICE.md) and the [line-reference provenance](skills/yorushika-mv-scenes/assets/line-figures/SOURCES.md) and [logo provenance](skills/yorushika-postcard-scenes/assets/SOURCES.md) before redistribution or other use.
