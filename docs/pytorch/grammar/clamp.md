
# [clamp]限制取值范围

[torch.clamp](https://pytorch.org/docs/stable/torch.html#torch.clamp)和`numpy.clip`作用一致，用于限制数组取值范围

## 定义

>torch.clamp(input, min, max, out=None) → Tensor

$$
y_{i}=\left\{\begin{matrix}
min & if x_{i}<min\\ 
x_{i} & if min \leq x_{i} \leq max\\ 
max & if x_{i} > max
\end{matrix}\right.
$$

如果要作用于`input`，则使用`torch.clamp_`

## 示例

```
>>> import torch
>>> a = torch.arange(12).reshape(3,4)
>>> a
tensor([[ 0,  1,  2,  3],
        [ 4,  5,  6,  7],
        [ 8,  9, 10, 11]])
>>> 
>>> torch.clamp(a, 3, 5)
tensor([[3, 3, 3, 3],
        [4, 5, 5, 5],
        [5, 5, 5, 5]])
```

## 相关阅读

* [[numpy][clip]限制取值范围](../python/[numpy][clip]限制取值范围.md)