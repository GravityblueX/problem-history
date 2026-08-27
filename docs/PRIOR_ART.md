# Prior Art / 方法谱系与查重边界

“问题史”不是从零发明一种史学。它明显与若干已有传统相邻。本项目应该主动承认这些谱系，再说明自己要组合、推进或实验什么。

## 1. R. G. Collingwood：Question and Answer

参考：

- Stanford Encyclopedia of Philosophy, R. G. Collingwood：<https://plato.stanford.edu/entries/collingwood/>
- Stanford Encyclopedia of Philosophy, Questions：<https://plato.stanford.edu/entries/questions/>
- 原著优先读：*An Autobiography*、*An Essay on Metaphysics*、*The Idea of History*。

### 与本项目最直接的关系

Collingwood 强调命题不能脱离它所回答的问题来理解，并把 presupposition / question-and-answer 放到历史理解的中心。

### 本项目不应假装原创的部分

- “理解答案要恢复它的问题”；
- “问题有前提”；
- “不同历史情境产生不同可问问题”。

### 我们可以继续做什么

把 question-and-answer 进一步做成可操作的历史数据模型：问题情境、表述、前提、答案空间、继承/变形关系和证据。

## 2. Quentin Skinner / Cambridge School：语境与言语行动

参考：

- Quentin Skinner, “Meaning and Understanding in the History of Ideas”
- *Visions of Politics*, Vol. I：<https://www.cambridge.org/core/books/visions-of-politics/meaning-and-understanding-in-the-history-of-ideas/96B251BDAB60C0E570F014E340F70EDD>

Skinner 批评把经典作者当作永恒问题的答题者，强调恢复作者在具体语言/政治语境中“正在做什么”。

### 对问题史的约束

这是最重要的防错机制之一：

> 不能先拿今天的问题 X，再去搜过去哪些人“回答过 X”。

必须证明历史行动者拥有相近的问题框架，并说明当时的言语行动和争论语境。

### 和本项目的差异

本项目不只重建单篇文本的 speech act，还想追踪 **problem formulation 跨时间的变形链**。

## 3. Reinhart Koselleck / Begriffsgeschichte：概念史

参考：

- *Futures Past: On the Semantics of Historical Time*：<https://mitpress.mit.edu/9780262610681/futures-past/>
- 其中包含 “Begriffsgeschichte and Social History”等方法性讨论。

概念史研究历史语义、基本概念及其与社会结构/历史时间的关系。

### 本项目必须借用

- 词义不是超历史稳定的；
- 语义变化本身是历史事件；
- 同一个现代词不能无损投射回过去。

### 但问题史不能等同于概念史

一个问题可能：

- 在没有稳定专名时已经存在；
- 换了一整套词仍继续存在；
- 同一个词背后其实已经换了问题。

因此需要同时保存 `vocabulary history` 与 `problem structure`，不能用词频直接替代问题史。

## 4. Michel Foucault：problematization

相关关键词：problematization / history of thought / practices / regimes of truth。

Foucault 后期多次把研究描述为追踪某些行为、经验、实践怎样成为反思对象和“问题”。

### 对本项目的启发

问题不是天然存在在那里等人回答；某件事情必须在特定知识、制度、道德和实践关系下才会“成为问题”。

### 使用警告

不要只用二手概括写“福柯的问题化理论”。真正采用这一支时，要回到具体访谈、讲座和著作语境，并区分 Foucault 自己不同时期的术语变化。

## 5. History of Ideas / Intellectual History

传统思想史、政治思想史、科学思想史已经积累了成熟的文本语境与人物研究。

本项目不应通过改名来重复：

- 某思想家的观点汇编；
- 某概念的历代释义；
- 某学派发展史；
- 当代研究综述。

真正的增量必须体现在“问题成为问题的条件”和“问题结构的变化”。

## 6. 数字思想史 / Computational Intellectual History

值得注意：计算方法已经进入思想史和概念史。

参考：

- *Explorations in the Digital History of Ideas*（Cambridge University Press）：<https://www.cambridge.org/core/books/explorations-in-the-digital-history-of-ideas/introduction/0185C087E60527AC121B635BCD350090>
- 2026 年综述 “Computational conceptual history of scientific concepts: From early digital methods to LLMs”：<https://arxiv.org/abs/2606.04118>

已有方法包括：

- 词频/搭配变化；
- distributional semantics；
- lexical semantic change；
- 网络和语料方法；
- LLM 辅助分类/语义分析。

### 本项目的计算边界

计算方法可以用于**发现候选变化**，不能直接宣布“问题已经变化”。

例如 embedding 漂移只能提示语义环境变了，仍需历史文本证明：

- 问题表述是否改变；
- 前提是否改变；
- 回答空间是否改变；
- 当事人是否真的把它视为同一问题。

## 7. 本项目的可能新贡献

如果只写方法文章，本项目很容易变成旧理论重述。真正值得实验的是：

### A. Problem Episode 数据模型

把历史问题拆成：

- formulation；
- presupposition；
- actors；
- institution；
- vocabulary；
- answer space；
- evidence；
- predecessor/successor；
- displacement / transformation。

### B. “问题变形”而不是“概念演化”图

图上的边应能区分：

- reformulated；
- narrowed；
- broadened；
- displaced；
- split；
- merged；
- became-unaskable；
- revived。

### C. 失败案例库

专门记录：

- 后见之明；
- 永恒问题幻觉；
- 只凭同词认定同问题；
- 只凭相似答案认定同问题；
- 把研究者问题误当历史行动者问题。

这可能比“成功案例”更有方法价值。

## 每开一个问题前必须回答

- [ ] 它与概念史研究是否已经高度重合？
- [ ] 是否已有成熟 intellectual history 专著？
- [ ] 我们追踪的是词，还是问题结构？
- [ ] 有无原始文本能证明历史行动者真的在问？
- [ ] 时间分段依据是什么，而不是为了凑年代？
- [ ] 哪一次变化是真正的 reformulation，而非换了作者？
- [ ] 计算方法提供的是证据、线索还是仅仅可视化？

答不清时，先做文献综述，不要急着“建图谱”。
