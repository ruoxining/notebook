## nn.ModuleList and nn.Sequential
TLDR:
`nn.ModuleList` is a list which is indexable and without extra functions, while `nn.Sequential` is a workflow with order and ability to call the forward functions automatically.

Please refer to more details from [PyTorch 中的 ModuleList 和 Sequential: 区别和使用场景 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/64990232). 

## Forward function in Pytorch
In training models with Pytorch, there is no need to explicitly call the forward function. The way to call the forward function is as follows.
```Python
 class Module(nn.Module):
    def __init__(self):
        super().__init__()
        # ...
    def forward(self, x):
        # ...
        return x
data = data
model = Module()
model(data)
```
instead of `model.forward(data)`.
This is because `model(data)` equals `mode.forward(data)` itself.
In class `nn.Module`, the function `__call__` has been overloaded as
```Python
def __call__(self, data):
	return self.forward(data)
```

## \*是element wise @和matmul是矩阵相乘 dot是点乘

```Python
import torch

tensor1 = torch.tensor([1, 2, 3])
tensor2 = torch.tensor([4, 5, 6])

result = tensor1 * tensor2

print(result)  # Output: tensor([4, 10, 18])
```

```Python
import torch

tensor1 = torch.tensor([[1, 2], [3, 4]])
tensor2 = torch.tensor([[5, 6], [7, 8]])

result = tensor1 @ tensor2

print(result)  # Output: tensor([[19, 22], [43, 50]])
```

```Python
import torch

tensor1 = torch.tensor([1, 2, 3])
tensor2 = torch.tensor([4, 5, 6])

result = torch.dot(tensor1, tensor2)

print(result)  # Output: tensor(32)
```

```Python
import torch

tensor1 = torch.tensor([1, 2, 3])
tensor2 = torch.tensor([4, 5, 6])

result = torch.dot(tensor1, tensor2)

print(result)  # Output: tensor(32)
```

## To train the model with GPU

```Python
import torch

# Step 1: Check for GPU availability
if torch.cuda.is_available():
    device = torch.device('cuda')
else:
    device = torch.device('cpu')

# Step 2: Move the model and data to the GPU
model = YourModel().to(device)
data = YourData().to(device)

# Step 3: Update the computation on the GPU
model.to(device)
data = data.to(device)

# Step 4: Perform training and inference
for epoch in range(num_epochs):
    # Training loop
    for batch in data_loader:
        inputs, labels = batch
        inputs = inputs.to(device)
        labels = labels.to(device)

        # Perform forward and backward pass, update model parameters

    # Inference
    with torch.no_grad():
        for batch in validation_data_loader:
            inputs, labels = batch
            inputs = inputs.to(device)
            labels = labels.to(device)

            # Perform forward pass for evaluation
```