# Basis

Eight Great Ideas 8 种伟大的思想

在计算机组成发展的过去 60 年里有 8 种伟大的思想形成了，这些思想将贯穿整门课，指导我们对硬件进行性能的优化。

- Design for Moore's Law 适应摩尔定律设计
    
    摩尔定律说每单位集成电路上的晶体管数量每 18-24 个月翻一番。计算机体系结构应当预测技术发展的速度，做适用于未来的设计。

- Use Abstraction to Simplify Design

    用抽象 Abstraction 来表示不同层次的设计。低层次的细节不应当对高层次显现。

- Make the Common Case Fast

    加快一般的情况，比加快稀有的情况更有效。

- Performance via Parallelism

    并行。

- Performance via Pipelining

    一种特殊的并行技巧被命名为 pipeline。（应该是一般用来指 pipeline CPU 的。）

- Performance via Prediction

    在不知道未来情况的时候，可以先做预测然后先开始做，比等到未来情况再开始做可能更快。（应该是专指跳转预测的）

- Hierarchy of Memories

    内存分层。

- Dependability via Redundency

    计算机不止需要变快，也需要可靠性。因为硬件设备可能坏掉，需要添加一些冗余的部件来协助检测和恢复。