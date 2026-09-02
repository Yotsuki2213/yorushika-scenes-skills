---
name: yorushika-mv-scenes
description: "Transform one user image into a source-aware pre-2022 Yorushika MV scene. Preserve composition; add a white sketched protagonist when no human subject exists or obscure existing subjects' visible heads with white hatching; route the scene through graphic-soliloquy, sunlit-memory, nocturnal-material, or fusion."
---

# Yorushika MV Scenes

Use one user-supplied scene image. Supporting line references never replace the user's scene.

## Defaults

`transform_mode=preserve-edit`, `preserve_strength=balanced`, `style_intensity=strong`, `mode=auto`, `text=auto`, `aspect=auto`, `identity=scene-only`. Use `redraw` only when explicitly requested. User instructions override defaults.

Read EXIF-oriented dimensions without modifying the original: landscape → approximately 16:9, portrait → approximately 3:4, square → approximately 16:9. These are framing preferences; accept nearby native ImageGen dimensions. Preserve viewpoint, subject scale, dominant axes and important edge content. Extend useful edges when needed; never stretch, mirror, tile, letterbox or crop an important subject to force a ratio.

## Fast conditional workflow

1. Inspect the source with `view_image`. Record only this compact Scene Card:

```text
orientation: landscape / portrait / square and oriented width × height
main_subject: the 1–2 scene-defining forms
human_branch: add-white-protagonist / cover-existing-heads / user-override
gesture: existing body action or planned action/contact
geometry: horizon, path, architecture, scale and overlap to preserve
eye_path: entry → anchor → intervention → quiet exit
quiet_area: usable low-information region
route: graphic-soliloquy / sunlit-memory / nocturnal-material / fusion
edit_mode: preserve-edit + strict|balanced|loose / redraw
preserve: hard locks and authorized edit zones
```

For a more detailed analysis only when the user requests it, read [composition/expression](references/composition-expression.md) or [frame analysis](references/frame-analysis-rubric.md). Research notes in [corpus notes](references/corpus-notes.md) are not part of normal generation.

2. Resolve the human branch, route and edit mode before loading detailed rules. Incidental background passers-by are not a human subject unless they carry the composition or narrative.
3. Read exactly one module from each applicable group:
   - Human: [add a protagonist](references/humans/add-white-protagonist.md) or [cover existing heads](references/humans/cover-existing-heads.md).
   - Route: [graphic-soliloquy](references/routes/graphic-soliloquy.md), [sunlit-memory](references/routes/sunlit-memory.md), [nocturnal-material](references/routes/nocturnal-material.md), or [fusion](references/routes/fusion.md).
   - Transform: [preserve-edit](references/transforms/preserve-edit.md) or [redraw](references/transforms/redraw.md).
4. Read the compact [prompt compiler](references/prompt-compiler.md), insert only those selected modules, and compile one coherent English ImageGen instruction. Keep the production prompt internal unless requested.
5. When line treatment is needed, inspect the single bundled [line-reference contact sheet](assets/line-figures/线稿参考联系表.png) and attach it as `SUPPORTING LINE STYLE ONLY`; attach the user's image as `EDIT TARGET`. Use an individual original reference only if the contact sheet cannot express a special action. Never attach the contact sheet and all three originals together.
6. Generate one raster image with built-in `image_gen` and save it as described below.

## Non-negotiable image behavior

- No human subject: add one legible pure-white, loosely scrawled protagonist. The default action is a believable still with the torso facing away and the head looking naturally back over one shoulder; when that default contradicts the scene—its sightlines, path, support or narrative—adapt the action freely while keeping it equally grounded and plausible. Choose walking, sitting, standing or leaning from visible support; keep joints, balance, weight-bearing contact, perspective and occlusion plausible. The head is fully anonymized with dense white strokes; body hatching keeps transparent gaps.
- Existing human subject(s): preserve body, clothing, pose, scale, placement and contact. Cover each primary subject's entire visible head—including crown, hair, face, ears and back of head—with dense irregular white hatching and mostly horizontal scribbles. Do not add another protagonist or re-pose the body. Do not invent an off-frame head.
- Head-cover regions and a new figure footprint are authorized edits even under `strict`. Elsewhere preserve principal objects, perspective, source texture and lighting direction according to the selected transform module.
- White-line figures remain pure white. Supporting ink, watercolor, print offsets and controlled distortion must follow source geometry rather than becoming a whole-frame filter.

## Route selection

- `graphic-soliloquy`: architecture, interiors, roads, books/paper, strong contours or print-like interruption.
- `sunlit-memory`: sky, sea, fields, stations, roads or open daylight and air.
- `nocturnal-material`: darkness, one light pool, strong shadow or one tactile material event.
- `fusion`: only when evidence is genuinely mixed; use dominant/secondary/tertiary 60/25/15.

The route controls atmosphere and material, never whether required human treatment occurs.

## Text and output

`text=auto` adds one original Japanese microcopy phrase of roughly 3–8 characters once. Do not quote lyrics, titles, logos or webpage text. User text wins; `text=none` adds none. Preserve native source text unless removal is requested.

Save under the active workspace root's `output/`, not inside the skill repository. Use `YYYYMMDD-标题.<ext>` with the local date and a short title; choose another short title rather than overwrite an existing file. Preserve all inputs.

Return the image, absolute saved path and a compact record: mode, strength, route, orientation/aspect, human branch/action or head region, principal locks and microcopy if used.
