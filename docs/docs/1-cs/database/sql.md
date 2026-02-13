# SQL Grammar


## 关系代数

5 种基本操作

- select
- project
- join
- union
- rename

扩展操作

- cartesian product
- set difference
- set intersection
- assignment

## SQL 语法

**select**

**select distinct**


**where**

**and / or**

**order by**

**insert to**

**update delete**

**JOIN 语句**

连接：用于把多个表的行结合起来。

![](../asset/sqljoins.png)

SQL 中几种 join 的类型

- inner join: 如果表中至少有一个匹配，则返回这些行
- left join: 即使右表中没有匹配，也要从左表返回所有的行（只是这样就没有右表的字段）
- right join: 即使左表中没有匹配，也要从右表返回所有的行（只是这样就没有左表的字段）
- full join: 只要其中一个表存在匹配，就返回行