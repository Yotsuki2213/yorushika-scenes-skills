# 明信片 / Postcard

## 从照片开始

```text
用 $yorushika-postcard-scenes 把这张照片做成明信片。
input=photo paper=auto age=light blend=auto
signature=auto lyrics=auto
```

先生成并保存 MV，再分析该真实成品的元素、构图、空间关系与情绪张力。按[选句规则](../skills/yorushika-postcard-scenes/references/lyric-selection.md)和全库候选提取器跨 `opus.md` 的发行分组召回歌词，再按情绪、构图、感官意象、语义余韵和版面长度重排。从同一歌曲条目选择日中对照，核对原文、组数、配对与歌名后，将确定的文字交给图像工具。新生成 MV 在自动歌词模式下不新增微文案；日中歌词放在明信片纸面上。

## 横向 MV：上图下文

```text
用 $yorushika-postcard-scenes 处理这张横向 MV。
input=mv paper=auto age=light signature=auto lyrics=auto
```

沿用上方居中图片、下方署名与歌词的布局。自动模式先尝试同一曲目的2组短连续歌词；若日文合并行或中文合并行无法以可读字号保持单行，则改用1组。歌词正文总共两行：上面是1–2句日文，下面是对应中文；两句之间只留排版间距，不新增标点。`——原歌名` 作为独立出处行。近似16:9或其他横向比例同样适用；正方形默认使用这一布局。

## 竖向 MV：左图右文

```text
用 $yorushika-postcard-scenes 处理这张竖向 MV。
input=mv paper=auto age=light signature=auto lyrics=auto
```

完整竖图放左侧，右上放 logo，右下左对齐放默认4组日中歌词，歌名最后。每组两种语言紧密对应，组间留出较大间距。卡片仍为横向4:3，图像保持原生尺寸。需要不同组数时可明确指定 `lyric_lines=2` 等，不增加必填参数。

## 预览配文或关闭文字

默认由助手核对后直接生成。若希望先审核，可说：

```text
先给我看画面分析、选好的日中歌词和原歌名，等我确认再生成明信片。
```

关闭歌词与歌曲出处使用 `lyrics=none`（兼容 `poem=none`）；关闭 logo 只接受显式的 `signature=none`。一般“不新增文字”请求只关闭歌词与出处，logo 仍然保留——除非明确要求去掉 logo，否则每张明信片都会带签名。已有 MV 文件直接复用，不为明信片重新生成场景。此阶段允许约占图片短边 1–4% 的外围以淡化、渗墨、干刷和纸纹明显溶入纸面；不补人物、不调整动作、不修补头部涂抹，并完整保护人物轮廓、四肢、承重、接触关系与白线。


## English invocation

```text
Use $yorushika-postcard-scenes with this portrait MV artwork.
Analyze its visible elements, composition and mood, then verify
4 Japanese/Chinese lyric pairs from one opus.md song entry.
Blend a visible 1–4% peripheral band into the added paper while
preserving every figure's pose, support, contact and white strokes.
Keep the complete image on the left, the logo above the lyrics
on the right, Japanese above Chinese per pair, and
——original song title on the final line.
```

For landscape/square input, retrieve across the full corpus and auto-select 1–2 short pairs. Put the selected Japanese original(s) on one row and their Chinese translation(s) on the next, with the song title on a separate attribution line. Use two pairs only when both language rows fit legibly; otherwise use one. Save new images to workspace-root `output/` as `YYYYMMDD-title.<ext>`; preserve originals and existing MV files in place.
