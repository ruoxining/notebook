# Parsing

本页完成了关于 LL(1), LR(0), SLR (aka. SLR(1)), LR(1), LALR(1) 文法的一些常用区别的整理。由于作者也学得不好，如果有错，请向我指出（可惜评论区我还没研究好怎样配，一定尽快配上，可以先其它途径联系我）。

本页面写作时的特点是尽量用自然语言来描述特点，而不是 latex 数学公式和图像。原因是我在其它资料搜到的讲解都事无巨细用大量公式和图像，使理解变得容易，但不适合速查和记忆。直白一点说就是笔者不想看到它们，一看就头疼。因此也造成了本文档的一个缺点：不是为初学者设计的。初学者推荐阅读 xyx 的笔记。做题时速查记忆可以看本文档。

怎样判断文法是...不是...

| 文法 | 判断是 | 判断不是 |
| :-- | :-- | :-- |
| LL(1) | (不含左递归 && 对于文法中每一个 non-terminal，它的产生式的 SELECT set（即开头的 terminal 与开头的 non-terminal 的 FIRST）两两不交，且不能同时推出空串) \|\| 产生式 lhs 两两不相同 | 含左递归 \|\| 遇到下一个要扫描的 terminal 输入时，有超过一种 derive 方法 |
| LR(0) | 构造出 LR(0) items DFA，如果不存在 shift-reduce & reduce-reduce conflicts | LR(0) items DFA 存在 shift-reduce | reduce-reduce conflicts |
| SLR (aka. SLR(1)) | 构造出 LR(0) items DFA，首先其不存在 reduce-reduce 冲突，且存在 shift-reduce 冲突（否则就为 LR(0) 语法了）。对于每个有 shift-reduce 冲突的地方，状态里面有可 shift 规则也有可 reduce 规则，如果 reduce 后得到的 non-terminal 的 FOLLOW set 与可 shift 规则新纳入的 terminal 都没有交 | shift-reduce conflict 中如果 reduce 后得到的 non-terminal 的 FOLLOW set 与可 shift 规则新纳入的 terminal 有交 |
| LR(1) | 构造出 LR(1) items DFA，如果不存在 shift-reduce & reduce-reduce conflicts | LR(1) items DFA，如果存在 shift-reduce \| reduce-reduce conflicts |
| LALR(1) | 构造出 LR(1) items DFA，如果合并同心集后没有产生 reduce-reduce conflicts（一定不会产生 shift-reduce conflicts，同心集不长那样） | LR(1) items DFA 如果合并同心集后产生了 reduce-reduce conflicts |

大家的 items DFA 怎么画...

| 文法 | items DFA |
| :-- | :-- |
| LL(1) | 它没有… | 
| LR(0) | 先画 NFA：所有 shift 的情况靠读取 non-terminal/terminal 转换，所有 reduce 的情况空转移。然后画 DFA：把空转移合并。 | 
| SLR (aka. SLR(1)) | 同画 LR(0)。只是多判断一下 shift-reduce conflict 的 FOLLOW 和 terminal 重合情况，但这个只体现在 parse table，不属于 DFA 关心的事。 | 
| LR(1) | 其它步骤同画 LR(0)，只是多了在所有 items 后面用逗号隔开一个 lookahead symbol。lookahead 的选择很像选择了对应产生式（不论是 lhs/rhs）的 FOLLOW set，即对应产生式之后接的 terminal 是什么。 | 
| LALR(1) | 同画 LR(1)。只是需要合并所有同心集，同心集是指产生式相同但是只有 lookahead symbol 不同的那些状态。 | 

大家的 parse table 怎么画...

| 文法 | parse table |
| :-- | :-- |
| LL(1) | non-terminals, nullable, FIRST, FOLLOW | 
| LR(0) | states, shift&reduce, goto | 
| SLR (aka. SLR(1)) | states, shift&reduce, goto | 
| LR(1) | states, shift&reduce, goto | 
| LALR(1) | states, shift&reduce, goto | 