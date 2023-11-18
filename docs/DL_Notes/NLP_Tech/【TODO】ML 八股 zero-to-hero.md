## ML
**设计模型的时候，如何确定embedding的size?**
embedding的大小一般是一个经验值，假设embedding对应的原始feature的取值数量为n，则一般会采用$log_2(n)$或者$k\sqrt[4]{n} (k<16)$来做初始的size，然后2倍扩大或缩小。

**Self Attention的表达式**
$$Softmax(\frac{QK^T}{\sqrt{d_k}})V$$
对QK进行scaling的目的是，scaling后进行softmax操作可以使输入数据的分布变得更好。数值会进入敏感区间，防止梯度消失，让模型更容易训练。

**attention计算方式及参数量？默写multi-headed attention?**
简约版
```Python
import torch
import torch.nn as nn
import torch.nn.functional as F
import math

class MultiHeadAttention(nn.Module):
	def __init__(self, d_model, num_heads):
		super(MultiHeadAttention, self).__init__()
		self.num_heads = num_heads
		self.d_model = d_model   # d_model is a emphirical number
		assert d_model % self.num_heads == 0
		
		# define the dimension of each head or subspace
		self.d_k = d_model // self.num_heads
		
		# these are still of dimension d_model. They will be split into numbers
		self.W_q = nn.Linear(d_model, d_model)
		self.W_k = nn.Linear(d_model, d_model)
		self.W_v = nn.Linear(d_model, d_model)
		
		# Output of all sub-layers need to be of dimension d_model
		self.W_o = nn.Linear(d_model, d_model)
		
	def scaled_dot_product_attention(self, Q, K, V, mask = None):
		batch_size = Q.size(0)   # layernorm?
		K_length = K.size(-2)    # 
		# scaling by d_k so that the soft(arg)max doesn't explode
		QK = torch.matmul(Q, K.transpose(-2, -1) / math.sqrt(self.d_k))# matrix product of tensors
		# apply the mask
		if mask is not None:  # mask is a matrix with 0 to be masked
			QK = QK.maksed_fill(mask.to(QK.type) == 0, float('-inf'))
		# calculate the attention weights (softmax over the lask dimension)
		weights = F.softmax(QK, dim = -1)
		# apply the self attention to the values
		attention = torch.matmul(weights, V)
		return attention, weights
		
	def split_heads(self, x, batch_size):
		"""
		The original tensor 
		with dimension batch_size * seq_length * d_model is divided by num_heads
		d_model // num_heads = d_k
		so now batch_size * seq_length * d_k
		"""
		return x.view(batch_size, -1, self.num_heads, self.d_k).transpose(1, 2)
		
	def forward(self, q, k, v, mask = None):
		batch_size = q.size(0)
		# linear layers
		q = self.W_q(q)
		k = self.W_k(k)
		v = self.W_v(v)
		# split into multiple heads
		q = self.split_heads(q, batch_size)
		k = self.split_heads(k, batch_size)
		v = self.split_heads(v, batch_size)
		# self attention
		scores, weights = self.scaled_dot_product_attention(q, k, v, mask)
		# concatenate heads
		concat = scores.transpose(1, 2).contiguous().view(batch_size, -1, self.d_model())
		# final linear layer
		output = self.W_o(concat)
		
		return output, weights
```
Multi-headed attention 得到的是两个输出，一个output（1 \* d_model）是线性的attention结果，一个weight矩阵是？维的.
出于运算速度的考虑，我们认为“一次大的矩阵乘法的执行速度比多次较小的矩阵乘法更快”，因此你可以在__init__中
```Python
self.qkv = nn.Linear(d_model, 3 * d_model)
```
在forward方法中
```Python
qkv = self.qkv(x)
q, k, v = torch.split(qkv, self.d_model, dim = -1)  # split into three tensors
```

**Lora可能存在的问题？**
（1）基于低秩的微调可能不always work，比如finetune与pretrain任务的gap过大的时候（如：中英差异）。当然这一点在LLM时代可能并不突出，因为我们认为LLM在与训练阶段已经get了基本所有的知识，finetune也只是在微调格式，因此可能不会有上述gap过大的情况。
（2）用LoRA时也要设置r和target module等，这部分超参的设置需要考虑。

**各种norm方式的优缺点**
常见的norm方式有以下四种：
![](../asset/Pasted%20image%2020230825221344.png)
Batch norm: 把每个batch中每句话相同位置的字向量看成一组做归一化。在处理序列数据（如文本）时，batch norm可能不会表现很好，因为序列数据通常长度不一，并且一次训练中batch的句子长度可能会有很大的差异，此外，batch norm对batch的大小也非常敏感，对于较小的batch大小，batch norm可能也会表现不好，因为每个batch的统计特性可能会有较大波动。

Layer norm: 在每个句子中进行归一化。Layer norm是对每个样本进行归一化，因此它们对batch大小不敏感，这使得它们在处理序列数据的时候表现得更好，另外layer norm在处理不同长度的序列时也更灵活。

Instance norm: 每一个字的字向量看成一组做归一化。优点是对每个样本的每个特征进行归一化，因此可以捕捉到更多的细节信息，能在风格迁移中表现更好，因为在这些任务中细节很重要。缺点是可能会过度强调细节信息，忽略了更宏观的信息。此外instance norm的计算成本相比batch norm和layer norm也更高。

Group norm: 把每句话的每几个字的字向量看成一组做归一化。group norm是batch norm和instance norm的折中方案，在一个子集（即组）上进行归一化。这使得group norm既可以捕捉到batch的统计特性，又可以捕捉到样本的细节信息。此外，group norm对batch大小也不敏感。缺点是group norm的性能取决于组的大小，需要通过实验确定最优组的大小。此外group norm的计算成本也比batch norm和layer norm更高。

**Gradient Clipping**
RNN可能遇到梯度爆炸问题。一个简单的方法是如果梯度变得很大，我们将梯度放缩使其变小。
算法是：当梯度大于一个常数c的时候，执行 $g\leftarrow c\times g/||g||$。


**为什么使用Dropout**
如果参数太多而训练样本过少，容易出现过拟合。具体表现为：在dev set上loss很小，在test set上loss很大。
过去会选择模型集成，训练多个模型进行组合。Dropout能比较有效缓解过拟合。由Hinton在2012年提出，并应用于AlexNet。
Dropout的原理是在前向传播的时候，让某个神经元的激活值以一定概率p停止工作，可以使模型泛化能力更强，因为不会太依赖某些局部特征。
![](Pasted%20image%2020230914203610.png)
工作流程：
1）随机（临时）删除一半的隐藏神经元，保留输入输出神经元不变，被删除的保留参数不变。
2）将输入前向传播后后向传播，只更新剩下神经元上的参数。
3）恢复被删掉的神经元（此时被删除的神经元保持原样，而没有被删除的神经元已经更新）。
4）重复上述过程。


下面的一篇一篇整理
- [Microstrong：深度学习中Dropout原理解析](https://zhuanlan.zhihu.com/p/38200980)
- [神经网络Dropout层中为什么dropout后还需要进行rescale？](https://www.zhihu.com/question/61751133/answer/794717140)
- [bingo酱：L1正则化与L2正则化](https://zhuanlan.zhihu.com/p/35356992)
- [韦伟：从反向传播推导到梯度消失and爆炸的原因及解决方案（从DNN到RNN，内附详细反向传播公式推导）](https://zhuanlan.zhihu.com/p/76772734)
- [Will：神经网络训练中的梯度消失与梯度爆炸](https://zhuanlan.zhihu.com/p/25631496)
- [LSTM如何来避免梯度弥散和梯度爆炸？](https://www.zhihu.com/question/34878706/answer/665429718)
- [LSTM如何来避免梯度弥散和梯度爆炸？](https://www.zhihu.com/question/34878706/answer/931557401)

## 四、机器学习

- [漫漫成长：奇异值分解（SVD）](https://zhuanlan.zhihu.com/p/29846048)
- [阿泽：【机器学习】逻辑回归（非常详细）](https://zhuanlan.zhihu.com/p/74874291)
- [精确率、召回率、F1 值、ROC、AUC 各自的优缺点是什么？](https://www.zhihu.com/question/30643044/answer/1205433761)
- [阿泽：【机器学习】支持向量机 SVM（非常详细）](https://zhuanlan.zhihu.com/p/77750026)
- [丢丢：一篇文章搞定GBDT、Xgboost和LightGBM的面试](https://zhuanlan.zhihu.com/p/148050748)
- [阿泽：【机器学习】决策树（上）——ID3、C4.5、CART（非常详细）](https://zhuanlan.zhihu.com/p/85731206)
- [阿泽：【机器学习】决策树（中）——Random Forest、Adaboost、GBDT （非常详细）](https://zhuanlan.zhihu.com/p/86263786)
- [阿泽：【机器学习】决策树（下）——XGBoost、LightGBM（非常详细）](https://zhuanlan.zhihu.com/p/87885678)

## 四、词向量

- [天雨粟：理解 Word2Vec 之 Skip-Gram 模型](https://zhuanlan.zhihu.com/p/27234078)
- [梦里寻梦：（十五）通俗易懂理解——Glove算法原理](https://zhuanlan.zhihu.com/p/42073620)
- [Luke：深入理解NLP Subword算法：BPE、WordPiece、ULM](https://zhuanlan.zhihu.com/p/86965595)
- [阿北：NLP三大Subword模型详解：BPE、WordPiece、ULM](https://zhuanlan.zhihu.com/p/191648421)
- [韦伟：史上最全词向量讲解（LSA/word2vec/Glove/FastText/ELMo/BERT）](https://zhuanlan.zhihu.com/p/75391062)
- [向阳树：词嵌入：ELMo原理](https://zhuanlan.zhihu.com/p/88993965)
- [张俊林：XLNet:运行机制及和Bert的异同比较](https://zhuanlan.zhihu.com/p/70257427)
- [海晨威：史上最细节的自然语言处理NLP/Transformer/BERT/Attention面试问题与答案](https://zhuanlan.zhihu.com/p/348373259)
- [如何看待瘦身成功版BERT——ALBERT？](https://www.zhihu.com/question/347898375/answer/863537122)
- [Mr.robot：面试中理解ALBERT？（NLP面经）](https://zhuanlan.zhihu.com/p/268130746)
- [JayJay：nlp中的词向量对比：word2vec/glove/fastText/elmo/GPT/bert](https://zhuanlan.zhihu.com/p/56382372)

## 五、循环神经网络

- [陈诚：人人都能看懂的GRU](https://zhuanlan.zhihu.com/p/32481747)
- [陈诚：人人都能看懂的LSTM](https://zhuanlan.zhihu.com/p/32085405)
- [Alan Lee：如何计算 LSTM 的参数量](https://zhuanlan.zhihu.com/p/147496732)

## 六、注意力机制

- [赵强：一文看懂 Attention（本质原理+3大优点+5大类型）](https://zhuanlan.zhihu.com/p/91839581)
- [大师兄：详解Transformer （Attention Is All You Need）](https://zhuanlan.zhihu.com/p/48508221)
- [小鹿鹿lulu：如何优雅地编码文本中的位置信息？三种positional encoding方法简述](https://zhuanlan.zhihu.com/p/121126531)

## 七、其它

- [孙孙：最通俗易懂的BiLSTM-CRF模型中的CRF层介绍](https://zhuanlan.zhihu.com/p/44042528)
- [谢玉强：论文笔记 —— Transformer-XL](https://zhuanlan.zhihu.com/p/70745925)
- [海晨威：NLP 中的Mask全解](https://zhuanlan.zhihu.com/p/139595546)
- [机器学习“判定模型”和“生成模型”有什么区别？](https://www.zhihu.com/question/20446337/answer/256466823)
- [如何用简单易懂的例子解释条件随机场（CRF）模型？它和HMM有什么区别？](https://www.zhihu.com/question/35866596/answer/236886066)
- [如何通俗地讲解 viterbi 算法？](https://www.zhihu.com/question/20136144/answer/763021768)
- [小小将：你必须要知道CNN模型：ResNet](https://zhuanlan.zhihu.com/p/31852747)
- [transformer中的attention为什么scaled?](https://www.zhihu.com/question/339723385/answer/782509914)
- [触摸壹缕阳光：一文详解Softmax函数](https://zhuanlan.zhihu.com/p/105722023)
- [陶将：优化算法Optimizer比较和总结](https://zhuanlan.zhihu.com/p/55150256)
- [余昌黔：深度学习最全优化方法总结比较（SGD，Adagrad，Adadelta，Adam，Adamax，Nadam）](https://zhuanlan.zhihu.com/p/22252270)
- [大师兄：模型优化之Layer Normalization](https://zhuanlan.zhihu.com/p/54530247)
- [天雨粟：Batch Normalization原理与实战](https://zhuanlan.zhihu.com/p/34879333)
- [杨明雪：谈谈神经网络权重为什么不能初始化为0](https://zhuanlan.zhihu.com/p/75879624)
- [李rumor：BERT模型蒸馏完全指南（原理/技巧/代码）](https://zhuanlan.zhihu.com/p/273378905)