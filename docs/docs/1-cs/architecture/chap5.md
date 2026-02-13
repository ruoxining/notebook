# chap5: Thread-level Parallelism

## 目录
- cache 一致性的概念
- 达成 cache 一致性两个协议

## cache 一致性的概念

**不知道怎么描述的两个术语**

!!! note 
    计组王道有一章专门讲。其它请通过王道学习，还有姜老师 ppt 也有一个小总结的表格。

| 概念 | 全名 | 特点 | 优点 |
| -- | -- | -- | -- |
| UMA | uniform memory access | 每个节点到 memory 的访问时间一致 | |
| NUMA | non-uniform memory access |每个节点到 memory 的访问时间不一致，到自己的快，到别人的慢 | 扩展到更大规模上的可扩展性强 |

**cache 一致性的术语**

如果 CPU 有多个核，或者如果 CPU 是分布式的，它们共用一个 cache，那么就需要使 cache 对所有核/节点的读写保持一致性，比如一个核/节点写的东西对其它核/节点可见，其它核/节点看见的都是最新的。

| 术语 | 一句话定义（在 ppt 上发现的，但是个人感觉不太准确） | 关注的方面是（这栏 from 课本更准确，但不是一句话定义） |
| -- | -- | -- |
| coherence | Memory accesses executed by each processor were kept in order. | reads and writes to the same location | 
| consistency | Memory accesses among different processors were interleaved. | reads and writes wrt other memory locations |


## 达成 cache 一致性两个协议

!!! note
    聪明的读者已经发现我已经不想写了

**Snooping协议**

!!! note
    请通过自己班老师 ppt 学习：MOESI 状态机 + 例题表格 两个图

**Directory协议**

!!! note
    请通过自己班老师 ppt 学习: 例题表格 一个图