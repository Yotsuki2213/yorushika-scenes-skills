# Yorushika Scenes Skills

从一张照片出发，保留场景的构图与情绪，再把它留在一张有纸感的明信片上。

[English](README.en.md) · [场景技能](skills/yorushika-mv-scenes/SKILL.md) · [明信片技能](skills/yorushika-postcard-scenes/SKILL.md) · [使用示例](examples/README.md)

本仓库将两个相互协作的 Codex Skill 放在同一个 `skills/` 目录下：一个负责场景影像，一个负责明信片的纸面与文字。仓库为个人私有维护版本；视觉研究、原创短诗参考和实际素材分开存放。

## 两个技能

| | MV 场景 | 明信片 |
| --- | --- | --- |
| 调用名称 | `$yorushika-mv-scenes` | `$yorushika-postcard-scenes` |
| 输入 | 用户提供的一张照片 | 照片，或已生成的 MV 场景图 |
| 目标 | 横向 16:9 场景图 | 横向 4:3 明信片正面 |
| 主要处理 | 构图分析、场景保留、白色线描、水墨与局部印刷断裂 | 场景纸色、轻旧纸纹、边缘融合、署名、可选日语短诗 |
| 文字 | 可选的一处原创日语微文案 | 通常1–3行原创日语短诗 |
| 依赖 | 内置 ImageGen 与本地图片查看能力 | 同一父目录中的 `yorushika-mv-scenes`，以及相同图像工具 |

```text
普通照片 → MV 场景生成 → 保存中间图 ─┐
                                      ├→ 明信片编排 → 检查并保存
已有 MV 场景图 → 检查并复用 ─────────┘
```

## 视觉方法

先读原图中的主体、空间关系、视线路径、色彩与材质，再选择处理方式。默认采用 `preserve-edit`，保留主体、主要几何和现场光线；需要完整重新创作时，才使用明确指定的 `redraw`。

可选场景路线：

- `graphic-soliloquy`：手绘轮廓、水墨场、局部印刷错位。
- `sunlit-memory`：空气感、远景、柔化的光色；仍以原图实际天气为准。
- `nocturnal-material`：暗部、局部光源与单一材质事件。
- `fusion`：按照主次层级融合三个方向。

白色线描人物保持微小、匿名、空心，并依附真实场景中的道路、岸边或石面。明信片阶段延续已经生成的场景，纸面颜色、留白和融合方式由画面决定。

## 开始使用

需要能调用内置 ImageGen 和查看本地图片的 Codex 环境。此仓库提供技能指令、参考资料与素材，不附带独立图像服务、API 密钥或模型权重。

私有仓库需要拥有访问权限的 GitHub 账户。可先克隆：

```powershell
gh repo clone Yotsuki2213/yorushika-scenes-skills
```

将两个技能文件夹复制到目标项目的 `.agents/skills/`。它们必须保持同级，以便明信片技能解析基础技能的相对路径。以下命令在目标项目根目录运行，假设仓库已经克隆为其直接子目录：

```powershell
$ErrorActionPreference = 'Stop'
$sourceRoot = Join-Path (Get-Location) 'yorushika-scenes-skills/skills'
$targetRoot = Join-Path (Get-Location) '.agents/skills'
$skillNames = @('yorushika-mv-scenes', 'yorushika-postcard-scenes')

# 先检查全部目标，保留已有安装，避免无意覆盖。
foreach ($name in $skillNames) {
    if (-not (Test-Path -LiteralPath (Join-Path $sourceRoot $name))) {
        throw "找不到源技能：$name"
    }
    if (Test-Path -LiteralPath (Join-Path $targetRoot $name)) {
        throw "目标技能已存在，请先比较版本并备份：$name"
    }
}
New-Item -ItemType Directory -Path $targetRoot -Force | Out-Null
foreach ($name in $skillNames) {
    Copy-Item -LiteralPath (Join-Path $sourceRoot $name) -Destination $targetRoot -Recurse
}
```

个人级安装也应将两个文件夹一起放到个人技能目录，并保持同级。单独使用场景技能不需要明信片技能；使用明信片技能则需要同时安装场景技能。

上传照片后调用：

```text
用 $yorushika-mv-scenes 处理这张照片。
保留原构图，使用 graphic-soliloquy，不添加文字。
```

```text
用 $yorushika-postcard-scenes 把这张照片做成明信片。
纸色取自画面，轻微做旧，搭配原创日语短诗。
```

## 日语短诗语料库

[japanese-verse-corpus.md](skills/yorushika-postcard-scenes/references/japanese-verse-corpus.md) 基于用户提供的11段歌词对照材料进行表达分析，包含14个表达单元、11条分段分析记录，以及日语句法、节奏、改行和画面适配规则。

原始完整歌词不随仓库分发。分析标签和编辑示例用于帮助创作新句子；示例不直接成为固定文案。自动短诗从当前图片的具体物与感受出发，用户指定文字和 `poem=none` 优先。

## 仓库结构

```text
yorushika-scenes-skills/
├── README.md
├── README.en.md
├── NOTICE.md
├── .gitignore
├── .gitattributes
├── assets/
│   └── brand/
│       └── README.md
├── examples/
│   ├── README.md
│   ├── mv-scene.md
│   └── postcard.md
└── skills/
    ├── yorushika-mv-scenes/
    │   ├── SKILL.md
    │   ├── agents/openai.yaml
    │   └── references/
    └── yorushika-postcard-scenes/
        ├── SKILL.md
        ├── agents/openai.yaml
        ├── references/
        │   ├── postcard-art-direction.md
        │   ├── prompt-compiler.md
        │   └── japanese-verse-corpus.md
        └── assets/
            ├── yorushika-logo.svg
            ├── yorushika-logo-black.png
            ├── yorushika-logo-white.png
            └── SOURCES.md
```

仓库组织参考 [gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) 的双技能与双语说明布局；此处的文档按本项目重新编写，不复制该仓库的示例图片、品牌素材或许可证。

## 输出与检查

技能默认在运行项目的 `Image生图/` 下分别保存输入副本、MV中间图和明信片，不覆盖原件。完整提示词和检查记录保存在项目文件中。

比例、原尺寸嵌入和文字准确度需要检查实际生成文件。生成模型可能忽略请求的像素尺寸或缩小画面；未通过要求的输出应标为审片或草稿，不应仅凭提示词就声称原生比例与尺寸得到保证。明信片流程不会自动反复生成或放大图像来掩盖差异。

本仓库没有收录个人项目照片、生成成果、完整歌词、MV参考帧、凭据或本机备份。`examples/` 目前提供可复用的调用与验收说明。

## 维护与权利

同时更新相关入口与引用文件，保持两个技能的同级结构。根目录 `assets/brand/` 记录素材位置；运行所需标志保留在明信片技能内，复制技能时不会漏掉依赖。

这是非官方个人项目。第三方标志及作品相关权利仍归各自权利人所有，具体来源见 [NOTICE.md](NOTICE.md) 和 [素材来源](skills/yorushika-postcard-scenes/assets/SOURCES.md)。当前未授予开源许可证。
