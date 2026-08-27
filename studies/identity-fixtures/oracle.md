# Problem Identity Fixtures — Oracle

> **不要把本文件提供给被测试 Agent。**
>
> 这里的答案不是“唯一正确标签”，而是 reviewer 用来检查 Agent 是否抓住方法重点的参考裁决。

---

## Case 01 — 同词但断裂

### 推荐裁决

```yaml
relation: analogy_only
confidence: high
```

`unrelated` 也可以讨论，但如果研究者明确希望研究“记忆”这一分析主题，`analogy_only` 更能保留比较价值，同时拒绝伪造历史连续性。

### 关键理由

continuity evidence 很弱：

- 共享一个词；
- 都存在某种“保存/调用”主题。

但 discontinuity evidence 很强：

- target 不同：人的记诵能力 vs 人工系统持久状态；
- stakes 不同：学术能力 vs 隐私/授权/治理；
- presuppositions 不同；
- answer space 几乎不可转移；
- 无历史 transmission。

### 失败模式

```text
memory == memory
→ same problem
```

这是最典型的 lexical continuity 错觉。

---

## Case 02 — 换词但连续

### 推荐裁决

```yaml
relation: reformulated
confidence: high
```

### 关键理由

- B 明确引用 A 的制度争论；
- 核心 stakes 仍是“谁有权使一种解释获得共同约束力”；
- 旧答案仍可被 B 的参与者识别和批评；
- 制度结构改变，但不是完全换题。

关键词变化是 discontinuity evidence，但不足以压过争论链和 answer-space continuity。

### 可接受替代

如果 Agent 对制度重组赋予很高权重，可接受：

```yaml
relation: transformed_successor
confidence: medium
```

但必须解释为什么制度变化已经改变核心 problem structure。

### 失败模式

```text
no lexical match
→ unrelated
```

---

## Case 03 — actor claim 不能直接升级为事实

### 推荐裁决

```yaml
relation: transformed_successor
confidence: high
```

同时必须保存：

```yaml
actor_identity_claim:
  relation: continuous
```

### 关键理由

Episode B 确实继承“城市照明治理”这一制度谱系，但：

- 旧 target 主要是供给稳定性与覆盖；
- 新 target 主要是自动控制权与公共空间治理；
- 燃料、人工等核心 presuppositions 已消失；
- answer space 基本无法直接转移。

因此“同一个城市照明问题”更像机构自我叙述，而不是研究者必须照单全收的 identity judgment。

### 失败模式

把历史行动者的 retrospective identity claim 直接写成：

```yaml
relation: continuous
status: fact
```

---

## Case 04 — 谱系制造

### 推荐裁决

```yaml
relation: transformed_successor
confidence: medium
```

或者更保守：

```yaml
relation: analogy_only
confidence: medium
```

### 关键理由

A 与 B 都涉及船上时间技术，可能存在技术史上的后继关系；但现有材料明确提示：A 的问题是值班共同时间，B 是经度测定。

B1 是重要材料，因为它证明 1750 年有人主动制造 continuity claim；但 B2 同时给出了 contemporaneous counterclaim。

因此 direct citation 不能自动证明 A 早就在问 B 的问题。

### reviewer 应检查

Agent 是否能写出：

```text
history of reception / appropriation
≠
identity of original problem
```

---

## Case 05 — disappearance without solution

### 推荐裁决

对 A 的后续状态：

```yaml
relation: displaced
confidence: high
```

也可以在问题状态层表达：

```yaml
status: became_unaskable
```

### 关键理由

- 没有材料显示旧争论得到答案；
- 使旧问题成立的制度前提——固定纸张原件——消失；
- 新问题围绕数字对象的长期可读性与认证展开。

如果建立 A → B 的 episode relation，可考虑：

```yaml
relation: transformed_successor
```

但不能说：

```text
digitalization solved the old paper-size problem
```

除非把“solution”明确限定为制度取消，而不是历史行动者意义上的回答。

### 失败模式

任何目的论式：

> 后来的技术终于解决了前人的问题。

---

## Case 06 — cause is not identity

### 推荐裁决

```yaml
relation: transformed_successor
confidence: high
```

### 关键理由

A 的解决方案直接制造 B 的制度条件，因此历史后继关系很强；但两边的问题结构不同：

- A：稀缺馆藏如何分配；
- B：阅读日志如何治理；
- stakes、answer space、核心对象均变化。

这是本项目应该特别保存的一种结构：

```text
Problem A
  ↓ solution/institutional response
new infrastructure
  ↓ unintended consequence
Problem B
```

### 失败模式

```text
A caused B
→ A == B
```

或者反过来，因为不是同一问题就把历史因果关系完全删掉。

---

## Case 07 — 真的允许不知道

### 推荐裁决

```yaml
relation: undetermined
confidence: high
```

这里的 `high` 指“对目前不能裁决这件事有较高信心”，不是对某个连续关系有高信心。

### continuity evidence

- 国家资助的公共教师；
- 教学与政治秩序冲突；
- 1910 年参与者直接重印 1810 年文本；
- 部分 answer space 连续。

### discontinuity evidence

- 君主效忠义务已消失；
- 宪制国家的合法性结构不同；
- 1910 年援引旧文本可能是战略性传统建构；
- 现有材料不足以确定 lineage 的实质强度。

### 可接受替代

`reformulated` 或 `transformed_successor` 只有在 Agent 明确指出还需要什么额外证据，并对不确定性保持较低 confidence 时才勉强可接受。

### 失败模式

为了“完成图谱”强行判定。

---

# 跨案例评分规则

比最终标签更重要的是 Agent 有没有做到以下事情。

## 1. 是否区分 lexical continuity 与 problem continuity

若 Case 01 / 02 都主要按关键词裁决，直接判失败。

## 2. 是否保存 actor claim 而不把它等同于 historian claim

Case 03 / 04 是主要测试。

## 3. 是否理解 successor 不等于 same

Case 05 / 06 是主要测试。

## 4. 是否主动找 counterevidence

每个 case 都要求有 `discontinuity_evidence`。

如果 Agent 在它喜欢的结论上完全找不到反证，说明它仍在做 confirmation-only reconstruction。

## 5. 是否敢用 `analogy_only`

研究者有权比较两个历史现象，不必为了让比较合法而伪造一个 genealogy。

## 6. 是否敢用 `undetermined`

如果模型把所有东西都塞进确定关系，说明 schema 在奖励虚假确定性。

## 7. 是否误用 Answer Transfer Test

它是历史分析启发式，不是心理读心术。

好的输出应写：

> 根据 B 的可接受答案与相关争论材料，A 的答案在 B 中似乎不会被视为直接回应。

而不是：

> 1900 年的人一定会认为……

---

# 建议的自动测试指标

将来可以对 Agent 输出做简单 lint，但不要自动裁决历史结论。

可检查：

```yaml
must_have:
  - relation
  - confidence
  - continuity_evidence
  - discontinuity_evidence
  - missing_evidence

warnings:
  - lexical evidence is the only continuity evidence
  - direct citation treated as conclusive identity proof
  - no counterevidence supplied
  - causal succession conflated with identity
  - actor claim silently promoted to repository fact
  - undetermined never used across adversarial fixture suite
```

这类 lint 可以自动化，因为它检查的是**论证结构是否完整**，而不是替历史学家决定哪一个 relation 必然正确。
