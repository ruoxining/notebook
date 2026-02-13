# Multilingual Task Survey

## Introduction

多语言模型 multilingual models 就是能解决多语言任务的模型。在主流训练数据是英语、稀有语言数据稀缺的背景下，如何将模型能力泛化到稀有语言是重要的问题。除了最近的大语言模型外，还会介绍传统方法和传统模型。

## Survey

### A Survey on Large Language Models with Multilingualism: Recent Advances and New Frontiers (2024)

#### 简介

本文介绍多语言大语言模型的训练、使用、挑战、未来研究方向等。由 Beijing Jiaotong University, University of Montreal 和 Tsinghua University 发布。

#### 训练



#### 有多语言能力的大语言模型概览


#### 多语言推理策略


#### 安全性


#### 多领域多语言大语言模型


#### 多语言数据资源


#### 多语言评测


#### 偏见和公平性




## Models


## Datasets


## Studies




### Do Llamas Work in English? (2024, EPFL)

猜想：多语言模型（比如 Llama）在使用以英语为主的语料进行训练时，会将英语作为一种思考的中间步骤 pivot language。

实验方法：对 Llama-2 系列模型，设计数据对 (非英语提示词，next token)。从顶层向量空间 high-dimensional space 探索中间嵌入 intermediate embeddings 如何计算下一个单词的规律。

发现三个阶段：

- intermediate embeddings 远离（不像） output embedding。
- 尽管 intermediate embedding 已经可以解码出语义上正确的下一个单词，但模型对英语词的预测概率更高。
- intermediate embedding 最终在嵌入空间中确定了特定的输入语言。

一句话总结：imtermediate embedding 所代表的抽象概念空间 concept space 更接近英语，可能导致多语言模型中的偏见问题。

### Language-Specific Neurons: The Key to Multilingual Capability in Large Language Models (2024, RUC)

#### 背景

识别多语言大模型里，产生特定语言能力的神经元仍然非常 challenging。

#### 方法

提出了 language activation probability entropy (LAPE) 来检测大语言模型不同语言对应的神经元。

LAPE: 为了减少 RLHF 可能带来的对语言偏好的的影响，主要关注预训练过的模型，而不是微调后的模型。

对于在第 i 层的第 j 个 neuron，定义在语言 k 上的激活概率 activation probability


$$ p_{i,j}^k = E(I(act_fn(\tilde{h}^iW_1^i)_j \lt 0 | language\spacek)) $$

I 是 indicator function（当给定条件为真时，指示函数的值为 1；当给定条件为假时，指示函数的值为 0）。

以此可以获得每个神经元对语言的分布

$$ p_{i,j} = (p_{i,j}^1, ... , p_{i,j}^k, ... , p_{i,j}^l) $$

定义上述分布的熵为 language activation probability entropy (LAPE) 。

$$ LAPE_{i,j} = -\sum^{l}_{k=1} p^{\prime k}_{i,j} log(p^{\prime k}_{i,j}) $$

使用 Llama-2, BLOOM, Mistral 和  Phi-2 进行实验，发现这些神经元主要在顶层和底层 embedding 上。

#### 发现

- 在不同具体的语言上，模型使用的都是一小部分 neuron。
- 可以通过激活或冻结部分神经元，来控制输出的语言。
- 相似的语言激活区域有一定重合度，比如 Chinese 和 Japanese。模型更大，这种效果更明显。
