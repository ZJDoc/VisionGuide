
# one-hot编码

利用`MSELoss`训练的时候需要将`1-D`标签数组进行`one-hot`编码，实现了好几个方式，小结一下

## 什么是one-hot编码

>One-Hot编码，又称为一位有效编码，主要是采用N位状态寄存器来对N个状态进行编码，每个状态都有它独立的寄存器位，并且在任何时候只有一位有效。
>
>One-Hot编码是分类变量作为二进制向量的表示。这首先要求将分类值映射到整数值。然后，每个整数值被表示为二进制向量，除了整数的索引之外，它都是零值，它被标记为1。

## sklearn实现

```
from sklearn.preprocessing import LabelBinarizer
import numpy as np

labels = np.arange(10)
np.random.shuffle(labels)
print(labels)
encoder = LabelBinarizer()
classes_onehot = encoder.fit_transform(labels)
print(classes_onehot)
# 输出
[6 8 2 7 9 5 4 3 0 1]
[[0 0 0 0 0 0 1 0 0 0]
 [0 0 0 0 0 0 0 0 1 0]
 [0 0 1 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 1 0 0]
 [0 0 0 0 0 0 0 0 0 1]
 [0 0 0 0 0 1 0 0 0 0]
 [0 0 0 0 1 0 0 0 0 0]
 [0 0 0 1 0 0 0 0 0 0]
 [1 0 0 0 0 0 0 0 0 0]
 [0 1 0 0 0 0 0 0 0 0]]
```

## pytorch实现

`pytorch`有多种实现方式

### 方式一

使用函数[torch.scatter](https://pytorch.org/docs/master/tensors.html#torch.Tensor.scatter_)

```
import numpy as np
import torch

num_classes = 10
num_images = 4
labels = np.arange(num_images)
np.random.shuffle(labels)
labels = torch.from_numpy(labels)
print(labels)
one_hot = torch.zeros(num_images, num_classes).scatter_(1, labels.unsqueeze(1), 1)
print(one_hot)
# 输出
tensor([2, 1, 0, 3])
tensor([[0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
        [0., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
        [1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 1., 0., 0., 0., 0., 0., 0.]])
```

### 方式二

`pytorch`内置了函数实现[torch.nn.functional.one_hot](https://pytorch.org/docs/master/nn.functional.html#torch.nn.functional.one_hot)

```
import numpy as np
import torch

num_classes = 10
num_images = 4
labels = np.arange(num_images)
np.random.shuffle(labels)
labels = torch.from_numpy(labels)
print(labels)
one_hot = torch.nn.functional.one_hot(labels, num_classes=num_classes)
print(one_hot)
# 输出
tensor([2, 1, 0, 3])
tensor([[0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]])
```

## 相关阅读

* [详解one-hot编码](https://www.cnblogs.com/shuaishuaidefeizhu/p/11269257.html)
* [PyTorch——Tensor_把索引标签转换成one-hot标签表示](https://blog.csdn.net/victoriaw/article/details/72874637)
* [[pytorch]如何将label转化成onehot编码](https://www.jianshu.com/p/4b14d440540f)
* [Pytorch doesn't support one-hot vector?](https://stackoverflow.com/questions/55549843/pytorch-doesnt-support-one-hot-vector)
