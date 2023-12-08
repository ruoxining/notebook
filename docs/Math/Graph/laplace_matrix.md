# Laplacian Matrix

## Basic Properties

- can be used to calculate the spanning trees of give graphs
- spectral decomposition allows constructing low dimensional embeddings that appear in many machine learning applications
- easy to define in simple graph
- for undirected graphs, both the adjacency matrix and the Laplacian matrix are symmetric, and col-sum are 0
- 是半正定矩阵
- 特征值中0的个数，是连通子图的个数
- 最小特征值是0，因为拉普拉斯矩阵每一行的和为0
- 最小非0特征值是图的代数连通度

## Definition
![](../asset/Untitled.png)


or L = D(degree matrix) - A(adjacency matrix)

## Normalization

## Eigendecomposition

## 为什么GCN要用到laplace矩阵

- 拉普拉斯矩阵可以谱分解（特征分解）GCN是从谱域的角度提取拓扑图的空间特征的。
- 拉普拉斯矩阵只在中心元素和一阶相邻元素处有非零元素，其他位置皆为0.
- 传统傅里叶变换公式中的基函数是拉普拉斯算子，借助拉普拉斯矩阵，通过类比可以推导出Graph上的傅里叶变换公式。

## Reference

[Laplacian matrix](https://en.wikipedia.org/wiki/Laplacian_matrix)