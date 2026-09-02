# MV 场景 / MV scene

## 保留式编辑

上传一张照片，然后调用：

```text
用 $yorushika-mv-scenes 处理这张照片。
transform_mode=preserve-edit preserve_strength=balanced
style_intensity=strong mode=graphic-soliloquy text=none
```

技能先读取实际方向、主体、空间关系与视线路径，再决定人物分支和可编辑区。无需额外填写人物或画幅参数。

| 输入 | 默认画幅 | 人物处理 |
| --- | --- | --- |
| 横图，无人物主体 | 约 16:9 | 添加一个潦草白线主体，默认背身自然回头，可按场景自行调整，重心与接触成立 |
| 竖图，无人物主体 | 约 3:4 | 添加一个默认背身自然回头的潦草白线主体，可按场景自行调整，保留竖向空间与视线路径 |
| 横图，有人物主体 | 约 16:9 | 保留身体、衣着与动作，密集白线覆盖可见头部 |
| 竖图，有人物主体 | 约 3:4 | 保留身体比例和位置，密集白线覆盖可见头部 |

人物画法参考随技能打包的图片：身体略抽象、潦草，断线与排线有透底间隙，但肩颈、四肢连接和承重符合现实逻辑。新增人物默认身体背对镜头，头部自然越肩回望，是同一人物的一个瞬间；例如沿路走远时回头，或坐在台阶上背身回望。当该默认动作与场景的视线、路径、支撑或叙事矛盾时，可自行调整为同样贴合场景的可信动作。原图已有主体保留原姿态，不强行回头。两种分支都用密集白色排线和横向涂抹覆盖整个可见头部，包括头顶、头发、脸、耳朵与后脑。水墨场与一次有方向的印刷断裂继续依附真实边界和材质。

## 自动选择路线与明确偏好

```text
用 $yorushika-mv-scenes 处理这张照片，mode=auto。
保留现场光线与主体关系，按输入方向输出。
```

同一人物分支适用于 graphic-soliloquy、sunlit-memory、nocturnal-material 和 fusion。用户可以明确覆盖默认行为，例如“不要新增人物”；技能应在记录和提示词中一致采用该要求。

## 边界情境

- 仅有零散背景路人：仍根据构图与叙事判断是否缺少人物主体，不自动把路人当作主角。
- 多人共同构成主体：分别覆盖可见头部，保留每个人的身体与相互关系。
- 头部在画外或完全被遮住：保留原有身体片段或遮挡，不补画头部。
- EXIF 旋转照片：按显示方向判定横竖，不按未旋转的存储宽高判定。
- 正方形输入：默认约 16:9；保持自然构图，按需要扩展边缘，接受生成器输出的接近比例。
- strict 与明确请求的 redraw：均执行人物分支；strict 允许指定人物编辑区域，redraw 保留未被明确释放的身体锚点。
- 竖向 MV 进入明信片：完整保留竖向画面，在外围增加横向 4:3 纸面，不裁掉或拉宽人物。


## English invocation

```text
Use $yorushika-mv-scenes on the attached photograph.
transform_mode=preserve-edit preserve_strength=balanced
style_intensity=strong mode=auto text=none
Preserve the weather, focal objects and spatial relationships.
Use the source orientation and the default human-subject treatment.
```

These cases describe intended behavior and invocation choices. They are not a record of completed image-generation tests.
