## Parameter-level



Huggingface's efficient training guide discusses a number of parameters and their effect on training efficiency.


- **Batch Size Choice**. Batch size refers to the number of data points to be input into a model concurrently during the training phase. Increasing the batch size will possibly result in an increase in the data parallelism and thus affect the training efficiency, but the maximum batch size is also limited by the memory (specifically RAM size) of the GPU.
- **Gradient Accumulation**. Gradient accumulation refers to a method that aims to calculate gradients in smaller increments instead of for the entire batch at once. It involves iteratively calculating gradients in smaller batches by performing forward and backward passes through the model and accumulating the gradients during the process. The gradient accumulation method increases the memory usage efficiency by increasing the effective batch size.
- **Gradient Checkpointing**. Traditionally, some data such as the activation from the forward pass is stored in the GPU memory in order to be reused in the backward pass, which can consume a great amount of memory for large models. The gradient checkpointing technique allows the model to save the activations as checkpoints in outer memories at lower memory hierarchies, which saves the GPU memory and thus may allow larger batch sizes.
- **Mixed Precision Training**. The data precision directly affects the model size -- if all the parameters of a model is degraded from \verb|fp32| to \verb|fp16|, the space it takes will be reduced to half. Meanwhile, certain models usually have specific parameters whose precision is not allowed to be reduced to protect the model's performance. Thus, the mixed precision training technique aims to optimize the computational efficiency of training models by utilizing lower-precision numerical formats for certain variables.
- **torch empty cache steps**. A parameter `torch_empty_cache_step` is allowed to be set to the model training procedure to clear the unused cache. This technique helps avoid CUDA out-of-memory errors by lowering peak VRAM usage at a cost of around 10\% slower performance (See https://github.com/huggingface/transformers/issues/31372).
- **Optimizer Choice**. An optimizer is a crucial element in model training and fine-tuning, changing the parameters to minimize the models' losses and enhance their performance. The algorithms that the optimizers adopt are designed to adjust the attributes of the neural network, including the weights and learning rates. Thus, they help reduce the overall loss and improve accuracy. The commonly used optimizers are stochastic gradient descent (SGD) and the Adam family, including RMSprop, Adam, AdamW, AdamGrad, etc.
- **Data Preloading**. The data reading and writing speed between the outer memory and the GPU is usually times slower than the GPU processing speed, thus being the bottleneck of the training speed. The data preloading technique, by allowing loading data to the memory, before the training starts, ensures the GPU is at full speed all the time.
- **DeepSpeed ZeRO**. DeepSpeed ZeRO is an easy-to-use and open-source deep learning optimization library providing a wide range of features and optimizations. It is designed to improve the efficiency and scalability of large-scale deep-learning training.
- **Using torch.compile**. The `torch.compile()` is a feature introduced by Pytorch 2.0 that automatically builds a computation graph for the model and optimizes the computing orders. It optimizes the training efficiency.
- **Parameter-Efficient Fine-Tuning (PEFT)**. For larger models that require two phases -- pre-training and fine-tuning, the fine-tuning phase typically recalculates all the model parameters which requires a significant amount of computation. The parameter-efficient fine-tuning technique (PEFT) allows the majority of model parameters to be frozen and a small portion to be trained, notably reducing the memory cost. Experiments have proved that the model performance remains stable with and without the PEFT. LoRA, QLoRA, and DoRA are several commonly adopted PEFT techniques.

Relevant table:

| Method/tool                       | Improves training speed? | Optimizes memory utilization? |
| --------------------------------- | ------------------------ | ----------------------------- |
| Batch size choice                 | True                     | True                          |
| Gradient accumulation             | False                    | True                          |
| Gradient checkpointing            | False                    | True                          |
| Mixed precision training          | True                     | Maybe                         |
| Torch empty cache steps           | False                    | True                          |
| Optimizer choice                  | True                     | True                          |
| Data preloading                   | True                     | False                         |
| DeepSpeed Zero                    | False                    | True                          |
| torch.compile                     | True                     | False                         |
| Parameter-efficient Tuning (PEFT) | False                    | True                          |
