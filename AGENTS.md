# AGENTS.md — Problem History research contract

本仓研究“问题如何成为问题、如何变形、如何消失”，不是人物观点百科，也不是把今天的问题倒灌给过去。

## 开工前阅读

依次阅读：

1. `README.md`
2. `ROADMAP.md`
3. `RESEARCH_PLAN.md`
4. `docs/PRIOR_ART.md`
5. 当前 `docs/METHOD.md` / `docs/FAILURE-MODES.md`（若已存在）
6. 当前 pilot/problem 下已有 episode、source 和 synthesis

## 最重要的约束

**先证明历史行动者确实在面对某个问题，再讨论答案。**

任何 Problem Episode 都必须区分：

- 历史文本中的明确 formulation；
- 可以从语境支持的 presupposition；
- 研究者的解释/推断；
- 后来的研究术语。

这四者不能在写作中悄悄合并。

## 反后见之明规则

禁止：

- 因为今天能用一句话提出 X，就假定过去的人也在问 X；
- 把同一个词跨几十年出现当成同一个问题连续存在；
- 把不同词自动判为不同问题；
- 只按政治年代分期而不证明 formulation/presupposition/answer-space 改变；
- 把后来的理论分类作为历史行动者自己的分类；
- 为了画图强迫复杂竞争框架变成单线进步史。

## 来源优先级

重要历史判断优先：

1. 历史行动者的一手文本/档案/同时代制度材料；
2. 权威版本、文集、数据库；
3. 专业研究文献；
4. 辅助性二手材料。

引用必须足以让下一位 agent 找回原文位置。能定位页码/章节/日期/版次时不要只给首页链接。

## Problem Episode 最低要求

一个正式 episode 至少应有：

- period/context；
- formulation evidence；
- actors；
- vocabulary；
- institutions；
- presuppositions；
- accepted/marginal/unthinkable answer space（只有证据支持时写）；
- competing formulations；
- ≥3 条一手证据（pilot 阶段）；
- predecessor/successor relation；
- uncertainty / hindsight-risk note。

## 计算工具边界

关键词、语义漂移、topic、network、LLM 提取只能产生：

```text
candidate / lead / anomaly
```

不能直接成为历史结论。任何重要断点必须回到原始文本核验。

## 默认研究循环

1. 检查当前研究状态；
2. 从 `RESEARCH_PLAN.md` 选择最早依赖满足的任务；
3. 做 literature/source audit；
4. 收集并定位原始文本；
5. 区分 formulation/presupposition/inference；
6. 主动寻找反例和竞争框架；
7. 写 episode/synthesis；
8. 对照 `FAILURE-MODES` 自检；
9. 提交 checkpoint；
10. 没有真正 blocker 时继续。

## 研究诚实规则

允许并鼓励这些结论：

- “目前只能证明词汇连续，不能证明问题连续”；
- “这个断点可能只是材料缺失”；
- “两个群体并不共享同一个问题框架”；
- “旧问题并未解决，而是失去提问条件”——但仅在证据支持时；
- “该候选不适合作为 pilot”。

## Stop conditions

- 找不到历史行动者层面的 formulation 证据；
- 只有今天研究者把材料组织成这个问题；
- 研究实质已经是成熟概念史，仅仅改名；
- 分期只靠外部年代；
- LLM/embedding 相似度成为唯一证据；
- 关键原文无法可靠定位；
- 为满足预设论点而忽略竞争框架。

停止或更换 pilot 可以是正确研究结果。
