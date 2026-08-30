# ImageGen Prompt Compiler

Use this reference every time `$yorushika-mv-scenes` compiles an ImageGen request. The objective is a precise, internally coherent art direction—not a bag of style adjectives. Write the final ImageGen prompt in English for visual specificity; keep user-facing notes and the Japanese microcopy gloss in the user's language.

Prompt disclosure: the compiled prompt is an internal generation artifact. Do not print it in the normal response; expose it only when the user explicitly asks for the prompt or requests a debugging trace.

## Contents

1. Source distillation record
2. Composition and expression pass
3. Preserve-edit policy
4. Auto-routing and weights
5. Composition modules
6. Route prompt modules
7. Palette, light, material, and motion
8. Typography
9. Preserve-edit prompt template
10. Full prompt template (redraw fallback)
11. Negative constraints and inspection

## 1. Source distillation record

Before writing the prompt, form this internal record from the attached image:

```text
scene_type: exterior / interior / liminal / object-led
preserve_anchors: 3–6 concrete elements actually visible in the source
transform_mode: preserve-edit by default / redraw only when explicitly requested
preserve_strength: strict / balanced / loose; balanced by default
style_intensity: restrained / strong / expressive; strong when a forceful Yorushika treatment is requested
line_figure_color: white-only (white ink / white pencil / white chalk-like stroke); never black, cobalt, red, or colored fill
hard_locks: subject, major geometry, horizon/axis, foreground material, or other user-requested invariants
soft_locks: details that may receive restrained line, color, grain, or light treatment
editable_zones: bounded regions where route treatment, local simplification, or lateral extension is allowed
remove_only: watermark, UI, or clutter explicitly marked for removal; otherwise leave source marks intact
source_texture_to_keep: photographic grain, water/sand/stone/fabric detail, and other textures that must remain legible
style_stack: source-anchored line-drawn presence / ink-watercolor field / one broken-distortion event, in a clear hierarchy
style_overlay_budget: 10–30% restrained, 30–55% strong, 45–65% expressive; structured regions only, never a uniform whole-frame filter
spatial_relations: foreground, middle ground, background, horizon, window/door/road axes
time_weather: observable light and atmosphere; do not invent a season unless visually supported
dominant_geometry: horizontal bands / vanishing road / window grid / isolated object / open field
human_presence: absent / distant / back view / cropped / side silhouette / currently identifiable
identity_to_remove: face, hairstyle specificity, uniform insignia, logos, tattoos, readable personal text
incidental_to_remove: UI, clutter, vehicles, passers-by, signage, compression artifacts, screenshot bars
material_candidates: water, sand, hair, paper, paint, glass, dust, cloth, shadow, firelight
emotional_tension: one concise relation such as waiting-versus-departure or brightness-versus-erasure
expression_read: one sentence describing how composition and material express the emotional tension
visual_weight_map: dominant light/dark/saturated/isolated masses and edge tension
eye_path: entry → focal anchor → graphic/material intervention → quiet exit
abstraction_map: retain / merge / omit / transform / expose decisions for each editable zone
```

In `preserve-edit`, preserve the **source content and relationship** among anchors in place; use the hard/soft lock lists to decide which pixels may change. In `redraw`, preserve only the relationship among anchors, not their exact pixels. Example for redraw: preserve “a narrow road leading toward the sea with a small back-facing figure,” but change the buildings, clothes, figure proportions, camera distance, and exact horizon placement.

If a person is recognizable, convert them into a scene-scale anonymous presence. Never describe face, ethnicity, exact age, celebrity likeness, identifiable hairstyle, or outfit branding in the ImageGen prompt.

## 2. Composition and expression pass

Do not select a style route until the source has been read as a composed statement. Build a compact Scene Card containing:

- core subjects and supporting elements;
- spatial invariants and dominant gesture;
- visual-weight map and natural quiet areas;
- semantic minimum and 1–2 source-shape candidates;
- one-sentence `expression_read` and an `eye_path` of entry → anchor → intervention → exit.

Then make an `abstraction_map` for the editable regions: what to retain, merge, omit, transform, and leave blank. Preserve the dominant axis, subject scale, value hierarchy, and source material before adding any graphic treatment. Style is a second pass attached to real contours, planes, shadows, paths, or material events—not a collection of detached effects.

## 3. Preserve-edit policy

Use `preserve-edit` as the default. The attached image is the edit target and must remain visibly present beneath the style treatment. Write the prompt as a constrained in-place edit rather than as a request for a new composition.

| preserve_strength | What to lock | What may change |
|---|---|---|
| `strict` | Target roughly 80–90% of source structure/pixels: subject, pose, scale, horizon, major edges, lighting direction, and principal texture | Local contour, grain, restrained palette grading, one material accent, and small watermark repair if requested |
| `balanced` | Keep the main subject and roughly 60–80% of source structure, spatial relationships, and texture | Bounded background simplification, lateral 16:9 extension, and a strong but source-anchored graphic field in editable zones |
| `loose` | Keep the primary subject and semantic anchors | Larger environmental edits and stronger local stylization; still do not replace the entire image |

`style_intensity` controls effect strength without releasing the composition locks:

- `restrained`: 10–30% local intervention, one or two edge accents, and no broad wash.
- `strong`: 30–55% structured intervention across one primary graphic field plus one or two subordinate pressure points. Use a clear three-part stack: line-drawn presence, ink/watercolor atmosphere, and one controlled break.
- `expressive`: 45–65% structured intervention with larger washes and more visible fractures, while keeping the semantic minimum, source axis, and focal-anchor placement intact.

For `mode=graphic-soliloquy` in preserve-edit, use the following overlay budget and hierarchy:

- Keep the original underlay, subject, horizon/axis, and source texture readable.
- Add one or two tiny anonymous **white-only** line-drawn figures or gesture marks anchored to a real source axis (shoreline, road, ledge, shadow, or horizon); keep them subordinate and non-identifiable. Use white ink/pencil/chalk-like strokes only; never black, cobalt, red, colored fill, or multicolor clothing for the figure layer.
- Add one broad but bounded sumi-ink/watercolor wash with visible bloom, pigment pooling, feathering, and dry-brush gaps, following the source gesture rather than floating decoratively.
- Add one controlled broken/distortion event—displaced contour shards, torn registration, RGB offset, scanline fracture, or a dissolving edge—aligned with source geometry.
- Add irregular ink/graphite contours and cobalt/indigo plus one restrained rust echo only at selected scene boundaries, not on every contour and never on the white line-drawn figure.
- Grade locally toward deep blue, cobalt, black, or dirty white while retaining the source's unedited colors elsewhere.
- Do not repaint the whole photograph, replace the subject, move the camera, or apply a uniform watercolor/animation filter.

If the user asks to remove a watermark, place it in `remove_only` and reconstruct only the immediately adjacent texture. Do not erase unrelated text, marks, or source detail. If the user does not ask for removal, preserve source marks unless they are a generated UI artifact.

## 4. Auto-routing and weights

Score only visible evidence:

| Evidence | Primary route |
|---|---|
| open sky/sea/field, summer daylight, long road, station, distant or back-facing figure | `sunlit-memory` |
| room/window/desk, architectural geometry, paper/symbols, hand-drawn contour, paint erasure, RGB offset | `graphic-soliloquy` |
| dark room/stage, one lamp, long shadow, isolated object, water/glass/dust/cloth/fire as the emotional center | `nocturnal-material` |

For `auto`:

- Clear single-route evidence: primary 75%, compatible secondary 25%, omit the third route from the prose.
- Mixed but coherent evidence: primary 65%, secondary 25%, tertiary 10%.
- If the user explicitly asks for `fusion`: primary 60%, secondary 25%, tertiary 15%.

Select weights before writing the prompt. Do not let a low-weight route override the dominant route's camera, palette, or exposure.

## 5. Composition modules

Choose exactly one primary module. Add at most one secondary camera accent.

### A. Wide negative-space horizon

For sea, sky, field, roofline, or distant landscape. Use a static wide shot, horizon around the lower third, 55–70% quiet sky/wall/air, one small off-center anchor, restrained perspective, and a calm 16:9 rhythm.

### B. Low walking fragment

For roads, paths, shorelines, feet, fabric, or movement. Use a low tracking viewpoint; crop the person to legs, back, or partial torso; let the road edge or shoreline create a diagonal; keep face outside the frame; use one controlled motion smear.

### C. Window-and-desk geometry

For interiors, writing, reading, waiting, or phone/table scenes. Use a side-view medium-wide shot; window grid or doorway as structural lines; high-key window light or one desk lamp; person small and face occluded by angle, paper, hair, or a painterly erasure.

### D. Isolated material stage

For dark interiors or object-led references. Use a sparse wide shot with 65–80% dark negative space, one pool of light, one figure/object, one long shadow, and one principal material event.

### E. Translucent memory overlap

For reflections, movement, hats, foliage, water, or emotionally doubled scenes. Keep the base photograph-like space readable, then place one irregular translucent paint/print layer across only 20–35% of the frame. Do not turn the whole image into watercolor.

When the source is portrait or square, **re-compose laterally**: continue the environment into new left/right space, reduce the human scale, and establish a new 16:9 horizon or architectural axis. Never stretch the source, duplicate background tiles, or place vertical white bars.

## 6. Route prompt modules

Insert the chosen module into the final prompt and adapt nouns to the source. Do not copy the module verbatim when it conflicts with visible anchors.

### graphic-soliloquy module

```text
Render the re-authored scene as a restrained hybrid of live-action spatial realism and hand-drawn 2D animation. Use irregular ink-and-graphite contour variation, simplified flat planes, selective dry-brush erasure, very fine paper grain, and a small amount of cobalt/red print misregistration along only a few moving or emotionally charged edges. Keep architecture and objects geometrically lucid. Let one painterly interruption conceal identity or interrupt the scene; do not apply a uniform filter over the whole frame.
```

### graphic-soliloquy preserve-edit overlay

```text
Edit the attached image in place and keep its original subject, major geometry, horizon or architectural axis, and tactile source texture visibly intact. Apply graphic-soliloquy only inside the named editable zones: irregular ink-and-graphite contour accents on selected edges, restrained cobalt/red print misregistration on a few emotionally charged boundaries, one localized dry-brush erase or paint interruption, and fine paper grain. Keep the photographic or source-rendered underlay readable outside those zones; do not repaint, replace, recenter, or uniformly filter the whole frame.
```

### graphic-soliloquy strong stack

```text
After the composition and expression are solved, apply a forceful but source-anchored Yorushika graphic stack. Keep the real scene as the underlay and follow its dominant axis: place one or two tiny anonymous **white-only** line-drawn figures or gesture marks on an existing shoreline, road, ledge, shadow, or horizon; lay one broad bounded sumi-ink/watercolor wash over a meaningful plane with visible bloom, pooling, feathered edges, and dry-brush gaps; then add one controlled broken/distortion event such as displaced contour shards, torn registration, RGB offset, scanline fracture, or a dissolving edge. Use cobalt/indigo, dirty white, graphite black, and at most one restrained rust echo for the scene treatment, but keep the figure layer pure white with no colored fill. Let the stack affect roughly 30–55% of the frame through connected fields and edge interruptions, while the source subject, geometry, light direction, and material texture remain legible. Never scatter random glitch, draw a cute mascot, or apply a uniform filter.
```

### sunlit-memory module

```text
Render the re-authored scene as a quiet summer memory with expansive air and modest human scale. Use pale cyan sky, softened sea or field color, warm ivory light, restrained grass/ochre accents, slight highlight bloom, clean atmospheric perspective, and gentle lens softness. Preserve tactile wind in hair or cloth, water/sand/road texture, and one subtle motion trace. Keep the frame spacious, bright, and emotionally distant rather than cheerful or postcard-like.
```

### nocturnal-material module

```text
Render the re-authored scene as a sparse low-key material study. Surround one anonymous figure or object with blue-black and warm umber negative space. Use a single localized lamp or reflected glow, a long quiet shadow, and one tactile phenomenon—water, glass, paper, dust, cloth, flower, or firelight—as the emotional event. Preserve deep blacks without crushing all detail; avoid theatrical spectacle, neon cyberpunk, or multiple competing effects.
```

### Fusion assembly

Write the dominant route first and give it the composition/exposure decisions. Add the secondary route as a material or edge treatment. Add the tertiary route as a small color or atmosphere accent. Example logic:

```text
Dominant sunlit-memory controls the wide horizon and exposure; graphic-soliloquy appears only as sparse cobalt dry-brush erasure around the anonymous figure; nocturnal-material contributes a single darker shadow or reflective object, not a night-time conversion.
```

## 7. Palette, light, material, and motion

Choose one recipe and adapt it to source evidence.

### Palette recipes

- Summer coast: pale cyan `#DDEFF2`, sea blue `#79B6CD`, ink navy `#12324F`, warm ivory `#F3EEE3`, sand gray `#B9AD9C`.
- Graphic blue: cobalt `#245EBE`, ultramarine `#173C8E`, blue-black `#101722`, dirty white `#EEEDE7`, a tiny rust accent `#B66C50`.
- Window paper: cool white `#EEF3F2`, pale blue-gray `#C9DCE2`, graphite `#3A424A`, ink blue `#244C73`, muted wood `#9A795E`.
- Nocturnal amber: blue-black `#09131D`, slate `#364352`, warm umber `#80533B`, lamp amber `#D39A5B`, paper beige `#DED5C7`.

Treat hex values as approximate art-direction anchors, not rigid swatches. Use at most five named colors in the prompt.

### Lighting phrases

Select one primary lighting statement:

- strong but softened coastal noon with slightly bleached highlights and cool reflected fill
- late-afternoon backlight with floating dust and restrained amber flare
- high-key north-window light, near-white walls, and pale cyan shadows
- one warm practical light in a dim room with a long soft-edged wall shadow
- overcast blue daylight with diffuse reflections and very low contrast

### Material hierarchy

Select exactly one principal event and at most one supporting texture:

- principal: water / sand / paper / paint / glass / cloth / dust / shadow / flower / firelight
- supporting: hair movement / concrete grain / window reflection / fine print grain / fabric fold

State how the event behaves: “cobalt paint erases the edge of the silhouette,” “a thin water reflection doubles the horizon,” or “paper dust catches the window light.” Avoid merely listing materials.

### Motion hierarchy

Use no more than one:

- slight lateral motion smear on hair or cloth
- a single translucent echo displaced by a few pixels
- restrained cobalt/red edge misregistration
- one dissolving dry-brush boundary
- wind indicated through cloth, grass, water, or loose paper

Do not combine all motion effects.

## 8. Typography

`text=auto` requires one original Japanese microcopy phrase, roughly 3–8 Japanese characters. Generate it from the distilled emotional tension, not from any Yorushika title or lyric. Validate all three conditions before use:

1. It is not copied from the source, a song title, or a lyric.
2. It is semantically connected to the new scene but does not narrate the entire image.
3. It appears once and remains short enough for reliable rendering.

Typography art direction:

- one line only; no subtitle, translation, credits, or second phrase inside the image
- thin Mincho-like or restrained handwritten Japanese glyphs
- occupy roughly 6–14% of frame width
- place in existing negative space, away from faces and primary material event
- use soft white, pale blue-gray, or muted ink at moderate/low contrast
- allow one hairline rule or very short underline, but no boxed logo treatment
- request correct Japanese glyphs and no extra text; if the output is garbled, report it during inspection and do not silently invent a successful reading

If the user supplies text, preserve its exact wording but still use it once. For `text=none`, remove the typography block from the final prompt and explicitly request no text anywhere.

## 9. Preserve-edit prompt template

Use this template whenever `transform_mode=preserve-edit` (the default). Replace every bracketed field and delete unused clauses. The percentages are art-direction targets, not a claim of pixel-perfect control.

```text
Use case: constrained reference-image edit for one cinematic 16:9 raster image.

Transform mode:
preserve-edit, preserve_strength=[strict / balanced / loose], style_intensity=[restrained / strong / expressive]. The attached source image is the edit target. Do not generate a replacement image from scratch.

Composition and expression read:
The source expresses [tension] through [dominant gesture/material]. The eye path is [entry] → [focal anchor] → [graphic/material intervention] → [quiet exit]. Preserve [semantic minimum, visual-weight hierarchy, and source axis] before styling.

Source invariants (hard locks):
Keep [subject/objects], [major spatial relationships], [horizon or architectural axis], [foreground material], and [source texture] unchanged in identity, pose, relative placement, scale, and material readability. Preserve [observable time/light direction] and the emotional tension of [concise tension].

Soft locks and editable zones:
Allow only restrained stylization of [soft-lock details]. Apply route treatment inside [bounded editable zones] and, if needed, extend the environment laterally into 16:9 without moving the original focal anchor. Keep all non-editable regions visually continuous with the source.

Watermark/removal scope:
[If requested: remove only the watermark in [location] and reconstruct adjacent [water/rock/sky/paper] texture; retain all unrelated source marks and detail.] [Otherwise: do not remove or invent source text/marks.]

Route and weighting:
[mode and weights]. Keep the original scene as the underlay; use the route only as a localized edge, material, color, or atmosphere intervention within the editable zones.

Graphic-soliloquy overlay (when selected):
Add a clear but source-anchored stack at the selected intensity: [one or two tiny anonymous **pure-white** line-drawn figures or gesture marks attached to a real source axis], [one broad bounded sumi-ink/watercolor wash with bloom, pooling, feathering, and dry-brush gaps], and [one controlled broken/distortion event aligned to a source edge]. The line-drawn figure layer must use white ink, white pencil, or white chalk-like strokes only; never black, cobalt, red, colored fill, or multicolor clothing. Add irregular ink-and-graphite contours and restrained cobalt/indigo plus one rust print echo only on selected scene boundaries, never on the white figure. Target [10–30% / 30–55% / 45–65%] of the frame according to `style_intensity`; leave the original subject, geometry, light direction, and material texture legible elsewhere. Do not apply a uniform filter or scatter unrelated glitch.

Camera and composition:
Keep the source camera viewpoint, horizon/vanishing line, crop logic, and focal-anchor placement intact. [If source is not 16:9: extend only the left/right environment naturally; never stretch, mirror, tile, or letterbox.]

Palette and lighting:
Retain the source palette as the base. Add [3–5 restrained route colors] only as local grading or marks. Preserve [primary lighting phrase], shadow direction, and exposure relationship; keep warm color limited to [specific function].

Material event:
Keep [principal source material] readable as the emotional material event. Let [one route accent] interact with it without replacing its texture. Support it only with [one secondary texture].

Human treatment:
Keep the source figure only as an anonymous scene presence: [back/side silhouette / cropped fragment / distant small figure / translucent presence]. Do not sharpen or invent facial identity, branded clothing, or character-design detail.

Typography:
[For text=auto: place the single original Japanese phrase “[microcopy]” once in [editable negative-space location], using [thin Mincho-like / restrained handwritten] glyphs in [color/contrast], approximately [size relationship]. Correct Japanese characters, no other words, no credits, no lyrics, no logo treatment.] [For text=custom: use exactly “[user text]” once and no other text.] [For text=none: no text, captions, letters, symbols, credits, logos, or watermarks anywhere in the image.]

Output:
Landscape 16:9. Preserve the source image as the dominant visual evidence, with a localized graphic-soliloquy treatment and coherent high-resolution finish. No whole-frame regeneration, subject replacement, or re-layout outside editable zones.

Avoid:
[compiled preserve-edit integrity, identity, text, and technical negative constraints].
```

## 10. Full prompt template (redraw fallback)

Use the following template only when `transform_mode=redraw` is explicitly requested. It intentionally permits a fresh composition while retaining the identity and copyright safeguards.

Replace every bracketed field. Remove unused clauses rather than leaving placeholders.

```text
Use case: reference-image scene transformation for a single cinematic 16:9 raster image.

Transform mode: redraw (explicit opt-in only). Re-author the scene from semantic anchors; do not use this template for the default preserve-edit behavior.

Composition and expression read:
The source expresses [tension] through [dominant gesture/material]. Preserve the source-derived [axis/visual-weight hierarchy/eye path] while re-authoring the environment.

Primary request:
Transform the attached reference image into a completely new composition using a distilled early Japanese alternative-music-video scene grammar. Preserve only [3–6 scene anchors] and their essential spatial relationship: [relationship]. Preserve the observable [time/weather/light cue] and the emotional tension of [concise tension]. Re-author all architecture, clothing, props, vegetation, and exact camera placement. Do not preserve a recognizable person, face, logo, title, lyric, or exact source-frame arrangement.

Reference-image use:
Treat the input as semantic scene evidence, not pixels to collage, trace, or reproduce. Remove [identity details] and [incidental clutter/UI]. If a person remains, reduce them to [anonymous treatment] and make the environment the narrative subject. [If needed: expand the environment laterally into a natural 16:9 scene; do not stretch or letterbox the source.]

Route and weighting:
[mode and weights]. [One sentence explaining how dominant, secondary, and optional tertiary roles divide composition, material, and atmosphere.]

Scene and subject:
[New authored scene description built from the preserved anchors, including foreground/middle ground/background and one principal action or state.]

Camera and composition:
[One composition module], [shot scale], [viewpoint], [horizon/vanishing line placement], [negative-space percentage], [figure/object placement]. Keep a quiet wide-frame rhythm and a single unmistakable focal anchor.

Visual medium and shape language:
[Adapted route module]. Keep the underlying space legible. Use [one motion treatment] only where emotionally meaningful.

Palette and lighting:
[3–5 palette colors or approximate hex anchors]. [One primary lighting phrase]. Maintain [contrast and saturation intent], with warm color limited to [specific function].

Material event:
Make [principal material] the single emotional material event: [behavior in the scene]. Support it only with [one secondary texture].

Human treatment:
[No person / distant small figure / back-facing figure / cropped walking fragment / side silhouette / translucent presence]. No identifiable facial features, likeness, branded clothing, or character-design emphasis.

Typography:
Place the single original Japanese phrase “[microcopy]” once in [negative-space location], using [thin Mincho-like / restrained handwritten] glyphs in [color/contrast], approximately [size relationship]. Correct Japanese characters, no other words, no credits, no lyrics, no logo treatment.

Output:
Landscape 16:9, coherent high-resolution cinematic still, intentional quiet negative space, materially believable light, fresh composition derived from the source scene rather than a recreation.

Avoid:
[compiled negative constraints].
```

For `text=none`, replace the typography paragraph with: `No text, captions, letters, symbols, credits, logos, or watermarks anywhere in the image.`

## 11. Negative constraints and inspection

Always compile negatives from the relevant groups; write them as one clear sentence rather than a keyword dump.

### Identity and copying

- no recognizable face or photorealistic identity likeness
- for `redraw` only: no exact source pose, wardrobe, hairstyle, prop arrangement, or camera recreation; for `preserve-edit`: do not invent or sharpen identity details beyond the hard locks
- no named MV frame, band member, album cover, title card, logo, or lyric

### Preserve-edit integrity

- no full-image regeneration when `transform_mode=preserve-edit`
- no subject replacement, pose/scale/horizon/major-geometry shift, or background re-layout outside editable zones
- no loss of the source's principal texture, lighting direction, or focal-anchor relationship
- no uniform watercolor, anime, paint, grain, or color-wash filter over the entire frame
- no unrelated new characters, props, logos, or decorative clutter; any added line-drawn figure must be tiny, anonymous, source-anchored, and explicitly part of the requested style stack
- no colored line-drawn person: the added line-figure layer must be pure white only, with no black, cobalt, red, colored fill, or multicolor clothing
- no accidental crop, stretch, letterbox, mirrored fill, repeated tile, or artificial sidebar

### Composition

- no giant centered anime face, character sheet, poster montage, split screen, collage border, duplicated person, or crowded group
- no stretching, letterboxing, mirrored background fill, repeated tiles, or artificial sidebars

### Style and material

- no glossy 3D render, generic commercial anime polish, neon cyberpunk, fantasy spectacle, vaporwave gradient, or maximalist texture soup
- no uniform watercolor filter over the whole image; no simultaneous paint + smoke + glass + fire + flowers + particles
- no random glitch carpet, arbitrary digital noise, or disconnected decorative brush swatches; distortion must follow a source edge or gesture
- no excessive film grain, chromatic aberration, bloom, or motion blur

### Text and technical residue

- no extra words, garbled pseudo-Japanese, subtitles, credits, Bilibili UI, playback controls, watermarks, or screenshot bars
- no malformed anatomy, floating limbs, duplicated hands, or unreadable focal object

After generation, inspect once and report:

```text
scene continuity: pass / concern
composition read: pass / concern
expression read: pass / concern
source-content retention: pass / concern
unchanged-anchor integrity: pass / concern
Yorushika style strength: pass / concern
style-stack hierarchy (line figure / ink-watercolor / broken distortion): pass / concern
white-line integrity: pass / concern / not applicable
graphic-overlay locality: pass / concern / not applicable
distortion alignment with source geometry: pass / concern / not applicable
identity removal: pass / concern
16:9 composition: pass / concern
dominant route legibility: pass / concern
single material event: pass / concern
text count and glyph fidelity: pass / concern / not applicable
logo/UI/lyric residue: pass / concern
exact-frame-copy risk: pass / concern
```

Do not automatically regenerate on a concern. Show the result and state the concern so the user can decide whether to request a revision.
