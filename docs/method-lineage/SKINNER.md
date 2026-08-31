# Skinner：从“恢复问题”到“恢复言语行动”

> 状态：method-lineage research note  
> 目的：在 Collingwood 的 question-and-answer 约束之上，补充 Quentin Skinner 对语言语境、言语行动与历史行动者可用描述的限制；同时明确哪些是 Skinner 自己的主张，哪些是后来的争论，哪些只是本项目拟采用的数据规则。

## 1. 为什么现在深化 Skinner

仓库已经完成两项关键前置工作：

1. `docs/IDENTITY-CHECK.md` 把 problem identity 改造成可反驳的历史判断；
2. `docs/method-lineage/COLLINGWOOD.md` 把 actor-question reconstruction 本身规定为需要证据支持的历史工作，并增加了反循环规则。

但仅仅恢复“作者在回答什么问题”仍然不够。

同一句 proposition 可以在不同争论中承担不同动作：辩护、反驳、讽刺、合法化、重新命名、排除竞争者、提出制度要求。若 Problem History 只保存 `formulation + answer`，仍可能把一个历史文本压缩成脱离行动语境的命题。

Skinner 的增量正在这里：

> 不只问“这句话是什么意思 / 回答什么问题”，还要问历史行动者在特定语言和争论条件下，**说这句话是在做什么**。

这可以进一步收紧本仓的 `reconstructed_actor` 门槛。

---

## 2. 一手/权威文本：Skinner 真正反对什么

### 2.1 1969 / 2002：反对把经典文本预先塞进“永恒问题”

Skinner 的经典文章：

- Quentin Skinner, “Meaning and Understanding in the History of Ideas,” *History and Theory* 8.1 (1969), 3–53.
- 修订版收入 *Visions of Politics*, Vol. I: *Regarding Method* (Cambridge University Press, 2002), ch. 4, pp. 57–89.
- Cambridge chapter page: https://www.cambridge.org/core/books/abs/visions-of-politics/meaning-and-understanding-in-the-history-of-ideas/96B251BDAB60C0E570F014E340F70EDD
- DOI: 10.1017/CBO9780511790812.007

2002 版开头明确把一种旧式思想史做法设为批评对象：研究者假定经典文本包含超时间的“universal ideas”“fundamental concepts”“abiding questions”，于是像读同时代作者一样直接询问古人对这些恒常议题给了什么答案。

Skinner 的反对不是：

```text
过去和现在绝对不能比较
```

而首先是：

```text
研究者今天拥有一个问题 Q
        ≠
历史行动者当时必然也在处理 Q
```

这与本仓的反后见之明底线完全一致。

### 2.2 “actor-available description” 的限制

1969 年文章后部有一条长期影响很大的限制：历史学家对行动者“做了什么”的描述，不能建立在行动者原则上完全无法理解或接受的分类上，再把该分类偷偷写成行动者自己的意图。

在后续讨论中，这常被概括为 Skinner 的 maxim：对行动的历史描述应落在行动者原则上可用于描述和分类其行为的范围之内。

本项目可借用的弱版本是：

> **任何 `explicit_actor` 或 `reconstructed_actor` formulation，都要检查其中的关键描述是否在当时的语言/实践世界中可用。**

但这不禁止研究者另设现代分析层。例如今天可以说某文本具有“国家能力”“知识生产”“性别治理”等分析意义；只是不能因此写成：

```yaml
problem_formulation:
  type: actor_explicit
  text: "国家能力问题"
```

除非能证明行动者当时确实拥有相应表达或足以支持的近邻分类。

### 2.3 语境不是“背景百科”，而是可行言语行动的范围

Skinner 1969 年的方法性结论并不是简单命令历史学家“多查背景”。他特别关心：

- 在某个具体时间、争论、体裁和受众面前，一组词能够 conventionally 完成哪些 communication / linguistic acts；
- 作者选择这些词时，可能是在已有惯例上顺势使用、争夺、扭转或重新定义什么；
- 哪些解释因为在当时语言环境中根本不构成可理解行动而应被削弱。

相关原始方法链还包括：

- Quentin Skinner, “Conventions and the Understanding of Speech Acts,” *The Philosophical Quarterly* 20.79 (1970), 118–138. DOI: 10.2307/2218084.
- Quentin Skinner, “On Performing and Explaining Linguistic Actions,” *The Philosophical Quarterly* 21.82 (1971), 1–21. DOI: 10.2307/2217566.
- Quentin Skinner, “Motives, Intentions and the Interpretation of Texts,” *New Literary History* 3.2 (1972), 393–408. DOI: 10.2307/468322.

对 Problem History 来说，真正可操作的转化不是“context 越多越好”，而是：

> **收集能改变我们对“这个行动者当时可能在做什么、可能在回答什么”的判断的语境。**

这是一条 context-selection rule。

### 2.4 2002：speech act 是对命题意义的额外维度

*Visions of Politics* Vol. I 第 6 章：

- “Interpretation and the Understanding of Speech Acts,” pp. 103–127.
- https://www.cambridge.org/core/books/abs/visions-of-politics/interpretation-and-the-understanding-of-speech-acts/3F6E8EAD5BE22567A7822818E7872087
- DOI: 10.1017/CBO9780511790812.009

Skinner 在这里再次借 Wittgenstein 与 J. L. Austin 说明：要理解一个严肃 utterance，不能只知道组成它的词的 sense/reference，还要理解词如何被使用、它作为 deed 完成了什么。

因此，本仓需要区分：

```text
propositional_content
    说了什么

illocutionary_action
    说这句话是在做什么
```

例如同样出现：

```text
“X 是自由的。”
```

在不同 episode 中可能是在：

- 定义法律资格；
- 驳斥某种奴役指控；
- 为一项制度改革提供合法性；
- 讽刺对手；
- 抢夺“自由”一词的正面评价；
- 将旧争论重新分类。

如果只保存 proposition，Problem Episode 可能错误地把这些动作合并成一个“自由问题”。

---

## 3. intention 不等于 motive，也不等于心理读心

Skinner 的方法经常被简化成“找作者意图”。这会误导本项目。

至少应拆开：

```text
motive
  为什么这个人想写/说这件事；可能涉及利益、经历、心理、策略来源

intention-in-performing-the-utterance
  他通过这个可公开理解的言语行动试图做什么
```

*Visions of Politics* 第 5 章专门讨论 motives / intentions / interpretation：

- “Motives, intentions and interpretation,” pp. 90–102.
- https://www.cambridge.org/core/books/abs/visions-of-politics/motives-intentions-and-interpretation/62A6BF0213BBC51317486BFCD60E3A99
- DOI: 10.1017/CBO9780511790812.008

对本仓最安全的规则是：

> 不从传记心理猜 actor problem；优先重建文本在可公开识别的语言/制度/争论中所执行的行动。

也就是说：

```yaml
motive:
  status: unknown
```

完全可以与：

```yaml
candidate_illocution:
  type: rebuttal
  evidence: [...]
  confidence: medium
```

同时存在。

---

## 4. 从 Skinner 可直接转成的项目规则

以下不是 Skinner 原封不动的数据模型，而是本项目从其方法提取的可测试规则。

### 4.1 `reconstructed_actor` 增加 actor-available-description 检查

目前 Collingwood note 已建议：

```yaml
problem_formulation:
  type: explicit_actor | reconstructed_actor | researcher
  text: "..."
  evidence: []
```

建议未来再加：

```yaml
actor_available_description:
  status: supported | contested | unsupported | undetermined
  evidence: []
```

这里检查的不是是否出现一模一样的现代术语，而是：

- 当时是否存在可让行动者理解该描述的分类与语汇；
- 同时期同行/对手是否使用近邻表述；
- 该 formulation 是否只由后世理论才变得可说。

若为 `unsupported`，应降级为：

```yaml
problem_formulation:
  type: researcher
```

而不是强行重建成 actor question。

### 4.2 增加 `speech_act_context`

建议 schema 原型：

```yaml
speech_act_context:
  utterance_or_passage: "..."
  actor: "..."
  audience: []
  genre_or_forum: "..."
  interlocutors: []
  candidate_illocution: "..."
  conventional_moves_available: []
  contested_or_innovative_uses: []
  evidence: []
  competing_readings: []
  confidence: low | medium | high
```

这能阻止 Agent 只做：

```text
抽一句 proposition
→ 现代释义
→ 直接推断 problem
```

### 4.3 Context 必须“有裁决作用”

禁止 context dump。

每条 context evidence 都应回答：

> 如果删掉这条材料，我们对 actor formulation、candidate illocution、answer space 或 askability 的判断会不会变化？

如果不会，它可能只是一般背景，不应被当成支撑问题重建的核心证据。

可考虑：

```yaml
context_evidence:
  source: "..."
  relevance_to:
    - actor_formulation
    - illocution
    - answer_space
  counterfactual_note: "without this evidence, interpretation X becomes weaker because ..."
```

### 4.4 同时保存 competing speech-act readings

言语行动重建仍然是历史判断，不应制造新的单一确定性。

例如：

```yaml
competing_readings:
  - reading: "institutional justification"
    evidence: []
  - reading: "polemical attack"
    evidence: []
```

在证据不足时允许：

```yaml
illocution_status: undetermined
```

这与 `IDENTITY-CHECK` 允许 `undetermined` 的原则一致。

### 4.5 增加候选 identity 维度：`pragmatic_role`

目前 identity check 已检查：

- target/object；
- stakes；
- presuppositions；
- answer space；
- historical recognition；
- askability。

Skinner 提示可再测试一个维度：

```yaml
pragmatic_role:
  episode_a: "..."
  episode_b: "..."
  relation: stable | shifted | ruptured | undetermined
```

这里的问题是：同一套词在两个时期是否仍执行相似的争论动作。

例如同一个术语可能经历：

```text
opponent's accusation
→ self-description
→ administrative category
```

即使 vocabulary 看起来连续，problem structure 也可能已经重排。

**但这目前只应作为 project hypothesis。** 不能预设 speech-act role 一变化，problem identity 就必然断裂；需要真实 episode 测试。

---

## 5. Collingwood → Skinner 的真正接口

Christopher Fear 2013 的论文提供了非常适合本仓的方法桥：

- Christopher Fear, “The question-and-answer logic of historical context,” *History of the Human Sciences* 26.3 (2013), 68–81.
- DOI: 10.1177/0952695113491757
- https://journals.sagepub.com/doi/10.1177/0952695113491757

Fear 的核心论点是：Collingwood 的 question-and-answer logic 可以解释为什么 Skinner 的 context 不是附加背景。若不知道作者认为自己正在处理的 problem-context，就无法可靠回答 Skinner 所关心的 intention 问题。

因此本项目可以把两条方法链接成：

```text
Collingwood
  statement 是在回答什么 question？
  question 依赖哪些 presuppositions？
        ↓
Skinner
  actor 在回答时，以当时可用语言正在做什么？
  哪些 conventions / interlocutors / genre 使该行动可理解？
        ↓
Problem History
  formulation + askability + speech-act role + transformation relation
```

重要的是，后二者不能互相替代：

- 知道 speech act 不等于已经恢复完整 problem；
- 恢复 candidate question 也不等于知道该文本在争论中执行何种行动。

---

## 6. 不能直接继承的强版本

### 6.1 不把“语言 convention”变成决定论

Mark Bevir 1992 对 linguistic contextualism 的批评值得保留：

- Mark Bevir, “The Errors of Linguistic Contextualism,” *History and Theory* 31 (1992), 276–298.
- Open-access record: https://escholarship.org/uc/item/0tr1n4mq

Bevir 反对一种过强解释：仿佛只要重建同时代 conventional context，就能以固定方法恢复作者意图。

本项目应采取较弱版本：

```text
convention/context
→ constrains and evidences interpretation
≠ mechanically determines interpretation
```

原因也很实际：

- 同时期 convention 可能彼此竞争；
- 行动者会讽刺、挪用、误用、创新；
- 档案只保存部分受众和语言环境；
- 历史解释仍需要比较证据与反证。

### 6.2 不把 Skinner 变成“禁止跨时代比较”的法令

Robert Lamb 对 Skinner 后期 contextualism 的批评指出：从反对不历史的解释，不能直接推出所有跨时代/perennial philosophical comparison 都无效。

本项目无需解决这一哲学争论，只需分层：

```yaml
researcher_analytic:
  question: "..."
  cross_temporal_comparison: true
```

可以合法存在。

真正禁止的是：

```text
researcher analytic question
→ 静默升级为 historical actor question
```

因此 Problem History 可以比较跨世纪问题，但谱系和 identity 仍需独立历史证据。

### 6.3 不把历史后果倒写成原始 intention

一篇文本后来：

- 成为经典；
- 被某群体引用；
- 被后世解释成某学说起点；
- 在制度上产生意外后果；

都不能直接证明作者当时就是在“创立那个传统”或“解决后来那个问题”。

需要分开：

```yaml
actor_intention: ...
later_reception: ...
historical_effect: ...
```

这对本仓追踪跨 50 年 transformation chain 尤其重要，否则后来的连续性会倒灌成最初节点的意图。

---

## 7. Skinner 对 Problem Episode 基础结构的直接增量

未来 `docs/METHOD.md` 可以吸收以下最小版本。

### Actor formulation

```yaml
problem_formulation:
  type: explicit_actor | reconstructed_actor | researcher
  text: "..."
  evidence: []
  actor_available_description:
    status: supported | contested | unsupported | undetermined
    evidence: []
```

### Speech-act layer

```yaml
speech_act:
  candidate_illocution: "..."
  audience: []
  interlocutors: []
  genre_or_forum: "..."
  linguistic_conventions: []
  innovative_or_contested_usage: []
  evidence: []
  counterevidence: []
  competing_readings: []
  confidence: low | medium | high
```

### Context selection

```yaml
context_item:
  source: "..."
  supports:
    - formulation
    - presupposition
    - illocution
    - answer_space
    - askability
  relevance_note: "..."
```

### Identity candidate

```yaml
pragmatic_role:
  a: "..."
  b: "..."
  status: stable | shifted | ruptured | undetermined
  evidence: []
  counterevidence: []
```

这些都是 **project design**，不是 “Skinner schema”。

---

## 8. 一个最小示例：为什么同一句话可能不是同一个 problem evidence

以下是虚构示例，只测试方法。

### Episode A

一位官员说：

> “本城人人皆可自由通行。”

语境显示他在回应外地商人对城门税的投诉。

可能 speech act：

```yaml
candidate_illocution: rebuttal_of_trade_restriction_charge
```

### Episode B

五十年后另一位官员重复同一句话，但语境是镇压后为政府合法性辩护。

可能 speech act：

```yaml
candidate_illocution: legitimation_after_repression
```

即使 proposition 与关键词完全相同，也不能直接得到：

```yaml
relation: continuous
```

需要再检查 target、stakes、presuppositions、answer space、historical recognition 和 askability。

Skinner layer 提供的是额外的 discontinuity / continuity evidence，不是新的自动判分器。

---

## 9. 证据强度

### A — 强：Skinner 自己的方法文本

- Skinner 1969, “Meaning and Understanding in the History of Ideas,” *History and Theory* 8.1: 3–53.
- 修订版：*Visions of Politics*, vol. I (2002), ch. 4, pp. 57–89.
- Skinner 1970, “Conventions and the Understanding of Speech Acts,” pp. 118–138.
- Skinner 1971, “On Performing and Explaining Linguistic Actions,” pp. 1–21.
- Skinner 1972, “Motives, Intentions and the Interpretation of Texts,” pp. 393–408.
- *Visions of Politics*, vol. I, ch. 5, pp. 90–102; ch. 6, pp. 103–127; ch. 10, pp. 175–187.

这些可以支持：反“永恒问题”读法、actor-available description、speech act / intention / context 的方法要求。

### B — 中强：方法桥与专业争论

- Fear 2013：Collingwood question-answer 与 Skinner historical context 的桥接。
- Bevir 1992：对过强 linguistic contextualism 的系统批评。
- Skinner 方法的后续批评可用于确定本项目不能直接继承的强版本。

### C — 本项目自己的方法重构

以下均不是 Skinner 原始术语或数据结构：

- `actor_available_description.status`；
- `speech_act_context` YAML；
- context counterfactual relevance test；
- `pragmatic_role` 作为 identity dimension；
- 强制保存 `competing_readings`；
- 把跨时代 analytic comparison 与 actor formulation 分层。

它们需要在真实 episode 中检验。

---

## 10. 后见之明与 Agent 失败风险

1. **Context inflation**：把同年代所有知识都堆成“语境”，却不能说明哪条材料改变解释。
2. **现代言语行动倒灌**：用今天的政治/社会科学动作标签替历史行动者命名，却没有当时可用描述支持。
3. **intention = motive**：从人物利益、性格或传记猜测文本的公开言语行动。
4. **convention determinism**：找到一种同时代惯例，就宣布作者必然只能按该惯例使用词。
5. **忽略争议性语言**：把一个时期当作共享同一 vocabulary/convention 的均质共同体。
6. **抹掉创新**：因为没有前例，就断言一种新用法当时不可能被理解；实际上行动者可能正在重新定义规则。
7. **经典后果倒写**：因为文本后来成为某传统开端，就把“创立传统”写成原始 intention。
8. **speech act 替代 problem**：知道作者在反驳某人，并不自动知道完整 problem structure。
9. **problem 替代 speech act**：知道作者面对 Q，也不能自动断定其发言是回答、讽刺、拒绝问题或改写提问。
10. **把 Skinner 当禁令**：为了避免后见之明而禁止所有现代比较，反而失去 researcher analytic layer。
11. **单一 audience 幻觉**：文本可能同时面向不同受众，完成不止一个行动。
12. **高置信度幻觉**：缺乏对手文本、体裁惯例或传播证据时，仍把 candidate illocution 写成事实。

---

## 11. 尚不确定

- 1969 原文与 2002 修订版在措辞和页码上不应混用。未来逐字引用必须明确 edition。
- 1970/1971/1972 几篇方法论文的权威在线页面可稳定定位 bibliographic metadata，但全文常受访问限制；需要长引文时应回到合法可访问的明确版次复核。
- Skinner 自身方法在数十年中有修订，不能把 1969 的每一个 polemical formulation 自动当成 2002 的最终立场。
- `pragmatic_role` 是否应成为正式 identity-check dimension 目前未验证。它可能只是辅助证据，而非 Problem Episode 的核心字段。
- 一个 actor 可同时完成多个 speech acts；schema 最终可能需要数组而非单值。
- “actor 原则上能够接受的描述”本身仍需历史重建，不能变成新的读心测试。

---

## 12. 建议写入位置

### `docs/METHOD.md`

未来应吸收至少五条规则：

1. `reconstructed_actor` formulation 增加 actor-available-description 检查；
2. formulation 与 speech act 分层；
3. context evidence 必须说明其裁决作用，禁止 context dump；
4. intention 与 motive 分开；
5. 允许 competing illocutionary readings 与 `undetermined`。

### `docs/IDENTITY-CHECK.md`

先不要直接改正式规则；建议把 `pragmatic_role` 作为待验证候选。至少用两个真实 episodes 测试后再决定是否加入七维检查。

### `schemas/problem-episode.schema.json`

等 M0 schema 开始实现时，至少给 speech-act / actor-available-description 留扩展空间，而不是只保存 `formulation: string`。

---

## 13. 下一步候选

方法谱系最自然的下一步是 **Reinhart Koselleck**。

原因不是“轮到下一个名家”，而是 Skinner 已经把 actor formulation 收紧到当时可用语言与行动；接下来必须处理另一个危险：

```text
vocabulary continuity
≠
concept continuity
≠
problem continuity
```

Koselleck 的 Begriffsgeschichte 可以用来检查：

- 一个词的语义时间结构如何变化；
- 历史基本概念与制度/社会结构如何互相作用；
- 问题没有稳定名称时如何追踪；
- 词汇延续时，Problem Episode 是否已经断裂。

之后再进入 Foucault 的 problematization，才能把“某对象如何开始成为可反思的问题”补上。

---

## 14. 本轮压缩结论

Skinner 对本项目真正增加的不是一句泛泛的“要看语境”，而是三条更严格的约束：

```text
1. 研究者的问题 ≠ 历史行动者的问题；
2. 命题内容 ≠ 行动者说这句话时完成的行动；
3. 语境应限定/检验可行解释，而不是成为无限背景，也不能机械决定唯一解释。
```

因此，Problem History 若要避免把过去写成现代问答题，未来的 Problem Episode 至少需要同时保存：

```text
question / formulation
+ presupposition
+ actor-available descriptions
+ speech-act role
+ competing readings
+ evidence / counterevidence
```

这一步把 Collingwood 的“恢复问题”进一步变成：**恢复一个历史行动者在当时可说、可做、可被理解的提问与回应行动。**
