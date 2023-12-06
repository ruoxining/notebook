100 Essentials from Morphology and Syntax

(半小时量子波动速读挑战 先用中文写了)

from Contents

1. Introduction
	这章里E. Bender提出了两个观点，应该是作为全书论证的basis
	- Understanding semantics and pragmatics is beneficial for building scalable Natural Language Processing (NLP) systems.
	- Knowledge of semantics and pragmatics can inform the design of NLP systems for understanding and generation.
	总结来说，两个观点分别说semantics和pragmatics有利于NLP模型scalable（做大）和做好understanding和generation。	
2. What is Meaning?
	 - meaning可以被validity和reference（指代）来建模
	 - NLU需要commonsense reasoning
	 - 词形上的meaning和context里的meaning不一样
	 - 现存的模型分为: locutionary, illocutionary 和 perlocutionary 模型（TODO）
	 - 
3. Lexical Semantics: Overview
	- 如果用符号学的角度来认为word是指向意义的opaque predicate symbols，会失去很多意义（猜测这个意义是context上的）
	- lexical semantics = word sense + semantic roles + connotation (内涵)
	- 有时lexical semantics不由单个word决定，是由词组搭配决定的
4. Lexical Semantics: Senses
	- 这章讲了lexical semantics的一些经典常识，不再摘录，仅记录一些关键词
	- polysemy, morphology, homonymy
	- word senses can change over time, meaning shifting, metaphor
	- you know the meaning of a word by the company it keeps
	- vector space representation
	
5. Semantic Roles
	- 介绍predicate semantics，也不做过多叙述

6. Collocations and Other Multiword Expressions (MWEs)
	- 词组搭配一般比word少一些ambiguity
	- MWE基本有word一样的性质

7. Compositional Semantics 成分语义
	- compositional semantics is largely about working out who did what to whom, where, when, how, and why
	- compositional semantic representations can be constructed for strings, with and without types and with and without explicit syntax.
	- Comparatives express the degree to which an entity has some gradable property in relation to some standard of comparison.
	- 这章没看懂讲的什么 是不是vector semantics

8. Compositional Semantics beyond Predicate-Argument Structure (TODO)
	- politeness markers, strategies
	- 

9. Beyond Sentences
	- 理解对话的意思牵扯到理解discourse（context）
	- lexical processing and discourse processing interact
	- 对话理解和生成遵守游戏理论模型，（TODO）

10. Reference Resolution 指代消解
	- antecedent to a pronoun 可以是一整个句子表达的一个抽象的概念
	- reference resolution depends on: grammatical factors, logical forms, modals, discourse structure

12. Presupposition
	- 话语可能含有entailment和presupposition（一说还可以有一种implicature，区别详见[我的semantics笔记](https://ruoxining.github.io/OBvault/Linguistics_Notes/Semantics/Definition%20Clearification/#implicature)）
	- presupposition的trigger（？TODO）有很多
	- some linguistic expressions pass embedded presuppositions up, some don't, and with others it depends （TODO）
	- presuppositions interact with discourse coherence （TODO）
	
12. Information Status and Information Structure 
	- 定义了一个叫 information status 的名词
	- 定义：information status是一种介绍所指与实在界的联系的语言学描述
	- 在morphology和syntax中的表达
	- 句子的信息结构表达了说话人认为/对听话者来说，哪些是旧的信息，哪些是新的信息。其表达形式有：topic, background, focus, contrast等。不同语言有不同的表达方式
	- 信息结构与truth condition是可能会相互作用的

13. Implicature and Dialogue
	- Implicature是指话外的话。分为conversational和conventional两种。
	- 识别implicature通常不一定需要识别出speaker的cognitive states。
	- 解释表达了什么，可能与判断所表达之事是否正确，不同
	- 在策略对话中，implicature可能是safe或unsafe的。
	- 同意或反对可能在implicature中
	- 有意义的沉默
	- 话语的韵律影响说话人的意思