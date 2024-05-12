# 数据库函数依赖

## 定义：函数依赖

函数依赖是指，在一个关系 R 中，如果属性（组）Y 的值是由属性（组）X 的值决定的，就称 Y 对 X 有函数依赖。考虑到本身函数的定义是 X 中的元素在 Y 中有唯一确定的值，那么这里的依赖就是指，两个元素如果在 X 中的值一样，那么在 Y 中的值也一样。

形式化定义：设 $R(U)$ 是属性集合 $U={A_1, A_2, ..., A_n}$ 上的一个关系模式，X, Y 是 U 上的两个子集，若对 $R(U)$ 的任一个可能的关系 $r$，$r$ 中不存在两个在 X 中属性值相等，在 Y 中属性值不等的元组。即称为“X 函数决定 Y”或“Y 函数依赖 X”，计作 X -> Y。

## 推导规则：Armstrong 公理系统
Armstrong 公理系统是描述数据库中的所有函数依赖关系的一系列 references（推理规则），在 1974 年由 William W. Armstrong 设计。

Armstrong 公理系统有三大公理（自反律，增广律，传递律），和一些引理。

**公理**

- 自反律：
- 增广律：
- 传递律：

**引理**

- 

## Normal Form 范式：6 个范式

我们在此要介绍一个数据库设计的目标：存储信息时没有不必要的冗余，检索信息的效率高。以及引入 norma form 范式的概念来介绍如何实现这个目标。

数据库设计的六大范式。TODO：讲解一下什么时候可以用这些范式

!!!
    精简版

| 名称 | 介绍 | 范例 | 范围 |
| -- | -- | -- | -- |
| 第一范式 1NF |  |  | 大，逐个包含下方的 |
| 第二范式 2NF |  |  | |
| 第一范式 3NF |  |  | |
| Buckus-Codd NF |  |  | |
| 第五范式 5NF |  |  | |
| 第六范式 6NF |  |  | 小，逐个被上方的包含 |

!!!
    冗余版

**First Normal Form 第一范式**

第一范式的含义：atomicity 原子性。即不能再继续拆分，属性不能再向下拆分。当一个关系模式 R 的所有属性都是 atomic 的，这个关系模型就是第一范式。

存在的问题：

- redundancy 冗余

- complicated updates 更新数据很复杂

- null-values: difficult to insert/remove

如何分解一个关系 R 使其符合第一范式？

首先介绍 decomposition 分解分为两类

- lossy decomposition 有损分解
    如果不能用分解后的几个关系重建原本的关系，就称分解为有损分解。

- lossless decomposition 无损分解
    如果关系 R 分解后产生关系集 (R1, R2) 且 R = R1 $\cup$ R2，则称为一个无损分解。如果一个关系是无损分解，则要满足条件 $\Pi_{R_1}(r) \Join \Pi_{R_2}(r) = r$，当 R1 和 R2 是关系 R 的分解，r(R) 指 R 上在分解时可能损失的一个关系时。

**Second Normal Form 第二范式**


**Third Normal Form 第三范式**


**Buckes-Cudd Normal Form BCNF范式**



**Fifth Normal Form 第五范式**


**Sixth Normal Form 第六范式**



## 函数依赖

## 闭包


## 最小覆盖


## References
- [blog](https://www.cnblogs.com/tangyanbo/p/4462734.html)
- [blog](https://www.cnblogs.com/ranran/p/4165200.html)
- [blog](https://www.cnblogs.com/ysql/p/4171432.html)