
# 调整张量打印位数

## 引言

打印`Python Pytorch`结果，其输出总是保持`4`位有效小数

```
>>> import torch
>>> a = torch.randn(3)
>>> a
tensor([0.7620, 0.4472, 0.5827])
>>> import numpy as np
>>> b = np.random.randn(3)
>>> b
array([-0.35009024, -0.02696787, -0.89501692])
>>> c = torch.from_numpy(b)
>>> c
tensor([-0.3501, -0.0270, -0.8950], dtype=torch.float64)
```

## 设置

`Pytorch`默认输出`4`位有效小数，也可以设置输出更多位数。

```
>>> torch.set_printoptions(precision=8)
>>> 
>>> c
tensor([-0.35009024, -0.02696787, -0.89501692], dtype=torch.float64)
```

*默认情况下张量数据类型为浮点型（`torch.float32`），也就是`32`位有效数字（后续数字就不准确率）*

## 相关阅读

* [为什么Pytorch中的Tensor只有四位小数呢？](https://www.zhihu.com/question/305576603)
* [Pytorch中tensor的打印精度](https://blog.csdn.net/wangpeng246300/article/details/111355945)