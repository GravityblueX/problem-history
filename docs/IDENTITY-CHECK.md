# Problem Identity Check

> **问题同一性不是数据清洗步骤，而是历史判断。**
>
> 在两个 Problem Episodes 之间画一条边之前，必须回答：我们凭什么认为它们在处理“同一个问题”、一个被改写的问题、一个后继问题，或者仅仅是今天看来相似？

这份文档把仓库目前最危险的判断——`problem identity`——从隐含直觉变成显式、可反驳、可复核的操作。

它不是要创造一个机械判分器。相反，它的目标是阻止 Agent 因为词相似、答案相似或现代标题相同，就自动把历史材料连成一条线。

---

## 1. 为什么必须单独做 identity check

传统 `Problemgeschichte` 最容易滑向一个强假设：

> 某些问题本身跨时代保持同一，历史变化的是表述、解决方案和问题意识。

Nicolai Hartmann 的方法给这种思路提供了最明确的经典形式。哲学史不应只是“思想家史”；它可以围绕问题本身组织。这个转向仍然值得借用。

但 Hans-Georg Gadamer 对这一路线的批评指出了关键危险：如果研究者站在今天先认定有一个跨时代恒常的“自由问题”“知识问题”，再回头把不同时代的提问都收进来，那么“问题的同一性”其实已经被研究者预先决定了。

Dirk Werle 的文学史 `Problemgeschichte` 提供了另一个有用方向：研究者可以把“问题”重建为一组文本的 primary context，并把文本理解为对某个问题情境的回应；但这种重建必须是一个受材料约束的假说，而不是无限制地挑选语境。

因此本项目采用：

```text
Hartmann：允许追踪 problem-lines
        +
Gadamer：problem identity 不得预设
        +
Werle：problem 是可检验的历史重建假说
        ↓
identity claim = defeasible historical claim
```

参考：

- Historisches Wörterbuch der Philosophie, “Problemgeschichte” 词条：
  https://www.schwabeonline.ch/schwabe-xaveropp/elibrary/start.xav?start=//*%5B@attr_id%3D%27verw.problemgeschichte%27+and+@outline_id%3D%27hwph_verw.problemgeschichte%27%5D
- H-Soz-Kult, “Begriffs-, Problem- und Ideengeschichte im digitalen Zeitalter”：
  https://www.hsozkult.de/event/id/event-58855?language=de
- Dirk Werle, “Problem und Kontext. Zur Methodologie der literaturwissenschaftlichen Problemgeschichte”, *Journal of Literary Theory* 8.1 (2014), 31–54：
  https://www.researchgate.net/publication/275686431_Problem_und_Kontext_Zur_Methodologie_der_literaturwissenschaftlichen_Problemgeschichte
- Forschungsstelle Historische Epistemologie und Hermeneutik, “Problem, Frage”：
  https://fheh.org/?page_id=1574

---

## 2. 默认规则：先不认定同一

两个 episode 看起来相似时，默认状态不是：

```yaml
relation: same_problem
```

而是：

```yaml
relation: undetermined
```

研究者或 Agent 必须提交一个 `identity claim`，并为它提供正反两组证据。

### 禁止的默认推理

以下任何一项都不能单独证明问题同一：

- 使用了同一个词；
- 被今天放在同一个学科栏目；
- 得到了相似答案；
- 后人给它们使用同一个标题；
- embedding 很接近；
- 两段材料讨论了同一个对象；
- 两个作者互相引用；
- 存在明显年代先后关系。

它们最多是 **lead**。

---

## 3. 不把“同一 / 不同”做成一个粗暴二元值

建议的 episode relation 至少区分以下层级。

```yaml
identity_relation:
  type: continuous | reformulated | transformed_successor | split | merged | displaced | revived | analogy_only | unrelated | undetermined
```

### `continuous`

核心问题结构具有较强连续性。表述、词汇、参与者可以变化，但前后材料仍处于可识别的共同争论或实践压力中。

### `reformulated`

旧问题仍可辨认，但提问方式、术语或可接受答案空间发生明显变化。

重点：**不是因为研究者能改写成同一句现代汉语就算 reformulated。**

### `transformed_successor`

后一个问题在历史上由前一个问题情境产生，但已经不宜宣称“还是同一个问题”。

这是本项目非常重要的边。

```text
A 没有被解决
↓
A 的制度 / 知识 / 语言前提变化
↓
B 成为新的可问问题
```

B 可以是 A 的历史后继者，而不需要是 A 的“同一问题新版”。

### `split`

一个原来捆绑的问题后来分裂为两个或更多相对独立的问题。

### `merged`

原本分别出现的问题，在新的理论或制度框架中被视为同一个更大问题的组成部分。

### `displaced`

旧问题没有得到公认答案，而是被另一套问题框架排挤出中心。

### `revived`

一个曾经失去活跃提问条件的问题后来重新出现。

注意：revival 仍需检查它是不是“复活”，还是只是借用了旧名称。

### `analogy_only`

历史行动者之间没有足够连续证据，但研究者认为二者可作比较。

这条边非常有用，因为它允许比较而不伪造谱系。

### `unrelated`

现有证据支持：相似只是表面，两个问题结构没有历史上的有效连续关系。

### `undetermined`

证据不足或正反证据冲突，暂不裁决。

这是合法终态，不应为了图谱完整强行升级。

---

## 4. Identity Check 的六个维度

每次声称两个 episodes 之间存在连续关系，至少检查以下六项。

不是六项都必须相同。真正要看的是：**哪些变化会改变问题本身的可理解结构。**

### 4.1 Target / object：到底什么被当作有待处理的对象

问：

- 两边指向的是同一种对象吗？
- 对象的分类方式是否变化？
- 同一个词是否已经指向另一类对象？

危险情况：

```text
同词
≠
同对象
≠
同问题
```

---

### 4.2 Stakes：为什么这件事值得问

同一句疑问，在不同制度条件下可能有完全不同的 stakes。

检查：

- 它是理论困难、政策困难、职业困难、道德困难、技术困难，还是身份危机？
- 谁承担问题不被解决的代价？
- 什么变化使它突然变得紧迫？

如果 stakes 完全改变，应提高“transformed / analogy_only”的可能性。

---

### 4.3 Presuppositions：问题成立需要哪些前提

这是 identity check 的核心。

问：

- 为了让这个问题有意义，当事人必须先相信什么？
- 哪些分类、制度、知识前提被默认？
- 前一个时代的关键前提，在后一个时代是否已经消失？

如果一个 episode 的核心前提在另一个 episode 中已经不可理解，那么不能只靠表述相似维持 problem identity。

---

### 4.4 Answer space：什么才算一个可能的答案

不要只比较历史上实际出现的答案，还要恢复**当时可想象的答案空间**。

检查：

- 哪些回答被视为有意义？
- 哪些回答被视为荒谬、越界或根本不可表达？
- 什么算“解决了问题”？
- 什么算失败？

这是判断问题是否真的发生变化的强信号。

如果 A 时代一个标准答案放到 B 时代会变成 category error，那么 continuity 必须受到强烈怀疑。

---

### 4.5 Problem-recognition / lineage：当事人是否认识到继承关系

最强证据之一是历史行动者自己建立了连续关系，例如：

- 明确引用此前争论；
- 声称重新提出、修正或解决旧问题；
- 对前代答案进行批评；
- 延续相同争论场、机构、体裁或术语网络。

但要注意：

> actor 自称“这是同一个问题”是重要证据，不是最终裁决。

历史行动者也会制造传统、发明祖先和重写谱系。

因此需要把“当事人的同一性主张”本身保存为证据，而不是直接变成数据库事实。

---

### 4.6 Askability：它在这个时代为什么能够被问

检查的不只是“有人有没有问”，还包括：

- 哪套语言让它可以被表述？
- 哪个制度让它成为必须处理的事？
- 哪种技术、知识分类或社会角色使它可见？
- 以前为何无需问、不能问或没有意义？

如果 askability 的条件发生根本变化，后一个 episode 可能是 emergence，而不是旧问题的自然延续。

---

## 5. 三个强制测试

六个维度用于分析；下面三个测试用于做关系裁决。

### Test A — Answer Transfer Test

从 episode A 取一个当时合理的候选答案，问：

> 如果把这个答案原样交给 episode B 的行动者，它仍会被识别成在回答自己的问题吗？

可能结果：

```text
yes                 → continuity evidence
partly / after rewrite → reformulation evidence
no, but historically generated B → transformed-successor evidence
no, category error  → discontinuity evidence
```

注意：这是分析性反事实，不是假装真的知道历史人物会怎么说。必须解释判断依赖哪些文本证据。

---

### Test B — Presupposition Removal Test

从 episode A 中抽掉一个核心前提，问：

> 如果这个前提在 B 中已经不存在，A 的问题还能以原来的逻辑成立吗？

如果不能，那么 B 即使使用同一个词，也可能已经是新问题。

---

### Test C — Historical Recognition Test

问：

> 除了今天的研究者之外，有没有历史证据把 A 和 B 放进同一条争论链？

证据强度可分：

```text
strong:
  direct citation / explicit inheritance / explicit refutation

medium:
  shared institutional debate / stable interlocutors / traceable transmission

weak:
  vocabulary resemblance / later retrospective grouping

none:
  only researcher analogy
```

`none` 并不禁止比较，但通常应使用 `analogy_only`，而不是 `continuous`。

---

## 6. 正反证据必须同时保存

禁止只写：

```yaml
evidence:
  - "两者都讨论 X"
```

应改成：

```yaml
identity_claim:
  relation: reformulated
  status: provisional

continuity_evidence:
  - type: explicit_inheritance
    source: "..."
    note: "B 明确把 A 的争论作为自己的前史"
  - type: answer_space_overlap
    note: "A 的两个主要答案在 B 中仍被视为可理解候选"

discontinuity_evidence:
  - type: presupposition_shift
    source: "..."
    note: "B 已不接受 A 默认的主体分类"
  - type: stake_shift
    note: "问题从神学正当化转成制度治理"

researcher_note:
  - "连续性存在，但不足以声称完全 same problem"
```

核心原则：

> **任何 continuity claim 都应该允许未来材料把它推翻。**

---

## 7. 区分三种“问题”来源

仓库必须标明一个 formulation 到底是谁的。

```yaml
formulation_source:
  type: actor_explicit | actor_reconstructed | researcher_analytic
```

### `actor_explicit`

历史行动者明确提出的问题。

例如正文中存在明确疑问、争论命题、待解决任务或自我描述。

这是最强证据，但仍不能脱离语境。

### `actor_reconstructed`

行动者没有用一句完整问题表述出来，但从多份同时代材料可以重建其问题结构。

必须给出重建链。

### `researcher_analytic`

研究者为了比较材料而提出的分析问题。

这不是低级证据；很多有效历史研究都需要研究者问题。

真正危险的是：

```text
researcher_analytic
↓（偷偷升级）
actor_explicit
```

因此 UI / schema 中必须始终可见来源类型。

---

## 8. Identity claim 也必须标明是谁的

问题来源之外，再加一层：谁声称它们是同一问题？

```yaml
identity_claim_source:
  type: actor | later_actor | contemporary_observer | historian | agent
```

例如：

```yaml
identity_claims:
  - source_type: later_actor
    relation: continuous
    evidence: "..."
  - source_type: historian
    relation: transformed_successor
    evidence: "..."
```

两个 claim 可以冲突。

仓库不需要立刻消灭这种冲突。

---

## 9. 最小裁决矩阵

Agent 在建立 episode 边时，至少填写：

| Dimension | A → B continuity? | Evidence | Counterevidence |
|---|---|---|---|
| target/object | yes / partial / no / ? | ... | ... |
| stakes | yes / partial / no / ? | ... | ... |
| presuppositions | yes / partial / no / ? | ... | ... |
| answer space | yes / partial / no / ? | ... | ... |
| historical recognition | strong / medium / weak / none | ... | ... |
| askability conditions | stable / changed / ruptured / ? | ... | ... |

然后才允许写：

```yaml
relation: ...
confidence: low | medium | high
status: provisional | reviewed
```

### 禁止自动总分

不要写：

```text
6 项中 4 项相同 → 66.7% → same problem
```

不同维度的重要性依赖历史情境。

例如一个核心 presupposition 的崩塌，可能比五项表面连续更重要。

---

## 10. Agent 自检问题

任何 Agent 想画 `A → B` 边之前，必须回答：

1. 我是在追踪历史行动者的问题，还是我自己定义的分析问题？
2. 如果删掉共同关键词，我还会认为二者连续吗？
3. A 的历史行动者会把 B 的某个答案识别为一种可理解的回答吗？根据什么材料？
4. B 的历史行动者是否继承、批评或知道 A？如果不知道，为什么仍要声称连续？
5. 两个 episode 的核心 presuppositions 是否兼容？
6. 什么答案在 A 中可能、在 B 中变得不可想象，反之亦然？
7. 问题的 stakes 是否改变到了足以改变问题结构？
8. 有没有证据表明旧问题其实消失了，只是词还留下？
9. 有没有证据表明词换了，但争论链实际上连续？
10. 我能不能写出至少一条反对自己 identity claim 的证据？
11. 如果不能证明连续，能否降级成 `analogy_only` 而不是硬连？
12. `undetermined` 是否比一个漂亮但虚假的结论更诚实？

---

## 11. 一个虚构例子：同词不等于同问题

以下只用于测试模型，不是历史论断。

假设两个虚构时代都频繁出现“记忆”一词。

### Episode A

```yaml
period: 1700s-fictional
formulation: "一个人如何保存足够多的典籍内容？"
stakes:
  - scholarly mastery
presuppositions:
  - knowledge is possessed primarily through individual learned memory
answer_space:
  - mnemonic systems
  - excerpt notebooks
```

### Episode B

```yaml
period: 2100s-fictional
formulation: "一个人工系统应当保留用户多少历史交互？"
stakes:
  - privacy
  - personalization
  - storage cost
presuppositions:
  - memory can be external persistent machine state
answer_space:
  - retention policies
  - summarization
  - deletion controls
```

它们可以被现代研究者放在“记忆史”中比较，但仅凭共同词 `memory`，最稳妥的关系可能只是：

```yaml
relation: analogy_only
```

如果后来找到清晰的技术/思想传递链，再升级关系。

---

## 12. 一个虚构例子：换词但问题可能连续

### Episode C

某制度内争论“谁有资格解释规则”。

### Episode D

几十年后已经不用“解释资格”这个词，而争论围绕“认证权限”展开。

如果存在：

- 同一制度争议的直接继承；
- D 明确批评 C 的解决方案；
- 旧答案在 D 中仍然可识别；
- stakes 与核心 presuppositions 大体连续；

那么即使关键词完全不同，也可能判定：

```yaml
relation: reformulated
```

这说明 lexical continuity 和 problem continuity 必须分开存储。

---

## 13. 一个虚构例子：真正重要的是 successor，而不是 same

### Episode E

问题成立于制度 X 存在的前提下。

### Episode F

制度 X 崩溃后，原来的问题已无法原样成立；但崩溃本身制造出一个新的问题 F。

此时最有解释力的边不是：

```text
E --same problem--> F
```

而是：

```text
E --institutional transformation--> F
```

或者：

```yaml
relation: transformed_successor
```

这可能正是问题史相对于“永恒问题史”真正值得记录的东西。

---

## 14. 对数据模型的直接要求

未来 `Problem Episode` schema 不应只有：

```yaml
predecessors: []
successors: []
```

而应把边本身做成一等对象，例如：

```yaml
relations:
  - target_episode: "episode-b"
    relation: transformed_successor
    identity_status: contested
    identity_claim_source: historian
    continuity_evidence:
      - source_id: "src-001"
        dimension: historical_recognition
        note: "..."
    discontinuity_evidence:
      - source_id: "src-002"
        dimension: presuppositions
        note: "..."
    confidence: medium
    reviewed_by: []
```

这样图谱上的边才不是漂亮箭头，而是可审计的历史判断。

---

## 15. 对计算方法的直接限制

未来 embedding、topic model、LLM classifier 可以输出：

```yaml
candidate_relation:
  suggested: reformulated
  basis:
    - lexical_similarity
    - context_similarity
```

但它只能触发人工 / Agent identity check。

不得自动写入：

```yaml
relation: reformulated
status: reviewed
```

特别禁止：

```text
semantic similarity
→ problem identity
```

因为问题同一性的关键证据往往来自：

- presupposition；
- stakes；
- answer space；
- transmission；
- institutions；
- askability。

这些都不能被单一向量距离可靠替代。

---

## 16. 与既有方法传统的边界

### 向 Hartmann 借什么

借：

- 不让人物成为唯一叙事主语；
- 允许追踪跨文本、跨作者的问题线；
- 把“解决尝试”放进历史结构。

不借：

- 把跨时代 problem identity 当作预设。

### 向 Gadamer 借什么

借：

- 问题内容与具体历史提问方式不可轻易拆开；
- 反对从历史之外宣布一个永恒问题恒常存在；
- 把问题的可理解性放回历史情境。

但本项目不会因此放弃跨时代比较。

解决办法是：

```text
比较可以做
谱系可以提
identity 必须证明
不确定可以保留
```

### 向 Werle 借什么

借：

- 把 problem reconstruction 当成一种有解释力的 context selection；
- 让“某文本/文本群在回应什么问题”成为可检验假说；
- 用问题限定无限扩张的 context。

同时增加本项目自己的限制：

> 一个 reconstructed problem 跨 episode 延续时，必须再次经过 identity check，不能因为研究者最初用同一个问题组织语料，就自动获得跨时代同一性。

---

## 17. 本项目暂定的最小原则

可以压缩成七条：

1. **Problem identity is a claim, not a key.**
2. **同词不证明同问题，换词不证明换问题。**
3. **历史后继关系不等于问题同一关系。**
4. **研究者可以提出比较问题，但必须标明它是研究者问题。**
5. **每个 continuity claim 同时保存 discontinuity evidence。**
6. **允许 `analogy_only` 与 `undetermined`。**
7. **边必须比节点更难创建。**

最后一条尤其重要。

如果以后图谱里随手就能画出几千条边，反而说明 identity check 失败了。

---

## 18. 下一步验证

这套规则现在仍然只是方法假说，需要故意找材料来破坏它。

下一轮不应急着扩大 schema，而应建立一组 `identity fixtures`：

- 同词但问题断裂；
- 换词但问题连续；
- 行动者宣称连续、研究者判断断裂；
- 后人制造了一条虚假的传统谱系；
- 旧问题不是被解决，而是失去 askability；
- A 导致 B，但 A ≠ B；
- 正反证据势均力敌，只能 `undetermined`。

两个 Agent 独立判断这些案例。

如果它们无法解释为什么选择某条关系，而只能输出标签，这套方法还不能进入自动化阶段。
