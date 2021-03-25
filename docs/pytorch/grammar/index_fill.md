
# [index_fill]在给定维度填充指定val

`PyTorch`提供了函数[index_fill_](https://pytorch.org/docs/stable/tensors.html?highlight=index_fill_#torch.Tensor.index_fill_)用于在张量的指定维度上填充指定`val`

## 定义

>index_fill_(dim, index, val) → Tensor

* `dim`：给定维度。`0`表示行，`1`表示列
* `index`：`LongTensor`。给定维度下的指定下标
* `val`：待填充值

## 示例

对于大小为$3\times 4$的张量

```
>>> import torch
>>> a = torch.arange(12, dtype=torch.float).reshape(3, 4)
>>> a
tensor([[ 0.,  1.,  2.,  3.],
        [ 4.,  5.,  6.,  7.],
        [ 8.,  9., 10., 11.]])
```

填充第`1/3`行，大小为`33`

```
>>> index=torch.LongTensor([0, 2])
>>> index
tensor([0, 2])
>>> a.index_fill(0, index, 33)
tensor([[33., 33., 33., 33.],
        [ 4.,  5.,  6.,  7.],
        [33., 33., 33., 33.]])
```

填充第`2/3`列，大小为`-1`

```
>>> index=torch.LongTensor([1,2])
>>> index
tensor([1, 2])
>>> a.index_fill(1, index, -1)
tensor([[ 0., -1., -1.,  3.],
        [ 4., -1., -1.,  7.],
        [ 8., -1., -1., 11.]])
```