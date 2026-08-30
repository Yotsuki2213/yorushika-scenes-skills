# Yorushika Scenes Skills

Two complementary Codex skills for transforming a supplied photograph into a scene-led MV artwork and a tactile landscape postcard.

[中文](README.md) · [MV scene skill](skills/yorushika-mv-scenes/SKILL.md) · [Postcard skill](skills/yorushika-postcard-scenes/SKILL.md) · [Examples](examples/README.md)

## The two skills

| | MV scene | Postcard |
| --- | --- | --- |
| Invocation | `$yorushika-mv-scenes` | `$yorushika-postcard-scenes` |
| Input | One user-supplied photograph | A photograph or an existing MV artwork |
| Target | Landscape 16:9 scene | Landscape 4:3 postcard front |
| Treatment | Composition analysis, source preservation, white line figures, ink and controlled print fractures | Scene-derived paper color, light aging, edge integration, signature and optional Japanese verse |
| Dependency | Built-in ImageGen and local image viewing | The sibling MV scene skill and the same image tools |

```text
Photo → MV scene generation → saved artwork ─┐
                                            ├→ postcard composition → inspection
Existing MV artwork → inspect and reuse ────┘
```

Read the source composition before styling. The default `preserve-edit` mode keeps the main subject, geometry and lighting. Full re-authoring requires an explicit `redraw` request. Available routes are `graphic-soliloquy`, `sunlit-memory`, `nocturnal-material`, and a weighted `fusion`. The route name does not authorize changing the photograph's actual weather.

White line figures stay small, anonymous, hollow and anchored to an existing surface. Postcard composition reuses the saved artwork and derives paper, margins and typography from it.

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
Choose paper from the scene's colors, light aging, and original Japanese verse.
```

See [scene examples](examples/mv-scene.md) and [postcard examples](examples/postcard.md) for controls and inspection expectations.

## Japanese verse reference

The bundled [Japanese corpus](skills/yorushika-postcard-scenes/references/japanese-verse-corpus.md) distills expression patterns from 11 user-provided lyric sections. It includes 14 expressive units, 11 analytical records, and Japanese syntax, rhythm and line-break guidance adapted to short postcard verse.

Full source lyrics are not distributed. Tags and editorial examples guide new writing rather than serving as ready-made captions. New verse follows visible scene anchors. Supplied wording and `poem=none` take precedence.

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
    │   └── references/
    └── yorushika-postcard-scenes/
        ├── SKILL.md
        ├── agents/openai.yaml
        ├── references/
        └── assets/
```

The repository layout follows the two-skill and bilingual-documentation organization of [gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill). Documentation here is written for this package. Its example images, brand assets and license have not been copied.

## Output and verification

The skills save source copies, intermediate artwork and postcard outputs separately under the active project's `Image生图/` directory. Detailed prompts and inspection notes stay with the generated project.

Inspect actual files for aspect ratio, artwork scale and glyph accuracy. Image generation may ignore requested pixel dimensions or resize the inset artwork. Label results that fail required checks as drafts; prompt instructions alone do not prove native-size preservation. The postcard workflow does not automatically regenerate or upscale to conceal a mismatch.

Personal photographs, generated projects, complete lyrics, MV reference frames, credentials and local backups are not bundled. The examples directory currently contains invocation and acceptance guides rather than an image gallery.

## Rights

This is an unofficial private project. No open-source license is granted by this repository. Third-party marks and creative works remain subject to their respective rights. Read [NOTICE.md](NOTICE.md) and the [asset provenance](skills/yorushika-postcard-scenes/assets/SOURCES.md) before redistribution or other use.
