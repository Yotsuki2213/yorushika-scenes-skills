# Layout: Top Image

Use for landscape and square MV artwork. Keep the complete image horizontally centered in the upper region; reserve lower paper for one signature, compact bilingual text and the separate song attribution.

Starting geometry:

```text
k = ceil(max(w / (4 * 0.90), h / (3 * 0.76)))
W = 4 * k
H = 3 * k
artwork_width = w
artwork_height = h
x = floor((W - w) / 2)
y = round(0.065 * H)
```

Adjust margins or increase `k` while retaining 4:3 and native artwork size. Never crop, stretch or shrink the MV to fit text.

In automatic mode, first try two short consecutive pairs. Put all selected Japanese in source order on one readable row and the corresponding Chinese on the next; separate two sentences with typesetting space only and add no punctuation. If either language wraps or becomes too small, try a shorter same-song window, then the next strongest candidate, then use one pair. Place the smaller exact `——original song title` on its own line.

Explicit 3–4-pair requests override the two-row default and use per-pair Japanese-above-Chinese groups. Keep signature and text in separate lower-paper bounds, preserve clear spacing, and cover none of the artwork.
