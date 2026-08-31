# Postcard Prompt Compiler

Use this compiler only after a real MV artwork has been saved or selected. For upstream scene generation, use the base skill's compiler instead. Write the image prompt in English, with the selected Chinese lyric text quoted exactly. Keep the compiled prompt internal.

## Resolve before prompting

Record:
- MV file path and actual oriented dimensions; whether it was reused or newly generated.
- Its recognizable scene anchors, existing line figure or local head-cover marks, ink field, fracture, lighting, source lettering and microcopy.
- Native artwork placement and adaptive landscape 4:3 outer dimensions; retain a portrait MV's portrait aspect and full extent within the card.
- Source-derived paper color, one main boundary blend and the chosen level of aging.
- Actual logo file or exact wordmark, if selected; the exact Chinese excerpt and its intended line breaks.
- For `lyrics=auto`, follow [lyric selection](lyric-selection.md) and read candidate context in [geci.md](geci.md). Record the source song, translator when present, file line numbers, 1–4 selected translation lines, visible anchors and emotional matching reason in the project notes. Preserve wording and punctuation. Pass only that excerpt as exact text to render; keep source metadata and selection notes outside the artwork unless requested. User-designated text, `lyrics=none` and the legacy `poem=none` alias take precedence over auto selection.
- Editable paper/periphery zones and protected subjects, source text and white-line marks.

Stage 2 references:
1. **EDIT TARGET:** the finished MV artwork, not the original unprocessed photo.
2. **SUPPORTING SIGNATURE ASSET:** the inspected logo PNG, only if used.

Use the chosen generated scene as actual image input. Do not include research frames, historical postcard scans or an unrelated visual style reference. A filename written in prose does not supply the image.

## Prompt structure

Populate this outline with concrete decisions; omit unused optional sections.

```text
Create one flat landscape 4:3 postcard front from reference image 1,
which is the already finished MV artwork. Preserve that artwork's
composition and graphic treatment as the scene inside the card.

The artwork is [w] by [h] pixels. Keep its complete native-size extent
at scale 1, located at [x,y] within a [W] by [H] pixel card; add paper
outside it. These refer to actual output pixels. Keep the artwork's
aspect, perspective, core object sizes and relative positions intact.

The scene carries [anchors, eye path and emotional relation]. Retain
its [white figure or local head scribbles, ink field, print fracture and lighting].
Keep body hatching gaps and dense head scribbles as inherited, with
pure-white drawing strokes. Retain photographic bodies and do not
reveal covered head details or add another figure. Protect [edge subjects,
native signs and existing microcopy]. Preserve source textures.

Use [paper color and source-grounded reason] stock with [specific
light aging cues]. The image and paper share the same subtle fiber
surface and ink absorption. Integrate [selected peripheral zones]
with [one blend treatment]. Keep the focal region crisp enough and
allow its existing ink edges to continue gently onto the paper.
Keep the existing MV style stable while composing the postcard.

Use [placement and reading order], with open paper mainly at
[location] and sufficient clearance around the image and text.

[If signature: reference image 2 is the exact signature asset; keep
its emblem and lettering together, aspect ratio and recognizable
geometry. Place it once in the lower paper at a quiet scale.]
[If wordmark: place the exact lowercase word "yorushika" once.]
[If lyrics: typeset this exact supplied Chinese lyric excerpt in
[ink/Chinese typeface/location], separated from
[existing microcopy/signature/scene]. Preserve every character and
punctuation mark, using the specified layout line breaks:
[exact selected Chinese excerpt]]
[If no new lyrics: retain existing microcopy and add no lyric text.]
[If no added text: add no new signature or lyrics; preserve native
photographed signs. Follow any explicit request about existing text.]

Deliver one finished flat postcard filling the canvas. Preserve
the artwork while limiting edits to paper, print-surface treatment,
peripheral integration and the chosen typography. Avoid changed
scene geometry, cropped source objects, extra figures, recolored
white outlines, heavy distress, blurred halos, dimensional framing,
desk mockups, duplicate signatures, UI, watermarks, unselected text and
unrelated added logos.
```

## Inspect the actual output

Measure the saved file; require `3*canvas_width == 4*canvas_height`. Compare artwork scale and composition with the actual MV input rather than the original photo. Pixel values in the prompt are intentions, not proof of preservation.

Check the scene first, then the paper connection, then the type. Compare every rendered Chinese lyric character and punctuation mark with the exact selected corpus excerpt; verify the 1–4 source-line count separately from layout wrapping. Inspect retained Japanese signs and logo lettering too. Treat inability to verify native scale, a dimensional mismatch, damaged lettering or lost figure/head coverage as a concern; preserve the output as a draft and describe the specific discrepancy. Do not automatically make a second style variant.

Keep original, intermediate and postcard files separately. The final response should emphasize the image, paper choice, preserved MV features, selected Chinese lyrics with source song/translator when available and matching reason, and any material concern, with actual dimensions and a saved path.
