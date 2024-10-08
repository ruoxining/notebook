# 数据库关系模式

为什么我们需要关系模式？

在设计数据库的时候，我们画完 E-R 图，要把图转化成表的形式化定义（比如 `Student(sid, course, department)` 这种格式）。这就需要我们对一些属性进行进一步约束，比如要关注这些问题：（1）在两个表里的键谁决定谁？要保证只有 candidate key 的属性才能决定其它属性。（2）有些表该合在一起，还是拆成多个表？如果表合得太多，有些信息可能出现太多次，产生信息冗余、插入异常、更新困难。（3）有些属性虽然不是主键，但又决定其它关系的值，这种情况叫做有函数依赖。

所以我们引入关系代数，来指导我们从 E-R 图到建立形式化定义的这一步骤。其实主要牵扯到的步骤就是关系分解。接下来我们先介绍分解，然后介绍其依赖的理论函数依赖的定义；然后介绍 6 种指导关系模式的范式，这些每种范式层层递进，是一些对数据库关系越来越严格的约束。

## 分解

如果一个关系是不好的，我们希望把它分解成好的关系。

介绍一下 decomposition 分解分为两类

- lossy decomposition 有损分解
    如果不能用分解后的几个关系重建原本的关系，就称分解为有损分解。

- lossless decomposition 无损分解
    一个关系是无损分解，定义是

    (1) $\Pi_{R_1}(r) \Join \Pi_{R_2}(r) = r$，当 R1 和 R2 是关系 R 的分解，r(R) 指 R 上在分解时可能损失的一个关系时。
        
    或者

    (2) 关系 R 分解后产生关系集 (R1, R2) 且 R = R1 $\cup$ R2。

    一个更直观的判断方法是，如果满足 (1) R1 $\cap$ R2 -> R1 且 (2) R1 $\cap$ R2 -> R2，则称为一个无损连接。其中箭头的意思是决定。如果连接后还能决定原来的两个关系，那么当然是无损链接。


这个分解的理论，是基于 (1) functional dependencies 函数依赖 (2) multivalued dependencies 多值依赖 两个理论的。

根据分解理论，我们就可以得到再下一步要介绍的六个范式。

## 函数依赖

概念区别

函数依赖：

部分函数依赖：设 X, Y 是关系 R 的两个属性集合，存在 X->Y, 若 X' 是 X 的真子集，存在 X‘->Y，则称 Y 部分依赖于函数 X。

传递函数依赖：设 X, Y, Z 是关系 R 中互不相同的属性集合，

完全函数依赖：

我看不懂。。。。。。


函数依赖是来自于应用层面的规定（Functional dependencies are constraints on the set of legal relations），先有函数依赖，再有数据库中的值。函数依赖要求两个值

通过

函数依赖可以被证伪（对于单个），不能被证实（对于所有）。

!!!
    本节以下 latex 鸟语全都不考

形式化的定义里函数依赖是指，在一个关系 R 中，如果属性（组）Y 的值是由属性（组）X 的值决定的，就称 Y 对 X 有函数依赖。考虑到本身函数的定义是 X 中的元素在 Y 中有唯一确定的值，那么这里的依赖就是指，两个元素如果在 X 中的值一样，那么在 Y 中的值也一样。

形式化定义：设 $R(U)$ 是属性集合 $U={A_1, A_2, ..., A_n}$ 上的一个关系模式，X, Y 是 U 上的两个子集，若对 $R(U)$ 的任一个可能的关系 $r$，$r$ 中不存在两个在 X 中属性值相等，在 Y 中属性值不等的元组。即称为“X 函数决定 Y”或“Y 函数依赖 X”，计作 X -> Y。

Armstrong 公理系统是描述数据库中的所有函数依赖关系的一系列 references（推理规则），在 1974 年由 William W. Armstrong 设计。

Armstrong 公理系统有三大公理（自反律，增广律，传递律），和一些引理。

**公理**

!!!
    对不起，我是懒狗，我不想敲 latex 写形式化定义了，用人话给大家讲吧。

设 F 为 R(U) 的一组函数依赖，记为 R(U, F)。

- 自反律
  
    如果一个属性集是另一个属性集的子集，那么说后者决定前者。可以叫做，属性集 X 决定它的属性子集。

- 增广律
    
    如果 X -> Y 在 F 这个函数依赖集合中，另一属性（组）Z 是属性集 U 中的元素，那么从 F 中可以推导得出 XZ 函数决定 YZ。有点像在说本来 X 决定 Y，后随便取一个属性集 Z，在两侧分别连接 X 和 Y，结果 XZ 还是决定 YZ。

- 传递律
    
    若 X -> Y，Y -> X，则 X -> Z。

**引理**

!!!
    学不动了光报个菜名吧

- 合并律
- 伪传递律
- 分解率
- 属性集闭包
- 覆盖
  - 最小覆盖


正则覆盖


## Normal Form 范式：6 个范式

接下来我们介绍数据库设计的六大范式。如前文所述，六个范式是对数据库关系属性层层递进、越来越严格的约束。

精简版如下（用于考前突击）：

| 名称 | 介绍 | 范例 | 范围 |
| -- | -- | -- | -- |
| 第一范式 1NF |  |  | 大，逐个包含下方的 |
| 第二范式 2NF |  |  | |
| 第一范式 3NF |  |  | |
| Buckus-Codd NF |  |  | |
| 第五范式 5NF |  |  | |
| 第六范式 6NF |  |  | 小，逐个被上方的包含 |

接下来是详细介绍。

**First Normal Form 第一范式**

简而言之：没有重复的列。

第一范式的含义：atomicity 原子性。即不能再继续拆分，属性不能再向下拆分。当一个关系模式 R 的所有属性都是 atomic 的，这个关系模型就是第一范式。

比如，string 应当被当作不可分割的。比如 ZJU 的学号第一位看本科生研究生，后面两位看年级，但这两个信息如果需要是应当被显示地保存在数据库中，而不是需要的时候去学号中分析查找的。如果这样做，相当于把解析字符串的工作给了应用程序，而字符串查找是一个比数据库查询慢的步骤，这样结果很不好。

第一范式没有消除冗余，它消除的是列里重复的信息。它把表格里冗余的列拆分成了多个行。

**Second Normal Form 第二范式**

简而言之：实体的属性完全依赖于主关键字。

第二范式是基于 fully functional dependency 完全函数依赖的。意思是，第二范式用于那些有复合键值的关系，比如当一个关系的主键是多个列的复合时。

如果一个关系本来就没有复合的属性，那本来就是 2NF 的。

如果一个关系有复合的属性，比如 AB -> C，那么 2NF 会把 AB 拆开。

TODO：怎么拆呢

**Third Normal Form 第三范式**

简而言之：不依赖于其它非属性。

A relation is in the third normal form, if there is no transitive dependency for non-prime attributes as well as it is in the second normal form. 

如果一个关系在第三范式里，它应当对于非主键属性没有传递依赖，并且在第二范式里。

**Boyce-Cudd Normal Form BCNF范式**

简而言之：每个依赖关系中，被依赖的都是主键

A relation is in BCNF if it is already 3NF, and if for any functional dependency say P->Q, P should be a super key.

比较 3NF 和 BCNF 的区别：

|  | 3NF | BCNF |
| -- | -- | -- |
| | 不应有 |  |
|  | 弱 | 强 |
|  |  | 减少了冗余 |
| | 保留了所有函数依赖 | 可能有的函数依赖没有被保存 |


**Fifth Normal Form 第五范式**



**Sixth Normal Form 第六范式**


做题的时候似乎只会让写：符合 1NF 的，3NF 的，BCNF 的三种分解。


## 函数依赖

## 闭包


## 最小覆盖


## References
- [blog](https://www.cnblogs.com/tangyanbo/p/4462734.html)
- [blog](https://www.cnblogs.com/ranran/p/4165200.html)
- [blog](https://www.cnblogs.com/ysql/p/4171432.html)