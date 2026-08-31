# Postcard Art Direction

The card should feel like a printed memory of the finished MV scene. Start from its light, found colors, edge materials and emotional tension. The whole output is the postcard front, shown flat and filling the canvas.

## Picture, paper and space

Use the saved MV artwork as the visual center of gravity. Keep its complete composition and aspect ratio, with the native pixel extent as the default. Place it roughly in the upper central area; a small asymmetric paper margin can support an off-center subject. Choose the layout from the image's existing eye path.

Size the outer 4:3 card around the actual oriented MV dimensions `w × h`. A practical starting layout is:

```text
k = ceil(max(w / (4 * 0.90), h / (3 * 0.76)))
W = 4 * k
H = 3 * k
artwork_width = w
artwork_height = h
x = floor((W - w) / 2)
y = round(0.065 * H)
```

This sets the artwork to 1:1 and adds paper. Margin fractions are adjustable design choices. Check that the artwork fits fully inside the card and that the lower space supports the selected signature and text. For an actual 1672 × 941 MV file, this starting layout gives a 1860 × 1395 postcard with artwork at (94, 91). The MV's own ratio may be approximate; preserve that actual file rather than silently cropping it to a nominal ratio.

Use the original photo only in the upstream scene stage. Stage 2 uses the generated artwork's dimensions and content. Preserve both source files unchanged on disk. If a fixed requested card size cannot contain the native artwork and paper margins, explain the conflict without changing its scale. User-authorized resizing must remain proportional and be recorded.

For a portrait MV source, retain its vertical composition and native extent inside the landscape 4:3 card; allow wider side paper instead of stretching or cropping the artwork. The same sizing calculation applies.

Favor a generous image with modest side/top margins and useful lower paper. A wide scene can meet a soft open paper field beneath it. A strongly directional scene can carry a small text block toward the opposite side. Leave enough quiet space for the eye to exit.

## Paper color from the scene

Choose one main stock color, with a gentle tonal variation where the print meets paper. These are examples, not fixed presets:

| Scene evidence | Possible stock | Printing character |
| --- | --- | --- |
| Sunlit sky, sea, pale highlights | Warm ivory, faded sky blue, pale sand | Airy highlights, delicate warm fibers |
| Blue shadows, grey buildings, overcast street | Blue-grey, light stone, muted cream | Cool image inks balanced by slightly warm paper |
| Earth, leaves, brick, warm interiors | Oatmeal, pale sage, faded terracotta | Dry fibers and restrained uneven absorption |
| Night, deep water, isolated warm light | Dusty navy, charcoal brown, muted slate | Quiet dark stock, pale signature, protected highlight detail |

White or black may suit a scene, but paper may take any coherent user-requested or source-derived color. Keep the chosen stock visibly related to the image without washing out its main chromatic anchors.

## Natural image-to-paper integration

Choose one primary transition and at most one supporting print treatment:

- **Ink bleed:** let existing watercolor or ink at selected picture edges seep a short distance into the same paper fibers.
- **Paper fade:** gently lower density only in peripheral low-detail areas so paper tone shows through; maintain the center, meaningful silhouettes and source text.
- **Imperfect print edge:** use a narrow, irregular density falloff and a few dry-brush gaps, with shared grain across the boundary.

A starting blend band is roughly 1–4% of the shorter artwork side; adjust to actual edge detail. Use outer paper for most spill. If an important object touches an edge, keep that edge legible and blend elsewhere. Never sacrifice the semantic minimum to make a soft boundary. Avoid an even blurred halo.

Carry existing MV washes outward instead of adding a competing wash. If the MV already has paper-like or dissolving edges, reuse those cues and match their stock tone. Show continuous print absorption across picture and paper so the photograph feels part of the card surface.

Keep the final piece flat. Dimensional picture frames, cast-shadow photo mounts and desk mockups change the object being designed. Do not add postcard-back address rules, recipient details or postal claims to the front. Stamps, seals or dates are optional only when requested or factually supplied.

## Light vintage character

`age=light` is the default: fine fibers, slight warmth or fading appropriate to the chosen stock, faint perimeter oxidation, and modest ink-density variation. Pick two or three quiet cues, not a full distress kit.

`age=none` uses fresh printed paper with natural grain. `age=moderate` may increase edge patina and local density variation while keeping the scene and lettering clear.

Apply age chiefly to paper and the image boundary. Preserve the source's weather and lighting, retain meaningful saturated colors, and keep the figure/head-cover strokes pure white rather than staining them sepia. Preserve body hatching gaps and the density of head scribbles; do not reveal covered head details. Avoid heavy scratches, dirt, large tears, deep creases or global yellowing unless explicitly requested.

## Signature and Chinese lyrics

Treat the image, inherited microcopy, selected Chinese lyrics and signature as a single reading order. In `lyrics=auto`, coordinate the excerpt with inherited microcopy; existing microcopy alone does not disable lyric selection. Keep source signage as part of the image rather than counting it as designed lyrics.

The signature normally sits in the lower paper, centered or aligned to the excerpt. About 8–15% of card width is a useful starting size; preserve the logo's aspect ratio and clear space. Select the bundled black or white asset by contrast on the chosen paper, not by a binary paper-color rule. For a supplied colored logo, retain its colors unless a permitted variant exists. Use the actual PNG as a supporting reference.

For automatic lyrics, follow [lyric selection](lyric-selection.md), reading candidate passages in [geci.md](geci.md). Select 1–4 Chinese translation lines from one song according to visible motifs and emotional tone. Preserve the corpus wording and punctuation; choose a coherent short excerpt suitable for the available paper. Use Chinese Song/Ming-style serif or restrained handwritten type in a legible ink color drawn from the artwork. Preserve user-designated wording and check every rendered Chinese glyph against the selected text.

Place the Chinese lyrics mainly in the open paper, separated from the signature and important scene details. A subtle relationship to the image boundary is welcome, but not text crossing a figure or focal object. Keep song and translator metadata in project notes and the response unless the user requests an on-card credit. Respect `lyrics=none`, its legacy `poem=none` alias and explicit no-added-text requests.

## Visual acceptance

At normal viewing size:
- The MV scene is immediately recognizable and remains the focus.
- Its inherited figure or head-cover treatment, ink field and controlled fracture retain their hierarchy, with protected bodies and dense anonymous head marks intact.
- Paper and picture feel like one printed surface, with legible source edges where needed.
- Color and patina suit the scene, and the paper reads as intentional postcard stock.
- The signature and selected Chinese lyrics are clear, restrained and well separated; the excerpt matches the supplied corpus exactly and responds to the scene's elements and mood.

At file level: verify the actual 4:3 canvas and the MV artwork's scale; label measurements as unverified when natural blending or model rendering prevents proof. Do not claim a geometrically exact or print-ready result solely from its prompt.
