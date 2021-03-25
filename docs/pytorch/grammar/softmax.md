
# [softmax]分类概率计算

模型输出置信度后，使用`softmax`函数计算每类成绩，`pytorch`提供了`softmax`实现

## 解析

可以使用类`nn.Softmax`或者使用函数`nn.functional.softmax`进行分类概率的计算

```
def softmax(input, dim=None, _stacklevel=3, dtype=None):
    # type: (Tensor, Optional[int], int, Optional[int]) -> Tensor
```

* `dim`：计算维度，`0`表示按列计算，`1`表示按行计算

计算公式如下：

$$
\text{Softmax}(x_{i}) = \frac{exp(x_i)}{\sum_j exp(x_j)}
$$

## 示例

```
# -*- coding: utf-8 -*-

"""
@author: zj
@file:   softmax.py
@time:   2020-01-27
"""

import torch
import torch.nn as nn
import torch.nn.functional as F

if __name__ == '__main__':
    inputs = torch.randn((2, 4))
    print('输入：', inputs)

    # 按行计算概率
    # 使用softmax类
    softmax = nn.Softmax(dim=1)
    res = softmax.forward(inputs)
    print('结果：', res)

    # 使用softmax函数
    res2 = F.softmax(inputs, dim=1)
    print('结果：', res)
```

计算结果如下：

```
输入： tensor([[-0.5450,  0.3742,  0.8121,  0.1191],
        [-0.8926,  0.2907, -0.1550,  0.1468]])
结果： tensor([[0.1071, 0.2686, 0.4162, 0.2081],
        [0.1089, 0.3555, 0.2277, 0.3079]])
结果： tensor([[0.1071, 0.2686, 0.4162, 0.2081],
        [0.1089, 0.3555, 0.2277, 0.3079]])
```

## 相关阅读

* [class torch.nn.Softmax(dim=None)](https://pytorch.org/docs/master/nn.html?highlight=softmax#torch.nn.Softmax)
* [torch.nn.functional.softmax(input, dim=None, _stacklevel=3, dtype=None)](https://pytorch.org/docs/master/nn.functional.html#torch.nn.functional.softmax)
* [softmax回归](https://blog.zhujian.life/posts/2626bec3.html)
* [从numpy到pytorch实现softmax回归](https://blog.zhujian.life/posts/1c195604.html)
* [使用softmax回归进行mnist分类](https://blog.zhujian.life/posts/dd673751.html)
* [softmax分类器](https://blog.zhujian.life/posts/e043b7fb.html)
* [[PyTorch][Numpy][Softmax]计算概率](https://blog.zhujian.life/posts/f6b1346b.html)