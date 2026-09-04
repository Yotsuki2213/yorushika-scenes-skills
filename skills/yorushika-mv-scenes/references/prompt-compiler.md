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
11. Negative constraints

## 1. Source distillation record

Before writing the prompt, form this internal record from the attached image:

```text
source_width/source_height: actual source dimensions after EXIF orientation
source_orientation: landscape / portrait / square
target_aspect: approximately 16:9 for landscape or square; approximately 3:4 for portrait, unless explicitly overridden; a framing preference
human_subject_present: true / false, based on compositional/narrative role, not incidental passers-by
human_treatment: add-white-protagonist / cover-existing-heads / user-override
human_subject_details: positions, actions, protected body anchors and visible head regions
figure_plan: location, depth plane, scale basis, action, back-facing torso, natural over-shoulder head turn, weight-bearing support, contact/occlusion and eye-path relation for addition; entire visible head-coverage regions for either branch
style_references: 1–2 inspected bundled line images when drawing is needed; separate from the scene edit target
scene_type: exterior / interior / liminal / object-led
preserve_anchors: 3–6 concrete elements actually visible in the source
transform_mode: preserve-edit by default / redraw only when explicitly requested
preserve_strength: strict / balanced / loose; balanced by default
style_intensity: restrained / strong / expressive; strong when a forceful Yorushika treatment is requested
line_figure_color: white-only (white ink / white pencil / white chalk-like stroke); never black, cobalt, red, or colored fill
hard_locks: existing bodies/clothing/poses, main objects, major geometry, horizon/axis and foreground material; exclude authorized head/figure regions
soft_locks: details that may receive restrained line, color, grain, or light treatment
editable_zones: visible heads to cover or the new figure footprint, bounded style regions and target-aware natural extension
remove_only: watermark, UI, or clutter explicitly marked for removal; otherwise leave source marks intact
source_texture_to_keep: photographic grain, water/sand/stone/fabric detail, and other textures that must remain legible
style_stack: source-anchored line-drawn presence / ink-watercolor field / one broken-distortion event, in a clear hierarchy
style_overlay_budget: 10–30% restrained, 30–55% strong, 45–65% expressive; structured regions only, never a uniform whole-frame filter
spatial_relations: foreground, middle ground, background, horizon, window/door/road axes
time_weather: observable light and atmosphere; do not invent a season unless visually supported
dominant_geometry: horizontal bands / vanishing road / window grid / isolated object / open field
human_presence: observed primary people or incidental background people; note visible and off-frame heads
identity_to_obscure: entire visible heads including crown, hair, face, ears and back of head; preserve body/clothing/pose unless the user requests other changes
incidental_to_remove: only source elements explicitly authorized for removal; do not erase background people or signs by default
material_candidates: water, sand, hair, paper, paint, glass, dust, cloth, shadow, firelight
emotional_tension: one concise relation such as waiting-versus-departure or brightness-versus-erasure
expression_read: one sentence describing how composition and material express the emotional tension
visual_weight_map: dominant light/dark/saturated/isolated masses and edge tension
eye_path: entry → focal anchor → graphic/material intervention → quiet exit
abstraction_map: retain / merge / omit / transform / expose decisions for each editable zone
```

In `preserve-edit`, preserve source content and relationships outside the authorized edit zones. In explicit `redraw`, re-author the unlocked environment from its semantic anchors; the resolved human branch, orientation, and existing body/clothing/pose/scale anchors still apply unless the user expressly releases them.

Follow [human treatment](human-treatment.md) for anonymity: obscure visible primary heads without shrinking or replacing bodies. Describe preserved clothing by its visible role rather than inventing identity, demographics, celebrity likeness or branding.

## 2. Composition and expression pass

Do not select a style route until the source has been read as a composed statement. Build a compact Scene Card containing:

- core subjects and supporting elements;
- spatial invariants and dominant gesture;
- visual-weight map and natural quiet areas;
- semantic minimum, resolved human branch/figure plan, source orientation/target aspect, and 1–2 source-shape candidates; for an added figure, the plan must settle location, depth, scale basis and support before action styling;
- one-sentence `expression_read` and an `eye_path` of entry → anchor → intervention → exit.

Then make an `abstraction_map` for the editable regions: what to retain, merge, omit, transform, and leave blank. Preserve the dominant axis, subject scale, value hierarchy, and source material before adding any graphic treatment. Style is a second pass attached to real contours, planes, shadows, paths, or material events—not a collection of detached effects.

## 3. Preserve-edit policy

Use `preserve-edit` as the default. The attached image is the edit target and must remain visibly present beneath the style treatment. Write the prompt as a constrained in-place edit rather than as a request for a new composition.

| preserve_strength | What to lock | What may change |
|---|---|---|
| `strict` | Target roughly 80–90% of source structure/pixels: bodies, clothing, poses, scale, geometry, lighting and principal texture | Authorized head coverage/new figure footprint, local accents, natural frame extension if needed, and watermark repair if requested |
| `balanced` | Keep protected subjects and roughly 60–80% of source structure, spatial relationships, and texture | Authorized human treatment, bounded simplification, target-aware natural extension and a source-anchored graphic field |
| `loose` | Keep the primary subject and semantic anchors | Larger environmental edits and stronger local stylization; still do not replace the entire image |

Required head coverage and a readable new protagonist remain allowed at every preservation/intensity setting. `style_intensity` controls supporting effect strength without releasing the other composition locks:

- `restrained`: 10–30% local intervention, one or two edge accents, and no broad wash.
- `strong`: 30–55% structured intervention across one primary graphic field plus one or two subordinate pressure points. Use a clear three-part stack: line-drawn presence, ink/watercolor atmosphere, and one controlled break.
- `expressive`: 45–65% structured intervention with larger washes and more visible fractures, while keeping the semantic minimum, source axis, and focal-anchor placement intact.

For `mode=graphic-soliloquy` in preserve-edit, use the following overlay budget and hierarchy:

- Keep the original underlay, subject, horizon/axis, and source texture readable.
- Apply the already resolved human branch: one readable **white-only** sketched protagonist with a scene-grounded action/contact, or dense local white head scribbles on the existing subjects with their bodies preserved. Use white ink/pencil/chalk-like strokes; body hatching has gaps and head coverage may be dense. Do not add an extra figure through this route module.
- Add one broad but bounded sumi-ink/watercolor wash with visible bloom, pigment pooling, feathering, and dry-brush gaps, following the source gesture rather than floating decoratively.
- Add one controlled broken/distortion event—displaced contour shards, torn registration, RGB offset, scanline fracture, or a dissolving edge—aligned with source geometry.
- Add irregular ink/graphite contours and cobalt/indigo plus one restrained rust echo only at selected scene boundaries, not on every contour and never on the white line-drawn figure.
- Grade locally toward deep blue, cobalt, black, or dirty white while retaining the source's unedited colors elsewhere.
- Do not repaint the whole photograph, replace the subject, move the camera, or apply a uniform watercolor/animation filter.

If the user asks to remove a watermark, place it in `remove_only` and reconstruct only the immediately adjacent texture. Do not erase unrelated text, marks, or source detail. If the user does not ask for removal, preserve source marks unless they are a generated UI artifact.

### Shared human and reference block

Apply [human treatment](human-treatment.md) before every route and in both templates. Background passers-by alone do not constitute a human subject. Preserve existing subject bodies, clothing and action; cover all visible primary heads locally, including back views. For fully hidden or off-frame heads, record coverage as not applicable without inventing a head or person. If no human subject exists, first resolve one scene-supported protagonist's `location`, `depth`, `scale_basis`, `support_contact`, `occlusion` and `eye_path`, then choose the compatible action. Match the figure's size to the scene perspective and nearby scale references; a distant figure may occupy a small part of the frame while its silhouette, action direction, weight and head scribble remain readable. Use a back-facing torso and natural look back over one shoulder when the connected joints and support can carry it. Cover the entire visible head, including crown, hair, face, ears and back of head; no features may read through. Preserve existing subjects' poses instead of imposing the new-figure turn on them.

When drawing is needed, inspect and attach 1–2 relevant bundled line references. Clearly label the user's scene as EDIT TARGET and the others as SUPPORTING LINE STYLE ONLY. Use the actual image-attachment mechanism, not filenames in prompt prose alone. Extract hand-drawn wobble, white contour/hatching, body gaps and head scribble density. Do not import backgrounds, large white preparation masks, exact poses or props. If unavailable, disclose the missing references and use the written grammar.

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

For sea, sky, field, roofline, or distant landscape. Use a static wide shot, horizon around the lower third, 55–70% quiet sky/wall/air, one small off-center anchor, restrained perspective, and quiet spacing within the resolved frame. For portrait inputs, retain the vertical depth and source axis rather than forcing a wide horizon.

### B. Low walking fragment

For roads, paths, shorelines, feet, fabric, or movement. Use the source's low viewpoint or existing body fragment; let the road edge or shoreline create a diagonal and use one controlled motion smear. Do not crop away a visible head merely to bypass its coverage. In preserve-edit, keep the existing viewpoint and body extent.

### C. Window-and-desk geometry

For interiors, writing, reading, waiting, or phone/table scenes. Use a side-view medium-wide shot; window grid or doorway as structural lines; high-key window light or one desk lamp; retain the subject's body scale and perform the resolved head coverage, or add the planned protagonist with a supported action.

### D. Isolated material stage

For dark interiors or object-led references. Use a sparse wide shot with 65–80% dark negative space, one pool of light, one figure/object, one long shadow, and one principal material event.

### E. Translucent memory overlap

For reflections, movement, hats, foliage, water, or emotionally doubled scenes. Keep the base photograph-like space readable, then place one irregular translucent paint/print layer across only 20–35% of the frame. Do not turn the whole image into watercolor.

Resolve approximate framing from EXIF-oriented dimensions: landscape → about 16:9, portrait → about 3:4, square → about 16:9 by default; explicit framing requests override this. Accept native generated dimensions near these targets. Extend necessary edges only when composition benefits, placing extension around protected anchors. Preserve the scale and body proportions of existing subjects; for a new figure, follow the resolved depth-based scale and do not enlarge it merely to increase prominence. Do not crop important subjects, stretch, mirror, tile or letterbox. Adapt modules to the resolved orientation and preserve-edit locks.

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
After the composition and expression are solved, apply a forceful but source-anchored Yorushika graphic stack. Keep the real scene as the underlay and follow its dominant axis: apply the resolved **white-only** human treatment (a scene-supported sketched protagonist, or local dense head scribbles with source bodies preserved); lay one broad bounded sumi-ink/watercolor wash over a meaningful plane with visible bloom, pooling, feathered edges, and dry-brush gaps; then add one controlled broken/distortion event such as displaced contour shards, torn registration, RGB offset, scanline fracture, or a dissolving edge. Use cobalt/indigo, dirty white, graphite black, and at most one restrained rust echo for the scene treatment, but keep the figure layer pure white with no colored fill. Let the stack affect roughly 30–55% of the frame through connected fields and edge interruptions, while the source subject, geometry, light direction, and material texture remain legible. Never scatter random glitch, draw a cute mascot, or apply a uniform filter.
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
Dominant sunlit-memory controls the source-aware spatial rhythm and exposure; graphic-soliloquy adds a bounded dry-brush scene-edge treatment; nocturnal-material contributes a darker shadow or existing reflective object. The white human branch and resolved target aspect stay unchanged.
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

If the user supplies text, preserve its exact wording but still use it once. For `text=none`, suppress added typography while preserving native source text unless its removal is explicitly requested.

## 9. Preserve-edit prompt template

Use this template whenever `transform_mode=preserve-edit` (the default). Replace every bracketed field and delete unused clauses. The percentages are art-direction targets, not a claim of pixel-perfect control.

```text
Use case: constrained reference-image edit for one cinematic [target_aspect] raster image.

Transform mode:
preserve-edit, preserve_strength=[strict / balanced / loose], style_intensity=[restrained / strong / expressive]. The attached source image is the edit target. Do not generate a replacement image from scratch.

Reference roles and resolved decisions:
[source image] is the EDIT TARGET. [Selected line references, if needed] are SUPPORTING LINE STYLE ONLY: borrow white contour/hatching and head scribbles, not their backgrounds, white preparation masks, exact pose or props. Source orientation=[source_orientation], target=[target_aspect], human_subject_present=[true/false], human_treatment=[resolved branch].

Composition and expression read:
The source expresses [tension] through [dominant gesture/material]. The eye path is [entry] → [focal anchor] → [graphic/material intervention] → [quiet exit]. Preserve [semantic minimum, visual-weight hierarchy, and source axis] before styling.

Source invariants (hard locks):
Keep [existing bodies/clothing/poses and main objects], [major spatial relationships], [horizon or architectural axis], [foreground material], and [source texture] intact outside the authorized human and style zones. Preserve body position, scale and material readability; the visible heads listed below are intentionally editable. For an added figure, follow the resolved [location], [depth], [scale basis], [support/contact] and [occlusion] from the Scene Card. Preserve [observable time/light direction] and the emotional tension of [concise tension].

Soft locks and editable zones:
Allow only restrained stylization of [soft-lock details]. Authorize [visible head regions or new figure footprint] for the resolved human treatment, including under strict preservation. Apply supporting route treatment inside [bounded editable zones] and extend [necessary edges] naturally into [target_aspect] while retaining the original focal anchor and body proportions. Keep all non-editable regions visually continuous with the source.

Watermark/removal scope:
[If requested: remove only the watermark in [location] and reconstruct adjacent [water/rock/sky/paper] texture; retain all unrelated source marks and detail.] [Otherwise: do not remove or invent source text/marks.]

Route and weighting:
[mode and weights]. Keep the original scene as the underlay; use the route only as a localized edge, material, color, or atmosphere intervention within the editable zones.

Graphic-soliloquy overlay (when selected):
Add a clear but source-anchored stack at the selected intensity: [the resolved pure-white human treatment, without an additional route-specific figure], [one broad bounded sumi-ink/watercolor wash with bloom, pooling, feathering, and dry-brush gaps], and [one controlled broken/distortion event aligned to a source edge]. The line-drawn figure layer must use white ink, white pencil, or white chalk-like strokes only; never black, cobalt, red, colored fill, or multicolor clothing. Add irregular ink-and-graphite contours and restrained cobalt/indigo plus one rust print echo only on selected scene boundaries, never on the white figure. Target [10–30% / 30–55% / 45–65%] of the frame according to `style_intensity`; leave the original subject, geometry, light direction, and material texture legible elsewhere. Do not apply a uniform filter or scatter unrelated glitch.

Camera and composition:
Keep the source camera viewpoint, horizon/vanishing line, crop logic, and focal-anchor placement intact. [If needed: naturally extend the selected edges to target_aspect; never crop important subjects, stretch, mirror, tile, or letterbox. Keep portrait sources vertically composed.]

Palette and lighting:
Retain the source palette as the base. Add [3–5 restrained route colors] only as local grading or marks. Preserve [primary lighting phrase], shadow direction, and exposure relationship; keep warm color limited to [specific function].

Material event:
Keep [principal source material] readable as the emotional material event. Let [one route accent] interact with it without replacing its texture. Support it only with [one secondary texture].

Human treatment:
[No human subject: add one readable pure-white sketched young man or young woman at [scene-derived location] in the [foreground/middle ground/background] depth plane. Set [scale] from [perspective lines and nearby scale references]; a distant figure may occupy a small part of the frame while remaining readable through silhouette, action direction, weight and head scribble. Use [scene-supported action] with [weight-bearing support, connected joints, contact and occlusion] physically believable. Use a back-facing torso and natural over-shoulder head turn when the resolved body relationship supports it. Use slightly abstract, loosely scrawled broken contours and uneven body hatching with transparent gaps. Cover the ENTIRE visible head, including crown, hair, face, ears and back of head, with dense irregular white hatching and horizontal scribbles; no head features read through. One person in one moment.]
[Existing human subject(s): keep [bodies/clothing/poses/positions/scales] intact. Cover [each entire visible primary head region, including crown, hair, face, ears and back of head] with dense irregular white hatching and mostly horizontal scribbles until none of the original head details can read through. Keep the existing pose and head placement; do not impose a back-facing/looking-back pose on an existing subject. Preserve nearby neck/body landmarks. Do not add another person. Hidden/off-frame heads remain hidden/off-frame.]
[Explicit human override: apply the user's instruction consistently.]
Compile only the applicable branch; retain the resolved scene-grounded location, depth, scale, contact and eye path, plus pure-white stroke contrast.

Typography:
[For text=auto: place the single original Japanese phrase “[microcopy]” once in [editable negative-space location], using [thin Mincho-like / restrained handwritten] glyphs in [color/contrast], approximately [size relationship]. Correct Japanese characters, no other words, no credits, no lyrics, no logo treatment.] [For text=custom: use exactly “[user text]” once and no other text.] [For text=none: no added text, captions, letters, symbols, credits, logos or watermarks; preserve native source text unless removal is requested.]

Output:
[Resolved orientation and approximate target_aspect; native generated dimensions are acceptable]. Preserve the source image as the dominant visual evidence, with a localized graphic-soliloquy treatment and coherent high-resolution finish. No whole-frame regeneration, subject replacement, or re-layout outside editable zones.

Avoid:
[compiled preserve-edit integrity, identity, text, and technical negative constraints].
```

## 10. Full prompt template (redraw fallback)

Use the following template only when `transform_mode=redraw` is explicitly requested. It intentionally permits a fresh composition while retaining the identity and copyright safeguards.

Replace every bracketed field. Remove unused clauses rather than leaving placeholders.

```text
Use case: reference-image scene transformation for a single cinematic [target_aspect] raster image.

Transform mode: redraw (explicit opt-in only). Re-author the unlocked scene from semantic anchors; retain the resolved human branch and protected body anchors unless explicitly released. Do not use this template for default preserve-edit.

Reference roles and resolved decisions:
[Source scene] supplies the scene anchors. [Selected line references, if needed] supply ONLY white contour/hatching, body gaps and head scribbles; do not copy their backgrounds or large white preparation masks. Source orientation=[source_orientation], target=[target_aspect], human_subject_present=[true/false], human_treatment=[resolved branch].

Composition and expression read:
The source expresses [tension] through [dominant gesture/material]. Preserve the source-derived [axis/visual-weight hierarchy/eye path] while re-authoring the environment.

Primary request:
Re-author the unlocked environment using a distilled early Japanese alternative-music-video scene grammar. Preserve [3–6 scene anchors], [existing subjects' body/clothing/pose/scale/position anchors unless explicitly released], and their essential spatial relationship: [relationship]. Preserve the observable [time/weather/light cue] and [concise tension]. Re-author [unlocked architecture/props/vegetation] while applying the required human treatment. Do not reconstruct a recognizable facial identity or copy supporting reference compositions.

Reference-image use:
Treat the input as scene evidence for the permitted redraw while retaining protected body anchors. Obscure [visible primary heads] or add [one planned protagonist] according to the human branch; remove only [other explicitly authorized elements]. [If needed: extend the necessary environment edges into target_aspect, preserving portrait or landscape orientation; do not stretch or letterbox.]

Route and weighting:
[mode and weights]. [One sentence explaining how dominant, secondary, and optional tertiary roles divide composition, material, and atmosphere.]

Scene and subject:
[New authored scene description built from the preserved anchors, including foreground/middle ground/background and one principal action or state.]

Camera and composition:
[One composition module], [shot scale], [viewpoint], [horizon/vanishing line placement], [negative-space percentage], [figure/object placement]. Keep quiet spacing adapted to the resolved orientation and a clear visual hierarchy.

Visual medium and shape language:
[Adapted route module]. Keep the underlying space legible. Use [one motion treatment] only where emotionally meaningful.

Palette and lighting:
[3–5 palette colors or approximate hex anchors]. [One primary lighting phrase]. Maintain [contrast and saturation intent], with warm color limited to [specific function].

Material event:
Make [principal material] the single emotional material event: [behavior in the scene]. Support it only with [one secondary texture].

Human treatment:
[Compile the same resolved human branch as the preserve-edit template: one slightly abstract scrawled white young man or young woman at the Scene Card's location and depth, with scale matched to perspective and nearby references, plausible joints/balance/support/contact and a fully scribbled head; or protected existing bodies/poses with dense white coverage on each entire visible primary head. A distant added figure may remain a small part of the frame if its silhouette, action direction, weight and head scribble stay readable. Use the back-facing torso and natural over-shoulder look back only when compatible with the resolved body relationship. Cover crown, hair, face, ears and back of head without visible features. Off-frame/hidden heads stay so; existing-subject treatment adds no extra person or pose change. Apply explicit user overrides when present.]

Typography:
Place the single original Japanese phrase “[microcopy]” once in [negative-space location], using [thin Mincho-like / restrained handwritten] glyphs in [color/contrast], approximately [size relationship]. Correct Japanese characters, no other words, no credits, no lyrics, no logo treatment.

Output:
[Resolved orientation and approximate target_aspect; native generated dimensions are acceptable], coherent high-resolution cinematic still, intentional quiet negative space, materially believable light, fresh composition derived from the source scene rather than a recreation.

Avoid:
[compiled negative constraints].
```

For `text=none`, replace the typography paragraph with: `No added text, captions, letters, symbols, credits, logos or watermarks; preserve native source text unless removal is requested.`

## 11. Negative constraints

Always compile negatives from the relevant groups; write them as one clear sentence rather than a keyword dump.

### Identity and copying

- no recognizable face or photorealistic identity likeness
- no copied character design, exact pose, props or composition from supporting style references; preserve the user's protected body anchors and obscure heads according to the branch
- no named MV frame, band member, album cover, title card, logo, or lyric

### Preserve-edit integrity

- no full-image regeneration when `transform_mode=preserve-edit`
- no replacement of protected source bodies/objects, body pose/scale/horizon/major-geometry shift, or background re-layout outside authorized edit zones; required head coverage/new figure placement is explicitly allowed
- no loss of the source's principal texture, lighting direction, or focal-anchor relationship
- no uniform watercolor, anime, paint, grain, or color-wash filter over the entire frame
- no unrelated extra characters, props, logos or decorative clutter; the planned added protagonist must be anonymous, legible, source-supported and the only default new person
- no colored line-drawn person: the added line-figure layer must be pure white only, with no black, cobalt, red, colored fill, or multicolor clothing
- no floating or perspective-breaking added figure, unsupported foot/pelvis/hand contact, or scale that conflicts with the scene's depth references; a small distant figure is acceptable when its action and contact remain readable
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
