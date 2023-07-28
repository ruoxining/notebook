乔姆斯基：
结构主义语言学到转换生成语法。
![[constructionist.png]]

1. 语言能力/语言表现：语言能力是人先天具有的独立能力，它通过学习某种或某些特定语言展现出来。
2. 深层结构/表层结构：深层结构通过转换规则生成表层结构。

语言学的工作不应当是搜集语言素材加以归纳，而是要解释语言的创造性。

CNF

```
S -> AB
A -> AA | a
B -> b | e
```

转换生成语法规则
$\Sigma = \{NP, Vp, T, N, Npsing, NPpl, Aux, V, C, M, En, S, Past, Af\}$
```
S -> NP + VP
VP -> Verb + NP
NP -> Det + N
Verb -> Aux + V
Det -> the, a...
N -> man, ball...
Aux -> will, can...
V -> hit, see...
```

传统（成分）语法规则
```
1. 主 + 谓
2. 主 + 谓 + 宾
3. 主 + 系 + 表
4. 主 + 谓 + 宾 + 双宾
5. 主 + 谓 + 宾 + 宾补
6. 主 + 谓 + 并列宾

...
```

《句法结构》（1957）核心句和转换概念。
![[Untitled 7.png]]

生成步骤
1. 生成核心句。
    ```
    S -> X1 | X2 | ... Xn
    ```
    
2. 转换结构（替换、省略、添加、换位）。
    ```
    X1 -> Y1Z1 | ...
    ...
    ```
    
3. 添加形态音位规则。
    ```
    Z1 -> W1
    ...
    Zn -> Wn
    ```
    

转换：整个转换生成过程可以分为三个步骤

1. 通过短语结构改写规则，得到表达式$R_c$，$R_c$由非终端语类符号组成，是深层结构。
2. 通过词汇插入规则得到表达式$R_1$，$R_1$由终端语类符号组成，但仍是深层结构。
3. 通过转换规则得到表达式$R_1$，$R_1$当然还是由非终端语类符号组成，但它是表层结构。
![[Linguistics_Notes/asset/Untitled 1 1.png]]

深层结构和表层结构

乔姆斯基语法体系中，指句子生成过程中特定阶段所采用的一种特殊操作手段或规则。深层结构是它的输入，表层结构是它的输出。

有的句子表层结构不同，深层结构相似。通过转换操作可以相互转化。
![[beat.png]]

有的句子深层结构不同，表层结构相似。通过转换操作不能相互转化。
![[please.png]]


## Recursion in Syntax & Grammar

in Syntax

A language is recursive if it is decided by some Turing machine

所以皮拉罕语不能被图灵机接受

语义学的recursive与计算理论的recursive是等价的吗

这个问题要不留一下，我目前初步觉得它是计算理论上recursive的，即能被图灵机decide的，因为（似乎是根据乔姆斯基）皮拉罕语的每一个句子应该都能用一种CFG生成（只需要设计出S->所有句法成分组合的non-terminal->terminal，不添加比如使NP->clause->NP+VP这样的规则就好），而我们证明过{a CFG generates string w}这个语言是recursive的。所以图灵机的recursive似乎与语法上的recursive不一样，不过怎么个不一样法呢？[表情]（以及刚刚想错了，皮拉罕语的例子挑战的是语法上的递归）