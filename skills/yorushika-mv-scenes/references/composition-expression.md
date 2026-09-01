# Composition & Expression Pass

This reference defines the first pass of `$yorushika-mv-scenes`: understand the supplied image as a composed statement before applying any Yorushika-derived visual treatment. It borrows the useful decision tools of the Gathered Scenes Zine approach—Scene Card, semantic minimum, visual-weight map, source-shape extraction, active negative space, and an abstraction map—without copying that skill's poster format, torn-paper requirement, or author branding.

## 1. Scene Card

Record only what is visibly supported by the image:

```text
source_orientation: landscape / portrait / square, from EXIF-oriented source dimensions
target_aspect: approximately landscape 16:9 / portrait 3:4; square defaults to approximately landscape 16:9; framing preference, not exact pixel equality
human_subject_present: true / false, judged by composition and narrative role rather than incidental passers-by
human_treatment: add-white-protagonist / cover-existing-heads / user-override
human_subject_details: primary subjects' positions, actions, protected bodies, entire visible head regions; if adding, back-facing torso, natural over-shoulder look back, weight-bearing support, action/contact and occlusion
core_subjects: 1–2 forms that make this specific scene identifiable
supporting_elements: 2–3 forms that establish place, time, or atmosphere
spatial_invariants: horizon, shoreline, vanishing line, relative positions, scale, overlap, facing direction
dominant_gesture: strongest horizontal, vertical, diagonal, curve, convergence, gaze, or movement
visual_weight_map: major light/dark masses, saturation pockets, texture density, isolation, and edge tension
native_color_atmosphere: dominant hue family, temperature, value range, and meaningful minor colors
source_shape_candidates: 1–2 contours, planes, silhouettes, shadows, or paths that can carry later graphic marks
natural_quiet_areas: low-information sky, water, wall, haze, ground, or empty space
semantic_minimum: smallest set of forms and relationships that still identifies this exact scene
expression_read: one sentence naming the visual tension, such as waiting-versus-departure or warmth-versus-erasure
eye_path: entry → anchor → material/graphic intervention → quiet exit
```

Do not begin with style words. First state where the eye enters, what it recognizes, what holds the emotional weight, and where the frame is allowed to breathe.

## 2. Composition invariants and visual weight

Mark the following as hard locks unless the user explicitly releases them:

- dominant horizon, shoreline, road, architectural axis, or perspective convergence;
- relative scale and position of the core subject(s), including existing bodies, clothing and poses;
- the dominant gesture that gives the frame its movement;
- the main light direction and the largest value relationship;
- the source-specific material that carries the scene (water, stone, fabric, paper, foliage, glass, or dust).

Visible heads selected for coverage and a new figure's footprint are authorized editable regions even under strict preservation. Follow [human treatment](human-treatment.md); do not lock facial detail against the required head scribble. Resolve these regions before applying style. Frame extension follows the resolved target aspect while keeping the source axis and subject proportions.

Use the weight map to decide where stronger graphic treatment can live. High-weight areas may receive a sharp contour or break; quiet areas can receive a broader wash or the new sketched protagonist where action, support and visibility fit. Do not distribute effects evenly merely to make the style visible.

## 3. Abstraction map

For each candidate graphic area, decide:

- **retain:** the 1–2 defining forms or relationships that must remain legible;
- **merge:** repeated waves, rock strata, foliage, windows, or texture into a calmer mass or rhythm;
- **omit:** clutter, redundant micro-detail, unrelated signage, and decorative noise;
- **transform:** selected edges into broken ink lines, flat planes, translucent watercolor, or displaced print fragments;
- **expose:** leave negative space so the image can pause around the intervention.

Medium abstraction is the default. Strong style means stronger transformation of selected areas, not loss of the semantic minimum or a generic replacement background.

## 4. Eye-path translation into Yorushika grammar

After the Scene Card is complete, translate the image in this order:

1. Keep the source-derived axis or gesture as the compositional spine.
2. Place one primary graphic event on that spine: a contour break, wash, or displaced edge.
3. Apply the resolved human branch: add one legible **pure-white** sketched protagonist if no human subject exists, with a back-facing torso and natural over-shoulder look back, choosing stable action, scale and contact from the scene; otherwise preserve existing subjects' bodies/poses and obscure their entire visible heads with dense white hatching and horizontal scribbles. A head outside the frame is not added. The branch is common to all routes, not conditional on whether a decorative figure would suit the style.
4. Use the quiet area for breathing room or a single micro-text element only if text is requested.
5. Let the eye exit through an unfinished contour, fading wash, or unprinted quiet field.

## 5. Strong graphic-soliloquy stack

When `style_intensity=strong`, use a hierarchy rather than a pile of effects:

### Primary: line-drawn presence

- the resolved human branch in uneven **white-only** ink/pencil/chalk strokes;
- for a new protagonist: a back-facing torso and natural over-shoulder look back, believable joints and support, slightly abstract scrawled contours and hatching with body gaps, scene-derived scale, and dense coverage of the entire visible head;
- for existing subjects: protected body anchors and dense local head scribbles; maintain the head's general scale without showing identity;
- connect the treatment to the source-derived axis and eye path while keeping environmental anchors legible.

The figure layer is deliberately white so it reads as a luminous memory mark against dark photo areas or watercolor fields. Other scene contours may use graphite, indigo, cobalt, or muted rust, but those colors must not enter the line-drawn person.

### Secondary: ink-and-watercolor atmosphere

- one broad translucent sumi-ink or watercolor wash that follows the dominant gesture;
- visible bloom, feathering, pigment pooling, dry-brush gaps, and paper-like bleed;
- preserve photographic texture beneath and beside the wash; keep the wash bounded rather than a global filter.

### Tertiary: broken print/distortion event

- one controlled fracture: displaced contour shards, torn registration, RGB offset, scanline break, or a short dissolving segment;
- align the break with the horizon, foam curve, rock ledge, path, or other source geometry;
- use a few cobalt/indigo and muted rust echoes, never random glitch across the whole frame.

The stack should feel emotionally motivated: the drawn figure can suggest distance, the wash can carry memory or weather, and the broken edge can express interruption or erasure. Keep the original composition recognizable even when 30–55% of its visible surface receives some form of structured intervention.

## 6. Final expression sentence

Before compiling the production prompt, write one internal sentence in this form:

```text
The scene expresses [tension] through [dominant gesture/material], so the graphic treatment follows [source axis] with [line-drawn presence], [ink/watercolor behavior], and [one controlled break], while [hard locks] remain intact.
```

The planned protagonist is an intentional addition when the human branch requires it. If its action/contact or any supporting effect cannot be grounded in the source, revise its placement or reduce the supporting style stack and return to the Scene Card.
