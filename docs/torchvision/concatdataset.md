
# [torchvision][ConcatDataset]连接多个数据集

`PyTorch`提供了类[torch.utils.data.ConcatDataset](https://pytorch.org/docs/stable/data.html#torch.utils.data.ConcatDataset)，能够连接多个不同的数据集

## 定义

>CLASS torch.utils.data.ConcatDataset(datasets)

* `datasets`：是一个列表，保存了多个数据集对象

## 示例

连接`MNIST`和`CIFAR100`

```
from torchvision.datasets import MNIST
from torchvision.datasets import CIFAR100
from torch.utils.data import ConcatDataset

import numpy as np

if __name__ == "__main__":
    mnist_data = MNIST('./data', train=True, download=True)
    print('mnist: ', len(mnist_data))
    cifar10_data = CIFAR100('./data', train=True, download=True)
    print('cifar: ', len(cifar10_data))

    concat_data = ConcatDataset([mnist_data, cifar10_data])
    print('concat_data: ', len(concat_data))

    img, target = concat_data.__getitem__(133)
    print(np.array(img).shape)
    print(target)
```

输出如下：

```
mnist:  60000
Files already downloaded and verified
cifar:  50000
concat_data:  110000
(28, 28)
9
```