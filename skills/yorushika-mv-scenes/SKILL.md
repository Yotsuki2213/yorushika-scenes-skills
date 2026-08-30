---
name: yorushika-mv-scenes
description: Transform one user-supplied reference image into a 16:9 scene-only image by first reading its composition and expression, then applying a strong but source-aware pre-2022 Yorushika MV visual grammar. Preserve the source by default while adding line-drawn figures, ink/watercolor, broken distortion, and graphic-soliloquy, sunlit-memory, nocturnal-material, or fusion treatment.
---

# Yorushika MV Scenes

Use this skill only with a user-supplied reference image. If no image is attached, ask for one and do not run a text-only generation.

## Contract

- Input: one reference image; `transform_mode=preserve-edit` by default (use `redraw` only when the user explicitly asks for a full re-author); `preserve_strength=balanced` by default with `strict`, `balanced`, or `loose` options; `style_intensity=strong` by default with `restrained`, `strong`, or `expressive` options; `mode=auto` by default or explicit `graphic-soliloquy`, `sunlit-memory`, `nocturnal-material`, or `fusion`; `text=auto` by default, or user text/`none`; aspect is always landscape 16:9; identity policy is always `scene-only`.
- Output: call the built-in `image_gen` tool to edit or create one raster image, then return the image, a compact record of the transform mode, preservation strength, selected route and weights, hard locks/editable zones, scene anchors, constraints, generated microcopy (if any), inspection notes, and the saved output path. Do not print the full prompt by default; include it only when the user explicitly asks for the prompt or a debugging trace.
- Never use bundled screenshots as image references during generation. The local screenshots are research notes only.

Typical preserve-and-style call:

```text
transform_mode=preserve-edit preserve_strength=balanced style_intensity=strong mode=graphic-soliloquy text=auto aspect=16:9 identity=scene-only
```

If the user says only “加上 graphic-soliloquy” or “保留原素材”, infer this preserve-edit call. Require an explicit `transform_mode=redraw` (or an unambiguous request for full re-generation) before using the redraw template.

## Workflow

1. Inspect the supplied image with `view_image` before compiling a prompt. First build the Scene Card from `references/composition-expression.md`: core subjects, supporting elements, spatial invariants, dominant gesture, visual-weight map, natural quiet areas, semantic minimum, expression read, and eye path. Only after this pass partition the source into `hard_locks`, `soft_locks`, `editable_zones`, and `remove_only` elements.
2. Read `references/composition-expression.md` for composition/expression analysis, `references/visual-grammar.md` for the three route grammars, and `references/prompt-compiler.md` every time an ImageGen prompt is compiled. Read `references/frame-analysis-rubric.md` only when a detailed extraction explanation is needed.
3. Route the image. `auto` chooses the strongest route from observable scene evidence and may add one compatible secondary accent. Route selection never implies full redraw. `fusion` uses a dominant/secondary/tertiary mix of 60/25/15; never mix all three equally.
4. Solve composition and expression before style: keep the source-derived axis, visual-weight hierarchy, semantic minimum, and eye path. Then choose one primary Yorushika element stack. In `preserve-edit`, keep the source composition and hard locks in place; expand laterally only where needed to reach 16:9. In `redraw`, re-authoring is allowed. Never stretch or merely letterbox the source.
5. Compile a production-ready ImageGen prompt. It must explicitly state the composition/expression read, transform mode, preservation strength, style intensity, hard locks, editable zones, source texture to keep, route weights, style stack, palette, lighting, material, anonymous-human treatment, microcopy, 16:9 framing, and negative constraints.
6. Generate one image with `image_gen`. Inspect the result once for source-content retention, unchanged-anchor integrity, expression legibility, strength and hierarchy of the Yorushika elements, locality of distortion, scene continuity, identity removal, aspect, text count, UI/logo residue, and exact-frame copying. Do not automatically make a second variant.

## Composition and expression first

Before adding any Yorushika treatment, read the reference as a designed image rather than a bag of objects. Use `references/composition-expression.md` to record the Scene Card, visual-weight map, semantic minimum, source-shape candidates, and one-sentence expression read. Preserve the dominant horizon, shoreline, path, axis, overlap, scale relationship, and eye path that make the source itself meaningful.

Style is a second pass. Effects must attach to the source's real gesture or material: a **pure-white** line-drawn small person follows an existing shoreline/road/horizon; an ink or watercolor wash follows a wave, shadow, rock plane, or atmospheric field; a broken/distorted fragment interrupts an existing edge or transition. Never add an effect just because it is recognizable as a style token.

## Preserve-edit policy

`preserve-edit` is the default behavior. Treat the attached image as the edit target, not merely as inspiration for a fresh image. Preserve the user's main subject, major spatial relationships, horizon or architectural axis, foreground material, and original texture unless the user marks them editable.

- `strict`: target retention of roughly 80–90% of the source structure and pixels; lock subject, pose, scale, horizon, major edges, and lighting direction. Apply only localized line, grain, palette, and material accents.
- `balanced`: target retention of the main subject and roughly 60–80% of the source structure; allow local simplification, lateral 16:9 extension, and a strong but bounded graphic field that follows the source's visual weight and eye path.
- `loose`: retain the primary subject and semantic anchors while allowing larger environmental changes; it is still an edit, not a full redraw. Use `redraw` explicitly for full re-authoring.

`style_intensity` controls the visibility of the treatment without changing the source composition:

- `restrained`: 10–30% local intervention, suitable for a quiet edge accent.
- `strong`: 30–55% structured intervention across one primary field and one or two supporting pressure points; this is the default when the user asks for a strong Yorushika feeling.
- `expressive`: 45–65% intervention with larger washes and breaks, but still preserve the semantic minimum, hard locks, and dominant eye path.

When `mode=graphic-soliloquy` is used with `preserve-edit`, keep the source underlay readable but make the style unmistakable. Build a hierarchy of one or two tiny anonymous **white-only** line-drawn figures or gesture marks, one broad bounded sumi-ink/watercolor wash, and one controlled broken/distortion event aligned to source geometry. The added figure layer must use white ink, white pencil, or white chalk-like strokes only—never black, cobalt, red, colored fill, or multicolor clothing. Add irregular ink/graphite contours, cobalt or red print offset to the scene edges (not to the white figure), pigment bloom, dry-brush erasure, and fine grain inside the named `editable_zones`; at `style_intensity=strong`, visible intervention may reach roughly 30–55% of the frame, but it must remain structured rather than a uniform filter. Preserve the unedited texture and geometry; do not replace the whole scene.

## Route selection

- `graphic-soliloquy`: use when the reference is driven by hand-drawn contour, flat planes, architecture/interior geometry, book/paper/symbols, sparse dialogue-like graphics, or controlled RGB misregistration. Favor deep blue, cobalt, black, dirty white, a small warm accent, grain, print offset, and hand-made 2D-animation texture. For a strong treatment, use a source-anchored **white-only** line-drawn little person or gesture mark, a visible sumi-ink/watercolor wash with pigment pooling and bleed, and one broken/distorted print or scanline fracture. Keep cobalt/red offsets on scene edges only; the line-drawn person remains pure white. In `preserve-edit`, these become bounded overlays while the original subject, geometry, and material remain visible.
- `sunlit-memory`: use for open sky, sea, field, residential coast, station, road, or summer daylight. Favor pale sky blue, warm ivory, grass green, ochre, and low-saturation pink; large negative space; a very small anonymous figure, back view, translucent silhouette, or no person; clean hand-drawn background; slight overexposure or haze.
- `nocturnal-material`: use for dark room/stage, single-point light, strong shadow, isolated object, or one tactile event such as water, flower, glass, paper, dust, cloth, or firelight. Favor navy, black, cool gray, tan, sparse composition, low-key exposure, and concealed/absent faces.
- `fusion`: choose a dominant route from the image and assign 60% to it, 25% to the most compatible secondary route, and 15% to the remaining route. Keep the dominant route visually legible.

## Text and safety constraints

- `text=auto` creates one original Japanese microcopy phrase of roughly 3–8 characters, used once as a graphic element. It must not quote lyrics/歌词, titles, logos, or copied webpage text. User-provided text overrides it; `text=none` removes text.
- Preserve the requested source content and emotional relation, while removing or anonymizing personal identity. Any person must be anonymous, a back/side silhouette, a small distant figure, a masked/occluded form, a translucent presence, or absent.
- In `preserve-edit`, do not replace the source subject or re-layout the whole frame. In `redraw`, do not recreate a screenshot, named MV frame, character likeness, band logo, album cover, lyric line, or exact prop arrangement; synthesize a fresh composition from the extracted grammar.
- Do not remove source text or marks unless the user asks. If watermark removal is requested, remove only the watermark and reconstruct adjacent texture; keep unrelated source content intact.
- Always keep the output landscape 16:9. Negative constraints must include: no photorealistic identity likeness, no readable lyrics, no logos, no album packaging, no UI overlays, no watermarks, no exact MV screenshot/frame duplication beyond the user-supplied source, no crowded equal-weight style soup.

## Response format

Return the generated image and a compact record containing: `transform_mode`, `preserve_strength`, `style_intensity`, `mode`, route weights, the composition/expression read, eye path, hard locks, editable zones, chosen Yorushika style stack, preserved scene anchors, discarded identity/incidental details, camera/composition choice, palette/light/material notes, microcopy plus Chinese gloss, source-retention, expression-legibility, style-strength, white-line integrity, and overlay-locality inspection notes, and the absolute saved path. Omit the full prompt unless the user explicitly asks for it or requests a debugging trace.
