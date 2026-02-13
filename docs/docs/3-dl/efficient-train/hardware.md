# Hardware 

## GPU

A graphic processing unit (GPU) is an electronic circuit designed for accelerating computer graphics. It is now widely adopted for non-graphic calculations such as the training of neural networks. 

GPU Parameters that are most cared about 

- **Memory** refers to the total amount of RAM available on a GPU. Since deep learning tasks require a significant amount of GPU, it determines the capacity for storing and accessing data required for processing tasks, impacting the efficiency and capability of the GPU to handle large datasets. 

- **Theoretical Performance** indicates the potential computational power of a GPU, typically measured in FLOPS (floating-point operations per second): $FLOPS = cores \times (boost) clock speed \times FMA $, where FMA stands for the fused multiply-add operations. This metric helps gauge the GPU's ability to perform complex calculations and handle intensive workloads. 

- **Memory Speed/Bandwidth** measures the rate at which data can be transferred between the GPU and its memory. Higher bandwidth allows for quicker data access and processing, enhancing overall GPU performance.

- **NVLink** is a high-speed communication interface that connects multiple GPUs. It enables faster data transfer and synchronization between GPUs, improving the efficiency of parallel processing and multi-GPU setups. 

- **Clock Speed** refers to the frequency at which a GPU's cores operate, typically measured in megahertz (MHz) or gigahertz (GHz). Higher clock speeds can lead to faster processing and improved performance for graphics and computing tasks.
    
- **Tensor Cores** are specialized processing units within a GPU designed to accelerate machine learning and AI workloads. They enable efficient handling of tensor operations, which are critical for deep learning applications.
    
- **Slot Width** describes the physical space a GPU occupies on a motherboard, usually measured in terms of the number of expansion slots it covers. Wider GPUs may offer enhanced cooling and performance but require more space inside the computer case.
    
- **Power (TDP)** stands for Thermal Design Power and represents the maximum amount of heat a GPU is expected to generate under typical workloads. It is measured in watts (W) and indicates the power consumption and cooling requirements of the GPU.


In a table:

| GPU      | GPU Memory | Memory Bandwidth | NVLINK  | CUDA Cores | Turning Tensor cores | RT cores |
| -------- | ---------- | ---------------- | ------- | ---------- | -------------------- | -------- |
| T4       | 16GB       | 320GB/s          | No      | 2,560      | 320                  | 40       |
| A40      | **48GB**   | 696GB/s          | **Yes** | 10,752     | 336                  | 84       |
| RTX 6000 | **48GB**   | **960GB/s**      | No      | **18,176** | **568**              | **142**  |



## A Taxonomy of Parallelism


### Data Parallelism 


Data Parallelism replicates the model across multiple GPUs, usually with two specific techniques: (1) fully shared data parallelism (FSDP), and (2) distributed data parallelism (DDP). 

We denote the training dataset as $D$, the shared model parameters as $W$, the model's operation on the dataset as $f(D_i, W)$, the $i$th processor as $p_i$, the number of processors as $P$, the $i$th machine which may be mapped to multiple processors as $m_i$, and the number of machines as $M$. 
In FSDP, the dataset $D$, ignoring its original division of batches, is further divided into $P$ smaller batches $D = {D_1, D_2, ..., D_P}$. Each processor $p_i$ performs a $f(D_i, W)$ on its small batch. 
Meanwhile, DDP extends the data parallelism technique across multiple machines. The dataset $D$ is first divided into $M$ subsets $D = {D_1, D_2, ..., D_M}$ for each machine, and each subset on $m_i$ is further divided into $P_i$ subsets according to the number of processors on each machine. After each processor performs the processing $f(D_{i,j}, W_k)$, synchronization will be taken across all machines to aggregate and update the model weights $W_k \leftarrow Aggregate(W_1, W_2, ..., W_M)$.

While the computation workload is efficiently distributed across GPUs, inter-GPU communication is required to keep the model replicas consistent between training steps. 

### Model Parallelism

Model parallelism is a distributed model deployment method that partitions the model parameters across GPUs to reduce the need for per-GPU memory. Common techniques of model parallelism include (1) tensor parallelism, (2) pipeline parallelism, and (3) expert parallelism. 

We denote the input data tensor as $W$, the model parameters as $W$, the function representing the model's operations as $f(X, W)$, and the $i$th processor as $p_i$, the number of processors as $P$.

Tensor Parallelism distributes the parameter tensor of an individual layer across GPUs. The model weights are divided along specific dimensions into $W = {W_1, W_2, ..., W_P}$, and thus each processor $p_i$ processes part of the model weights $f(X, W_i)$.

Pipeline Parallelism involves partitioning the computation graph of a model into several stages and assigning each stage to a different processor or machine, making it an analogy to the CPU's pipelining technique. The input tensor $X$ sequentially passes through each processor in each time step until the processing steps finish. This allows for overlapping execution of different stages, increasing the throughput. 

Expert Parallelism, also known as Mixture of Experts (MoE), involves dynamically selecting a subset of model parameters, to reach the original performance using the entire model. Additionally, MoE models require a gating network $g(X)$ to select the expert to output, which selects a subset of networks from the total $E$ sub-networks, as $ \epsilon =g(X), \epsilon \subseteq E $. Only the selected networks will be involved in the generation of the output $\sum_{k \in \epsilon} f(X, W_k)$. 


### Activition Partitioning

In large language model training, a large memory space is needed to store the input activation of the network layers. The activation partitioning techniques, which involves efficiently distributing the activations to ensure GPU usage, is another crucial technique for efficient training. Commonly used activation partitioning techniques involve (1) sequence parallelism and (2) context parallelism. We denote the input sequence as $X$, the context of this training, including the batches and environments, as $C$, the processing function as $f(X, C, W)$, and $P$ the number of processors.

Sequence Parallelism suggests that partitions are made by distributing computing load and activation memory across multiple GPUs along the sequence dimension of transformer layers. The input sequence $X$ is divided into sub-sequences $X = [X_1, X_2, ..., X_P]$. Each sub-sequence is sent into a processor with inner tensor forwarding techniques from the previous sub-sequence, denoted as $f(X_i, C, W_{i-1})$.

Context Parallelism distributes different contexts, usually including batches and environments, across multiple processors. It is useful in multi-task learning and reinforcement learning scenarios. The context $C$ is divided among processors $C = [C_1, C_2, ..., C_P]$,  and each processor processes the context with the entire input sequence, denoted as $f(X, C_i, W_i)$.



## Multi-GPU Training 

TODO

Reference: [🤗 Efficient Training on Multiple GPUs](https://huggingface.co/docs/transformers/en/perf_train_gpu_many){target="_blank"}
