# Math Word Problems

## An Introduction to Math Word Problems
The math word problem (MWP) aims to solve simple primary school math problems (in plain-text format) with deep learning methods. The problems usually consists of numbers no larger than 100 and only 5 operators (+, -, \*, / and =).
This blog is structured as follows. The Dataset part will introduce two main types, one indicating the locations of variables, and the other simply embedding the math formula within the natural language texts. The Methods parts will introduce several prevailing methods in solving this task, including both the models and workflows that improves the accuracy of models.

## Surveys
#### The Gap of Semantic Parsing: A Survey on Automatic Math Word Problem Solvers (2019)
This survey provides a comprehensive introduction to the MWP datasets and methods prior to 2019. This survey defines three stages of MWP solving, the Rule-based matching stage (1960-2010), Semantic parsing, feature engineering and statistical learning stage (2011-2017), and Deep learning and reinforcement learning stage (2017-2019).

#### Towards Tractable Mathematical Reasoning: Challenges, Strategies, and Opportunities for Solving Math Word Problems (2021)
This survey introduces the contemporary MWP datasets til 2021, and methods including rule-based, and neural network encoder-decoder structures. Specifically, this paper concludes three strategies for math word solving, (i) direct answer generation, (ii) expression tree generation for inferring answers, and (iii) template retrieval for answer computation. Considering the type of problem solving method, this paper concludes two classes. The first class is non-neural approaches (rule-base or pattern matching approaches, semantic parsing, and statistical machine learning approaches), within which a particular strategy of applying domain knowledge in classifying the problems (e.g. into change, part-whole and compare classes). The second class is neural approaches, including intuitions of (i) predicting the answer directly (ii) generating a set of equations or mathematical expressions and inferring answers from the by executing them (iii) retrieving the templates from a pool of templates derived from training data and augmenting numerical quantities to compute the answer. These neural approaches generally follow encoder-decoder architectures, which fall in four types (i) seq-to-seq (ii) Transformer-to-tree (iii) seq-to-tree (iv) graph-to-tree. 
![](../asset/截屏2023-08-16%2000.48.41.png)
Among the four methods, the tree-structured decoder attend both parents and siblings to generate the next token, while the bottom-up representation of sub-tree of a sibling could further help to derive better outcomes. The graph-based encoder aims to learn different types of relationships among the constituents of MWPs. This section also mentions that "Data augmentation is a popular preprocessing technique to increase the size of training data" (reverse operation-based augmentation techniques, different traversal orders of expression trees, and **weak supervision**). 
In section *Math Reasoning in Neural Approaches*, this paper mentions several further topics under math reasoning, interpretability and explainability, infusing explicit and definitive knowledge, and reinforcement learning. 

## Datasets
#### MAWPS: A Math Word Problem Repository (2016)
[sroy9/mawps: Code for MAWPS: A Math Word Problem Repository (github.com)](https://github.com/sroy9/mawps)
The data format is as follows.
```json
[
  {
    "iIndex": 1,
    "sQuestion": "Joan found 70.0 seashells on the beach. She gave Sam some of her seashells . She has 27.0 seashells . How many seashells did she give to Sam ?",
    "lEquations": ["X=(70.0-27.0)"],
    "lSolutions": [43.0]
  },
]
```

#### Math23k: Deep Neural Solver for Math Word Problems (2017)
[Deep Neural Solver for Math Word Problems (aclanthology.org)](https://aclanthology.org/D17-1088.pdf)
This dataset is in Chinese.
```Text
Problem: Dan have 2 pens, Jessica have 4 pens. How many pens do they have in total ? 
Equation: x = 4+2 
Solution: 6
```
#### MathQA (2019)
[MathQA-Dataset (math-qa.github.io)](https://math-qa.github.io/math-QA/)
This paper proposes a math dataset which enhances the AQuA dataset by providing fully-specified operational programs.
This dataset has a diverse range of operators.
![](../asset/截屏2023-08-14%2022.14.36.png)
#### MATH (2021)
[arxiv.org/pdf/2103.03874.pdf](https://arxiv.org/pdf/2103.03874.pdf)
MATH is a LaTeX format dataset, with its answer highlighted in a square block.
![](../asset/Pasted%20image%2020230814171003.png)


#### SVMAP
[arkilpatel/SVAMP: NAACL 2021: Are NLP Models really able to Solve Simple Math Word Problems? (github.com)](https://github.com/arkilpatel/SVAMP)
This dataset does not distinguish the data with the texts. An example data is as follows.
![](../asset/Pasted%20image%2020230814173843.png)


#### GSM8k: grade school math (2021)
Collected by OpenAI, this dataset consists of math problems in natural language descriptions, with the math formulas highlighted with special notes.The numbers are not explicitly highlighted with special symbols.
Several examples of the data format are as follows.
![](../asset/Pasted%20image%2020230814170723.png)

### DRAW
Providing 1000 grounded word problems.

### Algebra


### AsDiv



### MultiArith


### SingleEq





## Methods
### Models
Prior to 2017, the models for solving MWP are mainly concerning with neural networks. After Transformer has been released in 2017, attention-based models have been thriving. The novel models based on Transformer are mainly modifying the encoder and decoder structures, among which there are graph-encoder and tree-decoders.
#### Graph-to-Tree Learning for Solving Math Word Problems (2020)
This paper proposes a attention-based model Graph2Tree, consisting of graph-based encoder and a tree-based decoder.
The math word problems are constructed into Quantity Comparison Graph. 
![](../asset/截屏2023-08-14%2023.12.24.png)


#### Math Word Problem Solving with Explicit Numerical Values (2021)

A novel approach called NumS2T is proposed to solve MWP. NumS2T is constructed with (a) an attention-based seq2seq model to generate its math expressions, (b) a numerical value encoder to obtain the number-aware problem state which are then concatenated with the problem hidden state in (a) to obtain number-aware problem representation, and (c) a numerical properties prediction mechanism for comparing the paired numerical values, determining the category of each numeral and measuring whether they should appear in the target expression.!
![](../asset/截屏2023-08-14%2022.46.32.png)

#### Learning to Reason Deductively: Math Word Problem Solving as Complex Relation Extraction (2022)
This paper proposes a novel approach



### Workflows
Most of the recent works follow the method of knowledge distilling, which means to generate high quality data with LLMs and then train a small model with the generated (and sometimes then augmented) data. The workflow of such tasks mainly assembles that of the following paper.
#### Large Language Models Are Reasoning Teachers
This paper proposes a knowledge distilling method in solving math reasoning problems.
![](../asset/Pasted%20image%2020230814211856.png)


#### Solving Math Word Problems via Cooperative Reasoning induced Language Models (ACL 2023)
This paper develops a cooperative reasoning-induced PLM for solving MWPs called Cooperative Reasoning (CoRe), with a generator to generate reasoning paths and a verifier to supervise the evaluation. 


#### Scaling Relationship on Learning Mathematical Reasoning with Large Language Models (2023)

This paper mainly focus on the following two questions: (i) Which is a better performance indicator of LLMs? (pre-training loss amount/model size) (ii) How to improve small model's performance by data augmentation?
To answer the second question, this paper proposes a novel methods in data augmentation in the LLM data generation step which is called Rejection Finetuning (RFT). The algorithm of sampling data in RFT mainly adopts the thought of rejection sampling, which is expressed in the following pseudo-code. This paper assumes such an algorithm will yield as many as possible diverse reasoning paths.
![](../asset/Pasted%20image%2020230814215707.png)
The workflow of the RFT method is illustrated as follows, where the SFT stands for supervised finetuning.
![](../asset/截屏2023-08-14%2021.59.33.png)
With the novel method RFT, small models such as Llama-7b yields an accuracy of at most 49.7% on GSM8k, 14% higher than the previous SOTA method SFT.



### PAL
This work is a prompt engineering work.
```Text
Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 tennis balls. How many tennis balls does he have now? 
A: Roger started with 5 tennis balls. tennis_balls = 5 2 cans of 3 tennis balls each is bought_balls = 2 * 3 tennis balls. The answer is answer = tennis_balls + bought_balls 
Q: The bakers at the Beverly Hills Bakery baked 200 loaves of bread on Monday morning. They sold 93 loaves in the morning and 39 loaves in the afternoon. A grocery store returned 6 unsold loaves. How many loaves of bread did they have left?
```

```Text
A: The bakers started with 200 loaves loaves_baked = 200 They sold 93 in the morning and 39 in the afternoon loaves_sold_morning = 93 loaves_sold_afternoon = 39 The grocery store returned 6 loaves. loaves_returned = 6 The answer is answer = loaves_baked - loaves_sold_morning - loaves_sold_afternoon + loaves_returned
```




## Preview

