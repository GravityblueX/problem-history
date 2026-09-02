# Source Citation Minimum Standard

> **引用的目标不是“看起来像参考文献”，而是让另一个研究者能够重新定位同一份历史材料，并判断这份材料究竟支持了哪一个历史主张。**

本文件定义 `problem-history` 的最小 source citation / evidence provenance 规范。

它不是通用文献格式手册，也不要求仓库统一使用 Chicago、MLA 或某一种书目排版风格。它处理的是更靠前的一层：

```text
我们到底看了哪一个版本 / 哪一页 / 哪一份档案？
        ↓
数字文本从哪里来，是否只是 OCR？
        ↓
谁在什么时候说了什么？
        ↓
这条材料支持的是 actor formulation、context、presupposition，还是后来重构？
        ↓
如果以后链接失效、版本变化或研究者不同意，能否重新检查？
```

这份规范尤其服务于仓库最容易出错的三种历史判断：

1. 把今天的研究问题误写成历史行动者自己的问题；
2. 把后来的整理、回忆或政策史叙述误当成同时代 evidence；
3. 把一个方便访问的 HTML/OCR 页面误当成“原始文本本身”。

---

## 1. 核心原则

### 1.1 Citation 与 evidence claim 必须分开

一个书目条目只能回答：

> 这是什么材料？

它不能自动回答：

> 这份材料证明了什么？

因此本仓库把 source record 与 claim link 分开。

```yaml
source:
  id: src-001
  # 描述材料本身

claim_link:
  claim_id: claim-017
  source_id: src-001
  relation: supports
  # 描述这份材料怎样支持/反驳具体判断
```

禁止：

```yaml
evidence:
  - "Skinner 1969"
```

因为它没有说明：

- 哪一版；
- 哪一页；
- 哪一句；
- 支持什么判断；
- 是作者原话、研究者重述，还是后来解释。

---

### 1.2 `primary` 不是“更真实”的同义词

同时代材料非常重要，但 `primary source` 不能作为真实性评分。

一份同时代材料仍可能：

- 有明确政治、职业或制度目的；
- 只代表一个行动者或机构；
- 不知道关键事实；
- 有意隐瞒；
- 是宣传、修辞或事后自我辩护；
- 只适合证明“有人这样说”，不适合证明“事情就是这样”。

因此 source classification 必须拆轴，不使用：

```text
primary = high
secondary = low
```

这种粗暴排序。

Library of Congress 对 primary-source analysis 的公开指南同样强调：原始材料必须结合 creator、purpose、audience、point of view、historical context，并与其他来源相互比较，而不是作为未经解释的“历史事实块”。

参考：

- Library of Congress, “Getting Started with Primary Sources”  
  https://www.loc.gov/programs/teachers/getting-started-with-primary-sources/
- Library of Congress, “Citing Primary Sources”  
  https://www.loc.gov/programs/teachers/getting-started-with-primary-sources/citing/

访问：2026-09-03。

---

### 1.3 引用必须指向可重新定位的对象，而不只是一个网页

历史材料的“对象”可能是：

- 某一版书；
- 一篇报刊文章；
- 一封信；
- 一份会议记录；
- 某卷档案中的一个文件；
- 一张手稿的特定 folio；
- 一个录音的某个 timecode；
- 一个数据库中的某条记录；
- 一个扫描件中的特定图像；
- 一个不断更新的网站版本。

网页只是访问路径之一。

例如：

```text
Google Books / Internet Archive / HathiTrust / 某机构 HTML
```

通常是 **carrier / digital representation**，不是历史对象本身。

---

### 1.4 历史日期、版本日期、数字化日期、访问日期必须分开

至少区分：

```yaml
original_date: 1753
edition_date: 1772
scan_or_web_publication_date: 2018
accessed: 2026-09-03
```

禁止把现代网页的发布日期写成历史行动者文本的日期。

也禁止看到：

```text
Last updated: 2025
```

就把一个 1902 年文件当成“2025 source”。

---

## 2. Source record 的最小字段

对于会被用于历史结论的来源，至少保存以下字段。

```yaml
source_id: src-...

identity:
  creator: "..."
  title: "..."
  original_date: "YYYY-MM-DD | YYYY | circa | range | unknown"
  language: "..."
  source_type: "..."

version:
  edition_or_version: "..."
  editor: "..."
  translator: "..."
  publication_place: "..."
  publisher: "..."
  edition_date: "..."

locator:
  type: page | folio | paragraph | section | column | item | file | timecode | image | canvas | other
  value: "..."

provenance:
  repository_or_host: "..."
  collection_or_series: "..."
  catalogue_or_item_id: "..."
  stable_identifier: "DOI / Handle / ARK / catalogue URI / other"
  url: "..."
  accessed: "YYYY-MM-DD"

digital_representation:
  mode: facsimile | diplomatic_transcription | edited_transcription | html | ocr | born_digital | audio | video | other
  facsimile_checked: true | false | not_applicable
  ocr_only: true | false
  notes: "..."
```

不是每个字段都必须有值；但缺失应该显式可见，而不是被默认补全。

例如：

```yaml
translator: null
catalogue_or_item_id: unknown
facsimile_checked: false
```

比完全不记录更安全。

---

## 3. 不再用单一 A/B/C 代表“证据等级”

现有 pilot 使用过 `Evidence level A/B/C`。这种局部标签可以保留，但不能升级成全仓统一的可信度等级。

原因是至少有三个独立维度：

### 3.1 Temporal relation

```yaml
temporality:
  contemporary
  near_contemporary
  retrospective
  later
```

### 3.2 Relation to the historical action

```yaml
participant_relation:
  actor
  opponent
  witness
  institution
  audience
  external_observer
  later_scholar
  later_official_history
```

### 3.3 Evidential function

```yaml
evidential_function:
  explicit_problem_formulation
  reconstructed_actor_context
  presupposition
  vocabulary
  speech_act
  stakes
  answer_space
  institutional_condition
  uptake_or_reply
  continuity_claim
  discontinuity_claim
  emergence
  disappearance_or_displacement
  negative_evidence
  later_reconstruction
  discovery_lead
```

同一来源可以在不同 claim 中承担不同 function。

例如一份 1956 年会议报告可以：

- 强力证明某机构公开采用了某种 formulation；
- 中等程度支持当时制度 stakes；
- 很弱地支持“所有知识分子都这样理解”；
- 完全不能单独证明私人信念。

所以 evidence strength 必须是 **claim-relative**。

---

## 4. Claim link：每条重要结论必须知道自己从哪里来

建议最小结构：

```yaml
claim_id: claim-1956-answer-space-01
claim_type: historical_reconstruction
text: "..."

source_links:
  - source_id: src-1956-03
    relation: supports
    directness: explicit | inferential | contextual
    locator: "p. 17"
    note: "行动者直接列出可接受政策选项"

  - source_id: src-1956-07
    relation: complicates
    directness: explicit
    locator: "letter, 1956-02-14"
    note: "私人通信显示另一套 stakes"
```

允许的 `relation` 至少包括：

```text
supports
contradicts
complicates
contextualizes
dates
locates
transmits
later_reinterprets
```

这比一个粗糙 `evidence: []` 更适合 problem history，因为同一材料经常同时产生 continuity 与 discontinuity evidence。

---

## 5. Locator 是硬要求，不是装饰

对于能够稳定定位的材料，不接受只给首页 URL。

### 印刷书 / 论文

优先：

```text
page / pages
chapter + page
section + paragraph（无稳定分页时）
```

### 报刊

优先：

```text
date + title + page + column
```

### 手稿 / 档案

优先：

```text
repository + collection/series + file/item + folio/page/internal number
```

The National Archives (UK) 的公开指南特别建议保留其 catalogue reference 的原始结构，并尽量引用 catalogue hierarchy 中最低可用层级，再加入具体 page / folio / internal identifier。

参考：

- The National Archives, “Citing records in The National Archives”  
  https://www.nationalarchives.gov.uk/help-with-your-research/discovery-help/citing-records-national-archives/

访问：2026-09-03。

美国 National Archives 的公开说明同样强调，档案引用应能识别 document、series/record group、repository，并在数字记录中保留 Catalog 定位信息。

参考：

- National Archives, “Frequently Asked Questions — How do I cite a record in the Catalog?”  
  https://www.archives.gov/citizen-archivist/faqs
- National Archives, “Citing the Records of Congress”  
  https://www.archives.gov/legislative/research/citation.html

访问：2026-09-03。

### 音频 / 视频

优先：

```text
recording identifier + timecode range
```

例如：

```yaml
locator:
  type: timecode
  value: "00:31:18-00:32:04"
```

### 数字 facsimile

如果页面图像和印刷页码不同，应同时保存：

```yaml
printed_page: 128
scan_image: 147
```

否则换平台后很容易失去定位能力。

---

## 6. 数字文本必须记录 mediation layer

历史文本进入 Agent 之前，经常经历：

```text
physical source
  ↓
scan / photograph
  ↓
OCR
  ↓
manual correction
  ↓
HTML / plain text / PDF extraction
  ↓
LLM interpretation
```

其中每一步都可能改变证据。

因此不能只保存：

```yaml
url: "..."
```

而应说明研究实际读取的是哪一层。

### 推荐值

```yaml
digital_representation:
  mode: facsimile
  facsimile_checked: true
```

或：

```yaml
digital_representation:
  mode: ocr
  facsimile_checked: false
  ocr_only: true
  notes: "关键词由 OCR 命中；尚未回图像校对"
```

### 强制规则

```text
OCR hit
≠
verified quotation
```

任何进入最终引文、关键 actor formulation 或 identity verdict 的词句，若 facsimile 可获得，原则上应回图像核验。

TEI P5 把 source description、encoding relation、revision history、责任人以及 transcription ↔ facsimile 的连接都作为电子文本可复核性的核心组成部分。这里不要求仓库采用 TEI XML，但借用它的 provenance 原则。

参考：

- TEI P5, “The TEI Header”  
  https://tei-c.org/release/doc/tei-p5-doc/en/html/HD.html
- TEI P5, “Representation of Primary Sources”  
  https://www.tei-c.org/release/doc/tei-p5-doc/en/html/PH.html
- TEI P5, `<respStmt>`  
  https://tei-c.org/release/doc/tei-p5-doc/en/html/ref-respStmt.html

访问：2026-09-03。

---

## 7. Edition / version 必须进入证据链

对于方法文本、政治文件、文学作品、演讲整理、回忆录、译本等，版本差异可能改变结论。

至少问：

- 这是初版还是后来修订版？
- 文字是否经编辑者整理？
- 演讲稿是当时稿件、速记、录音转写，还是多年后出版？
- 译本是否改变关键概念？
- 后来的选集是否删改题目、段落、标点或措辞？

如果 conclusion 依赖某个具体措辞，必须绑定具体 version。

禁止：

```text
作者 1969 年说过 X
```

但引用实际上来自 2002 年作者自己修订后的重印文本，而且没有说明版本差异。

这条规则已经在 Skinner、Foucault 方法谱系研究中实际遇到，因此必须上升为全仓 source rule。

---

## 8. Translation 不应覆盖原文责任

如果研究使用译文，至少保存：

```yaml
translation:
  status: published | researcher | machine_assisted | unknown
  translator: "..."
  source_language: "..."
  original_locator: "..."
```

关键术语关系到 problem identity 时，应尽量保存原词，例如：

```yaml
term:
  original: "Problematik"
  translation_used: "problematic / 问题结构"
  note: "不自动等同于 repository 的 Problem Episode"
```

禁止：

```text
译文用了同一个词
→ 原语言概念连续
→ problem continuity
```

翻译本身可以是历史 evidence，但需要被当成一个新的 historical act 来研究，而不是透明管道。

---

## 9. Stable identifier 优先于裸 URL，但 identifier 也不能替代版本信息

对论文、书目对象和数字档案，优先记录可用的 persistent identifier：

- DOI；
- Handle；
- ARK；
- archive catalogue ID；
- library persistent URI；
- stable item identifier。

DOI Foundation 将 DOI 定义为独立于当前位置的持久标识符；其价值正在于对象移动或 URL 改变时仍能维持 identity / resolution。

参考：

- DOI Foundation, “What is a DOI?”  
  https://www.doi.org/the-identifier/what-is-a-doi
- DOI Handbook  
  https://www.doi.org/doi-handbook/html/

访问：2026-09-03。

但：

```text
DOI
≠
exact textual locator
```

DOI 只解决“是哪一个对象”的一部分问题。仍需记录 version / page / section。

---

## 10. Mutable Web Source

如果来源本身是会变化的网页，而不是稳定扫描件，应至少保存：

```yaml
web_source:
  canonical_url: "..."
  accessed: "2026-09-03"
  page_title: "..."
  organization: "..."
  dated_by_publisher: "..."
  archived_snapshot: "..."   # 可得时
```

### 特别区分

```text
page publication/update date
≠
historical event date
≠
original document date
≠
access date
```

如果网页只是转载历史文本，还必须继续寻找它所依据的版次/文献身份。

网页可用于发现线索，但“官方站点”三个字也不能自动解决 edition provenance。

---

## 11. Quotation policy

### 11.1 直接引文

每个关键直接引文必须有：

- source ID；
- exact locator；
- version/edition；
- transcription/facsimile verification status。

### 11.2 Paraphrase

改写不是免引用区。

如果 paraphrase 承担 actor-level evidence，也必须绑定 source + locator。

### 11.3 关键词摘录

单个关键词不能脱离句法和 speech-act context 自动成为 problem formulation。

建议至少保留：

```yaml
quote_scope:
  immediate_sentence: true
  surrounding_context_checked: true
```

必要时记录前后段落。

---

## 12. Evidence strength：不用假精确分数

本仓库暂不使用 `0.87` 之类的伪精确 evidence score。

建议使用可解释的维度式判断：

```yaml
evidence_assessment:
  actor_proximity: strong | medium | weak | not_applicable
  knowledge_position: strong | medium | weak | unknown
  genre_fit: strong | medium | weak
  locator_precision: strong | medium | weak
  text_verification: facsimile_checked | trusted_edition | transcription_only | ocr_only
  independence: independent | derivative | unclear
  competing_evidence_checked: true | false
  overall_for_this_claim: strong | medium | weak | lead_only
  note: "..."
```

### 一个来源不能自己给自己独立性

以下不能算两个独立证据：

```text
现代网页 A
现代网页 B
```

如果二者都转载同一份后来编纂的材料。

需要追踪 derivative chain。

```yaml
derived_from:
  - source_id: src-older-edition
```

---

## 13. Source role 与 formulation source 要联动

`IDENTITY-CHECK.md` 已要求区分：

```yaml
formulation_source:
  actor_explicit
  actor_reconstructed
  researcher_analytic
```

source citation 必须让这个字段可审计。

### `actor_explicit`

要求：

- 行动者或参与争论的机构材料；
- exact locator；
- wording 可核验；
- 不把后来的 editorial heading 当作 actor wording。

### `actor_reconstructed`

要求：

- 至少一条 actor/contemporary source；
- 另外的 context / reply / institution / vocabulary evidence；
- 明确写出推断链；
- 保留 competing reconstruction。

### `researcher_analytic`

可以只由现代研究问题驱动，但必须显式标记，不能借一个历史引文伪装成 actor formulation。

---

## 14. Negative evidence 需要额外 provenance

对于：

```text
没有找到
没有记录
没人再说
```

citation 要比 positive evidence 更严格。

至少记录：

```yaml
negative_search:
  corpus_or_archive: "..."
  coverage: "..."
  date_range: "..."
  search_terms: []
  alternate_terms_checked: []
  access_limitations: []
  digitization_limitations: []
  expected_recording_reason: "..."
```

否则：

```text
0 result
```

只是在描述本次检索，不是在描述历史世界。

详细规则见开放研究包 `docs/NEGATIVE-EVIDENCE.md`（合并后作为本规范的配套文档）。

---

## 15. 一个可直接复制的最小模板

```yaml
source_id: src-example-001

identity:
  creator: "Author / institution"
  title: "Exact title"
  original_date: "YYYY-MM-DD"
  language: "en"
  source_type: "printed_report"

version:
  edition_or_version: "first edition"
  editor: null
  translator: null
  publication_place: "London"
  publisher: "Publisher"
  edition_date: "YYYY"

locator:
  type: page
  value: "42-43"

provenance:
  repository_or_host: "Institution"
  collection_or_series: null
  catalogue_or_item_id: "..."
  stable_identifier: "..."
  url: "..."
  accessed: "YYYY-MM-DD"

digital_representation:
  mode: facsimile
  facsimile_checked: true
  ocr_only: false
  notes: "OCR used only for discovery; quotation checked against scan."

classification:
  temporality: contemporary
  participant_relation: actor

claim_links:
  - claim_id: claim-example-01
    evidential_function: explicit_problem_formulation
    relation: supports
    directness: explicit
    strength_for_claim: strong
    note: "Actor directly frames X as the difficulty requiring action."

uncertainty:
  - "Only demonstrates this actor/institution's formulation."
  - "Does not establish broader social uptake."
```

---

## 16. Minimal acceptance gate

任何准备进入：

- Problem Episode；
- identity relation；
- emergence / displacement / became-unaskable 判断；
- synthesis 中的关键历史结论；

的 evidence，至少回答以下十个问题：

1. **Which source?** 精确是哪一份材料？
2. **Which version?** 哪一个版本 / edition / transcription？
3. **When?** 原始日期是什么？现代数字化日期是否被分开？
4. **Where?** 页、folio、item、timecode 或其他精确 locator 在哪里？
5. **Who?** creator / actor / institution 是谁？
6. **For whom / why?** audience 与 source purpose 是否影响解释？
7. **Through what mediation?** scan、OCR、编辑文本还是转载 HTML？
8. **What claim?** 它究竟支持或反驳哪一个 claim？
9. **How directly?** 是 explicit、inferential 还是 contextual？
10. **What can it not prove?** 至少写一条 evidence boundary。

如果其中 1–4 无法回答，这条材料通常只能停在：

```text
lead / discovery source
```

而不能承担强 identity 或 actor-formulation verdict。

---

## 17. AI self-check

Agent 写出任何“历史行动者当时的问题是……”之前，必须自检：

- 我引用的是行动者文本，还是后来的人替他总结？
- 我看到的是原始 wording，还是 OCR/译文/选集标题？
- 我能指出 exact locator 吗？
- 我是否把网页发布日期误当成历史日期？
- 我是否知道这一版与初版有没有差异？
- 这份 source 证明的是“有人这样说”，还是我正在把它扩大成“当时的人都这样想”？
- 我是否保存了反证或竞争材料？
- 如果另一个研究者明天点击不到这个网页，他还能凭 citation 找回材料吗？

任一关键问题回答不了时，应降级 claim：

```text
strong conclusion
→ provisional
→ lead_only
→ evidence_gap
```

而不是补写更自信的文字。

---

## 18. 与后续 schema 的关系

本文件先冻结 **研究约束**，不立即冻结 JSON Schema。

未来 `problem-episode.schema.json` 至少应能表达：

```text
source identity
version
locator
provenance
digital mediation
claim-source relation
source temporality
participant relation
evidential function
verification status
uncertainty
```

但字段名字和嵌套结构可以根据真实 pilot 调整。

尤其不要现在把：

```yaml
strength: A
```

写死成 schema enum。

真实历史材料很可能证明它过于粗糙。

---

## 19. 当前仓库迁移建议

### 1949–1956 pilot

`studies/1949-intellectual-transition/sources.md` 当前的 A/B/C 分类应保留为历史记录，但未来新增来源建议改用本文件的多轴分类。

优先补：

- 1951 报告的稳定全文版次与页码；
- 1956 会议材料的 exact locator；
- 非官方 actor material 的 archive/edition provenance。

### Method lineage

Collingwood / Skinner / Koselleck / Foucault 笔记以后若升级为正式 `METHOD.md` 的直接引文，应再次检查：

- 原始版 / 修订版；
- page locator；
- edited lecture / interview / transcription status；
- 二手论文是否只是用于定位，而不是替代 primary text。

### Future 50-year pilot

从第一条 source 起就使用本规范，不要在 synthesis 阶段再补 provenance。

否则最容易出现：

```text
几个月后知道“这句话很重要”
但已经不知道它究竟从哪个版次、哪一页、哪一个数字文本复制出来
```

---

## 20. 本规范不做什么

它不：

- 指定论文最终必须使用 Chicago / MLA / GB/T 7714 中哪一种排版；
- 把 primary source 自动评为高可信；
- 用元数据代替 source criticism；
- 要求每一条背景事实都建立复杂 YAML；
- 要求所有数字文本转换成 TEI；
- 假装 precise citation 可以消除解释争议。

它只要求：

> **任何足以改变 Problem Episode 或 problem identity 的历史证据，都必须留下可重新定位、可识别版本、可追踪数字中介、可对应具体 claim 的证据链。**

---

## References / standards consulted

以下资料用于确定“可重新定位、版本可辨、数字来源有 provenance”这一最低标准；本文件中的 YAML 与字段设计均为本仓库自己的 operationalization，不宣称这些机构提供了 Problem History schema。

- Library of Congress. “Getting Started with Primary Sources.”  
  https://www.loc.gov/programs/teachers/getting-started-with-primary-sources/
- Library of Congress. “Citing Primary Sources.”  
  https://www.loc.gov/programs/teachers/getting-started-with-primary-sources/citing/
- U.S. National Archives. “Frequently Asked Questions,” section on citing Catalog records.  
  https://www.archives.gov/citizen-archivist/faqs
- U.S. National Archives. “Citing the Records of Congress.”  
  https://www.archives.gov/legislative/research/citation.html
- The National Archives (UK). “Citing records in The National Archives.”  
  https://www.nationalarchives.gov.uk/help-with-your-research/discovery-help/citing-records-national-archives/
- Text Encoding Initiative. *TEI P5 Guidelines*, “The TEI Header.”  
  https://tei-c.org/release/doc/tei-p5-doc/en/html/HD.html
- Text Encoding Initiative. *TEI P5 Guidelines*, “Representation of Primary Sources.”  
  https://www.tei-c.org/release/doc/tei-p5-doc/en/html/PH.html
- DOI Foundation. “What is a DOI?”  
  https://www.doi.org/the-identifier/what-is-a-doi
- DOI Foundation. *DOI Handbook*.  
  https://www.doi.org/doi-handbook/html/

Web resources checked 2026-09-03.
