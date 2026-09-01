# 明信片 / Postcard

## 从照片开始

```text
用 $yorushika-postcard-scenes 把这张照片做成明信片。
input=photo paper=auto age=light blend=auto
signature=auto lyrics=auto
```

先生成并保存 MV，再分析该真实成品的元素、构图与情绪。按[选句规则](../skills/yorushika-postcard-scenes/references/lyric-selection.md)从同一歌曲条目选择日中对照，核对原文、组数、配对与歌名后，将确定的文字交给图像工具。新生成 MV 在自动歌词模式下不新增微文案；日中歌词放在明信片纸面上。

## 横向 MV：上图下文

```text
用 $yorushika-postcard-scenes 处理这张横向 MV。
input=mv paper=auto age=light signature=auto lyrics=auto
```

沿用上方居中图片、下方署名与歌词的布局，默认固定2组。每组日文在上、中文在下；歌词最后单独一行是 `——原歌名`。近似16:9或其他横向比例同样适用；正方形默认使用这一布局。

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

关闭歌词与歌曲出处使用 `lyrics=none`（兼容 `poem=none`）；关闭 logo 使用 `signature=none`。一般“不新增文字”请求关闭两者。已有 MV 文件直接复用，不为明信片重新生成场景。此阶段允许约占图片短边 1–4% 的外围以淡化、渗墨、干刷和纸纹明显溶入纸面；不补人物、不调整动作、不修补头部涂抹，并完整保护人物轮廓、四肢、承重、接触关系与白线。

## 检查与情境推演

| 情境 | 预期行为 |
| --- | --- |
| 横图、近似16:9、正方形 | 上方居中图片，下方固定2组日中对照与原歌名 |
| 竖图、近似3:4、其他竖向比例 | 左图、右上 logo、右下4组歌词和歌名 |
| EXIF 旋转 | 以实际显示方向分流，原文件不改动 |
| MV 无人物或人物姿态不同于新版默认 | 原样保留，不在明信片阶段补人或改成背身回头 |
| MV 头部覆盖不足或存在其他场景问题 | 不在排版时修图；如实说明，明确要求修订时先独立完成新 MV |
| 线稿人物、白线或文字碰到边缘 | 溶图绕开该保护区或只向外纸面晕染，动作与白线不能减弱 |
| 明确指定句数 | `lyric_lines` 优先于默认4组 |
| 单独覆盖版式 | 改变摆放，组数默认仍按实际 MV 方向 |
| 双语长句 | 同组数换短片段或调整/扩大纸面，重新核对；不缩小或裁切 MV |
| 缺少日文、译文或配对不明 | 换候选；仍无法满足时在生成前说明并请求调整 |
| 重复收录或译本不同 | 使用同一曲目条目的成对文字、歌名与译者，不跨版本混用 |
| 指定文案但无法核对双语/出处 | 不补译或编造歌名；需要补充信息时先询问 |
| 关闭歌词、署名或全部新增文字 | 分别省略对应内容，不留虚构占位文字 |
| 用户要求先确认 | 展示分析、双语文本和歌名，收到确认后再生成 |

实际出图后检查：

- 明信片为横向4:3：`3 × width == 4 × height`；`artwork_scale=1` 对照真实 MV 文件检查，无法证明时标记未验证。
- 图片完整，布局分支正确；约占图片短边 1–4% 的外围溶图清楚可见，可沿安全边缘连续展开，中心与场景锚点仍可辨认。
- 人物轮廓、四肢关系、颈肩回头、承重点、接触/遮挡、身体排线和头部白线逐项保留；任一动作读不清都算失败。
- 两种语言逐字对照，日上中下配对正确，组数与排版折行数分开。
- 最后一行保留 `——` 与所选条目的原歌名，不误用专辑名或译者。
- 字符、标点、logo、间距清楚，文字不盖图、不越界；译者和匹配理由放项目记录与交付说明。
- 失败项目如实记录为草稿问题，不把提示词视为实际验证，不自动反复生成。

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

For landscape/square input, retain the upper-centered artwork and lower signature/text with exactly 2 pairs by default. Save new images to workspace-root `output/` as `YYYYMMDD-title.<ext>`; preserve originals and existing MV files in place.
