# 明信片 / Postcard

## 从照片开始

```text
用 $yorushika-postcard-scenes 把这张照片做成明信片。
input=photo paper=auto age=light blend=auto
signature=auto lyrics=auto
```

流程先生成并保存MV场景，再使用该实际文件排版。默认从附带的 `geci.md` 中选择与画面元素和情绪匹配的1–4句中文歌词，保留原词与标点，并记录曲目、译者（若有）、行号和匹配理由。新生成MV时不新增微文案，中文歌词放在明信片纸面留白中。

## 复用已有场景

上传已生成的MV图后调用：

```text
用 $yorushika-postcard-scenes 把这张MV场景做成明信片。
input=mv paper=auto age=light signature=none lyrics=none
```

已有场景直接复用；不会为了进入明信片阶段重新生成一张MV图。原生招牌和源图文字遵循技能的保留规则。

## 检查要点

- 明信片目标为横向4:3，检查实际文件的 `3 × width == 4 × height`。
- 默认 `artwork_scale=1`，检查嵌入场景是否保留原生尺寸；无法证实时明确说明。
- 若生成器返回的整张卡片比MV原图还窄，就不能声明满足原尺寸嵌入。
- 纸张颜色、局部渗墨、文字和署名应共同服务场景，主体和白线人物保持可辨。
- 中文歌词逐字对照所选语料，区分原文选句数与排版折行数；曲目、译者与匹配理由记录在项目文件和交付说明中。
- 失败的几何或文字检查记录为草稿问题，不自动反复生成。

## English invocation

```text
Use $yorushika-postcard-scenes with the attached MV artwork.
input=mv paper=auto age=light blend=paper-fade
signature=auto lyrics=auto
```

Preserve the saved artwork, derive the paper from its colors, and select 1–4 Chinese lyric lines from the bundled geci.md to match visible elements and mood. Inspect actual canvas dimensions, inset scale, edge integration and exact Chinese glyphs against the source, as well as retained Japanese signs and logo lettering. Save new images in workspace-root `output/` as `YYYYMMDD-title.<ext>`; preserve original inputs and historical outputs in place.
