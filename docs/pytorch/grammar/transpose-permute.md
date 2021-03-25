
# [transpose][permute]维度转换

`PyTorch`提供了两个函数用于维度转换

* [transpose](https://pytorch.org/docs/stable/torch.html#torch.transpose)
* [permute](https://pytorch.org/docs/stable/tensors.html?highlight=permute#torch.Tensor.permute)

## transpose

>torch.transpose(input, dim0, dim1) → Tensor

函数`transpose`每次仅能调整两个维度

```
>>> import torch
>>> a = torch.arange(24).reshape(2, 3, 4)
>>> a.shape
torch.Size([2, 3, 4])
# 切换第1维和第2维
>>> torch.transpose(a, 1, 2).shape
torch.Size([2, 4, 3])
# 切换第0维和第2维
>>> torch.transpose(a, 2, 0).shape
torch.Size([4, 3, 2])
```

## permute

>permute(*dims) → Tensor

使用`permute`能够一次性调整多个维度

```
>>> import torch
>>> a = torch.arange(24).reshape(2, 3, 4)
>>> a.shape
torch.Size([2, 3, 4])
>>> a.permute(2, 0, 1).shape
torch.Size([4, 2, 3])
```