# Yorushika Scenes Skills

从一张照片出发，保留场景的构图与情绪，再把它留在一张有纸感的明信片上。

[English](README.en.md) · [场景技能](skills/yorushika-mv-scenes/SKILL.md) · [明信片技能](skills/yorushika-postcard-scenes/SKILL.md) · [使用示例](examples/README.md)

本仓库将两个相互协作的 Codex Skill 放在同一个 `skills/` 目录下：一个负责场景影像，一个负责明信片的纸面与文字。仓库为个人私有维护版本；视觉研究、歌词资料和实际素材分开存放。

## 两个技能

| | MV 场景 | 明信片 |
| --- | --- | --- |
| 调用名称 | `$yorushika-mv-scenes` | `$yorushika-postcard-scenes` |
| 输入 | 用户提供的一张照片 | 照片，或已生成的 MV 场景图 |
| 目标 | 横图约 16:9；竖图约 3:4；正方形默认约 16:9 | 横向 4:3 明信片正面 |
| 主要处理 | 构图分析、场景保留、白色线描、水墨与局部印刷断裂 | 场景纸色、轻旧纸纹、边缘融合、署名、中文歌词 |
| 文字 | 可选的一处原创日语微文案 | 按画面与情绪从 `geci.md` 选择1–4句中文歌词 |
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

无人物主体时，添加一个有明确动作、与真实场景接触的白色排线人物，成为画面的人物主体；已有主体时，保留身体、衣着、姿态与位置，用密集白色排线和横向涂抹覆盖可见头部。新人物身体保留排线间隙，头部允许密集覆盖。背景路人不自动视为主体，头部在画外时不补画。

按 EXIF 校正后的输入方向选择横向约 16:9 或纵向约 3:4 的构图方向，接受接近目标的自然输出尺寸；按构图需要自然扩展边缘，保留主体比例与主要空间关系。三张随技能打包的 [线稿参考](skills/yorushika-mv-scenes/references/human-treatment.md) 提供笔触与动作参考。明信片阶段保留已经生成的画幅、人物及头部处理，外部纸面仍为横向 4:3。

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
纸色取自画面，轻微做旧，按画面与情绪匹配1–4句中文歌词。
```

## 中文歌词选句

[geci.md](skills/yorushika-postcard-scenes/references/geci.md) 是用户提供的日中歌词对照资料副本。默认 `lyrics=auto` 按[选句规则](skills/yorushika-postcard-scenes/references/lyric-selection.md)，结合画面元素与情绪，从同一曲目条目中选择1–4句中文译文，保留原词与标点，并记录曲目、译者（若有）、行号和匹配理由。

用户指定文字优先；`lyrics=none` 关闭新增歌词，兼容旧参数 `poem=auto|none`。新生成 MV 时默认将新增微文案设为 `text=none`，已有 MV 文字则保留。历史 [日语表达分析](skills/yorushika-postcard-scenes/references/japanese-verse-corpus.md) 继续保留，当前自动配文使用中文歌词选句流程。歌词与译文权利归相关权利人，资料来源按用户文件记录，未独立核验。

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
    │   ├── references/
    │   │   └── human-treatment.md（与其他视觉参考同级）
    │   └── assets/line-figures/（三张参考 PNG 与 SOURCES.md）
    └── yorushika-postcard-scenes/
        ├── SKILL.md
        ├── agents/openai.yaml
        ├── references/
        │   ├── postcard-art-direction.md
        │   ├── prompt-compiler.md
        │   ├── lyric-selection.md
        │   ├── geci.md
        │   └── japanese-verse-corpus.md
        └── assets/
            ├── yorushika-logo.svg
            ├── yorushika-logo-black.png
            ├── yorushika-logo-white.png
            └── SOURCES.md
```

仓库组织参考 [gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) 的双技能与双语说明布局；此处的文档按本项目重新编写，不复制该仓库的示例图片、品牌素材或许可证。

## 输出与检查

新生成的 MV 图片与明信片统一保存到当前工作区根目录的 `output/`，命名为 `YYYYMMDD-标题.png`（扩展名跟随实际格式），例如 `20260831-秋日步道.png`。同名时使用不同的简短标题，不覆盖已有文件；原始图片和历史输出保留原位。完整提示词和检查记录保存在项目文件中。

检查实际生成文件的尺寸、方向、构图与文字准确度。MV 的 16:9 和 3:4 是大致画幅，轻微比例差异不影响交付，无需为此裁切、缩放或重新生成。明信片仍按自身的横向 4:3 纸面和原尺寸嵌入要求检查；提示词不能代替实际验证，真实问题在交付说明中记录。

本仓库随 MV 技能打包三张用户选定的线稿参考，随明信片技能附带用户提供的 `geci.md` 歌词对照资料。历史 MV 研究截图集合、其他个人项目照片、生成成果、凭据和本机备份不在包内。`examples/` 目前提供可复用的调用与验收说明。

## 维护与权利

同时更新相关入口与引用文件，保持两个技能的同级结构。根目录 `assets/brand/` 记录素材位置；运行所需线稿参考与标志分别保留在对应技能内，复制技能时不会漏掉依赖。

这是非官方个人项目。第三方标志及作品相关权利仍归各自权利人所有，具体来源见 [NOTICE.md](NOTICE.md) 、[线稿参考来源](skills/yorushika-mv-scenes/assets/line-figures/SOURCES.md) 和 [标志来源](skills/yorushika-postcard-scenes/assets/SOURCES.md)。当前未授予开源许可证。
