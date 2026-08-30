# 逐帧分析字段

每张参考帧按以下字段记录。值应描述可观察的画面事实，不猜测人物身份、故事出处或未显示的歌词。

| 字段 | 记录要求 |
|---|---|
| frame | 研究目录中的相对路径和顺序编号 |
| source_clock | 原始截图文件名中的电脑时间；无视频时间码时保持原样 |
| scene_anchors | 3–6 个具体空间/物件锚点 |
| composition | 景别、机位、水平线/消失点、留白、人物尺度 |
| palette | 主色、辅助色、冷暖关系、明暗和饱和度 |
| line_shape | 轮廓、平涂、建筑几何、笔触、错位或拖影 |
| light_atmosphere | 日光、逆光、窗光、暗室、雾化、颗粒或闪烁 |
| material_event | 水、沙、发丝、颜料、纸、布、玻璃、尘或火光 |
| human_treatment | 背影、剪裁、遮脸、剪影、半透明或缺席 |
| text_graphic | 文字/符号是否存在、位置、方向、占比；不抄录歌词 |
| route | graphic-soliloquy / sunlit-memory / nocturnal-material，可多标签 |
| confidence_note | 画面清晰度、播放器残留、裁切异常和分析置信度 |

质量规则：播放器控件、蓝色“播放”残留、黑白信箱边缘等截屏痕迹只写入 `confidence_note`，不得被当成 MV 风格特征。
