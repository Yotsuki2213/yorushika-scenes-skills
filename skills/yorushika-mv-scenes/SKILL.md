---
name: yorushika-mv-scenes
description: "Transform one user-supplied image into a source-aware pre-2022 Yorushika MV scene: approximately landscape 16:9 or portrait 3:4 according to input orientation. Preserve composition and texture, add a loosely sketched white protagonist facing away and looking back when no human subject exists, or cover existing subjects' entire visible heads with white hatching. Apply ink/watercolor and controlled distortion through graphic-soliloquy, sunlit-memory, nocturnal-material, or fusion."
---

# Yorushika MV Scenes

Use this skill with one user-supplied scene image. If none is identifiable, ask for it before generation. Supporting line-art references do not substitute for the user's scene.

## Contract

- Defaults: `transform_mode=preserve-edit`, `preserve_strength=balanced`, `style_intensity=strong`, `mode=auto`, `text=auto`, `aspect=auto`, `identity=scene-only`. Keep the existing `strict|balanced|loose` preservation, `restrained|strong|expressive` intensity, and explicit route controls. Use `redraw` only when explicitly requested.
- Resolve output from the source's EXIF-oriented dimensions: landscape → **approximately 16:9**, portrait → **approximately 3:4**, square → **approximately 16:9** by default. These are framing preferences, not exact pixel-ratio requirements. A later explicit user framing request takes precedence.
- Resolve human treatment before style: no human subject → add one loosely scrawled white protagonist with a back-facing torso and natural over-shoulder look back; existing human subject(s) → preserve their bodies/poses and cover entire visible heads with dense white hand-drawn hatching/scribbles. These branches apply to every route and both transform modes. Explicit user instructions override defaults.
- Output one raster image using built-in `image_gen` and return the image with a compact result record and absolute saved path. Keep the full production prompt internal unless requested.
- Historical MV research screenshots are analysis material only. The bundled [line-figure reference](references/human-treatment.md) may be used as a labeled supporting style input, never as the scene edit target. Use [线稿小人抠图联系表.png](assets/line-figures/线稿小人抠图联系表.png) as the default and only bundled line-style reference.

Typical call:

```text
transform_mode=preserve-edit preserve_strength=strict style_intensity=strong mode=graphic-soliloquy text=auto aspect=auto identity=scene-only
```

“加上 graphic-soliloquy” or “保留原素材” means preserve-edit, not full redraw.

## Workflow

1. Inspect the scene with `view_image` and read its actual EXIF-oriented dimensions. Build the Scene Card using [composition/expression](references/composition-expression.md): subjects, geometry, gesture, visual weight, quiet areas, semantic minimum, expression, and eye path. Record `source_orientation`, `target_aspect`, `human_subject_present`, `human_treatment`, subject actions/positions, and visible head regions. If a new figure is needed, resolve its scene-supported location, depth plane, scale basis, contact and occlusion before selecting its action or style.
2. Read [human treatment](references/human-treatment.md), [visual grammar](references/visual-grammar.md), and [prompt compiler](references/prompt-compiler.md) before compiling. Read [frame analysis](references/frame-analysis-rubric.md) only for detailed extraction explanations. When figure/head drawing is needed, inspect the default and only bundled [线稿小人抠图联系表.png](assets/line-figures/线稿小人抠图联系表.png).
3. Resolve the human branch and target frame, then partition `hard_locks`, `soft_locks`, `editable_zones`, and `remove_only`. Existing bodies, clothing, poses and positions remain protected; visible heads to obscure and any new figure footprint are explicitly editable. Include natural extension zones as needed.
4. Select the style route from scene evidence. `auto` chooses the strongest route and compatible accents; `fusion` uses 60/25/15. The route controls atmosphere and material, not whether the human branch is performed.
5. Compile one internally consistent production prompt: source composition, resolved orientation/aspect, human treatment, reference roles, locks, edit zones, route weights, materials, light, microcopy and constraints. Attach the actual source and selected style images using the tool's supported reference mechanism.
6. Generate one image and save it under the active workspace root's `yorushika/` using the Output files convention below.

## Human subject and white-line treatment

Use the detailed branch decisions and reference selection in [human-treatment.md](references/human-treatment.md).

Judge a **human subject** by composition, readable action and narrative role; incidental background passers-by alone do not satisfy this condition. An existing drawn human subject also counts.

- **No human subject:** add one legible young man or young woman protagonist in pure-white irregular contour and hatching. Choose the location from the source's perspective, support plane, eye path and quiet space, then set the figure's size from its depth plane and nearby scale references. A distant figure may occupy only a small part of the frame when that is the natural spatial reading; keep the silhouette, action direction, head scribble and contact readable at that scale. Default to a torso facing away from the camera and a natural look back over one shoulder only when the neck, shoulders, pelvis, feet and support can carry it; otherwise use the scene-supported action already resolved in the Scene Card. Keep joint connections, weight-bearing balance and contact believable; abstract the strokes, not the body's physical logic. Preserve source objects and depth.
- **Human subject present:** retain the body, clothing, gesture, relative scale and placement. Cover each visible primary subject's head with dense white hand-drawn hatching and predominantly horizontal scribble strokes, covering the whole visible head, including crown, hair, face, ears and back of head, so no head detail reads through. Do not re-pose existing subjects to match the new-figure default. Keep coverage local and proportionate. Do not add another protagonist by default.
- Keep transparent gaps between the new figure's body strokes; dense head coverage is allowed. A newly drawn head also receives full-head anonymous scribble treatment; body contours may be incomplete, abstract and loosely scrawled while remaining readable. If an existing subject's head is outside the frame, do not invent one.
- These authorized regions remain editable under `strict`. In `redraw`, re-author the unlocked environment while keeping this human branch and protected body anchors unless the user explicitly releases them.

## Orientation and framing

Read dimensions after applying EXIF orientation to interpretation; do not rotate or overwrite the original file. Record the oriented `source_width × source_height`.

| Oriented source | Default target |
| --- | --- |
| width > height | landscape, approximately 16:9 |
| width < height | portrait, approximately 3:4 |
| width = height | landscape, approximately 16:9 |

Keep the camera viewpoint, subject proportions, source axis and important edge content. Favor natural framing near the target aspect and accept the generator's native dimensions. Extend the necessary edges only when it benefits composition, placing extension around the source's focal anchor and eye path. Never stretch, mirror, tile, letterbox, or crop important subjects to force the ratio. Preserve the portrait image's vertical movement instead of converting it to a wide scene.

## Output files

Save each generated image in `yorushika/` directly under the active workspace root, creating the folder if needed. Resolve this location from the task workspace, not the skill or repository directory. Use `标题-MV.<ext>` with a short scene title and the actual file extension, for example `江南水乡-MV.png`; do not add a date prefix. Sanitize the title for Windows filenames by removing reserved characters (`< > : " / \ | ? *`) and trailing spaces or periods. If the same name exists, append a short numeric suffix such as `标题-MV-2.png` instead of overwriting it. Preserve original inputs, existing `output/` files and existing `yorushika/` files in place.

## Composition and preservation

Read the source as a composed statement before styling. Preserve the dominant horizon, shoreline, path, architecture, overlap, scale relationships and eye path. Human treatment is an intentional graphic event in this composition: its location, gaze/action and contrast must join the source's visual movement.

The attached scene is the edit target in `preserve-edit`. Keep principal objects, body anchors, geometry, foreground materials, original texture and lighting direction outside the named editable regions.

- `strict`: target roughly 80–90% source structure/pixel retention; localized accents. Required head coverage or the new figure footprint is still allowed.
- `balanced`: retain the main subjects and roughly 60–80% source structure; allow bounded simplification, natural framing extension and a strong source-anchored graphic field.
- `loose`: retain the semantic anchors while allowing broader environment edits; it remains an edit.
- `redraw`: explicit re-authoring of unlocked environment from scene anchors. Preserve the resolved human treatment and orientation; do not use it implicitly for route changes.

Retention percentages are art-direction estimates, not measured guarantees. `style_intensity` controls the supporting treatment without making a required figure or head cover illegible: `restrained` targets 10–30% local intervention; `strong`, 30–55%; `expressive`, 45–65%. Keep these as structured fields, not a uniform filter.

For strong graphic-soliloquy, build a hierarchy of the resolved white-line human treatment, a broad bounded sumi-ink/watercolor wash, and one controlled broken/distortion event aligned to source geometry. Keep original texture readable beneath/beside the wash. Irregular graphite contours and restrained cobalt/red print offsets belong on selected scene edges; figure and head-cover strokes remain pure white.

## Route selection

- `graphic-soliloquy`: architecture, interior geometry, books/paper, hand-drawn contour, graphic dialogue and controlled registration errors. Favor deep blue, cobalt, black, dirty white, a small warm accent, handmade 2D texture, pigment bloom and dry-brush gaps.
- `sunlit-memory`: open sky, sea, field, coast, station, road or summer daylight. Favor pale sky blue, warm ivory, grass green, ochre, low-saturation pink, air, haze and meaningful quiet areas. Apply the same human branch with scene-appropriate action and readable white marks.
- `nocturnal-material`: dark rooms, single-point light, strong shadow or an isolated material event. Favor navy, black, cool gray, tan and one tactile event such as water, glass, paper, dust, cloth or light. Apply the same human branch using contrast and the existing light pool.
- `fusion`: dominant/secondary/tertiary 60/25/15; let the dominant route determine atmosphere while the human branch and target aspect remain fixed.

## Text and source constraints

- `text=auto`: one original Japanese microcopy phrase of roughly 3–8 characters, used once as a graphic element. Do not quote lyrics, song titles, logos or webpage text. User text overrides it; `text=none` suppresses added text.
- Preserve native source text/marks unless removal is requested. If watermark removal is requested, repair only its local region.
- Keep people anonymous through the defined head treatment without erasing their bodily action. Do not reconstruct identity or copy a reference character design, named MV frame, band logo, album packaging, lyric line or exact reference prop arrangement.
- Preserve source content outside the authorized edits; no whole-frame filter, arbitrary glitch, malformed anatomy, ungrounded figure, generated UI, new watermark, extra logo or crowded equal-weight effects.

## Response

Return the image and a compact record: `transform_mode`, `preserve_strength`, `style_intensity`, route/weights, `source_orientation`, `target_aspect`, `human_subject_present`, `human_treatment`, figure placement/depth/scale basis/contact or head-coverage choice, key anchors/locks, effect zones, microcopy/gloss if any, and absolute saved path. Keep the full production prompt and detailed notes in project files unless requested.
