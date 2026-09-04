# Problem History Failure Modes

> **本文件的目标不是列“写作注意事项”，而是把会制造伪问题谱系的错误变成可被 Agent 主动检查的失败模式。**

每一种 failure mode 都包含：症状、为什么危险、最低修复和 AI 自检。它们来自已完成的 `IDENTITY-CHECK.md`、Collingwood / Skinner / Koselleck / Foucault 方法谱系、`NEGATIVE-EVIDENCE.md` 与 `SOURCE-CITATION.md` 的收敛。

---

## F01 — Perennial-problem projection / 永恒问题投射

**症状**

先写一个今天的问题，例如“文学有什么用？”“机器能否思考？”，再把历代作者依次排成回答者。

**为什么错**

现代标题只是 researcher question；它不能证明不同时代的行动者共享同一 target、stakes、presuppositions 或 answer space。

**最低修复**

- 明标 `researcher_analytic`；
- 分别恢复各时期 actor formulation；
- 在建立 lineage 前执行 `IDENTITY-CHECK`。

**AI 自检**

> 如果删掉我今天给这条谱系起的标题，历史行动者之间还存在可定位的共同问题链吗？

---

## F02 — Same word = same problem / 同词即同问题

**症状**

因为两个时期都出现 `freedom / 文学 / intelligence / labor` 等同一词，就直接连 `continuous`。

**为什么错**

```text
lexical continuity ≠ semantic continuity ≠ conceptual continuity ≠ problem continuity
```

同词可能换对象、换 stakes、换制度功能；不同词也可能承载连续问题。

**最低修复**

比较同期语义场、对立词、行动者用法、对象和 answer space，再做 identity verdict。

**AI 自检**

> 除了“用了同一个词”，我还有哪两条独立 continuity evidence？

---

## F03 — Semantic-drift determinism / 语义变化即问题变化

**症状**

词义、embedding、搭配或概念发生变化，于是直接宣布 problem transformed。

**为什么错**

语义变化只是 evidence layer；问题结构可能仍连续。计算语义尤其只能先产生 `candidate / lead / anomaly`。

**最低修复**

必须再检查 target、stakes、presuppositions、answer space、historical recognition 与 askability。

**AI 自检**

> 如果我完全不知道这个词的 embedding 变了，仅凭历史行动者的实践和争论证据，我还会判 problem transformed 吗？

---

## F04 — Answer-to-question circularity / 从答案循环制造问题

**症状**

看见一段文本像是在“回答 X”，于是发明 X，再用原文本证明行动者确实面对 X。

**为什么错**

reconstruction 与 validation 使用同一份唯一证据，证据链没有独立支点。

**最低修复**

`reconstructed_actor` 至少增加独立的同时代支持：对手、回复、制度记录、作者其他文本、会议互动等。

**AI 自检**

> 如果移除我最初解释为“答案”的那段文本，是否仍有证据支持 candidate question？

---

## F05 — Actor / researcher collapse / 研究者问题冒充行动者问题

**症状**

用现代分析词汇写出一句漂亮问句，然后叙述成“当时的人开始问……”。

**为什么错**

现代问题可能有解释力，但未必是行动者可表达、可理解或实际争论的问题。

**最低修复**

强制 `explicit_actor / reconstructed_actor / researcher_analytic` 三层标记。

**AI 自检**

> 我能给出行动者原句或同时代可用的等价表达吗？如果不能，为什么这不是 researcher formulation？

---

## F06 — Actor-language anachronism / 行动者语言不可用

**症状**

把后来才出现的概念组合、分类或理论语言直接塞给早期行动者。

**为什么错**

一个问题只有在当时语言/分类环境中可理解，才能升级为 `reconstructed_actor`。

**最低修复**

执行 actor-language admissibility check，寻找同时代 vocabulary、近义表达、用法标准、争论对手和创新性用法。

**AI 自检**

> 当时的人如何用自己的词说出我这句话？如果无法改写而不依赖后来的概念，它应该留在哪一层？

---

## F07 — Speech-act / problem collapse / 言语行动等于问题

**症状**

文本“在辩护某制度”，于是自动重建 actor-question 为“该制度是否正当？”；或者因为两段文本都在“攻击”，就认为问题相同。

**为什么错**

行动者说了什么、在做什么、在回答什么，是三个相关但不同的判断。

**最低修复**

分别保存 `problem_formulation` 与 `utterance_action`，并为两者提供独立证据。

**AI 自检**

> 我的 question reconstruction 是否只是把 speech-act label 改写成问句？

---

## F08 — Context wallpaper / 语境背景墙

**症状**

堆大量政治、社会、经济背景，却无法说明哪一项实际改变了文本解释。

**为什么错**

无限 context 无法证伪，也容易让研究者挑选任何背景来支持预设解释。

**最低修复**

每条 context evidence 标明 function：vocabulary、opponent、audience、stakes、answer space、uptake、askability 等。

**AI 自检**

> 删除这段背景后，我对 formulation 或 problem structure 的判断会发生什么具体变化？

---

## F09 — Context determinism / 语境决定论

**症状**

“经济危机出现，所以行动者必然提出 X 问题”；“制度变化直接产生唯一思想回应”。

**为什么错**

同一 difficulty 可能产生多个互相矛盾的问题化与回应。context 可以 constrain / instigate，不能充当 deterministic decoder。

**最低修复**

寻找 competing formulations 和 rival responses。

**AI 自检**

> 同样的历史条件下，有没有行动者得出不同 diagnosis 或根本没有采用我重建的 problem frame？

---

## F10 — Difficulty = problem / 客观困难等于历史问题

**症状**

研究者知道某时期有污染、贫困、技术瓶颈、行政失效，就写成“当时已经出现环境问题/劳工问题/治理问题”。

**为什么错**

现实困难可以存在很久而没有成为 thought / debate 的对象。

**最低修复**

寻找 actor questioning、criticism、defense、new classification、institutional redesign、competing responses 等 problematization evidence。

**AI 自检**

> 我的证据证明的是“困难存在”，还是“行动者把困难组织成了一个需要回答的问题”？

---

## F11 — First mention = emergence / 首次存世出现即问题诞生

**症状**

找到一个最早词例或最早问句，就把该年定为 problem birth date。

**为什么错**

这可能只是当前检索边界、档案存续、词汇变化或首次显式表达；问题化过程可能更早也可能更晚。

**最低修复**

把 first mention 当 terminus / evidence point；另外寻找 loss of familiarity、debate、institutional change、response plurality。

**AI 自检**

> 我是在给“最早存世证据”定日期，还是已经证明“问题从此前不可问/不活跃转为可问/活跃”？

---

## F12 — Absence = unaskability / 沉默即不可问

**症状**

后期资料不再出现 Q，就判 `became_unaskable`。

**为什么错**

`became_unaskable` 是强 modal claim，需要证明支撑问题的条件已经被拆除；absence 只可能是弱负证据。

**最低修复**

寻找 positive transition evidence：分类废止、jurisdiction 变化、核心前提崩塌、answer 成为 category error 等。

**AI 自检**

> 我证明了“没人留下记录”，还是证明了“旧问题按原结构已经不再成立”？

---

## F13 — Disappearance = solution / 消失即解决

**症状**

一个争论不再出现，于是叙述成问题“被解决”。

**为什么错**

问题可能被 displaced、reclassified、institutionally reassigned、silenced 或失去 askability。

**最低修复**

分别检验 `solved / displaced / weakened / became_unaskable / evidence_gap`。

**AI 自检**

> 有行动者证据说明他们认为问题已经解决吗？如果没有，还有哪些退出机制？

---

## F14 — Archive silence = actor silence / 档案沉默即行动者沉默

**症状**

档案馆或数据库没有材料，于是写“当时没人关心”。

**为什么错**

silence 可能在 record creation、selection、preservation、access、digitization、retrieval 或 later narrative 任一层产生。

**最低修复**

区分 `actor_silence / source_silence / archive_silence / retrieval_silence / narrative_silence`。

**AI 自检**

> 我知道记录从行动者到今天的哪一环可能丢失吗？

---

## F15 — Retrieval zero = historical zero / 零检索即历史零

**症状**

关键词、全文检索、OCR 或 embedding search 没命中，就判 absent。

**为什么错**

可能存在 alternate vocabulary、OCR 错误、未数字化文献、metadata 缺失或 genre mismatch。

**最低修复**

记录检索策略、coverage、aliases、OCR 状态与未覆盖 source genres；必要时输出 `evidence_gap`。

**AI 自检**

> 我的“没有”是 corpus statement，还是 historical statement？

---

## F16 — Censorship inversion / 审查环境下反向误读沉默

**症状**

高风险话题公开材料很少，于是推断 concern 很低。

**为什么错**

审查、职业风险、秘密、隐私或弱势群体自我保护可能导致 `high concern + high silence`。

**最低修复**

寻找私人材料、执法/审查痕迹、间接表达、替代词、机构内部材料；降低负证据强度。

**AI 自检**

> 如果行动者非常关心但公开说出来会有代价，我今天看到的记录会不会恰好也是沉默？

---

## F17 — Primary-source fetish / 一手材料天然正确

**症状**

因为材料同时代，就把它当成最高可信历史事实。

**为什么错**

primary source 仍可能宣传、误解、隐瞒、只代表单一立场，或只适合证明“有人这样说”。

**最低修复**

证据强度必须 claim-relative；检查 creator、purpose、audience、point of view、knowledge position 与 counterevidence。

**AI 自检**

> 这份材料最强能证明什么？我是否让它证明了超出作者所知/所代表范围的命题？

---

## F18 — Retrospective backprojection / 后来叙事倒灌

**症状**

用几十年后的官方史、回忆录、教材或研究综述来证明早期行动者当时就拥有同样的 problem frame。

**为什么错**

后来的 coherent narrative 可能重排、统一或发明谱系。

**最低修复**

将其标为 `retrospective / later_reinterprets`，只用于证明后来的记忆/谱系建构，除非有同时代证据回接。

**AI 自检**

> 如果没有这份后来的叙事，我还能从当时材料中恢复同一个 formulation 吗？

---

## F19 — Edition / version collapse / 版次塌缩

**症状**

引用 2002 修订版，却写“作者 1969 年说”；用后来编辑的讲座转录替代当时文本而不说明。

**为什么错**

修订、编辑、翻译、删节会改变可用于方法或 actor wording 的证据。

**最低修复**

记录 original date、edition/version、editor、translator、locator、digital representation。

**AI 自检**

> 我现在引用的具体措辞在我声称的那个历史版本中真的存在吗？

---

## F20 — OCR confidence laundering / OCR 命中洗成确定引文

**症状**

机器识别文本直接进入关键 actor formulation 或逐字引文。

**为什么错**

OCR 对旧字体、版面、专名、否定词、数字和标点尤其容易出错，而这些小差异可能改变 problem reconstruction。

**最低修复**

关键措辞在 facsimile 可得时回图像核验；否则显式标 `ocr_only / unverified`。

**AI 自检**

> 这条判断如果 OCR 少了一个“不”字是否会改变？我看过原图吗？

---

## F21 — Translation equivalence / 同译词即同概念

**症状**

不同语言的历史词都被翻成同一个现代汉语/英语词，于是判断 concept/problem continuity。

**为什么错**

翻译会压缩语义场、语用角色、制度含义和历史时间层。

**最低修复**

保存 original term、translation responsibility、alternative translations 与 contemporaneous use；必要时把 translation 本身当历史过程研究。

**AI 自检**

> 如果我只看原词而不是统一译词，这两边仍然像同一个问题吗？

---

## F22 — Object naturalization / 把问题对象当成天然不变

**症状**

假设“疯癫”“儿童”“劳动”“文学”“机器智能”等对象从古至今先验存在，只是观点不同。

**为什么错**

对象可能通过分类、测量、制度 jurisdiction、专业实践和 truth/evaluation rules 才获得历史上特定边界。

**最低修复**

检查 inclusion/exclusion、分类权、观测技术、记录制度、institutional jurisdiction 与 object-status claims。

**AI 自检**

> 两个时期说的是“同名对象”，还是对象的边界和可见方式已经改变？

---

## F23 — Causation = identity / 因果后继即同一问题

**症状**

因为 A 导致 B，就连成 `continuous`；或者因制度 A 产生争论 B，就认为 B 是 A 的新版。

**为什么错**

历史后继关系不等于 problem identity。A 可以产生一个全新的 B。

**最低修复**

优先考虑 `transformed_successor`，并执行 Answer Transfer / Presupposition Removal / Historical Recognition tests。

**AI 自检**

> 如果我删掉“A 导致 B”这条因果关系，A 与 B 的问题结构本身还足够相似吗？

---

## F24 — Citation = lineage / 引用前人即问题连续

**症状**

B 引用了 A，于是直接视为同一争论链。

**为什么错**

引用可能是借权威、反讽、重新命名、制造传统或把旧作者征用进新问题。

**最低修复**

把 actor 的 continuity claim 保存为 evidence，再检查 target、stakes、presuppositions 与 answer space。

**AI 自检**

> B 引用 A，是因为继承同一问题，还是为了在新问题中利用 A？

---

## F25 — Canonical-author compression / 把集体争论压成一位大师

**症状**

复杂 debate 被写成“X 提出了问题，Y 回答了问题”，忽略会议、议会、专业组织、行政流程中的互动。

**为什么错**

很多 problem formulations 是在 proposal → objection → reformulation → uptake 中形成，不属于单个人。

**最低修复**

允许 `exchange / debate / institutional_process / mixed` episode unit，并保存 opponent/audience/uptake。

**AI 自检**

> 如果移除最著名的作者，这个问题场是否仍能从互动记录中被观察到？

---

## F26 — Winning-formulation bias / 只保存后来胜出的表述

**症状**

episode 只保留最终制度化或最著名 formulation，把同期 rival diagnoses 删除。

**为什么错**

会把开放争论写成必然演化，污染 answer space 与 emergence reconstruction。

**最低修复**

保存 competing formulations、rejected answers、failed proposals 和 uptake/refusal。

**AI 自检**

> 当时一个不知道后来结局的人，会认为还有哪些问题表述和答案是活的？

---

## F27 — Graph-completion bias / 为了图谱完整强行建边

**症状**

看到两个 episode 就认为必须选一个连续关系；`undetermined` 很少使用。

**为什么错**

图的完整性不是历史证据。Problem History 的原则是 **edges harder than nodes**。

**最低修复**

`analogy_only / unrelated / undetermined` 均视为合法终态；每条 edge 同时保存正反证据。

**AI 自检**

> 如果这两个节点永远没有边，研究结论是否仍然成立？如果成立，为什么我要强行连接？

---

## F28 — Continuity-only evidence / 只搜支持谱系的材料

**症状**

一旦提出 lineage，就只寻找引用、相似词和相似答案。

**为什么错**

identity claim 必须可被未来材料推翻；不找 discontinuity evidence 会产生 confirmation bias。

**最低修复**

每次 identity verdict 都必须分别输出 `continuity_evidence` 与 `discontinuity_evidence`。

**AI 自检**

> 什么材料如果找到，会迫使我把 `continuous` 降级为 `reformulated / transformed_successor / analogy_only / undetermined`？我找过吗？

---

## F29 — Conjecture hardening / 推测熟悉化成事实

**症状**

第一版写“可能是”，后续文档不断引用，最终没有新证据却变成“是”。

**为什么错**

重复不会增加证据强度。Langlois 与 Seignobos早已警告，研究者会因反复思考而把 conjecture 误感为更确定。

**最低修复**

claim 保存 status、evidence 与 provenance；升级强度必须指向新增证据。

**AI 自检**

> 这条结论自上一次 confidence 升级以来新增了什么证据？如果答案是“没有”，为什么等级变了？

---

## F30 — Method-author dehistoricization / 把方法论作者写成永恒教义

**症状**

把“Skinner”“Foucault”“Koselleck”“Collingwood”各压成一句固定规则，不区分版本、时期、修订和后人重构。

**为什么错**

本项目要求历史化问题，就不能让自己的方法来源逃离历史化。

**最低修复**

引用具体文本、年份、版次；区分 author claim、later reconstruction 与 project design。

**AI 自检**

> 这条规则是作者在我引用的那个版本中真的提出的，还是后来学者/本仓的操作化？

---

## F31 — Theory-to-schema laundering / 理论术语洗成数据字段

**症状**

某理论家使用 `presupposition / problematization / concept / speech act`，于是数据库立即把它们当成未经争议的字段和枚举。

**为什么错**

理论概念的技术意义与本项目研究字段未必相同；schema 一旦冻结会把解释争议伪装成数据事实。

**最低修复**

所有操作化字段先标 `project design`，经过真实 episodes 和 adversarial calibration 后再冻结。

**AI 自检**

> 这个字段是在保存材料，还是在把某个理论立场偷偷变成数据库真理？

---

## F32 — False precision / 伪精确证据评分

**症状**

给历史证据打 0.83、92/100 等分数，却不能解释数值如何获得。

**为什么错**

看似可计算，实际掩盖了 directness、independence、source purpose、survival 与 counterevidence 等不同维度。

**最低修复**

用 explainable status：`high / medium / low / contested / undetermined`，并写出理由。

**AI 自检**

> 两个研究者看到同样材料，能否按明确规则重现这个数字？如果不能，为什么要用数字？

---

## F33 — Evidence-level essentialism / 给来源永久贴“高/低证据”等级

**症状**

“一手材料=A，高可信；二手材料=B；回忆=C”，然后所有 claim 都照此排序。

**为什么错**

证据强度是 claim-relative。同一文献对不同命题的证明力完全不同。

**最低修复**

拆分 temporality、participant relation、evidential function 与 claim link。

**AI 自检**

> 这份 source 对“有人公开这样说”与“整个群体都这样想”的强度为什么应该相同？

---

## F34 — Research-boundary erasure / 把资料边界当历史边界

**症状**

“我查到的材料从 1850 开始，所以问题从 1850 开始”；“数据库没有，所以不存在”。

**为什么错**

研究工具、语种能力、访问权限、数字化范围和时间预算都是 researcher-side constraints。

**最低修复**

显式记录 `evidence_gap / corpus_coverage / unavailable_sources / next_search`。

**AI 自检**

> 这条时间边界属于历史对象，还是属于我当前能看见的材料？

---

## F35 — Beautiful-lineage bias / 为了漂亮故事牺牲歧义

**症状**

把复杂争论写成一条“问题提出—发展—解决”的线性链，删除 split、merge、revival、displacement 与失败支线。

**为什么错**

历史问题常分裂、合并、被取代、复活或长期未定。漂亮叙事不能成为 evidence criterion。

**最低修复**

优先表达歧义；必要时保持多个 competing reconstructions。

**AI 自检**

> 我是否因为一条更直的时间线“更好讲”，而删除了会使 lineage 变复杂的材料？

---

# 快速 failure-mode gate

提交研究包前，至少逐项问：

```text
[ ] 我有没有把 modern title 当 actor question？
[ ] 我有没有用同词/embedding 代替 identity evidence？
[ ] reconstructed_actor 是否有独立支持？
[ ] actor-language 是否可用？
[ ] speech act 与 problem formulation 是否分开？
[ ] context 是否有具体解释功能？
[ ] difficulty 是否被误写成 problem？
[ ] first mention 是否被误写成 emergence？
[ ] silence 是否经过 negative-evidence gate？
[ ] disappearance 是否被误写成 solution？
[ ] source version / locator / OCR 是否可复核？
[ ] primary source 是否被过度授权？
[ ] retrospective narrative 是否倒投给早期 actor？
[ ] translation 是否抹平原词差异？
[ ] object 是否被假定为跨时代天然不变？
[ ] causation/citation 是否被误写成 identity？
[ ] competing formulations 是否被保留？
[ ] continuity 与 discontinuity evidence 是否都搜索过？
[ ] confidence 升级是否真的新增证据？
[ ] `undetermined / analogy_only / evidence_gap` 是否被允许？
```

若多项不能回答，不应继续冻结 schema 或构建 problem graph。

---

# M0 calibration 应专门诱发的错误

后续 5 段真实文本 calibration 和 identity fixtures 不应只测试“能不能做对”，还应故意诱发以下捷径：

1. 给一个现代标题，观察 Agent 会不会倒投 actor question；
2. 提供同词异义文本，观察是否自动 `continuous`；
3. 提供换词但有明确传承的文本，观察是否漏掉 continuity；
4. 提供一段“答案”但没有独立问题证据，观察是否循环重建；
5. 提供严重现实困难但没有同时代 problematization，观察是否 `difficulty = problem`；
6. 提供公开沉默但私人/审查材料存在的案例，观察是否 `silence = absence`；
7. 提供明显 semantic shift 但 problem structure 基本稳定的案例；
8. 提供 actor 自称继承、但核心 presupposition 已断裂的案例；
9. 提供证据正反冲突的案例，观察是否真正使用 `undetermined`；
10. 提供后来的漂亮统一叙事，观察是否倒灌到早期行动者。

方法通过的标准不是两个 Agent 总给出相同标签，而是：

- 它们都能清楚分离 actor evidence 与 researcher inference；
- 分歧可以定位到具体 source / presupposition / answer-space 判断；
- 它们主动寻找 counterevidence；
- 没有证据时会停在 `undetermined / evidence_gap`；
- 不会仅因为 prompt 希望有一条 lineage 就制造 edge。
