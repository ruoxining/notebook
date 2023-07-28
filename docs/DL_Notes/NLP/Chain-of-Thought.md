
# 任务目标
本实验旨在测评ChatGPT在阅读理解任务（Multiple-choice Comprehension, MRC）上的表现，并使用多种方法挖掘提示词，通过不改变数据集和模型只改变提示词的方法，提高大模型在MRC上的表现。

# 实验设计
为节约时间和金钱成本，对于每个实验，我们仅测试20个问题

# 数据集
AQuA数据集题提供了100,000道用自然语言描述的数学题。
[https://github.com/deepmind/AQuA](https://github.com/deepmind/AQuA)

# Benchmark: Zero-shot Prompting
最简单的MRC问题，只输入question和options
The dataset consists of about 100,000 algebraic word problems with natural language rationales. Each problem is a json object consisting of four parts:
- `question` - A natural language definition of the problem to solve
- `options` - 5 possible options (A, B, C, D and E), among which one is correct
- `rationale` - A natural language description of the solution to the problem
- `correct` - The correct option

```cpp
{
"question": "A grocery sells a bag of ice for $1.25, and makes 20% profit. If it sells 500 bags of ice, how much total profit does it make?",
"options": ["A)125", "B)150", "C)225", "D)250", "E)275"],
"rationale": "Profit per bag = 1.25 * 0.20 = 0.25\nTotal profit = 500 * 0.25 = 125\nAnswer is A.",
"correct": "A"
}
```

结果
正确率 0.15 （3/20）

## Few-shot Prompting
1-shot 0.2（4/20）

## CoT
0.25（5/20）

## Self-Consistency
```
# 将问题按句子分开，并随机打乱句子
question_sentences = question.split('. ')
question = '. '.join(shuffled(question_sentences))
# 分别将问题输入给多个ChatGPT
for i in range(GPT_number):
	answers.append(query(ChatGPT_i, question))
# 将回答更多的答案vote为正确答案
final_answer = top_one(answers)
```

对于每个问题，我们先将question随机打乱，然后输入给三个gpt（不相邻的三轮），让它们vote

因为太简单其实也可以不做了

## multi-step verifier
这个要接一个verifier model
```
# 分别将问题输入给多个ChatGPT，探索尽可能多的推理路径
for i in range(GPT_number):
	answers.append(query(ChatGPT_i, question))

# 使用一个fine-tuned的Verifier，根据数据集标签为answer的每一步打分
scores = []
for answer in answers:
	score = 0
	for step in answer:
		score += Verifier(step, gold_label)
	scores.append(score)

# 将score更高的答案vote为正确答案
final_answer = top_one(scores->answer)
```

## +knowledge
因为原来的math inference数据集不适合，里面的表达没有什么需要特殊的外部知识的

所以我们直接改用原来这篇的数据集HotpotQA，该数据集内部提供问题、回答，和相应的文章context。

acurracy wo query: 0.26090945241420427

acurracy w query: 0.2006805658979623

## Chain-of-Thought Prompting Elicits Reasoning in Large Language Models
添加lets think step by step + 带cot的1-shot

正确率
template:
```cpp
prompt = [I, t, q] -> y
I: instruction
t: example
q: question
y: answer
```

example:
```cpp
There are 3 cars in the parking lot already. 2 more arrive. Now there are 3 + 2 = 5 cars. The answer is 5.
```

applicable to
- math word problems (free response)
- math word problems (multiple choice)
- CSQA (commonsense)
- strategyQA
- date understanding
- sports understanding
- SayCan (instructing a robot)
- Last Letter Concatenation
- coin flip (state tracking)

## The CoT Collection: Improving Zero-shot and Few-shot Learning of Language Models via Chain-of-Thought Fine-Tuning
### Abstract
- introduce CoT collection: a new instruction-tuning dataset that augments 1.88 million CoT rationales across 1060 tasks

### The CoT Collection
- CoT Collection is an instruction-tuning dataset including 1.88 million CoT rationales
- distribution of data:
![[cot_finetuning.png]]


## SELF-CONSISTENCY IMPROVES CHAIN OF THOUGHT REASONING IN LANGUAGE MODELS

### Introduction
- introduce a novel decoding strategy called self-consistency to replace the greedy decoding strategy used in cot prompting

## method
- prompt a language model using chain-of-thought prompting
- replace “greedy decode” in CoT prompting by sampling from the language model’s decoder to generate a diverse set of reasoning paths
- marginalize out the reasoning paths and aggregate by choosing the most consistent answer in the final answer set

two assumptions
- we hypothesize that correct reasoning processes, even if they are diverse, tend to have greater agreement in their final answer than incorrect processes.
- by normalizing the answers. the normalization closer → generations are “similarly alike”
![[self_consistency.png]]
### Advancement
- far simpler than prior approaches (train an additional verifier) or train a re-ranker given additional human annotations to improve generation quality
- unsupervised

## Interleaving retrieval with cot reasoning for knowledge-intensive multi-step questions

### Abstract
- when necessary knowledge is not available or up-to-date within a model’s parameters
- multi-step QA: what to retrieve depends on what has already been derived

### Method
IRCoT mian components
- a base retriever that can take a query and return a given number of paragraphs from a corpus or knowledge source
- a language model with zero/few-show CoT generation capabilities
- a small number of annotated questions with reasoning steps explaining how to retrieve at the answer in natural language (CoT) and a set of paragraphs from the knowledge source K that collectively support the reasoning chain and answer.

## Making Large Language Models Better Reasoners with Step-Aware Verifier

### Abstract
main components
- it generates diverse prompts to explore different reasoning paths for the same question
- it uses a verifier to filter out incorrect answers based on a weighted voting scheme
- it verifies each reasoning step individually instead of the whole chain

# PoT (Program of Thought)

template
original paragraph (incorrect)
```cpp
The first number is 0, the second number is 1, therefore, the third number is 0+1=1.
The fourth number is 1+1=2. The fifth number is 1+2=3. The sixth number is 2+3=5.
(skip..)
The 50th number is 32,432,268,459
```

PoT (correct)
```cpp
length_of_fibonacci_sequence = 50
fibonacci_sequence = np.zeros(length_of_)
fibonacci_sequence[0] = 0
fibonacci_sequence[1] = 1
for i in range(3, length_of_fibonacci_sequence):
	fibonacci_sequnce[i] = fibonacci_sequence[i-1] +
	fibonacci_sequence[i-2]
ans = fibonacci_sequence[-1]
```

# CoS (Chain of Symbol Prompting)

template
shared model input
```cpp
There are a set of bricks. 
The yellow brick C is on top of the brick E . 
The yellow brick D is on top of the brick A . 
The yellow brick E is on top of the brick D . 
The white brick A is on top of the brick B . 
For the brick B, the color is white. 
Now we have to get a specific brick. 
The bricks must now be grabbed from top to bottom, and if the lower brick is to be grabbed, the upper brick must be removed first. 
How to get brick D?
```

cot prompting (wrong)
```cpp
The bricks from bottom to top is B, A, D, E, C 
1. Remove brick A from the top of brick B. 
2. Remove brick E from the top of brick D. 
3. Now brick D is the topmost yellow brick and can be grabbed.
```

cos prompting (correct)
```cpp
B/A/D/E/C 
C/E 
E/D 
D
```