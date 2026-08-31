# 🦌 Yorushika Scenes Skills

## A postcard for the part of you that still remembers summer.

> Wind crosses the platform. Blue settles into paper.<br>
> Someone in the photograph keeps walking; a small patch of shade stays behind.<br>
> Pick a photo you have never quite been able to delete.

[中文](README.md) · [MV scenes](skills/yorushika-mv-scenes/SKILL.md) · [Postcards](skills/yorushika-postcard-scenes/SKILL.md) · [Examples](examples/README.md) · [Asset index](assets/brand/README.md)

Two companion Codex skills: **one turns a photograph into a source-aware scene with a Yorushika MV atmosphere; the other sets that scene on tactile paper with Japanese/Chinese lyric pairs.**

The creative direction draws on blue, wind, shade, flowers, journeys and memory in [opus.md](skills/yorushika-postcard-scenes/references/opus.md), alongside the handmade visual language of pre-2022 Yorushika MVs. Think of the ink in *藍二乗*, the summer memories of *花に亡霊*, the departure in *夜行* and the passing season in *春泥棒*. The introductory prose here is original, not a lyric quotation.

Bring a street corner, a riverbank, an old house or the last light of an afternoon. Leave a little room for white lines and paper. 🦌

*Unofficial personal project · Personal, non-commercial use only · Credit and @ the original creator when posting*

## Invite the deer into your workspace 🦌

### Quick install: send this request to Codex

Open Codex in the workspace where you want to create, then paste:

```text
Use $skill-installer to install these two skills from the main branch of:
https://github.com/Yotsuki2213/yorushika-scenes-skills

Repository paths:
- skills/yorushika-mv-scenes
- skills/yorushika-postcard-scenes

Install both into .agents/skills/ at the current workspace root.
Keep the folders as siblings and preserve all SKILL.md, agents,
references and assets content.
If either skill already exists, compare versions and ask before replacing it.
If private-repository authentication fails, explain the access needed;
do not ask me to paste a token into the conversation.
Check the installed references and assets, then tell me how to invoke both skills.
```

Before setting off:

- **Image tools:** Codex needs built-in ImageGen, local image viewing and permission to write outputs. This package contains no model weights, API keys or standalone image service.
- **Repository access:** The repository is currently private. Use an authenticated GitHub account with access.
- **Discovery:** Cloning alone does not install the skills. Project-local skills belong in `.agents/skills/`. Check on the next turn; restart Codex if they still do not appear. See the [official skill documentation](https://learn.chatgpt.com/docs/build-skills).
- **Keep the pair together:** MV scenes can run alone; postcards require the sibling MV skill. Figure references, logos and the lyric corpus are bundled. No private screenshot collection needs to move with you.

Already downloaded the repository? Send this instead:

```text
Find my downloaded yorushika-scenes-skills repository and install both
complete folders under its skills/ directory into this workspace's .agents/skills/.
Keep them as siblings and check relative references and assets.
Compare and ask before replacing an existing installation.
```

After a future repository update, synchronize the installed copies too. A git pull does not update folders you previously copied elsewhere.

## First letter: let the photograph breathe

Attach a photo and ask:

```text
Use $yorushika-mv-scenes on this photograph.
Preserve the composition, choose graphic-soliloquy, and add no text.
```

The skill first reads the scene: where the road leads, where shadows fall, who is waiting, and which part of the sky should remain quiet. It then preserves the main geometry, textures and light while adding white drawing, ink washes and localized print misregistration.

**People belong to the story.** Without a human subject, add one readable white sketched protagonist with scene-grounded action. With existing subjects, preserve bodies, clothing, poses and positions, covering visible heads with dense white hatching. Incidental passers-by do not automatically count as subjects; off-frame heads are not invented. See [human treatment and references](skills/yorushika-mv-scenes/references/human-treatment.md).

Choose today's atmosphere:

| Route | What it brings |
| --- | --- |
| `graphic-soliloquy` | Notebook-margin monologue: hand-drawn contours, blue-black ink, localized print slips |
| `sunlit-memory` | Air and distance: softened light, foliage and meaningful quiet space |
| `nocturnal-material` | A little light after dark: glass, water, paper or another isolated material event |
| `fusion` | One leading atmosphere with two quieter supporting textures |

The default is `preserve-edit`; full re-authoring requires an explicit `redraw` request. A route does not change the photograph's actual weather or turn every scene into a sunny summer day.

Landscape inputs aim for **about 16:9**, portraits **about 3:4**, and squares default to **about 16:9**. Nearby native dimensions are accepted; important subjects are not cropped or stretched to force a ratio.

## Second letter: send the scene on paper ✉️

Attach a photo or an existing MV artwork:

```text
Use $yorushika-postcard-scenes to make a postcard from this image.
Choose lightly aged paper from the scene's colors.
Analyze the actual MV artwork, then select and verify matching
Japanese/Chinese lyric pairs and the original song title from opus.md.
Use the orientation-based layout and generate after verification.
```

A photograph goes through the MV stage first. An existing MV artwork is reused. Only once the real artwork is ready does the search for words begin:

**Obtain MV → analyze elements, composition and emotion → verify lyrics/title → compose and generate → inspect and save**

| MV orientation | Postcard layout | Default lyrics |
| --- | --- | --- |
| Landscape / square | Upper-centered image; signature and words in the lower paper | **2 Japanese/Chinese pairs** |
| Portrait | Complete image left; logo upper-right, lyrics below, title last | **4 Japanese/Chinese pairs** |

Both use a landscape **4:3** outer card. Layout follows actual EXIF-oriented MV dimensions, not an exact input-ratio test. Preserve the MV artwork's native pixel extent by default and add paper around it; do not crop, stretch or silently shrink it to fit the words.

Each pair places the Japanese original above its corresponding Chinese translation. A separate final line carries the original song title:

```text
Japanese original
Corresponding Chinese translation

Japanese original
Corresponding Chinese translation

——Original Japanese song title
```

This is a layout diagram, not text to render literally. Actual text comes from one song entry in [opus.md](skills/yorushika-postcard-scenes/references/opus.md), retaining wording, punctuation and paired translations without mixing versions. The assistant verifies the selection before passing fixed text to ImageGen. It proceeds directly unless you ask to preview the wording first.

The postcard retains the MV's white hatching, anonymous heads and spatial relationships. Let the paper age a little; keep the scene alive.

## How many words today?

Say what you want in ordinary language:

- **“Just the picture this time.”** A general no-added-text request disables added lyrics, song attribution and signature.
- **“Keep the logo, skip the lyrics.”** `lyrics=none` removes lyrics and song attribution.
- **“Keep the lyrics, skip the logo.”** Use `signature=none`.
- **“Two pairs for this portrait, please.”** Explicit `lyric_lines=2` overrides defaults; 1–4 pairs are supported.
- **“Show me the wording first.”** Preview the selected text and source, then wait for approval.
- **“Use these words I wrote.”** Keep supplied wording without inventing translations or song credits.

Legacy `poem=auto|none` remains supported. More options: [MV examples](examples/mv-scene.md) and [postcard examples](examples/postcard.md).

## Where the memories go

New images are saved in **`output/` at the active workspace root**, named with a date and short title:

```text
20260831-autumn-path.png
20260831-autumn-postcard.png
```

Originals, reused MV images and previous outputs remain intact. Choose a different short title on a naming collision; use the actual image format's extension.

Inspect real dimensions, composition, human treatment, white strokes, logo and lettering. MV framing is approximate; postcards retain actual 4:3 and native-artwork-scale checks. Generation can introduce glyph or layout errors. Report failed or unverified checks honestly; a requested value in a prompt is not proof.

## Inside the paper box

```text
yorushika-scenes-skills/
├── README.md / README.en.md       Two language editions
├── LICENSE.md                     Use terms
├── examples/                     Invocation and acceptance guides
├── assets/brand/README.md         Asset index
└── skills/
    ├── yorushika-mv-scenes/       Composition, white lines, ink and MV atmosphere
    │   ├── SKILL.md / agents/
    │   ├── references/
    │   └── assets/line-figures/   Three figure references
    └── yorushika-postcard-scenes/ Paper, layouts and bilingual selection
        ├── SKILL.md / agents/
        ├── references/           Includes opus.md
        └── assets/               Black/white logos, SVG and provenance
```

The lyric corpus supplies current selections; historical Japanese analysis and MV research notes remain separate. Runtime assets live inside their own skills. Private research screenshots, other project photos and generated outputs are not distributed.

Maintain entrypoints and references together, preserve intentional research-note differences, and check skill structure, relative links, assets and Git changes before publishing updates. Directory organization draws on [gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill).

## Take the scenery; leave a credit 🦌

**Personal use only. No commercial use. When posting work made with this project, credit the source and @ the original creator.**

- Personal learning, experimentation and non-commercial creation are permitted. Commercial commissions, sales of outputs or templates, paid services, advertising, marketing and other commercial uses are prohibited.
- Credit **Yorushika Scenes Skills**, link the repository and @ the project creator. The currently verified project identity is GitHub [@Yotsuki2213](https://github.com/Yotsuki2213). On other platforms, use an account confirmed by the creator; if tagging is unavailable, retain the author credit and link.
- Retain relevant photographer, lyricist, translator and other third-party credits, and obtain necessary use/publication permissions. **Attribution is not permission.**
- This is an unofficial fan project, not a Yorushika, creator or label endorsement. The personal non-commercial license covers only original material the repository author is entitled to license; it does not relicense lyrics, logos or figure references.

Full terms: [LICENSE.md](LICENSE.md). Third-party provenance is recorded in each skill's `assets/SOURCES.md`.

---

*There is a photograph in your album that feels like a song still playing. Start there.*
