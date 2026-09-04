# Problem History Method

> **核心原则：问题本身也必须被历史化。**
>
> 本仓库不是把今天的问题标题投射到过去，再收集历代“答案”。一个 `Problem Episode` 是一个可反驳的历史重建：在特定时间、行动者、语言、制度与实践条件下，某件事怎样成为可问、值得问、必须处理或可以争论的问题。

本文件把已经完成的 `IDENTITY-CHECK.md`、Collingwood / Skinner / Koselleck / Foucault 方法谱系、`NEGATIVE-EVIDENCE.md` 与 `SOURCE-CITATION.md` 收敛成 M0 的执行方法。它不是一个机械判分器，也不是任何单一理论家的原始 schema。

---

## 1. Problem Episode 的工作定义

一个 `Problem Episode` 不是一个关键词，也不是一个主题，更不是研究者为了整理材料写出的现代标题。

本项目把它定义为：

> 在一个有边界的历史情境中，一组行动者、制度或互动过程，把某个对象/困难组织成可被提出、争论、诊断、治理、解决、拒绝或重新定义的问题；这种组织方式具有可定位的 formulation、stakes、presuppositions、answer space 与 askability 条件，并且能够由历史证据支持或推翻。

至少区分：

```text
historical condition / difficulty
        ≠
actor-recognized problem
        ≠
historical problematization reconstructed by researcher
        ≠
researcher's present analytic question
```

一个 episode 可以围绕单个作者，也可以围绕：

```yaml
episode_unit:
  type: author_text | exchange | debate | institutional_process | mixed
```

当问题通过 proposal → objection → reformulation → reply → uptake 逐步形成时，不要强迫它绑定一个 canonical author。

---

## 2. 三层 formulation：永远不要静默互换

每个问题表述都必须标来源层级：

```yaml
problem_formulation:
  type: explicit_actor | reconstructed_actor | researcher_analytic
  text: "..."
  evidence: []
  confidence: high | medium | low | undetermined
```

### `explicit_actor`

历史行动者明确提出问题、疑问、困难、任务、争点或必须处理的事项。它不要求句末有问号，但必须能从原始材料中直接定位。

### `reconstructed_actor`

行动者没有留下完整问句，但多条独立的同时代证据支持：该 formulation 是对其当时问题结构的合理重建。

最低要求：

- 不得只从一段“答案”反推问题，再用同一段材料证明问题；
- 必须有额外的同时代文本、对手回应、制度记录、争论上下文、作者自述或其他独立支持；
- 必须通过 actor-language admissibility check；
- 必须保存 competing reading / counterevidence。

### `researcher_analytic`

今天研究者为了比较、组织或解释历史材料提出的问题。它完全合法，但不能伪装成历史行动者自己的 formulation。

**硬规则：**

```text
useful modern question
≠
historical actor question
```

---

## 3. 先固定 source，再做解释

任何会影响 episode 或 identity verdict 的材料先按 `docs/SOURCE-CITATION.md` 建 provenance。

至少要知道：

- creator / institution；
- historical date；
- edition / version / translation；
- exact locator；
- repository / stable identifier；
- digital mediation layer；
- 是否只是 OCR；
- 这条 source 实际支持哪个 claim。

```text
OCR hit ≠ verified quotation
web host ≠ original historical object
primary source ≠ automatically true
```

引用必须能让别人重新找到同一个版本和同一个位置。

---

## 4. Actor-language admissibility：历史行动者能不能这样问

对 `reconstructed_actor`，必须检查该 formulation 是否能用行动者当时可获得的词汇、分类和争论方式表达。

```yaml
actor_language:
  status: supported | contested | unsupported | undetermined
  available_vocabulary: []
  conventional_uses: []
  innovative_or_deviant_uses: []
  opponent_or_reply_evidence: []
  counterevidence: []
```

`unsupported` 并不表示现代分析无价值，只表示它必须留在 `researcher_analytic` 层。

这里采用 Skinner 的约束：理解一段 serious utterance 不能只看字面 sense/reference，还要问行动者借它在当时语境中做什么；但 speech act 与 problem formulation 仍须分开。

```yaml
utterance_action:
  label: defend | attack | redefine | warn | justify | classify | reject | other
  evidence: []
  confidence: high | medium | low | undetermined
```

```text
same speech act ≠ same problem
same proposition ≠ same speech act
```

Cambridge 版 Skinner 方法文本：
https://www.cambridge.org/core/books/abs/visions-of-politics/meaning-and-understanding-in-the-history-of-ideas/96B251BDAB60C0E570F014E340F70EDD

---

## 5. Context 只能作为有功能的证据，不能做背景墙

每一条 context evidence 都必须说明它改变了哪个解释判断：

```yaml
context_evidence:
  - source_id: src-...
    function:
      - available_vocabulary
      - conventional_move
      - target_or_opponent
      - audience
      - institutional_stakes
      - answer_space
      - uptake_or_reply
      - askability_condition
    note: "..."
```

如果一段“时代背景”删掉之后，对 formulation、intelligibility、stakes、answer space、interaction 或 askability 的判断完全不变，它通常不是 episode 的核心 evidence。

**禁止：**

```text
context exists → actor must have asked Q
```

社会、经济、政治条件可以诱发或约束 problematization，但不能机械推出唯一的问题形式。

---

## 6. Episode 的核心问题结构

每个成熟 episode 至少重建以下维度。

### 6.1 Target / object

- 什么被当作有待处理的对象？
- 谁定义它？
- 分类边界是什么？
- 同名对象是否已经换了历史含义？

### 6.2 Stakes

- 为什么现在值得问？
- 谁承担“不解决”的代价？
- 是理论、政策、职业、技术、伦理、身份还是制度压力？

### 6.3 Presuppositions

- 这个问题成立需要哪些前提？
- 哪些是行动者明说的，哪些是受证据支持的重建？
- 哪些行动者拒绝这些前提？

Collingwood 的 question-and-answer / presupposition 逻辑提供方法启发，但本项目的 `presupposition` 不是其技术意义上的 `absolute presupposition`。

SEP 当前 Collingwood 条目对“没有相关 presupposition，问题不会产生”的方法背景有清楚定位：
https://plato.stanford.edu/entries/collingwood/

### 6.4 Answer space

不要只列实际出现的答案，还要恢复当时哪些答案被认为：

- meaningful；
- acceptable；
- possible but disputed；
- absurd / forbidden / category error。

```yaml
answer_space:
  observed_answers: []
  plausible_contemporary_answers: []
  excluded_or_unthinkable_answers: []
  criteria_for_success: []
```

### 6.5 Responsibility

谁被认为应该改变？

```yaml
problem_responsibility:
  actor | institution | state | profession | technology | public | mixed | contested
```

同一对象如果责任结构发生根本变化，可能已经是 transformed successor。

### 6.6 Object-status claim

行动者是否明确声称“对象本身已经变了”？把这种当时人的变化判断保存下来，不要只留下研究者的断代。

---

## 7. 词汇与语义只是证据层，不是 problem identity

Koselleck 方法线要求至少分开：

```text
lexical continuity
        ≠
semantic continuity
        ≠
conceptual continuity
        ≠
problem continuity
```

同词出现只能先作为 lexical lead。语义变化也不能自动升级为 problem transformation。

推荐 evidence promotion：

```text
lexical lead
→ semantic evidence
→ concept-in-action evidence
→ problem-structure evidence
→ identity / transformation verdict
```

每一次升级都需要新增证据，而不是换一个更强标签。

Koselleck 的 Hardenberg 例子清楚显示：词义解释需要作者、受众、同时代语言使用和社会结构共同约束，但语言与社会也不能彼此还原：
https://germanhistory-intersections.org/en/knowledge-and-education/ghis:document-129

---

## 8. Askability：问题为什么在这里能够被问

`askability` 不是“出现了这个词”。至少检查：

- 哪套语言和分类让它可表达；
- 哪个制度/职业/实践让它成为必须处理的对象；
- 哪种知识、测量、记录或技术让对象可见；
- 谁拥有提出或裁决它的资格；
- 以前为什么无需问、不能问或没有意义；
- 哪些条件后来改变。

```yaml
askability:
  status: askable | contested | weakened | displaced | became_unaskable | revived | undetermined
  supporting_conditions: []
  blocking_conditions: []
  positive_transition_evidence: []
  negative_evidence: []
```

Foucault 的 1984 说明提供两个硬边界：现实困难可以存在很久才形成有效 problematization；同一困难也可能产生多个互相矛盾的回应。因此：

```text
historical difficulty ≠ historical problem
context / difficulty ≠ unique problem formulation
```

公开文本定位：
https://www.foucault.info/documents/foucault.interview/

### 8.1 `emergence`

不要把 first surviving mention 当作 birth date。高置信度 emergence 至少应寻找若干积极迹象：

- 原本熟悉的实践失去熟悉性；
- actor questioning / hesitation；
- debate / criticism / defense；
- 新分类、测量或评价标准；
- institutional reassignment；
- competing responses；
- policy / technical redesign。

### 8.2 `became_unaskable`

这是比“后来没人问”更强的 modal historical claim。通常需要积极证据证明旧问题赖以成立的关键条件已被拆除，例如：

- object category 被废止；
- institution 不再有 jurisdiction；
- 核心 presupposition 崩塌；
- 原答案在新框架中成为 category error；
- 支撑问题的社会角色或技术实践消失；
- 新 problem frame 明确接管旧争论。

```text
no later mention ≠ became_unaskable
problem disappeared ≠ problem solved
```

---

## 9. Negative evidence：沉默必须经过 gate

使用 silence 支持 `weakened / displaced / became_unaskable / actor did not recognize Q` 前，按 `docs/NEGATIVE-EVIDENCE.md` 至少回答：

1. 我到底想否定哪个精确 hypothesis？
2. 如果它是真的，谁理应注意到？
3. 为什么这个 source genre 理应记录它？
4. 记录是否大概率保存、开放、数字化并被检索到？
5. censorship、genre mismatch、archival loss、vocabulary shift、strategic silence 等 rival explanations 是否同样能解释零结果？
6. 有没有积极 transition evidence？

必须区分：

```text
actor_silence
source_silence
archive_silence
retrieval_silence
narrative_silence
```

Langlois 与 Seignobos 对 argument from silence 的经典警告仍然适用：绝大多数事实并不会完整留下记录，只有当“本应记录且本应保存”这些额外前提成立时，沉默才可能变强。
https://www.gutenberg.org/cache/epub/29637/pg29637-images.html

当资料能力不足时，应使用：

```yaml
research_status: evidence_gap | undetermined
```

而不是把 repository/corpus 的边界写成历史世界的边界。

---

## 10. Competing formulations 与 interaction evidence

一个 episode 不应只保存“胜出版本”。优先寻找：

- explicit opponent；
- objection / reply；
- competing diagnosis；
- rival terminology；
- rejected answer；
- institutional uptake / refusal。

```yaml
interaction_context:
  target_or_opponent: []
  audience: []
  prior_move: []
  uptake_or_reply: []
  rival_formulations: []
```

这既能约束 actor-question reconstruction，也能显示一个 problem field 是否真的存在，而不是研究者从孤立文本中拼出的幻象。

---

## 11. Episode 之间的关系：边必须比节点更难创建

关系定义与六维 identity check 以 `docs/IDENTITY-CHECK.md` 为准：

```text
continuous
reformulated
transformed_successor
split
merged
displaced
revived
analogy_only
unrelated
undetermined
```

每条非 `undetermined` edge 至少提交：

```yaml
identity_claim:
  relation: "..."
  status: provisional | supported

continuity_evidence: []
discontinuity_evidence: []

checks:
  target_object: "..."
  stakes: "..."
  presuppositions: "..."
  answer_space: "..."
  historical_recognition: "..."
  askability: "..."
```

并执行：

- Answer Transfer Test；
- Presupposition Removal Test；
- Historical Recognition Test。

**禁止：**

```text
A caused B → A and B are the same problem
actor cites predecessor → continuous
same word → continuous
same answer → continuous
embedding similarity → continuous
```

`analogy_only` 和 `undetermined` 都是成功结果，不是失败。

---

## 12. Claim-relative evidence strength

不要给 source 本身打一个永久的 A/B/C“可信度”。同一材料可能强力证明“某机构公开用了某句话”，却不能证明“所有行动者都这样想”。

对重要 claim 记录：

```yaml
claim:
  text: "..."
  layer: actor_explicit | actor_reconstructed | researcher_analytic
  source_links:
    - source_id: src-...
      relation: supports | contradicts | complicates | contextualizes | dates | locates | transmits | later_reinterprets
      directness: explicit | inferential | contextual
      locator: "..."
      note: "..."
```

证据强度至少解释：

- directness；
- contemporaneity；
- independence；
- specificity；
- source-purpose / audience；
- preservation / mediation；
- counterevidence。

不要制造没有解释意义的伪精确分数。

---

## 13. 最小 Episode 研究包

在 schema 冻结前，成熟 episode 至少应有以下信息：

```yaml
episode:
  id: "..."
  time_range: "..."
  place_or_institution: []
  episode_unit: "..."

problem_formulations:
  - type: explicit_actor | reconstructed_actor | researcher_analytic
    text: "..."
    evidence: []

structure:
  target_object: []
  stakes: []
  presuppositions: []
  answer_space: []
  problem_responsibility: []
  object_status_claims: []

interaction:
  opponents: []
  audiences: []
  rival_formulations: []
  uptake_or_reply: []

askability:
  status: "..."
  supporting_conditions: []
  blocking_conditions: []

vocabulary_and_semantics:
  lexical_forms: []
  semantic_evidence: []

sources: []
claims: []

uncertainty:
  competing_reconstructions: []
  evidence_gaps: []
  hindsight_risks: []
```

这是 research packet，不是最终 JSON Schema；真实案例和 calibration 可能继续修改它。

---

## 14. 标准研究流程

### Step 1 — 先写 researcher question

明确我们今天为什么研究这组材料，并标记为 `researcher_analytic`。

### Step 2 — 建 source map

优先一手/同时代材料；记录版本、locator、数字中介和来源目的。

### Step 3 — 找 explicit actor formulations

先抄出行动者实际说法，不急着统一成现代标题。

### Step 4 — 允许 reconstruction，但必须过 gate

恢复 actor question、actor language、speech act、opponent、audience、reply，并保存 competing readings。

### Step 5 — 重建 problem structure

target / stakes / presuppositions / answer space / responsibility / object status。

### Step 6 — 重建 askability

找 supporting / blocking conditions 与 emergence/displacement 的积极证据。

### Step 7 — 主动找反证

至少寻找一个能削弱当前 formulation 或 continuity claim 的材料方向。

### Step 8 — 只有在 episode 独立成立后才建 edge

先建立节点，再使用 `IDENTITY-CHECK` 比较。不要先决定 lineage 再去填 episode。

### Step 9 — 写 uncertainty

把 `unknown / evidence_gap / contested / undetermined` 明写出来。

---

## 15. Stop / hold conditions

出现以下情况时先停，不要升级结论：

- 只有今天研究者使用该问题表述；
- actor-language admissibility 无法支持；
- formulation 完全来自单段“答案”的循环反推；
- 只有关键词/embedding/主题相似；
- 只有后来统一叙事，没有同时代问题证据；
- context 能解释“为什么可能出现”，却没有 actor-level problem evidence；
- negative claim 只来自零检索；
- source version / locator / OCR 无法核验关键措辞；
- continuity 与 discontinuity evidence 冲突且无法裁决；
- 为了图谱完整必须强迫 `undetermined` 变成某条边。

正确输出通常是：

```text
researcher_analytic only
candidate / lead / anomaly
contested
undetermined
evidence_gap
```

---

## 16. M0 calibration：方法完成不等于方法通过

本文件完成后仍不能冻结 schema。ROADMAP 的验收要求保持不变：

- 选 5 段真实历史文本；
- 两个 Agent 独立判断 explicit problem / implicit presupposition / researcher inference；
- 不向 Agent 提供 oracle；
- 比较它们是否会把 modern paraphrase 升级成 actor wording；
- 要求它们分别输出 continuity 与 discontinuity evidence；
- 用 adversarial fixtures 检查 `analogy_only / unrelated / undetermined` 是否真正被使用。

如果两个 Agent 不能稳定区分三层 formulation，应先修改本方法，不做图谱、不冻结 schema。

---

## 17. 方法谱系的分工，而不是“理论家拼盘”

```text
Collingwood
  question ↔ answer；reconstruction 本身是历史判断；presupposition 与 askability

Skinner
  actor-available language；speech act；bounded context；opponent/audience/uptake

Koselleck
  word ≠ concept；semantic change ≠ problem change；同步/历时语义层

Foucault
  difficulty ≠ problem；problematization；object formation；emergence / askability

Historical source criticism / archival method
  silence gate；provenance；version；locator；mediation；claim-relative evidence
```

这些路线互相约束，没有任何一条单独决定 problem identity。

---

## 18. 最短 AI 自检

提交一个 Problem Episode 前，必须能回答：

1. 这个问题表述是谁的——行动者、重建还是研究者？
2. 如果是重建，我有独立证据还是从“答案”循环反推？
3. 行动者当时有可用语言表达它吗？
4. 我是否把 speech act 当成 problem formulation？
5. context evidence 具体解释了什么？
6. 我是否把现实困难自动写成历史问题？
7. 我是否把同词/语义相似升级成 problem continuity？
8. answer space 和 presuppositions 有证据吗？
9. askability 的出现/消失是否有积极 transition evidence？
10. 我是否把 archive/retrieval silence 当成 actor silence？
11. 关键 source 的版本、locator 和数字中介可复核吗？
12. 我主动保存了反证和 competing reconstruction 吗？
13. 如果证据不足，我是否允许 `undetermined / evidence_gap`？
14. 建 edge 前，我能同时解释 continuity 与 discontinuity evidence 吗？

任何一题答不上来，都应降低 claim 强度，而不是补一个更肯定的形容词。
