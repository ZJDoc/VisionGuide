
# [sampler]采样器

学习`torchvision`提供的采样器操作，首先介绍常用的几种采样器，然后介绍采样器的使用

## 源码

源码地址：[pytorch/torch/utils/data/sampler.py ](https://github.com/pytorch/pytorch/blob/0bde610c14b92d351b968a0228df29e92442b1cc/torch/utils/data/sampler.py#L160)

## 采样器

### Sampler

[torch.utils.data.Sampler](https://pytorch.org/docs/master/data.html#torch.utils.data.Sampler)是采样器基类

```
class Sampler(object):
    def __init__(self, data_source):
        pass

    def __iter__(self):
        raise NotImplementedError
```

所有采样器必须实现迭代器函数：返回一个迭代器，输出数据集下标

### SequentialSampler

[torch.utils.data.SequentialSampler](https://pytorch.org/docs/master/data.html#torch.utils.data.SequentialSampler)按顺序返回数据集元素下标

```
class SequentialSampler(Sampler):
    r"""Samples elements sequentially, always in the same order.

    Arguments:
        data_source (Dataset): dataset to sample from
    """

    def __init__(self, data_source):
        self.data_source = data_source

    def __iter__(self):
        return iter(range(len(self.data_source)))

    def __len__(self):
        return len(self.data_source)
```

### RandomSampler

[torch.utils.data.RandomSampler](https://pytorch.org/docs/master/data.html#torch.utils.data.RandomSampler)提供一个打乱的元素下标顺序

### WeightedRandomSampler

[torch.utils.data.WeightedRandomSampler](https://pytorch.org/docs/master/data.html#torch.utils.data.WeightedRandomSampler)对数据集进行加权随机采样，通过对所有元素下标添加指定的权重，增强高权重元素的采样顺序

## 使用

通常将采样器与`DataLoader`结合使用

### 自定义数据类

自定义一个数据集类，其元素为数字`1-50`，假定前`40`个是负样本，后`10`个是正样本

```
from torch.utils.data import Dataset

class CustomDataSet(Dataset):
    def __init__(self):
        """
        2类数据集，前40个元素是负样本，后10个元素是正样本
        """
        self.data = list(range(50))

    def __getitem__(self, index: int):
        return self.data[index], int(index > 40)

    def __len__(self) -> int:
        return len(self.data)
```

### 顺序采样

```
from torch.utils.data import DataLoader
from torch.utils.data import SequentialSampler

data_set = CustomDataSet()

sampler = SequentialSampler(data_set)
data_loader = DataLoader(data_set, batch_size=10, sampler=sampler, shuffle=False, num_workers=8)
print('epochs: %d' % (len(data_loader)))
for item in data_loader:
    inputs, targets = item
    print(inputs)
```

输出如下：

```
epochs: 5
tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
tensor([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
tensor([20, 21, 22, 23, 24, 25, 26, 27, 28, 29])
tensor([30, 31, 32, 33, 34, 35, 36, 37, 38, 39])
tensor([40, 41, 42, 43, 44, 45, 46, 47, 48, 49])
```

顺序采样输出按照原先数据集排序输出。**`DataLoader`内部已集成了`SequentialSampler`，不设置任何`sampler`，同时设置`shuffle=False`(默认)即可**

```
class DataLoader(object):
    ...
    ...
        if sampler is None:  # give default samplers
            if self._dataset_kind == _DatasetKind.Iterable:
                # See NOTE [ Custom Samplers and IterableDataset ]
                sampler = _InfiniteConstantSampler()
            else:  # map-style
                if shuffle:
                    sampler = RandomSampler(dataset)
                else:
                    sampler = SequentialSampler(dataset)
```

### 随机采样

随机采样器的使用方式和顺序采样器一样，自定义`RandomSampler`

```
from torch.utils.data import DataLoader
from torch.utils.data import RandomSampler

data_set = CustomDataSet()

sampler = RandomSampler(data_set)
data_loader = DataLoader(data_set, batch_size=10, sampler=sampler, shuffle=False, num_workers=8)
print('epochs: %d' % (len(data_loader)))
for item in data_loader:
    inputs, targets = item
    print(inputs)
```

输出如下：

```
epochs: 5
tensor([25, 37, 35, 11, 34, 27, 45,  9,  6, 31])
tensor([21, 19, 32, 40, 30, 48, 16, 28, 38,  8])
tensor([41,  2, 13, 14, 36, 20, 18, 44, 46, 33])
tensor([ 1, 26, 12, 10,  4, 39,  3, 49, 29,  5])
tensor([24, 43,  7, 47,  0, 23, 15, 17, 22, 42])
```

同样的，设置`DataLoader`属性`shuffle`为`True`即可实现随机采样功能

### 加权随机采样

使用加权随机采样器可以解决**类别数目不平衡**问题

#### 定义

[torch.utils.data.WeightedRandomSampler](https://pytorch.org/docs/master/data.html#torch.utils.data.WeightedRandomSampler)的定义如下：

```
class WeightedRandomSampler(Sampler):
    r"""Samples elements from ``[0,..,len(weights)-1]`` with given probabilities (weights).

    Args:
        weights (sequence)   : a sequence of weights, not necessary summing up to one
        num_samples (int): number of samples to draw
        replacement (bool): if ``True``, samples are drawn with replacement.
            If not, they are drawn without replacement, which means that when a
            sample index is drawn for a row, it cannot be drawn again for that row.

    Example:
        >>> list(WeightedRandomSampler([0.1, 0.9, 0.4, 0.7, 3.0, 0.6], 5, replacement=True))
        [0, 0, 0, 1, 0]
        >>> list(WeightedRandomSampler([0.9, 0.4, 0.05, 0.2, 0.3, 0.1], 5, replacement=False))
        [0, 1, 4, 3, 2]
    """

    def __init__(self, weights, num_samples, replacement=True):
        if not isinstance(num_samples, _int_classes) or isinstance(num_samples, bool) or \
                num_samples <= 0:
            raise ValueError("num_samples should be a positive integer "
                             "value, but got num_samples={}".format(num_samples))
        if not isinstance(replacement, bool):
            raise ValueError("replacement should be a boolean value, but got "
                             "replacement={}".format(replacement))
        self.weights = torch.as_tensor(weights, dtype=torch.double)
        self.num_samples = num_samples
        self.replacement = replacement

    def __iter__(self):
        return iter(torch.multinomial(self.weights, self.num_samples, self.replacement).tolist())

    def __len__(self):
        return self.num_samples
```

其迭代器使用了函数[torch.multinomial](https://pytorch.org/docs/master/torch.html?highlight=torch%20multinomial#torch.multinomial)，定义如下

```
torch.multinomial(input, num_samples, replacement=False, *, generator=None, out=None)
```

* `input`：权重张量
* `num_samples`：采样个数
* `replacement`：默认为`False`，表示是否可以重复采样

对于不同格式的输入`input`

* 如果输入`input`是张量，那么输出`out`大小为`num_samples`
* 如果输入`input`是`m`行矩阵，那么输出`out`同样是矩阵，大小为`(m, num_samples)`
* 如果`replacement`为`True`，那么同一行中可以重复采样

#### 示例

自定义数据集中正负样本比为`1:4`，为了让批量数据中的正负样本比达到`1:1`，需要提高正样本权重

$$
\frac {N_{positive}}{N_{negative}} * \frac {W_{positive}}{W_{negative}(=1)} = \frac {1}{1}
==>
W_{positive} = 4
$$

```
from torch.utils.data import DataLoader
from torch.utils.data import WeightedRandomSampler

data_set = CustomDataSet()

batch_size = 10
weights = torch.cat((torch.ones(40), torch.ones(10) * 4), 0)
sampler = WeightedRandomSampler(weights, batch_size, replacement=False)

data_loader = DataLoader(data_set, batch_size=batch_size, sampler=sampler, shuffle=False, num_workers=8)
print('epochs: %d' % (len(data_loader)))
for item in data_loader:
    inputs, targets = item
    print(inputs)
    print(targets)
```

输出结果如下：

```
epochs: 1
tensor([41, 48,  2,  5, 15, 20, 43, 44, 40, 26])
tensor([1, 1, 0, 0, 0, 0, 1, 1, 0, 0])
tensor(4)
```

当前设置采样器采样个数为单次批量大小，加载数据后发现确实能够提高正样本的采样比例。为了保持多次采样结果均实现正负样本比`1:1`，其程序修改如下：

```
if __name__ == '__main__':
    data_set = CustomDataSet()

    batch_size = 10
    weights = torch.cat((torch.ones(40), torch.ones(10) * 4), 0)
    sampler = WeightedRandomSampler(weights, batch_size, replacement=False)

    data_loader = DataLoader(data_set, batch_size=10, sampler=sampler, shuffle=False, num_workers=8)
    for i in range(5):
        print('#' * 10)
        for item in data_loader:
            inputs, targets = item
            print(inputs)
            print(targets)
```

输出如下：

```
##########
tensor([43,  1, 42, 32, 13, 22,  2, 40, 48, 10])
tensor([1, 0, 1, 0, 0, 0, 0, 0, 1, 0])
##########
tensor([12, 30, 41, 35, 42, 38, 49, 19, 27, 15])
tensor([0, 0, 1, 0, 1, 0, 1, 0, 0, 0])
##########
tensor([45, 39, 23, 16, 43, 47, 27, 31, 49, 21])
tensor([1, 0, 0, 0, 1, 1, 0, 0, 1, 0])
##########
tensor([33, 40, 44, 45, 36, 23, 10,  5, 15, 16])
tensor([0, 0, 1, 1, 0, 0, 0, 0, 0, 0])
##########
tensor([46, 35,  0, 44, 15,  5, 41, 26, 47, 40])
tensor([1, 0, 0, 1, 0, 0, 1, 0, 1, 0])
```