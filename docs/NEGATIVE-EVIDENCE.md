# Negative Evidence：沉默、缺失与 `became_unaskable` 的证据规则

> 状态：cross-cutting method research note  
> 目的：补足当前方法链中最薄弱的一段——当研究者看到“后来不再出现”“档案里找不到”“某词消失”时，究竟在什么条件下可以把这种沉默当作历史证据；尤其用于约束 `askability.weakened / displaced / became_unaskable`。

## 1. 为什么现在需要这份笔记

当前仓库已经完成四条核心方法谱系：

- Collingwood：actor-question reconstruction 本身是历史判断；
- Skinner：重建必须通过 actor-language / speech-act / interaction context；
- Koselleck：lexical / semantic / conceptual continuity 不能自动升级为 problem continuity；
- Foucault：historical difficulty 不等于 historical problem，`absence != unaskability`，问题消失也不等于问题被解决。

但还有一个方法缺口没有单独处理：

> **如果“没有出现”本身要被用作 evidence，我们如何判断这个 silence 是行动者层面的历史事实，还是 source creation、archival survival、access、digitization、retrieval 或 researcher selection 造成的？**

这不是边缘问题。Problem History 的核心目标之一就是研究：

- 问题为什么出现；
- 为什么继续可问；
- 为什么变弱、被替代；
- 为什么最终可能不再可问。

其中最后两项极易被 `search result = 0` 误导。

本笔记只解决这一件事，不引入新的“第五位方法论大师”，也不提前冻结 schema。

---

## 2. 一手方法文本：历史学很早就知道“沉默”需要额外前提

### 2.1 Langlois & Seignobos：`argument from silence` 不是普通缺词检索

Charles-Victor Langlois 与 Charles Seignobos 的 *Introduction aux études historiques*（1898；英文译本 *Introduction to the Study of History*）在 Book III, ch. III “Constructive Reasoning” 中专门讨论 negative reasoning / argument from silence。

公共领域英文全文：

- Project Gutenberg: https://www.gutenberg.org/ebooks/29637
- HTML full text: https://www.gutenberg.org/files/29637/29637-h/29637-h.htm

对本项目最重要的不是他们把“默证”宣布成可靠方法，而是恰好相反：他们要求先承认 documents 永远不完整，而且大量历史事件从未被记录，大量已经写下的记录也会遗失。

其操作性结论可以概括为：

```text
no surviving mention
≠
no historical fact
```

只有在一个更窄的条件成立时，silence 才可能具有较强负面意义：

- 该来源本来就在系统记录这一类事项；
- 作者/机构理应知道这件事；
- 如果它存在，按该来源的目的与体裁，它应当自然地被记录；
- 不能有很强的 lost-record / non-recording 理由解释沉默。

他们还明确警告：不能把 researcher inference 混进 document content。由推理得到的历史结论必须和文献直接给出的事实分开保存；不确定的推论不能因为反复使用而逐渐变成“已经证实的事实”。

这与本仓已有的：

```text
explicit_actor
reconstructed_actor
researcher
```

三层结构完全兼容，并进一步要求：

> `negative evidence` 本身也必须标明它是从 source silence 推出来的，而不能伪装成 actor statement。

### 2.2 对本仓的第一条硬规则

因此未来 `METHOD.md` 应明确：

> **“行动者没有问 Q”与“目前没有找到行动者问 Q 的记录”是两个不同命题。**

同样：

> **“问题在时期 B 已经不可问”与“时期 B 的现存/已检索语料里没有 Q”是两个不同命题。**

---

## 3. 现代形式分析：McGrew 为什么要求拆开 notice / record / survival

Timothy McGrew, “The Argument from Silence,” *Acta Analytica* 29.2 (2014), 215–228, DOI: 10.1007/s12136-013-0205-5。

作者公开 PDF：

- https://timothymcgrew.com/wp-content/uploads/2024/01/The-Argument-from-Silence-Acta-Analytica-Tim-2013.pdf

McGrew 的重要贡献不是要求历史学家给每条史料计算精确概率，而是把“如果它存在，我们应该看到证据”的直觉拆成至少三步：

1. **Notice**：如果历史事实/状态 H 成立，相关行动者或记录者有多大可能注意到它？
2. **Record**：如果已经注意到，它有多大可能被记录进这类 source？
3. **Survive / become known**：如果记录过，它有多大可能保存下来，并被今天研究者获得/知道？

任何一项很弱，最终的 silence 都会变成很弱的 negative evidence。

对本项目尤其重要的是，这三个条件并不只适用于“某事件是否发生”，也可转成：

```text
如果 actor-problem Q 当时真的 active：

Q 是否会被相关行动者意识到？
        ↓
是否会在我们选择的 source genre / institution 中表达或记录？
        ↓
这些记录今天是否大概率保存、开放、可检索、能被我们的检索策略找到？
```

只有这条链相对可靠，`silence` 才能从“资料缺口”升级成“有限负证据”。

### 3.1 还必须比较 rival explanation

McGrew 的另一个关键点是：

```text
silence under H
```

不能单独评估，还必须问：

```text
silence under rival hypothesis
```

是不是同样常见甚至更常见。

例如：

```text
H1: 问题仍然 active，但相关表达被审查/未记录/档案丢失
H2: 问题已经不再 active

observed: 没有记录
```

如果 H1 与 H2 都很容易产生“没有记录”，那么这个 silence 对二者几乎没有裁决力。

所以本仓不需要伪精确的 Bayes 数字，但必须保存 **contrastive explanation**：

> 为什么“没有证据”在 `Q 不存在/不再可问` 这个解释下，比在其他合理解释下更可期待？

---

## 4. 档案学修正：record silence 不能直接倒推 actor silence

### 4.1 Trouillot：silence 可以在历史生产链的不同阶段产生

Michel-Rolph Trouillot, *Silencing the Past: Power and the Production of History* (Beacon Press, 1995；20th-anniversary ed. 2015)。

出版社：

- https://www.beacon.org/Silencing-the-Past-P2496.aspx

Society of American Archivists 的 `archival silence` 词条保存并定位了 Trouillot 的经典方法说明：silence 会在 source creation、archive assembly、retrieval/narrative 与 retrospective significance 等不同阶段产生，而且不同 silence 不能用同一种办法解释。

- SAA Dictionary: https://dictionary.archivists.org/entry/archival-silence.html

对本仓的实际含义是：

```text
actor did not formulate Q
```

不能仅凭：

```text
archive has no Q
```

因为中间至少可能经历：

```text
actor / practice
→ record creation
→ selection / preservation
→ archive organization / access
→ digitization / OCR / indexing
→ researcher retrieval
→ researcher narrative selection
```

任何一层都可能制造 silence。

### 4.2 Carter：silence 甚至可能是行动者策略，而不是“没有问题”

Rodney G. S. Carter, “Of Things Said and Unsaid: Power, Archival Silences, and Power in Silence,” *Archivaria* 61 (2006), 215–233。

- https://archivaria.ca/index.php/archivaria/article/view/12541

Carter 特别提醒：档案中的 silence 不只可能来自有权者排除弱势者，也可能来自被记录者主动 withholding / refusal。

这给 Problem History 一个非常具体的防错规则：

> 对可能涉及风险、审查、隐私、秘密、违法性、职业惩罚或弱势群体自我保护的材料，**silence 甚至可能和 actor concern 很强同时存在**。

所以：

```text
high stakes + high silence
```

绝不能自动解释成：

```text
low concern / no problem
```

---

## 5. 对 Problem History 最重要的新区分：五种 silence 不能折叠

建议未来 `METHOD.md` 至少概念上区分：

### 5.1 `actor_silence`

在有理由期待 actor 表态的具体 interaction 中，actor 没有提出/承认某个问题。

这是最接近 actor-level negative evidence 的一种 silence，但仍要检查：

- 是否有表达风险；
- 是否存在礼仪/体裁限制；
- 是否由别人控制记录；
- 是否有 tacit shared knowledge 使得无需明说。

### 5.2 `source_silence`

某一类文献中没有该 formulation / category / concern。

必须问：该 source 是否本来负责记录这一类内容？

### 5.3 `archive_silence`

档案集合中没有相应记录。

这可能来自：

- 从未创建；
- 未移交；
- 被销毁；
- 未收集；
- 被排除；
- 封存/限制访问；
- cataloging 不可见。

### 5.4 `retrieval_silence`

研究者检索没有结果。

这还可能只是：

- search term 错；
- 同时期使用另一套 vocabulary；
- spelling / translation / OCR 失败；
- 只查 digitized corpus；
- metadata 粒度不足；
- relevant genre 根本没进入当前 corpus。

### 5.5 `narrative_silence`

后来的史学、机构叙事或知识传统不再谈它。

这最多证明后来的 narrative significance 改变，不能直接证明原 actor-problem 消失。

---

## 6. 一个比 `absence != unaskability` 更严格的 negative-evidence gate

以下是 **project design**，不是 Langlois、McGrew、Trouillot 或 Carter 的原始 schema。

当研究者要用沉默支持：

- `problem weakened`；
- `problem displaced`；
- `problem became_unaskable`；
- `actor did not recognize Q`；

至少回答以下六问。

### Gate N1 — Hypothesis precision

我们到底想用 silence 否定什么？

```yaml
negative_claim:
  hypothesis: "actor group X treated Q as an active problem in period T"
  target_status: absent | weakened | displaced | became_unaskable | undetermined
```

禁止把模糊命题：

```text
“后来没人关心了”
```

直接当历史结论。

### Gate N2 — Expected observer / recorder

如果 Q 真的 active，谁最可能注意到并留下证据？

必须具体到：

- actor group；
- institution；
- genre；
- procedure；
- archive series。

如果答不出 expected recorder，沉默几乎没有裁决力。

### Gate N3 — Recording expectation

为什么这个 source **应该说**？

强 source 例子：

- 规则上要求穷举的 register；
- 完整 minutes；
- 某一固定类别的 annual report；
- 持续记录某类案件的 court / administrative series；
- 同类事项通常都会进入的 professional reporting system。

弱 source 例子：

- 私人日记；
- 选择性回忆录；
- 宣传文本；
- 短篇演说；
- 强审查环境下的公开文本；
- 作者没有理由涉及该议题的作品。

### Gate N4 — Survival / access / retrieval

必须分别问：

- 原记录是否大概率保存？
- 当前 archive 是否覆盖？
- 是否存在封存/销毁/移交中断？
- 数字化比例是多少？
- OCR / indexing 是否可信？
- 是否搜索了 contemporaneous aliases / rival vocabulary？

没有这一步，`search zero` 只能叫 retrieval result，不能叫 historical absence。

### Gate N5 — Rival silence explanations

至少列出两个竞争解释：

```yaml
rival_explanations:
  - censorship
  - genre_mismatch
  - archival_loss
  - vocabulary_shift
  - deliberate_withholding
  - institutional_reassignment
  - researcher_sampling
```

然后说明为什么目标 hypothesis 比这些解释更能解释当前 silence。

### Gate N6 — Positive transition evidence

如果结论要升级到 `became_unaskable`，不能只依赖 silence。

优先寻找：

- contemporaries 明确说旧问题“不再适用 / 无意义 / 不成立”；
- 旧分类被废除或重分类；
- institution 明确失去/转移 jurisdiction；
- 旧 answer space 成为 category error；
- 支撑问题的 practice / role / technology 消失；
- 对手不再回答旧 Q，而明确把争论改写到新的 problem frame；
- 教科书、程序、法规或专业规范明确退出旧 question structure。

这类材料才是 `unaskability` 的核心 positive evidence。

---

## 7. `not asked` 与 `unaskable` 是完全不同强度的历史命题

这是本轮最重要的概念修正。

```text
not observed asking Q
<
no reliable evidence of Q
<
Q weak / marginal / dormant
<
Q displaced by another frame
<
Q became historically unaskable
```

`became_unaskable` 是一个 **modal historical claim**：

> 在该 historical configuration 中，旧 Q 的某些关键 presuppositions / categories / institutions / practices / accepted distinctions 已经不再允许 Q 以原结构成立。

因此：

```text
frequency → 0
```

最多是线索。

而：

```text
“没有人实际问”
```

也仍然弱于：

```text
“行动者已经无法在原有意义上问”
```

后者必须证明 blocking conditions。

---

## 8. 一个可执行的 negative-evidence packet

建议未来 schema 或 episode research note 可以先用下面的临时结构测试：

```yaml
negative_evidence:
  claim: "..."

  silence_type:
    - actor_silence
    - source_silence
    - archive_silence
    - retrieval_silence
    - narrative_silence

  expected_recording_environment:
    actors: []
    institutions: []
    source_genres: []
    archive_series: []
    why_expected: "..."

  notice:
    assessment: high | medium | low | undetermined
    evidence: []

  record:
    assessment: high | medium | low | undetermined
    evidence: []

  survive_access_retrieve:
    assessment: high | medium | low | undetermined
    evidence: []
    digitization_limits: []
    vocabulary_limits: []

  rival_explanations: []
  positive_transition_evidence: []
  counterevidence: []

  conclusion:
    strength: none | weak | bounded | strong
    supports: absent | weakened | displaced | became_unaskable | undetermined
    rationale: "..."
```

注意：

- 不建议真的让 Agent 填虚假的小数概率；
- `high / medium / low` 也必须有 evidence；
- 只要关键一环 `low / undetermined`，整体 negative claim 就应明显降级；
- 对 `became_unaskable`，即使 negative evidence 很强，也仍优先要求 positive transition evidence。

---

## 9. 不要把 corpus 当成过去本身：数字研究尤其危险

这条规则应与 Koselleck note 的 computation boundary 合并。

```text
no hit in corpus
≠
no term in archive
≠
no formulation in surviving sources
≠
no formulation historically
≠
problem unaskable
```

尤其需要记录：

- corpus 来源机构；
- document types；
- 时间覆盖；
- digitization percentage（若能知道）；
- OCR / layout limitations；
- language / orthography normalization；
- excluded collections；
- access restrictions；
- search aliases。

如果两个时期的数字化程度差异巨大，就不能拿 raw hit count 比较“问题兴衰”。

### 9.1 搜索之前先写 `expected-source set`

建议为了防止 negative-evidence cherry-picking，研究者在宣布“没找到”之前先写：

```yaml
expected_source_set:
  why_these_sources_should_contain_Q_if_active: "..."
  source_types: []
  date_range: "..."
  known_gaps: []
  search_terms_and_aliases: []
```

这比搜索结束后再挑选“最沉默”的 archive 更能约束 Agent。

---

## 10. 可以直接进入 `FAILURE-MODES.md` 的错误

### 10.1 Silence = Absence

错误：没有看到记录，就断言历史事实不存在。

AI 自检：

> 如果它存在，谁应该记录？为什么这个来源应当记录？记录又为什么应该保存到今天？

### 10.2 Absence = Unaskability

错误：没有实际 formulation，就宣布问题不可问。

AI 自检：

> 我有证明 blocking conditions 的 positive evidence 吗？还是只有 zero hit？

### 10.3 Corpus Completeness Illusion

错误：把数据库、全文库、搜索引擎当作完整历史档案。

AI 自检：

> 当前 corpus 漏掉了哪些 genre、institution、region、language、undigitized collections？

### 10.4 Digitization Bias

错误：较晚时期资料数字化更多，于是看起来“问题更多”；较早时期检索结果少，于是被误判为 absent。

AI 自检：

> 两个时期的 source survival / digitization / OCR 条件可比较吗？

### 10.5 Genre Mismatch

错误：在本来不会系统记录某问题的 source 中找不到，就当作负证据。

AI 自检：

> 为什么这类文献应当自然出现 Q？

### 10.6 Censorship Inversion

错误：受审查环境中没有公开讨论，于是认为 actor 不关心。

AI 自检：

> 是否存在 suppression、private circulation、coded language、disciplinary risk 或 records destruction？

### 10.7 Strategic Silence Misread

错误：行动者有意 withholding，却被解释成没有 concern。

AI 自检：

> 沉默本身是否可能是一种策略、保护、拒绝记录或拒绝 archive 的行动？

### 10.8 Retrieval = Archive

错误：搜索没结果，就声称 archive 没材料。

AI 自检：

> 是否查过 alternate terms、catalog hierarchy、non-OCR scans、finding aids、adjacent series？

### 10.9 Survival Bias

错误：只用 surviving sources 判断过去什么“重要”。

AI 自检：

> 哪些 records 系统性更容易保存，哪些 actor 的 materials 系统性更容易消失？

### 10.10 Narrative Silence = Historical Silence

错误：后来教科书/史学不再讲，就说过去的问题已经消失。

AI 自检：

> 消失的是 historical problem，还是后来 narrative relevance？

### 10.11 One Silent Source = Period Silence

错误：一个作者不谈 Q，就推广到整个时代。

AI 自检：

> 是否有独立 actor groups / institutions / source families 可以交叉验证？

### 10.12 Asymmetric Search

错误：对想证明连续的时期拼命找 aliases，对想证明断裂的时期只搜一个固定词。

AI 自检：

> 两个时期是否使用了对称的 source-search effort 和 vocabulary expansion？

### 10.13 Negative Evidence Without Rival Explanations

错误：只解释“为什么 silence 支持我的结论”，不问还有什么能产生同样 silence。

AI 自检：

> 至少列出两个 rival explanations，并说明为什么它们较弱。

### 10.14 Conjecture Hardening

错误：最初只写“可能不再可问”，几轮迭代后变成“已经不可问”，但证据没有增加。

AI 自检：

> confidence 提升是因为新增证据，还是因为我已经习惯了自己的 hypothesis？

这一条直接呼应 Langlois / Seignobos 对 conjecture 被反复思考后“熟悉化成确定性”的警告。

---

## 11. 对 `askability` 状态的保守裁决建议

在 schema 冻结前，建议研究层先采用以下裁决语言：

### `active`

有明确 actor formulations、争论、制度响应、competing answers。

### `weakened`

仍有 actor evidence，但 frequency / institutional centrality / response field 明显下降，并有正面材料解释这种下降。

### `dormant`

当前窗口缺乏活跃争论，但没有充分证据证明旧问题已经 structurally invalid。

### `displaced`

有 positive evidence 表明另一 formulation / classification / jurisdiction 接管了原问题位置。

### `evidence_gap`

主要问题在 source coverage / archive / retrieval，不允许历史化成 actor status。

### `became_unaskable`

高门槛：不仅旧 formulation 消失，而且有证据表明其关键 presupposition、object category、institutional jurisdiction、practice 或 answer space 已不再允许旧 Q 按原结构成立。

### `undetermined`

positive / negative evidence 冲突，或关键 recording/survival 条件不明。

其中：

```text
evidence_gap
```

尤其重要。它防止 Agent 把自己的资料能力边界伪装成历史世界的边界。

---

## 12. 和四条既有方法线怎样咬合

### 12.1 Collingwood

Collingwood 的 `does not arise` 提醒我们：问题能否产生依赖 presuppositions。

Negative-evidence 方法增加：

> “我没有找到它产生”的证据，不等于“相关 presuppositions 不存在”。

所以 `does not arise` 不能由 silence 单独推断。

### 12.2 Skinner

Skinner 要求 actor-available description 与 context。

Negative-evidence 方法增加：

> 固定现代关键词搜不到，可能只是 actor vocabulary 不同；只有经过 historical vocabulary expansion 后的 silence 才稍有意义。

### 12.3 Koselleck

Koselleck 已经阻止：

```text
word disappears → concept disappears → problem disappears
```

Negative-evidence 方法进一步要求：词汇消失是否来自 source / archive / retrieval pipeline，也必须说明。

### 12.4 Foucault

Foucault note 已规定：

```text
absence != unaskability
```

本笔记给这条规则补上了 evidence mechanics：notice → record → survive/access/retrieve → rival explanation → positive transition evidence。

---

## 13. 建议写入仓库的位置

### `docs/METHOD.md`

增加一节 **Negative evidence and silence**，至少包含：

- `not found != absent != unaskable`；
- five silence types；
- negative-evidence gate；
- `evidence_gap` 作为合法结论；
- `became_unaskable` 的 positive-evidence requirement。

### `docs/FAILURE-MODES.md`

优先吸收本笔记第 10 节 14 类错误。

### future schema

暂不立即冻结字段，但可测试：

```text
negative_evidence
source_coverage
known_archive_gaps
retrieval_limits
rival_explanations
positive_transition_evidence
```

### identity / askability fixtures

建议未来至少增加四组 adversarial case：

1. **A1 — source silence but problem active**：审查/秘密材料导致公开 source 沉默；
2. **A2 — retrieval silence**：关键词换了，但 alternate vocabulary 显示 problem continuity；
3. **A3 — real displacement**：旧 framing 消失，同时 institution / classification / answer space 有正面重组证据；
4. **A4 — genuine evidence gap**：archive survival 不足，正确答案必须保持 `undetermined / evidence_gap`。

---

## 14. 证据强度

### 强

- Langlois & Seignobos 的公共领域原始方法文本，直接讨论 argument from silence 的限制；
- McGrew 2014 原论文作者公开 PDF，直接拆分 notice / record / survival 并以概率框架分析 silence；
- Trouillot 的方法命题有明确版次与页码传统，并由 SAA Dictionary 等专业档案学资源定位；
- Carter 2006 为同行评议档案学论文，直接讨论 archival silence 与 deliberate silence。

### 中

- 将上述历史方法论转换成 Problem History 的 `negative-evidence gate`；这是 project design，需要用真实 episode 测试。

### 尚未验证

- `five silence types` 是否足以覆盖所有历史材料；
- `evidence_gap` 是否应成为正式 askability status，还是只作为 source-status；
- `became_unaskable` 是否要在 schema 中与 `displaced / dormant` 完全分离；
- 多个相互独立的 silent source families 在何种情况下可以显著提高负证据强度。

---

## 15. 后见之明风险

本方法层本身也有风险：

1. 研究者知道今天什么“重要”，于是错误假设历史作者也一定会记录；
2. 今天觉得某个 silence “惊人”，但这种惊讶来自现代价值而不是 source genre 的 historical expectation；
3. 为了证明 lineage rupture，研究者选择性强调 silence；
4. 为了证明 continuity，研究者又选择性把 silence 全解释成 archive loss；
5. 现代完整行政记录的经验被倒投到 premodern / fragile archival regimes；
6. 把数字检索能力误当作历史 record coverage。

因此最小自检应是：

> **“如果我不知道自己希望得到什么结论，我是否仍会认为这个 source 理应出现这条 evidence？”**

---

## 16. 下一步候选

这份笔记补齐了四条方法谱系之后最明显的横向缺口：如何处理 negative evidence，特别是 problem disappearance / unaskability。

下一步最值得做的已经不是继续增加理论人物，而是：

1. 综合 `COLLINGWOOD / SKINNER / KOSELLECK / FOUCAULT / NEGATIVE-EVIDENCE` 写 `docs/METHOD.md`；
2. 同步建立 `docs/FAILURE-MODES.md`；
3. 把本笔记的 A1–A4 加入 adversarial fixtures；
4. 再拿真实 historical text 测试 `explicit actor / reconstructed actor / researcher` 与 `active / displaced / evidence_gap / became_unaskable` 是否能被两个 Agent 稳定区分。

如果测试失败，应回到方法规则，而不是急着做 M1/M2 大规模 lineage。
