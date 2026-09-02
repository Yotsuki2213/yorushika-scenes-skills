# Compact ImageGen Prompt Compiler

Read this after the compact Scene Card has resolved one human module, one route module and one transform module. Do not load unused branches. Write the final visual instruction in English and keep it internal unless requested.

## Inputs

Use only resolved values:

- source orientation and approximate target aspect;
- `main_subject`, `gesture`, `geometry`, `eye_path`, `quiet_area` and `preserve`;
- selected human, route and transform module;
- one principal material event and at most one motion/distortion event;
- exact microcopy or `text=none`;
- labeled image roles.

The user's image is `EDIT TARGET`. The contact sheet or one original line reference is `SUPPORTING LINE STYLE ONLY`. A filename in prompt prose is not an attachment.

## Assembly order

Compile one compact request in this order:

```text
Use case: style-transfer image edit.
Edit target: the supplied source scene.
Framing: [orientation and approximate target aspect]; preserve [geometry and edge anchors].
Scene locks: [main subject, viewpoint, scale, body actions, light and texture].
Authorized edits: [human region, bounded style field, natural frame extension if needed].
Human treatment: [selected human module adapted to the actual action/head regions].
Art direction: [selected route module; principal material; source-aligned intervention].
Transform policy: [selected transform module and strength].
Microcopy: [exact text and placement, or none].
Image roles: source is EDIT TARGET; line image is SUPPORTING LINE STYLE ONLY.
Constraints: [the compact invariant block below].
```

Use source-specific nouns. Do not paste module headings, alternative routes, rejected options, analysis prose, numeric scoring or percentage explanations into the production prompt.

## Shared invariant block

Keep this meaning, phrased once:

- preserve camera viewpoint, principal objects, source axes, relative scale, existing body poses/contact and meaningful texture outside authorized regions;
- execute the selected human branch in pure-white irregular strokes; protect readable anatomy and action while fully anonymizing every applicable visible head;
- keep ink/watercolor/print treatment bounded and attached to source contours, planes, shadows or material events;
- retain the source light direction and recognizable semantic minimum;
- no important crop, stretching, mirroring, tiling, letterbox, replacement background or global filter;
- no malformed anatomy, floating figure, duplicate person, readable head identity, colored figure strokes, random whole-frame glitch, generated UI, new watermark or extra logo.

## Intensity and text

`restrained` uses roughly 10–30% localized intervention; `strong` uses one connected graphic field plus one subordinate break across roughly 30–55%; `expressive` enlarges those same connected events to roughly 45–65% without adding more effect types. These are art-direction ranges, not measured guarantees. Required human treatment stays legible at every intensity.

For `text=auto`, use one original Japanese phrase of roughly 3–8 characters once in a quiet area. Never use lyrics, song titles, logos or copied webpage text. Preserve native photographed text unless the user requests removal.

In explicit watermark removal, repair only the adjacent source texture. Do not silently remove unrelated marks, signs or people.
