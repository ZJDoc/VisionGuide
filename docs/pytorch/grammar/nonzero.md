
# [nonzero]非零元素下标

[torch.nonzero](https://pytorch.org/docs/stable/torch.html?highlight=nonzero#torch.nonzero)能够返回张量中所有非零元素下标

## 定义

```
torch.nonzero(input, *, out=None, as_tuple=False) → LongTensor or tuple of LongTensors
```

返回一个`2`维张量，每一行表示一个元素的下标

## 测试

```
>>> import torch
>>> a = torch.tensor([1, 1, 1, 0, 1])
>>> torch.nonzero(a)
tensor([[0],
        [1],
        [2],
        [4]])
>>> torch.nonzero(a).shape
torch.Size([4, 1])
```