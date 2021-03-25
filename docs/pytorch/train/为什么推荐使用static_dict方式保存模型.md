
# 为什么推荐使用static_dict方式保存模型

在官网教程[[译]保存和加载模型](./[译]保存和加载模型.md)中给出了多种模型使用方式，其中最常用的有

1. 保存/加载`static_dict`
2. 保存/加载完整模型

对于第一种方式，只保存训练好的模型的学习参数，但是加载时需要额外提供定义的模型结构；对于第二种方式，直接使用`PyTorch`的保存和加载函数即可，不过教程中也提到了第二种方式的缺陷，就是需要在调用时维护模型类文件的路径，否则会出错

之前一直使用第一种方式进行模型的读写，直到遇到了下面这个问题，才真正理解了第二种方式的缺陷

## ModuleNotFoundError: No module named 'models'

使用[ultralytics/yolov5](https://github.com/ultralytics/yolov5)的时候出现了如上错误。在网上查找了资料后发现这就是保存/加载完整模型带来的问题。参考

* [torch.load() requires model module in the same folder #3678](https://github.com/pytorch/pytorch/issues/3678)
* [ModuleNotFoundError: No module named 'models' #18325](https://github.com/pytorch/pytorch/issues/18325)
* [Pytorch.load() error:No module named ‘model’](https://discuss.pytorch.org/t/pytorch-load-error-no-module-named-model/25821)

## 解析

`PyTorch`集成了`Pickle`工具进行模型的保存和加载。如果直接保存完整模型，那么附带的需要在调用时维持和模型定义文件的相对位置，否则会出现错误

## 解决

解决方式就是维护调用文件和模型定义文件之间的相对位置，保证`Pickle`能够找到模型定义文件

1. 使用`sys.path`设置

```
import sys
sys.path.insert(0, './yolov5')
```

2. 设置`PYTHONPATH`环境变量

## 相关

在[ultralytics/yolov5](https://github.com/ultralytics/yolov5)提了一个问题

* [ModuleNotFoundError: No module named 'models' #353](https://github.com/ultralytics/yolov5/issues/353)