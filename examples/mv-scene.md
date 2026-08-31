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
| 横图，无人物主体 | 约 16:9 | 添加一个白色排线主体，动作与真实场景接触 |
| 竖图，无人物主体 | 约 3:4 | 添加一个白色排线主体，保留竖向空间与视线路径 |
| 横图，有人物主体 | 约 16:9 | 保留身体、衣着与动作，密集白线覆盖可见头部 |
| 竖图，有人物主体 | 约 3:4 | 保留身体比例和位置，密集白线覆盖可见头部 |

人物画法参考随技能打包的图片：身体排线有透底间隙，头部以密集白色排线和横向涂抹匿名化。水墨场与一次有方向的印刷断裂继续依附真实边界和材质。

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

## 检查要点

- 读取真实文件尺寸，检查横竖方向与自然构图；16:9 和 3:4 为大致目标，轻微比例差异可直接交付。
- 新增人物是否清楚可辨，动作、支撑、透视和遮挡是否成立。
- 已有主体的身体、衣着、姿态和位置是否保留，可见头部是否充分覆盖。
- 白线是否保持纯白、身体排线是否有间隙、头部是否允许密集涂抹；参考图的大面积白色遮挡标记是否被误带入。
- 主要空间关系、现场光线和材质是否保留，风格介入是否有局部层级，文字是否符合设置。
- 真实的方向、构图或人物处理问题在交付说明中如实记录；提示词中的要求不等于实际生成结果。
- 新生成图片保存为工作区根目录下的 `output/YYYYMMDD-标题.png`，例如 `output/20260831-秋日步道.png`；保留原始文件，避免覆盖同名输出。

## English invocation

```text
Use $yorushika-mv-scenes on the attached photograph.
transform_mode=preserve-edit preserve_strength=balanced
style_intensity=strong mode=auto text=none
Preserve the weather, focal objects and spatial relationships.
Use the source orientation and the default human-subject treatment.
```

These cases describe intended behavior and inspection criteria. They are not a record of completed image-generation tests.
