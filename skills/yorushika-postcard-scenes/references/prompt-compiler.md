# Postcard Prompt Compiler

Use this compiler only after a real MV file has been obtained and analyzed and the final text has been verified. For upstream scene generation, use the base skill's compiler. Write design instructions in English; quote the exact Japanese, Chinese and original song title without translation. Keep the full prompt internal.

## Resolve before prompting

Record these decisions before calling ImageGen for a postcard:

- Actual MV path, EXIF-oriented dimensions and whether it was reused or generated.
- Visible elements, subject positions, depth, eye path, quiet areas, motion, light/color and evidence-based emotion; distinguish observations from associations.
- Protected anchors, existing body/white-line/head-cover treatment, ink field, fracture, source signs and microcopy.
- Layout (`top-image` or `left-image-right-text`), native artwork bounds and 4:3 card dimensions, paper/blend/age choices, signature asset and its bounds, text bounds and reading order.
- For automatic text, the completed [lyric selection](lyric-selection.md): one song entry, exact paired originals/translations and both source line numbers, translator when present, matching reason, count and final layout breaks. Keep the exact original-title attribution `——original song title` in the rendering text.
- Completion of assistant verification or, only if requested, user approval. Do not generate with unresolved source, pairing, count or attribution concerns.

Default counts come from MV orientation: landscape/square exactly 2 pairs, portrait exactly 4; explicit `lyric_lines=1..4` wins. An explicit placement override does not itself alter count. With `lyrics=none`, no lyric retrieval or song attribution is needed. Preserve designated wording; do not invent a missing translation or unverified attribution. Apply the entrypoint's text/signature overrides before compilation.

Use the [art direction](postcard-art-direction.md) calculation for the resolved layout. Verify that native artwork and all chosen content fit before compiling. Any excerpt changed for fit must be verified again. The assistant handles selection; the image tool only renders the final verified content.

Reference roles:

1. **EDIT TARGET:** the actual finished MV artwork, not the unprocessed photo.
2. **SUPPORTING SIGNATURE ASSET:** the inspected logo PNG, only when used.

Supply real image inputs using the available built-in tool's supported reference arguments. Do not pass a corpus file or candidate list as a visual reference, invent model-selection parameters, or claim a particular backend model version. A filename mentioned only in prompt prose is not an attached image.

## Prompt structure

Resolve every applicable slot, insert exactly one layout module below, and omit unused text/signature sections.

```text
Create one flat landscape 4:3 postcard front from reference image 1,
the already finished MV artwork.

The artwork is [w] by [h] pixels. Preserve its complete native-size
extent at scale 1, at [x,y] inside a [W] by [H] pixel card. Add paper
outside it. Keep its aspect, perspective, core object sizes and
relative positions intact.

The scene shows [observed elements, composition, eye path, light
and emotion]. Retain [anchors, white figure/local head scribbles,
ink field, controlled fracture and source lettering]. Preserve
body hatching gaps, pure-white marks and dense head coverage.
Retain photographic bodies and inherited anonymous heads.
Protect [edge subjects and existing microcopy].

Use [scene-derived paper color and reason], [aging cues] and one
shared fiber/ink-absorption surface. Integrate [peripheral zones]
through [selected boundary blend], preserving focal clarity.
Keep the accepted MV treatment stable.

[Insert the selected layout module with concrete bounds.]

[If logo: reference image 2 is the signature asset; preserve its
emblem, lettering, aspect and geometry as one unit. Place it once
within [resolved signature bounds].]
[If wordmark: place the exact lowercase word "yorushika" once
within [resolved signature bounds].]

[If automatic or verified corpus lyrics: render exactly [N]
Japanese/Chinese pairs in [text bounds, typefaces and ink].
For each pair, put Japanese above its corresponding Chinese,
with a small within-pair gap and a larger between-pair gap.
Keep both readable; Chinese may be slightly smaller.
Follow the supplied grouping and layout breaks exactly.
After the last pair, put the supplied original-song attribution
on its own line. Render this exact text:
[verified Japanese/Chinese pairs followed by ——original song title]]
[If user-designated text: render the verified supplied wording
and requested language/layout exactly; include a song attribution
only if supplied or verified. Do not invent additional wording.]
[If lyrics are disabled: add neither lyrics nor a song attribution.]
[If signature is disabled: add no logo or wordmark.]
[If no added text: add neither signature nor lyrics/song title;
retain native photographed signs and existing text as instructed.]

Only render the supplied final wording; do not choose other lyrics,
translate, rewrite or add credits. Keep text and signature outside
the artwork with readable spacing and no clipped glyphs.

Deliver one finished flat postcard filling the canvas. Limit edits
to paper, print surface, peripheral integration and chosen typography.
Avoid changed scene geometry, cropped source objects, extra figures,
recolored white marks, heavy distress, blurred halos, dimensional
frames, desk mockups, duplicate signatures, UI and new watermarks.
```

### Layout module — top image

```text
Keep the MV artwork horizontally centered in the upper region at
[artwork bounds]. Arrange [signature, if enabled] and [paired lyric
block plus final song title, if enabled] in the lower paper at
[their separate bounds]. Keep the scene dominant and the lower
reading order uncluttered, with no typography covering the image.
```

### Layout module — left image, right text

```text
Place the complete MV artwork on the left at [artwork bounds],
vertically centered, with a clear gap before the right column
[column bounds]. Keep [signature, if enabled] at the top of that
column. Below it, left-align [N verified Japanese/Chinese pairs,
if enabled], each Japanese original immediately above its Chinese
translation. Put the exact original-song attribution on a separate
final line beneath the last pair. Preserve clear pair spacing,
column margins and separation from the image.
```

## Inspect the actual output

Measure the saved file and require `3*canvas_width == 4*canvas_height`. Compare native artwork size and anchors with the actual MV input, not the original photo; verify `artwork_scale=1` from measurable bounds/anchor positions. Prompt values alone prove neither geometry nor preservation.

Inspect in this order:

1. **Layout:** the resolved branch is present. Top-image retains upper-centered artwork with lower content. Left-image-right-text has the full image on the left, signature above lyrics on the right and attribution last. Respect explicit layout and disabled-content overrides.
2. **MV preservation:** complete composition, source lettering, depth, photographic bodies, white body hatching gaps and dense head coverage remain legible. No new figures or exposed covered heads.
3. **Paper/signature:** coherent scene-derived color and age, restrained edge integration, proper logo contrast/aspect/geometry, no overlaps or clipping.
4. **Text:** compare every Japanese and Chinese glyph, internal space and punctuation against the verified source. Check correct within-pair correspondence and Japanese-above-Chinese order, pair count independently of wrapping, and the exact two-dash prefix plus original song title on its own final line. Inspect retained signs and logo lettering too.
5. **Legibility:** both languages and title are readable, with adequate within-/between-pair spacing, no text on the image and no column overflow. Disabled lyrics/title/signature are actually absent.

Check the expected count: portrait default 4, landscape/square default 2, or explicit `lyric_lines`; lyric/count/attribution checks are not applicable when lyrics are disabled. For user-designated wording, compare against that wording and only require bilingual/title content if supplied or verified.

If natural blending prevents reliable scale measurement, mark it unverified. Preserve a failed output as a draft and explain the actual concern; do not automatically regenerate, resample or silently correct it to conceal failure. Do not claim print-ready or geometrically exact output from the prompt alone.

Save using the entrypoint's workspace-root `output/`, `YYYYMMDD-标题.<ext>` convention. Keep original and intermediate files intact. Handoff: image, reused/generated MV source, layout, paper, preserved MV features, bilingual selection, original title/translator when available and matching reason, actual dimensions, saved path and material concerns.
