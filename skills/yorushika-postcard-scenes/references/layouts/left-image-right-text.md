# Layout: Left Image / Right Text

Use for portrait MV artwork. Keep the complete portrait on the left, vertically centered, with a clear gap before an independent right information column. Place one logo above four left-aligned bilingual groups, then the song attribution. Keep all text and signature off the image.

Starting geometry:

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
column_top = round(0.10 * H)
column_bottom = floor(0.90 * H)
```

Increase `k` if needed while retaining 4:3 and native artwork size. Never crop, stretch or shrink the MV.

For each of the four pairs, place Japanese directly above its corresponding Chinese. Use a small intra-pair gap and a larger inter-pair gap; Chinese may be slightly smaller but both remain readable. Put exact `——original song title` on a separate final line. Keep logo geometry intact with a visible break before the lyric groups.

An explicit pair count overrides four, but the Japanese-above-Chinese grouping remains. If the requested text is long, prefer a shorter verified excerpt, adjust margins or enlarge the paper rather than changing wording or using unreadable type.
