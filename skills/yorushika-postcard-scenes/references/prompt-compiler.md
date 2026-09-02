# Postcard Prompt Compiler

Use this compiler only after a real MV file has been obtained and analyzed and the final text has been verified. For upstream scene generation, use the base skill's compiler. Write design instructions in English; quote the exact Japanese, Chinese and original song title without translation. Keep the full prompt internal.

## Resolve before prompting

Record these decisions before calling ImageGen for a postcard:

- Actual MV path, EXIF-oriented dimensions and whether it was reused or generated.
- Visible elements, subject positions, depth, eye path, quiet areas, motion, light/color and evidence-based emotion; distinguish observations from associations.
- `blend_band`: roughly 1–4% of the shorter MV side, allowed across broad or continuous perimeter regions for opacity fade, pigment bleed, paper fade, dry-brush gaps and matched grain; `protected_action_zones`: all people/line figures, body and limb silhouettes, shoulder/neck turn, weight-bearing and contact points, pose-defining occlusion, white body/head strokes and source text.
- Layout (`top-image` or `left-image-right-text`), native artwork bounds and 4:3 card dimensions, paper/blend/age choices, signature asset and its bounds, text bounds and reading order.
- For automatic text, the completed [full-corpus lyric selection](lyric-selection.md): motif/relation/affect terms, corpus coverage, one song entry, exact paired originals/translations and both source line numbers, translator when present, emotional/compositional matching reason, count and final layout rows. Keep the exact original-title attribution `——original song title` in the rendering text.
- Completion of assistant verification or, only if requested, user approval. Do not generate with unresolved source, pairing, count or attribution concerns.

Default counts come from MV orientation: landscape/square automatically selects 1–2 pairs and consolidates them into one Japanese row plus one Chinese row; portrait uses exactly 4 paired groups. Use two landscape pairs only when both combined language rows fit legibly without wrapping, otherwise use one. Explicit `lyric_lines=1..4` wins; explicit 3–4 landscape pairs may exceed two rows. An explicit placement override does not itself alter count. With `lyrics=none`, no lyric retrieval or song attribution is needed. Preserve designated wording; do not invent a missing translation or unverified attribution. Apply the entrypoint's text/signature overrides before compilation.

Use the [art direction](postcard-art-direction.md) calculation for the resolved layout. Verify that native artwork and all chosen content fit before compiling. Any excerpt changed for fit must be verified again. The assistant handles selection; the image tool only renders the final verified content.

Reference roles:

1. **EDIT TARGET / FIXED SCENE:** the actual finished MV artwork, not the unprocessed photo or a style reference to redraw. Preserve the scene center and every protected action zone; only the resolved peripheral blend band and added paper/layout are editable.
2. **SUPPORTING SIGNATURE ASSET:** the inspected logo PNG, only when used.

Supply real image inputs using the available built-in tool's supported reference arguments. Do not pass a corpus file or candidate list as a visual reference, invent model-selection parameters, or claim a particular backend model version. A filename mentioned only in prompt prose is not an attached image.

## Prompt structure

Resolve every applicable slot, insert exactly one layout module below, and omit unused text/signature sections.

```text
Create one flat landscape 4:3 postcard front from reference image 1,
the already finished MV artwork.

The artwork is [w] by [h] pixels. Preserve its complete native-size
extent at scale 1, at [x,y] inside a [W] by [H] pixel card. Add paper
outside it. Keep its aspect, perspective, every object size and
relative position intact. Treat it as a fixed artwork layer, not
a scene to redraw or regenerate. Postcard edits are limited to
boundary blending, outer paper and layout.

The scene shows [observed elements, composition, eye path, light
and emotion]. Retain [the actual existing anchors, figures,
head scribbles, ink field, fracture and lettering, only if present].
Preserve existing body hatching gaps, white marks, head coverage
and photographic bodies exactly as they are in this MV; absent
features remain absent and existing imperfections remain unchanged.
Protect [protected_action_zones: every figure/body/limb silhouette,
shoulder-neck turn, weight-bearing support, contact point,
pose-defining occlusion, white body/head strokes and source text].
Do not move, crop, fade, dissolve, re-pose or repaint them. Do not
repair or reapply head coverage, add a missing figure, or restyle
the center of the scene.

Use [scene-derived paper color and reason], [aging cues] and fibers
matching the existing print surface. Blend a visibly substantial
but controlled peripheral band, roughly 1–4% of the artwork's
shorter side, along [broad/continuous selected edges] through
[opacity fade / ink bleed / paper fade / dry-brush gaps and grain].
Allow low-priority edge texture to dissolve into paper and carry
spill outward. Interrupt or route the blend around every protected
action zone and source text; where they touch an edge, blend
outward only. Do not let the transition weaken the figure's action.

[Insert the selected layout module with concrete bounds.]

[If logo: reference image 2 is the signature asset; preserve its
emblem, lettering, aspect and geometry as one unit. Place it once
within [resolved signature bounds].]
[If wordmark: place the exact lowercase word "yorushika" once
within [resolved signature bounds].]

[If landscape/square automatic or explicit 1–2 pairs: render exactly
[N] verified Japanese/Chinese pairs as TWO visual lyric rows in
[text bounds, typefaces and ink]. Row 1 contains the supplied Japanese
original(s) in source order; row 2 contains the corresponding Chinese
translation(s) in the same order. If N=2, separate the two sentences
with typesetting space only and add no punctuation. Do not wrap either
language row or reduce it to unreadable type. Put the supplied
original-song attribution on a separate smaller line after the two
lyric rows. Render exactly:
[combined Japanese row]
[combined Chinese row]
[——original song title]]
[If portrait or explicit landscape 3–4 pairs: render exactly [N]
Japanese/Chinese paired groups in [text bounds, typefaces and ink].
For each pair, put Japanese above its corresponding Chinese, with a
small within-pair gap and a larger between-pair gap. Follow the supplied
grouping and layout breaks exactly. Put the supplied original-song
attribution on its own line after the final pair.]
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
to added paper, named edge blending and chosen typography/layout.
Do not redraw the MV center or modify protected action zones.
Avoid changed scene content/geometry, cropped source objects, extra figures,
recolored white marks, heavy distress, blurred halos, dimensional
frames, desk mockups, duplicate signatures, UI and new watermarks.
```

### Layout module — top image

```text
Keep the MV artwork horizontally centered in the upper region at
[artwork bounds]. Arrange [signature, if enabled] and [compact lyric
block plus final song title, if enabled] in the lower paper at
[their separate bounds]. For automatic or explicit 1–2 pairs, keep
the lyric body to one Japanese row and one Chinese row, then place
the smaller attribution on its own line. Keep the scene dominant and
the lower reading order uncluttered, with no typography covering the image.
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
