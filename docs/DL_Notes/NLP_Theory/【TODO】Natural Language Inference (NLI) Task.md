#确定写不出来先放弃吧
## Task Description
Natural Language Inference (NLI) problem concerns the logic reasoning relationship of sentences or facts in natural language texts. 

## Relevant Survey
There are several relevant surveys on the NLI tasks.
#### A survey of paraphrasing and textual entailment method (2017)
[https://www.jair.org/index.php/jair/article/view/10651](https://www.jair.org/index.php/jair/article/view/10651)

#### An overview of Natural Language Inference Data Collection: The way forward? (2017)
[https://aclanthology.org/W17-7203.pdf](https://aclanthology.org/W17-7203.pdf)

#### Logical formalizations of commonsense reasoning: a survey (2017)
[https://www.jair.org/index.php/jair/article/view/11076/26258](https://www.jair.org/index.php/jair/article/view/11076/26258)

#### Recent Advances in Natural Language Inference: A Survey of Benchmarks, Resources, and Approaches (2019) 
[https://arxiv.org/abs/1904.01172](https://arxiv.org/abs/1904.01172)

#### A Survey on Recognizing Textual Entailment as an NLP Evaluation (2020)
[https://aclanthology.org/2020.eval4nlp-1.10.pdf](https://aclanthology.org/2020.eval4nlp-1.10.pdf)

#### SYMBOLIC AND NEURAL APPROACHES TO NATURAL LANGUAGE INFERENCE (2021)
[https://scholarworks.iu.edu/dspace/bitstream/handle/2022/26642/dissertation_final_hai_hu.pdf?sequence=1&isAllowed=y](https://scholarworks.iu.edu/dspace/bitstream/handle/2022/26642/dissertation_final_hai_hu.pdf?sequence=1&isAllowed=y)


#### Natural Language Inference a dissertation (BIll MacCartney)
[https://www-nlp.stanford.edu/~wcmac/papers/nli-diss.pdf](https://www-nlp.stanford.edu/~wcmac/papers/nli-diss.pdf)

#### Toward reasoning in large language models: A survey  
[https://arxiv.org/abs/2212.10403](https://arxiv.org/abs/2212.10403)
The structure of this paper is as follows. 
![](../asset/截屏2023-08-17%2017.39.52.png)
This paper first provides differentiations among deductive reasoning, inductive reasoning and abductive reasoning, and among formal reasoning and informal reasoning. At the end, this paper states that it focuses explicitly in informal deductive reasoning in large language models.
Deductive reasoning
```Text
Premise: All mammals have kidneys. 
Premise: All whales are mammals. 
Conclusion: All whales have kidneys.
```
Inductive reasoning
```Text
Observation: Every time we see a creature with wings, it is a bird. 
Observation: We see a creature with wings. 
Conclusion: The creature is likely to be a bird.
```
Abductive reasoning
```Text
Observation: The car cannot start and there is a puddle of liquid under the engine. 
Conclusion: The most likely explanation is that the car has a leak in the radiator.
```

In the *Towards Reasoning in Large Language Models* section, this survey discusses three main methods in solving math reasoning problems. For fully supervised fine-tuning method, it is suggested that the two main limitations are the lack of the datasets containing explicit reasoning, and the lack of the generializability of models. For CoT methods, this paper introduces CoT as a trigger of LLMs reasoning ability, and introduces several variant of CoT including zero-shot CoT, and three methods towards Rationale engineering, Rational refinement (complexity-based prompting, algorithmic prompting, and Auto-CoT), Rationale exploration (self-consistency probing), and Rationale verification. The Hybrid Method section introduces the Reasoning-Enhanced Training and Prompting and the Bootstrapping & Self-Improving methods. In section *Measuring Reasoning in Large Language Models*, this paper introduces several task variants to the reasoning task, including Arithmetic Reasoning, Commonsense Reasoning and Symbolic Reasoning. Four findings are proposed in this survey, which are that "Reasoning seems an emergent ability of LLMs", "CoT elicits reasoning of LLMs", "LLMs show human-like content effect on reasoning", and "LLMs are still unskilled at complex reasoning". This paper also points out concerns on whether LLMs are reasoning or simply "generating reasoning-like responses".


## Dataset
The natural language reasoning datasets usually follows the multiple choice structure -- given  a premise consisting of a series of sentences and a hypothesis of usually one-sentence length, the label indicates the relationship between them, which are "entailment", "neutral" or "contradiction". According to the length of the premises, the NLI datasets can be classified as sentence-level, paragraph-level and document-level.
### Sentence-level




### Paragraph-level



### Document-level



## Method


### Sentence-level


### Paragraph-level


### Document-level


## Preview