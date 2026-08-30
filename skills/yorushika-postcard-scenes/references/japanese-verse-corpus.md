# ヨルシカ歌詞の表現分析・蒸留コーパス

ユーザー提供の歌詞対訳集から、情景、語りの距離、感覚、記憶、言い直しなどの表現上の働きを抽出した日本語版。`yorushika-postcard-scenes` におけるオリジナル短詩の参考資料として使用する。

## 0. 資料の範囲

```yaml
corpus_id: yorushika-lyric-style-distillation-ja-20260831
version: 1
language: ja
source_sections: 11
source_parallel_lines: 388
source_unique_japanese_lines: 349
source_json_records: 6
source_section_ids: [其一, 其二, 其三, 其四, 其五, 其六, 其七, 其八, 其九, 其十, 其十一]
use_case: original_japanese_postcard_verse
examples: newly_written_editorial_examples
```

分析対象は提供された11区分に限る。ヨルシカの全作品を代表する統計ではない。388行は原稿の太字行を単位として数えた値で、原曲の正式な改行数を意味しない。末尾の6件のJSONは本文と重なる時間軸資料として扱い、二重に数えない。区分番号を識別子とし、曲名の追加調査は行わない。

原稿の日本語を表現分析の中心とし、中国語訳は意味確認の補助とする。中国語の説明から派生した新しい用例と、原稿から観察した特徴を区別する。本書の用例は編集時に書き起こした文章であり、歌詞の引用でも、作者による発言でもない。

## 1. ポストカードでの使い方

短詩を書くことが決まったら、この資料を読んでから文章を作る。紙面の余白、既存の文字、画面の感情に合わせ、通常は1〜3行にまとめる。

1. 実際の画面から具体物を一つ選ぶ。窓、岸、影、道など、画像で確認できるものを優先する。
2. 光、温度、距離、動きのうち、画面に根拠のある感覚を一つ選ぶ。
3. 以下の表現単位から、場面に合う働きを一つか二つ選ぶ。
4. その画面のために新しい日本語を書く。用例は構造の説明として参照し、そのまま印字しない。
5. 音読して助詞、語順、改行を確認する。説明を減らし、画面と詩の間に余白を残す。

ユーザーが指定した詩や改行は保持する。`poem=none`、文字追加なしの指定、あるいは既存のマイクロコピーだけで十分な場合には、新しい詩を追加しない。語彙表を根拠に、画像にない花、海、夕日、人物や季節を作り足さない。

喪失、恋愛、自己否定は選択肢である。晴れた道には好奇心や軽さ、静かな部屋には安堵が合うこともある。画面やユーザーの希望に合わなければ、「君」、別れ、悲しみ、詩についての言及を入れる必要はない。

画像生成には採用した日本語と改行だけを正確に渡す。資料全体、候補文、分析用タグは印字対象にしない。中国語の意味説明は成果物の外で伝える。

## 2. 中心となる表現の動き

直接は言いにくい感情を、手で触れられる場所や物に預ける。光や匂いが身体に届き、その感覚から相手や時間の不在が見えてくる。最後に問題が残っていても、風景や動作は続いている。

```text
具体的な情景 → 感覚 → 誰かとの距離 → 記憶の変化 → 余韻
```

長い文章では、歌、詩、書く行為が経験を保存する器になる場合がある。短いカードでは、この流れの一部分だけを使う。すべての段階を数行に押し込めない。

### 表現の八つの軸

| タグ | 観察した働き | カードへの応用 |
| --- | --- | --- |
| `RELATIONAL_ADDRESS` | 相手を呼びながら、距離を取り直す | 呼びかけ、呼びかけの省略、空いた場所 |
| `MATERIALIZED_EMOTION` | 感情が色、温度、重さ、音になる | 一つの具体物に気持ちを託す |
| `MEMORY_ERASURE` | 記憶が薄れたり、別の形になったりする | 残っているものと変わったものを並べる |
| `ART_AS_SURVIVAL` | 書くことが経験を保存する | 紙や手紙が画面に関わる場合に使う |
| `SEASONAL_WEATHER` | 季節や天気が時間を示す | 写っている光、空気、動きから選ぶ |
| `SELF_NEGATION` | 自分の判断を疑い、言い直す | 必要なときだけ小さなためらいを置く |
| `FRAGMENTED_DIALOGUE` | 反復や短い断片が発話の呼吸になる | 一度の言い直し、短い行、間 |
| `MOTION_AND_DEPARTURE` | 移動する景色と留まる感情がずれる | 道、岸、車窓、歩く方向を使う |

これらは読解上の分類である。中国語版の重みづけは編集上の目安であり、統計的に推定した係数ではないため、本版では数値による配分を指定しない。

### 日常の細部

狭い部屋、冷めた飲み物、生活費、街灯などの生活の細部が、花、月、空と隣り合う。自然物だけで美しい情景を重ねるより、生活の手触りと光景が接するところに注目する。

### 感情の折り返し

```text
伝えたい → うまく言えない → 物に託す → まだ言い足りない
忘れたい → 細部だけ残る → 名前を変えて保存する
歩き出す → 何かに気づく → 立ち止まる → また歩く
```

## 3. 語彙の領域

中央列は資料に見られる語やモチーフを読みやすく整理したもの。右列は新しい文章のための拡張候補で、原稿にすべて出現するという意味ではない。

| 領域 | 観察の手がかり | 新しい場面への展開候補 |
| --- | --- | --- |
| 人称・関係 | 君、僕、私、あなた | 返事、隣の席、呼びかける前の間 |
| 天候・季節 | 夜、夏、春、秋、冬、空、雲、雨、風、月 | 朝の霧、冬の窓、湿った歩道 |
| 植物 | 花 | 草の種、鉢の土、壁際の苔 |
| 街と移動 | バス、街、高架下、自転車、海岸 | 歩道橋、改札、閉店後の通り |
| 部屋と境界 | 部屋、窓、身体、喉 | 廊下、ドアの隙間、鏡、カーテン |
| 身体感覚 | 目、手、心臓、口、指先 | 肩、耳、足の裏、息の長さ |
| 色と質感 | 灰色、藍、白さ、冷たさ | 錆色、反射、乾いた面、曇りガラス |
| 言葉と制作 | 歌、詩、言葉、音、ノート、書く、描く | 余白、消し跡、封筒、録音の間 |
| 記憶と時間 | 想い出／思い出、忘れる、夢、人生 | 古い日付、期限、折り目、色の薄れ |
| 空白と否定 | 何も、わからない、最低、空っぽ | 返らない声、途中の文、未記入欄 |

### 組み合わせ方

一つの具体的な領域に、別の感覚や時間を重ねる。数行の詩なら一組で十分である。

```text
天気 ＋ 身体      雨粒の間隔で、息を整える。
街 ＋ 時間        閉じたシャッターに、昨日の光が少し残る。
物 ＋ 関係        隣のカップだけ、まだ温かい。
紙 ＋ 動作        書き足す代わりに、封筒の角を伸ばす。
生活 ＋ 季節      小さな灯りの外で、夜の匂いが変わる。
```

## 4. 語り手と相手

### 判断を言い直す語り手

語り手は、自分が思い出し、説明し、言い換えていることに気づいている。断定の後に小さなためらいを置くと、考えている最中の声になる。

- 判断した直後に、別の可能性を思いつく。
- 「平気だ」という説明と、手や視線の動きが食い違う。
- 大きな結論を出しかけて、身近な物に戻る。
- 終わったつもりでも、最後の動作が終わっていない。

### 局部で見せる相手

相手は指先、袖、声の調子、空いた場所などを通して現れる。人物の来歴を説明せず、その人を思い出す根拠だけを置く。画像に人物がいなくても、観察者の目線や距離だけで文章を成立させられる。

| 距離 | 文章の形 | 効果 |
| --- | --- | --- |
| 近い | 呼びかけ、小さな動作、触れた感覚 | 親密さと現在性 |
| 中くらい | 昔の場所や動作を思い返す | 物が関係を保存する |
| 遠い | 人の代わりに景色や紙の状態を描く | 読者が余白を補える |

## 5. 修辞の操作

| ID | 操作 | 日本語での形 | 働き |
| --- | --- | --- | --- |
| R01 | 呼びかけ | ねえ、君、あるいは省略された相手 | 距離を縮める |
| R02 | 反復 | 同じ短い言葉に一度だけ変化をつける | ためらいや持続 |
| R03 | 言い直し | いや、たぶん、そう思っていた | 判断を開いたままにする |
| R04 | 自問 | だろうか、どうして、何を | 答えのない場所を示す |
| R05 | 仮定 | もし、なら、としたら | 感情に仮の形を与える |
| R06 | 物質化 | 抽象的なことを色、温度、重さに移す | 感覚として伝える |
| R07 | 感覚の移動 | 見たものを音や触感でも捉える | 記憶のずれ |
| R08 | 日常への着地 | 大きな考えから小さな物に戻る | 生活の手触り |
| R09 | 小さな願い | 待って、置いておいて、行こう | 行為にならない願望 |
| R10 | 制作への折り返し | 紙、消し跡、書き終える動作 | 経験を保存する |
| R11 | 終わりの保留 | 結論の後に残る動作 | 続いている時間 |
| R12 | 対照 | 温かい／冷たい、動く／留まる | 一つの場面の二面性 |

### 可変の文型

文型は構文関係を示す。穴埋めで固定フレーズを量産せず、画像の物と動詞に合わせて語順も作り直す。

```text
[具体物]に触れると、[感覚]だけが遅れてきた。
[言おうとしたこと]より先に、[小さな動作]が終わっていた。
[場所]は同じなのに、[細部]の見え方が違う。
[出来事]を覚えている。けれど、[一部分]だけが曖昧だ。
[物]を片づけるつもりで、[別の動作]をしていた。
[問い]。その間にも、[画面の動き]は続いている。
```

## 6. 音、文体、改行

長めの行で情景を置き、短い行で見え方を変える。カードでは一行に複数の説明を詰めず、名詞と動詞の関係が追える長さにする。

```text
閉店した店の窓に、まだ明るい空が映っている。
帰ろうか。
```

口語の「たぶん」「まだ」「もう」「だけ」は声の距離を調整する。重ねすぎると曖昧さだけが残るため、意味のある箇所に置く。

```text
覚えている → 覚えていたつもりだ → 手だけが覚えている
帰ろう → 少し待とう → もう一度だけ景色を見る
```

日本語として自然にするため、次を確認する。

- 主語を毎行繰り返さず、省略しても関係が分かるか。
- 「僕」「私」「君」「あなた」の選択に意味があり、途中で不用意に変わっていないか。
- 普通体と丁寧体の切り替えが意図的か。
- 助詞や助動詞だけが次行に残らず、改行が呼吸に合うか。
- 漢字を増やして詩らしさを作っていないか。読みやすい表記か。
- 句読点と余白が役割を持っているか。三点リーダーの多用になっていないか。
- 感覚の転用が読み手に伝わり、単なる不自然な連語になっていないか。

## 7. 感情の経路

| 経路 | 動き |
| --- | --- |
| 記憶 | 物を見る → 身体が反応する → 相手を思う → 細部だけ残る |
| 生活と制作 | 日常の行き詰まり → 記録する → 形が残る → 次の日へ |
| 感覚 | 光や匂い → 身体 → 言葉にならない → 別の細部を描く |
| 移動 | 出発する → 景色が変わる → 気持ちは遅れる → 進む |

カード用には「物を見る → 細部だけ残る」など、二つの動きに圧縮できる。すべてを悲しみに結びつけず、画面によって驚き、安堵、期待、遊び心も許す。

## 8. 構成の型

| ID | 長い文章での順序 | カードへの圧縮 |
| --- | --- | --- |
| A_MEMORY_LETTER | 呼びかけ → 物 → 昔 → 現在 → 確認 → 未完の手紙 | 物一つと、言い残したこと |
| B_SEASONAL_CUT | 天気 → 移動 → 感覚 → 回想 → 景色の変化 → 季節の移ろい | 光と、その中の小さな変化 |
| C_ARTIFACT | 制作 → 行き詰まり → 疑い → 消す → 残る → 余白 | 紙の上の一動作 |
| D_DIALOGUE_VOID | 呼びかけ → 問い → 仮の答え → 言い直し → 問い → 間 | 一つの問いと、続く景色 |
| E_DEPARTURE | 場所 → 出発 → 道中 → 距離 → 変化 → 続く移動 | 歩く方向と、留まる物 |

## 9. 表現単位14件

`example_ja` は仕組みを示す新規用例。画像ごとに別の文章を作るための参考である。

```yaml
- id: AT-REL-001
  tag: direct_address_with_withdrawal
  formula: 呼びかけようとして、小さな動作に置き換える
  function: 伝える直前の距離
  example_ja: 声をかけそびれて、窓の曇りを指でなぞった。

- id: AT-REL-002
  tag: partial_portrait
  formula: 人物の一部分に記憶を預ける
  function: 説明されない人物像
  example_ja: 袖のほつれだけ、別れた日のまま覚えている。

- id: AT-REL-003
  tag: asymmetrical_memory
  formula: 同じ出来事を違う細部で覚えている
  function: 共有した時間のずれ
  example_ja: 私は風の強さを、あなたは遅刻した時刻を覚えていた。

- id: AT-IMG-001
  tag: ordinary_object_as_emotion
  formula: 日用品の状態で気持ちを示す
  function: 生活の手触り
  example_ja: 向かいのカップが冷えるまで、椅子を戻せなかった。

- id: AT-IMG-002
  tag: weather_as_time
  formula: 天気の変化と行動の遅れを重ねる
  function: 言葉にしない時間差
  example_ja: 晴れてからも、傘を閉じる場所を探していた。

- id: AT-IMG-003
  tag: urban_transit_memory
  formula: 交通の終わりと、人の動作をずらす
  function: 移動のあとに残る時間
  example_ja: 最終便の表示が消えても、靴先は道路を向いていた。

- id: AT-IMG-004
  tag: color_to_sensation
  formula: 色の印象を身体の感覚に移す
  function: 見ることの身体性
  example_ja: 曇りガラスの白さが、冷えた指に移った気がした。

- id: AT-LNG-001
  tag: self_negating_statement
  formula: 断定のあと、動作によって言い直す
  function: 判断の揺れ
  example_ja: 平気だと言ってから、何度も同じボタンを掛け直した。

- id: AT-LNG-002
  tag: repeated_question
  formula: 問いを繰り返す代わりに、二度目を飲み込む
  function: 発話の間
  example_ja: 覚えてる、と聞いた。二度目は口の中に残した。

- id: AT-LNG-003
  tag: conditional_emotion
  formula: 感情を仮の物質として扱う
  function: 抽象的なことに手触りを与える
  example_ja: ためらいに重さがあるなら、この封筒は少し傾く。

- id: AT-LNG-004
  tag: semantic_relabeling
  formula: 日常の痕跡に新しい呼び名を与える
  function: 記憶の保存方法を変える
  example_ja: 消し残した日付を、しばらく栞と呼ぶことにした。

- id: AT-END-001
  tag: artwork_closure_with_residue
  formula: 書く行為が終わっても、周囲の動作を残す
  function: 終わりの余韻
  example_ja: ペンを置いたあとも、カーテンが余白を撫でていた。

- id: AT-END-002
  tag: farewell_as_instruction
  formula: 小さな依頼のあとに、相手の痕跡を残す
  function: 命令になりきらない願い
  example_ja: 鍵は置いていって。玄関の音だけ、まだ覚えていたい。

- id: AT-END-003
  tag: motion_without_resolution
  formula: 答えを出さずに具体的な動作を続ける
  function: 開かれた時間
  example_ja: 決められないまま、川沿いの灯りを一つずつ通り過ぎた。
```

## 10. 原稿区分ごとの抽象記録11件

以下は各区分に対する編集上の読解であり、作者の意図を断定するものではない。区分ごとの特徴を比較するための記録として使う。

```yaml
- record_id: REC-001
  source_section: 其一
  semantic_scene: 交通の結節点と人のいる風景
  speaker_distance: 近い
  primary_motion: 相手の動作が日常の物の見え方を変える
  sensory_anchor: 接触と空間
  rhetoric: [direct_address_with_withdrawal, ordinary_object_as_emotion]
  emotional_arc: 注目、ためらい、言葉の勢い
  ending_state: 動く場面が残る

- record_id: REC-002
  source_section: 其二
  semantic_scene: 夜の移動と生活の行き詰まり
  speaker_distance: 中くらい
  primary_motion: 街を進みながら自分の判断を反復する
  sensory_anchor: 夜風と呼吸
  rhetoric: [self_negating_statement, semantic_relabeling]
  emotional_arc: 嫌悪、高揚、記憶への執着
  ending_state: 自己評価が揺れ続ける

- record_id: REC-003
  source_section: 其三
  semantic_scene: 夏の記憶と身近な場所
  speaker_distance: 中くらい
  primary_motion: 景色の細部から過去へ戻る
  sensory_anchor: 空と季節の匂い
  rhetoric: [weather_as_time, partial_portrait]
  emotional_arc: 回想、距離、内側に残る記憶
  ending_state: 言葉にしきれない関係

- record_id: REC-004
  source_section: 其四
  semantic_scene: 身体の内側と言葉の生まれる場所
  speaker_distance: 近い
  primary_motion: 身体と歌に相手を保存しようとする
  sensory_anchor: 喉と温度
  rhetoric: [conditional_emotion, farewell_as_instruction]
  emotional_arc: 理解、忘却への恐れ、猶予の願い
  ending_state: 表現を続ける時間

- record_id: REC-005
  source_section: 其五
  semantic_scene: 言葉と自分の隔たり
  speaker_distance: 近い
  primary_motion: 定義しながら、その定義を問い直す
  sensory_anchor: 色と匂い
  rhetoric: [semantic_relabeling, repeated_question]
  emotional_arc: 説明、疑問、自然の動きへの転換
  ending_state: 季節を進む声

- record_id: REC-006
  source_section: 其六
  semantic_scene: 狭い部屋と生活の数字
  speaker_distance: 中くらい
  primary_motion: 幸福や時間を生活の尺度で測る
  sensory_anchor: 冷たさと部屋の広さ
  rhetoric: [ordinary_object_as_emotion, self_negating_statement]
  emotional_arc: 願い、欠乏、記憶の言い換え
  ending_state: 詩へ移される関係

- record_id: REC-007
  source_section: 其七
  semantic_scene: 正午の景色とノート
  speaker_distance: 遠い
  primary_motion: 夢と人生を書きながら評価し直す
  sensory_anchor: 色と紙面
  rhetoric: [artwork_closure_with_residue, semantic_relabeling]
  emotional_arc: 妥協、相手への集中、描き続けること
  ending_state: 景色の中に残る相手

- record_id: REC-008
  source_section: 其八
  semantic_scene: 高さを変えて見える街と夏
  speaker_distance: 遠い
  primary_motion: 離れても相手を探す視線が残る
  sensory_anchor: 光、音、高さ
  rhetoric: [direct_address_with_withdrawal, motion_without_resolution]
  emotional_arc: 発話の不足、移動、見失うこと
  ending_state: 遠ざかる季節

- record_id: REC-009
  source_section: 其九
  semantic_scene: 傾く光と自分への問い
  speaker_distance: 中くらい
  primary_motion: 光に触れる感覚から関係を捉える
  sensory_anchor: 眩しさと指先
  rhetoric: [color_to_sensation, conditional_emotion]
  emotional_arc: 悲しみ、接触、相手の発見
  ending_state: 静けさの中の未確定な感情

- record_id: REC-010
  source_section: 其十
  semantic_scene: 飲み物、海辺、色の薄れる時間
  speaker_distance: 中くらい
  primary_motion: 物の色と季節の細部に記憶を重ねる
  sensory_anchor: 灰白色、潮騒、海風
  rhetoric: [ordinary_object_as_emotion, weather_as_time]
  emotional_arc: 言い訳、分からなさ、保存の願い
  ending_state: 書くことに託される記憶

- record_id: REC-011
  source_section: 其十一
  semantic_scene: 羽と異なる速度で進む存在
  speaker_distance: 遠い
  primary_motion: 飛ぶ動きと人の時間を重ねる
  sensory_anchor: 乾き、光、速度
  rhetoric: [motion_without_resolution, partial_portrait]
  emotional_arc: 凝視、追い越されること、ためらう動き
  ending_state: 遠くへ開かれる方向
```

## 11. カード用の短い編集例

以下は配置と長さの例であり、完成済みの定型文集ではない。場面条件が一致しても、その画像の細部から書き直す。

### A：人の少ない道と横からの光

```text
曲がり角の光を踏まないように、
今日は少し、遠回りした。
```

### B：紙と小さな卓上灯

```text
書き足さなかったところまで、
灯りが届いている。
```

### C：水面と静かな岸

```text
岸に腰を下ろすと、
水の音にも、いくつかの間があった。
```

### D：空いた椅子と窓の光

```text
椅子を寄せる。
窓の明るさが、膝まで来た。
```

## 12. 選択と推敲

優先すること：画面にある具体物、自然な日本語、一つの感覚、一つの小さな変化、文字を置かない余白。意味が十分に伝われば、比喩も人称も入れなくてよい。

気をつけること：美しい名詞の列挙、毎回同じ別れ、根拠のない季節、説明だけの結末、過剰な言い直し、歌詞の特徴的な語順を残した置き換え。作品の自指や自己否定を毎回の必須条件にしない。

原稿や既存の詩に近いと感じる場合は、単語だけでなく、物、動作、視点、比喩の関係から作り直す。例文の言い換えだけで新規性を判断しない。

## 13. 評価の観点

| 観点 | 確認すること |
| --- | --- |
| 情景との関係 | 実際の画面から生まれた文章か |
| 具体性 | 一つの物や動作を追えるか |
| 日本語 | 助詞、語順、語の組み合わせ、改行が自然か |
| 感情の余白 | 感情をすべて説明せずに伝わるか |
| 紙面との関係 | 既存文字や署名と競合せず、判読できるか |
| 独立性 | 歌詞、曲名、既存詩、用例の特徴的な表現に依存していないか |

必要なら各項目を0〜2点で記録できるが、点数は編集用の目安であり、特定作家への近さを証明する指標ではない。文字列の一致だけでも判定できない。特徴的な比喩の関係と、ありふれた日本語表現を区別する。

## 14. 制作時の記録形式

```yaml
record_id: POSTCARD-001
language: ja
source_image: actual_selected_mv_image_path
corpus_id: yorushika-lyric-style-distillation-ja-20260831
visible_anchors: []
sensory_anchor: null
selected_atoms: []
emotional_relation: null
verse_ja: []
gloss_zh: null
existing_microcopy: null
new_verse_decision: null
originality_review: pending
glyph_review: pending
```

`visible_anchors` は実際の画像で確認した物だけを記録する。`selected_atoms` は必要なものだけ選ぶ。採用した詩は `verse_ja` の行順を保持する。不要なときは配列を空にして理由を記録する。画像生成前の文章確認と、生成後の字形確認を分ける。まだ画像を作っていない段階で検査済みと記録しない。

## 15. この資料から持ち帰るもの

感情が物の状態に変わること、関係が距離や局部に現れること、時間が小さな動作のあとにも続くこと。この三つの見方を、毎回違う画面に適用する。

一枚のカードに必要なのは、場面の細部と文章が互いを少し変えることだけである。

## 出典と版管理

- 原資料：ユーザー提供の `yorushika/歌词.md`。原資料は本リポジトリに同梱せず、技能の実行時にも必要としない。
- 編集元：`20260830-Yorushika-词风蒸馏语料库-版本001.md`。
- 日本語版作成日：2026-08-31。
- 技能内の参照先：`yorushika-postcard-scenes/references/japanese-verse-corpus.md`。
- 中国語版の説明を日本語に整理し、ポストカードの短詩に合わせて用例と評価基準を調整した。
- 原稿と中国語版を保持する。新たな歌詞取得や曲名の補完は行っていない。
