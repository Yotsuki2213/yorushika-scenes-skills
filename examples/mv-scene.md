# MV 场景 / MV scene

## 保留式编辑

上传一张照片，然后调用：

```text
用 $yorushika-mv-scenes 处理这张照片。
transform_mode=preserve-edit preserve_strength=balanced
style_intensity=strong mode=graphic-soliloquy text=none
```

技能先判断主体、空间关系、视线路径和可编辑区。图形处理围绕真实的边界与材质展开：纯白空心小人物、局部水墨层和一次有方向的印刷断裂。

## 自动选择路线

```text
用 $yorushika-mv-scenes 处理这张照片，mode=auto。
保留现场光线与主体关系，画面中不加人物。
```

## 检查要点

- 实际输出比例是否达到目标16:9；不要只读取提示词中的尺寸。
- 主要空间关系、溪流或道路走向、主体和现场光线是否保留。
- 新增人物如存在，是否匿名、纯白空心、接触真实表面。
- 风格介入是否有局部层级，而非整图滤镜。
- 文字是否符合 `text` 设置。

## English invocation

```text
Use $yorushika-mv-scenes on the attached photograph.
transform_mode=preserve-edit preserve_strength=balanced
style_intensity=strong mode=auto text=none
Preserve the weather, focal subject and spatial relationships.
```

Inspect the actual image for framing, preservation, localized graphic treatment and requested text behavior. Generation targets are not guarantees of exact dimensions.
