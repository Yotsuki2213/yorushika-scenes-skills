# Compact Postcard Prompt Compiler

Use only after a real MV exists, orientation has selected one layout module, and all text is final. Write the visual instruction in English while quoting Japanese, Chinese and the original title exactly. Keep it internal unless requested.

## Resolve

Use only:

- MV path and EXIF-oriented `w × h`;
- the five-field MV handoff;
- chosen 4:3 card dimensions and selected layout bounds;
- paper, age and blend behavior;
- one inspected signature asset, always resolved; `none` only for an explicit user omission request;
- final verified lyric rows/groups and `——original song title`, or no text.

The MV is `EDIT TARGET / FIXED SCENE`. The resolved logo is `SUPPORTING SIGNATURE ASSET` and is required on every postcard; only an explicit user omission request produces a signature-less card. Never attach the corpus, shortlist, original photo or unused logos.

## Assembly

Compile one compact request in this order:

```text
Create one flat landscape 4:3 postcard front.
Fixed artwork: place the supplied finished MV at native scale 1 within [artwork bounds].
Scene locks: preserve its complete composition, center, viewpoint, bodies, action/contact, white strokes, head covers and source text.
Paper: [stock color, visible fine fibers and age cues].
Inherited MV print field: preserve any existing cobalt/indigo wash, bloom, pooling, feathered edge and dry-brush break; carry a restrained portion outward into the matching paper rather than flattening it.
Boundary: use a visibly substantial but controlled [resolved 1–4% peripheral band] across broad or continuous permitted edges. Combine [source-matched opacity fade / pigment bleed into paper fibers / paper fade / irregular dry-brush gaps and matched grain], routing around [protected regions].
Layout: [the one selected layout module with concrete bounds].
Signature: [one exact attached logo and bounds, or `none` only for an explicit user omission request].
Text: [exact final Japanese/Chinese rows or groups and exact attribution, or none].
Constraints: [shared block below].
```

Do not include scene-analysis prose, retrieval candidates, scoring, unused layout alternatives, rejected lyrics or upstream MV style instructions.

## Shared constraints

- Treat the MV as fixed artwork; do not redraw its center, add/re-pose a person, repair head coverage or recolor white marks.
- Preserve native aspect, scale, geometry, depth and all protected action/text zones.
- Limit edits to added paper, the named peripheral band, one required signature and verified typography. Preserve inherited MV watercolor/ink fields and their material edge behavior; do not clean them into a faint border treatment.
- Keep text and logo outside the artwork, exact, readable and unclipped; do not select, translate, rewrite or add credits. Generate the signature from the attached asset only; do not omit it, replace it with drawn text or invent a substitute logo.
- No source crop/stretch, blurred halo, heavy distress, dimensional frame, desk mockup, duplicate signature, generated UI or new watermark.

Use the actual lines from the selected layout module rather than copying both branches. The image tool renders the final design; it does not retrieve lyrics or make content decisions.
