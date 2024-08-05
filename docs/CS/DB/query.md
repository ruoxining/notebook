# Query Process 查询处理

查询处理的基本步骤是：（1）Parsing and translation 解析和翻译 （2）Optimization 优化 （3）Evaluation 评估。

[](../asset/dbquery.png)

我们最关注的其实是优化步骤。优化一步是基于以下假设：一种 SQL 查询可能对应了多种等价的关系代数表达式。可以通过估计每种优化方法的 cost 来评估方法的好坏。查询优化会选择最节约的方式进行查询。

那么问题就规约成了从所有等价的关系代数表达式中，选择 cost 最小的一个。那么问题就变成了如何计算 cost！

Cost is generally measured as *total elapsed time* for answering query. Many factors contribute to the time cost: `disk access + CPU + network communication`. 但是前面讨论过，一个查询被执行的时候需要被加载到磁盘上，而磁盘读写非常慢；CPU 时间可以忽略不计；只要不是网络应用就不用管网络传输开销。所以目前我们关注的 cost 最大的来源就是磁盘访问时间，其中包含 seek, block read, block write 的用时。因此定义以下 cost 计算方法：

在 B 个 block 中查询 S 次的时间 = B * 转移到一个 block 的时间 + S * 一次查询的时间。

而查询中，读写耗时更多，其中写比读更耗时。所以我们希望查找和查询的时间都更少。

（TODO：这里计算的时候要基于两个假设，cost 依赖于主存中缓冲区的大小，更多的内存可以减少 disk access；另外通常考虑最坏的情况，即主存只提供最少的内存来完成查询工作）

接下来来估计关系代数各个操作的 cost

**Select 选择的 cost 计算**

有三种 select 的算法

- 线性搜索

    去依次查询每个 block 判断是否满足查询条件。

- 索引搜索



- Primary index, equality on key 搜索一条记录


- Primary index, equality on non-key 需要搜索多条记录


- Secondary index 二级索引


**Sort 排序的 cost 估计**

sort 操作一般使用外部归并排序。对于一个大小为 M 的内存，b_r 表示 block 的数量。sort 分为以下两个步骤：(1) create sorted runs，数据从磁盘读入内存中，因为内存大小是 M，每次能处理 M 个数据项 (2) merge the runs。

需要的 merge pass 的总数 $\lceil log_{M-1}(b_r/M) \rceil$。

创建和每次 run 的过程中 disk access 的数量 2br。

外部排序中总的 disk access 次数 $(2\lceil log_{M-1}(b_r/M) \rceil+1)b_r$


**Join 连接的 cost 估计**

以下有几种实现 join 的算法 (1) nested-loop join (2) block nested-loop join (3) indexed nested-loop join (4) merge-join (5) hash-join。

- nested-loop join
    For each tuple in the outer relation, scan the entire inner relation to find all matching tuples. 

    计算 theta-join 表达式：

    ```
    for each tuple tr in sr do begin
        for each tuple ts in s do begin
            test pair (tr, ts) to see if they satisfy the join condition
    ```

    r is called the outer relation and s the inner relation of the join.

- block nested-loop join
    
    Similar to the nested-loop join, but processes the relations in block rather than tuple by tuple to reduce the number of I/O operations.
    
    ```
    for each block br of r do begin
        for each block bs of s do begin
            for each tuple tr in br do begin
                for each tuple ts in bs do begin
                    check if (tr, ts) satisfy the join condition
                        if they do, add tr·ts to the result
                end
            end
        end
    end
    ```

    最坏的情况：
        block transfer b_r * b_s + b_r

    基础情况：

- index nested-loop join


- merge-join
    Requires both relations to be sorted on the join key. Merges the sorted relations by iterating through them in parallel.


- hash join

    Uses a hash table to partition the tuples of one relation based on the join key, then probes the hash table with the tuples of the other relation.


对比：

Nested-loop Join: Simple but inefficient for large datasets due to 
𝑂
(
∣
𝑅
∣
×
∣
𝑆
∣
)
O(∣R∣×∣S∣) complexity.
Block Nested-loop Join: Optimized version of nested-loop join that processes blocks to reduce I/O operations.
Merge Join: Efficient for sorted relations, with complexity dominated by the sort operations.
Hash Join: Very efficient for large datasets, especially when one relation can fit into memory, with 
𝑂
(
∣
𝑅
∣
+
∣
𝑆
∣
)
O(∣R∣+∣S∣) complexity assuming good hashing.


**Duplicated Deletion 重复消除**

排序和投影可以消除重复

考得不多。


**Aggregation 聚合**

也可以用排序或投影来做。



## Query Optimization 查询优化

对给定查询，优化的方法有：

- Equivalent expressions 等价表达式

    这种属于逻辑优化，设计关系代数表达式。比如，我们做数学题时计算 a\*b + c\*b，优化成 (a+c) \* b，就像一种逻辑优化。
    
    它也叫 Cost based optimization.

    在数据库中原则一般是往往先去做选择和投影（已经对初始表做过一次选择，减少了很多记录），再连接。

- Different algorithms for each operation 相同算子的不同表达式

    这种属于物理层面的优化。比如，我们做数学题时不再用笔算，而是用计算器算，就像是一种物理层面的优化。

    它也叫 Transformation based optimization.

    

!!! 
    TODO 下面的几个专题究竟是什么逻辑排的


### Equivalent expressions



### Statistics for Cost Estimation