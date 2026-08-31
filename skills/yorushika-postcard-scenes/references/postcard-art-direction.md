# Postcard Art Direction

The card should feel like a printed memory of the finished MV scene. Start from its light, found colors, edge materials and emotional tension. The whole output is the postcard front, shown flat and filling the canvas.

## Picture, paper and orientation

Use the saved MV artwork's actual EXIF-oriented dimensions `w × h`. Preserve its complete composition, aspect and native pixel extent at `artwork_scale=1`. The outer card remains landscape 4:3. Orientation, not exact ratio equality, selects the default layout:

| Actual MV | Layout | Default lyric count |
| --- | --- | --- |
| Landscape, including near 16:9 and other wide ratios | `top-image`: upper centered image, lower signature/text | 2 Japanese/Chinese pairs |
| Portrait, including near 3:4 and other tall ratios | `left-image-right-text`: left image, upper-right logo, lyrics below it | 4 Japanese/Chinese pairs |
| Square | `top-image` | 2 Japanese/Chinese pairs |

Explicit layout preferences override placement. An explicit `lyric_lines` overrides the orientation-based count; changing layout alone does not change that count. Apply the text/signature suppression controls before assigning content zones.

### Landscape/square MV — top image

Retain the existing upper, horizontally centered artwork, with modest side/top margins and lower paper for signature, paired lyrics and final song title. A small asymmetry may support the image's eye path.

Use this starting layout, then adapt paper margins for the verified bilingual text:

```text
k = ceil(max(w / (4 * 0.90), h / (3 * 0.76)))
W = 4 * k
H = 3 * k
artwork_width = w
artwork_height = h
x = floor((W - w) / 2)
y = round(0.065 * H)
```

For a 1672 × 941 MV file, this gives a 1860 × 1395 starting card with artwork at (94, 91). The lower area must fit the default 2 pairs (or explicitly requested count), signature and title legibly. These dimensions are a starting geometry, not proof that every excerpt fits.

### Portrait MV — left image, right information column

Keep the full portrait on the left, vertically centered, with a clear gap before an independent right column. Place the logo in the upper part of that column, left-aligned lyric pairs below it, and the original song attribution after the last pair. Keep all text and signature off the image.

Use a separate starting geometry:

```text
k = ceil(max(w / (4 * 0.50), h / (3 * 0.88)))
W = 4 * k
H = 3 * k
artwork_width = w
artwork_height = h
x = round(0.05 * W)
y = floor((H - h) / 2)
gap = ceil(0.04 * W)
column_x = x + w + gap
column_right = floor(0.95 * W)
column_width = column_right - column_x
column_top = round(0.10 * H)
column_bottom = floor(0.90 * H)
```

For a 900 × 1200 MV file, this gives a 1820 × 1365 starting card, artwork at (91, 82), and a right column from x=1064 to x=1729. Size the logo proportionally within the upper column; reserve a visible break before the four bilingual groups. Japanese sits directly above Chinese within each group, with more space between groups than between their two languages. Chinese may be slightly smaller, but both must remain readable.

### Fit and preservation

Margin fractions and type size are design starting points, not fixed templates. Check that the whole artwork fits inside the card and that the selected text, logo and title fit their own region without overlap or clipping. If necessary, first select a shorter excerpt with the same required pair count, adjust margins or enlarge the 4:3 paper by increasing `k`; recompute placements while keeping `artwork_width=w` and `artwork_height=h`. Re-verify any changed excerpt before compilation.

Do not crop, stretch or silently reduce artwork scale to fit text. If a fixed user-requested card size cannot accommodate the native artwork and required content, explain the conflict before generation. User-authorized resizing must be proportional and recorded. Use only the actual generated MV artwork in this stage; preserve both original photo and MV files on disk.

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

## Signature, bilingual lyrics and original song title

Treat the image, inherited microcopy, selected bilingual pairs, song title and signature as one reading order. Existing microcopy alone does not disable automatic lyrics. Source signage remains part of the image.

Use the already verified selection from [lyric selection](lyric-selection.md). Render each Japanese original above its corresponding Chinese translation, keeping each pair together and distinguishing pair count from visual wrapping. Use compatible Japanese Mincho/Chinese Song-style serif or restrained handwritten type in a legible scene-derived ink color. Preserve wording and punctuation. After the last pair, use a separate line containing the exact `——original song title`; translator and line-number metadata stay in notes and the handoff unless requested on-card.

For `top-image`, keep the signature and lyric block in the lower paper, with clear separation; adapt alignment to the scene. For `left-image-right-text`, put the signature above the lyrics in the right column, and left-align the lyric block and final attribution. Give each language readable size, small intra-pair spacing and larger inter-pair spacing. Do not split a pair into distant areas or separate all Japanese from all Chinese.

About 8–15% of card width is a starting signature size, constrained by the chosen content region. Keep its aspect and clear space. Select the actual bundled black/white PNG by contrast on the chosen paper; retain a supplied colored logo's colors unless a permitted variant exists. Use one signature and preserve emblem and name together.

Apply `signature=none` by omitting the signature without adding a placeholder. `lyrics=none` omits lyrics and song attribution, keeping the selected image placement and intentional open paper. General no-added-text requests omit both. Explicit wording and count requests take precedence; follow the selection guide for missing bilingual text rather than adding a translation.

## Visual acceptance

At normal viewing size:

- The MV scene is immediately recognizable and remains the focus.
- Its inherited figure or head-cover treatment, ink field and controlled fracture retain their hierarchy, with protected bodies and dense anonymous head marks intact.
- Paper and picture feel like one printed surface, with legible source edges where needed.
- Color and patina suit the scene, and the paper reads as intentional postcard stock.
- The correct orientation-based layout is visible, including the upper-right signature and right-column text for portrait MV input.
- Both languages, their pair grouping and the final original-song attribution are clear, restrained and well separated. Refer to the compiler's [output checklist](prompt-compiler.md#inspect-the-actual-output) for exact text/count verification.

At file level: verify the actual 4:3 canvas and the MV artwork's scale; label measurements as unverified when natural blending or model rendering prevents proof. Do not claim a geometrically exact or print-ready result solely from its prompt.
