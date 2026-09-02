# Shared Postcard Art Direction

Read after orientation selects exactly one layout module. The final output is a flat landscape 4:3 postcard front filling the canvas.

## Fixed artwork boundary

The saved MV is `EDIT TARGET / FIXED SCENE`, not a prompt to recreate it. Keep its complete aspect and native pixel extent at `artwork_scale=1`. Lock the center, viewpoint, geometry, all bodies/limbs, gesture, support/contact, white body hatching, full-head scribbles, source text and existing microcopy.

Define `blend_band` as roughly 1–4% of the shorter MV side. This is a visible material transition, not an invisible safety margin: use enough of the band to create broad or continuous image-paper interpenetration where the perimeter permits. Combine a source-matched opacity fade with pigment/ink bleed into paper fibers, paper fade, irregular dry-brush gaps and matching print grain. Route around protected figure/action/text zones; when one reaches an edge, carry the blend outward onto paper. Never crop, shift, dissolve, repair or repaint those zones.

## Paper and print

Choose one stock color from the handoff's dominant colors and light:

- pale sky/sea → warm ivory, faded sky blue or pale sand;
- cool buildings/overcast shadows → blue-grey, stone or muted cream;
- earth/leaves/warm interiors → oatmeal, pale sage or faded terracotta;
- night/deep water/warm point light → dusty navy, charcoal brown or muted slate.

Carry existing MV washes outward instead of adding a competing wash. If the MV contains a cobalt/indigo watercolor or ink field, preserve its bloom, pooling, feathered edges and dry-brush breaks as an inherited print layer, and let a restrained portion continue into the paper. Match paper absorption and grain at the edge; avoid flattening the wash into a faint tint or an even blurred halo.

`age=light` adds only two or three quiet cues—fine fibers, slight warmth/fading, faint perimeter oxidation or modest ink-density variation—chiefly on paper and the blend band. Keep enough fiber and ink-density variation for a tactile printed-memory surface, especially where the blue wash meets paper. `age=none` stays fresh; `age=moderate` increases restrained patina. Never sepia-stain white figure strokes, globally yellow the MV, or add heavy dirt, tears and scratches unless requested.

Keep the piece flat: no dimensional frame, cast-shadow photo mount, desk mockup, postcard-back address rules or invented postal marks.

## Typography and signature

Use the exact verified Japanese, Chinese and `——原歌名` in a restrained handwritten type as the default. Let it carry the pre-2022 Yorushika hand-lettered character: uneven pressure and stroke width, slightly wobbly baselines, casual felt-pen or brush-pen rhythm with occasional dry-brush gaps—close to the scrawled Japanese microcopy in the MVs, never a polished commercial font. Chinese lines use a matching handwritten style that reads as the same hand. Keep every line readable despite the wobble; readability outranks character. Fall back to a compatible Mincho/Song-style serif only when the user explicitly requests a printed typeface or the handwritten render fails legibility. Ink color stays scene-derived and readable. Preserve punctuation. Keep translator and line metadata off-card unless requested.

Every postcard carries exactly one logo or wordmark; the signature is required card furniture, not a decoration. On light paper use the black bundled PNG; on dark paper use the white PNG. Preserve logo geometry, aspect and clear space; 8–15% of card width is a starting size constrained by the selected layout. Only the user's explicit `signature=none` or equally explicit omission request removes it; `lyrics=none` and no-added-text requests never suppress the logo.

If native artwork plus required content cannot fit a fixed user-requested size, explain the conflict before generation. Otherwise enlarge the 4:3 paper proportionally; never shrink, crop or stretch the MV to make text fit.
