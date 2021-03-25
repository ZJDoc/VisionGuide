
# [AdaptiveMaxPool][AdaptiveAvgPool]自适应池化层操作

空间金字塔池化操作解放了固定输入的限制，保证了输出固定大小，在`PyTorch`中使用`AdaptiveMaxPool`和`AdaptiveAvgPool`实现

## AdaptiveMaxPool

包含了一维/二维/三维实现

* [AdaptiveMaxPool1d](https://pytorch.org/docs/stable/nn.html#adaptivemaxpool1d)
* [AdaptiveMaxPool2d](https://pytorch.org/docs/stable/nn.html#adaptivemaxpool2d)
* [AdaptiveMaxPool3d](https://pytorch.org/docs/stable/nn.html#adaptivemaxpool3d)

### 一维示例

```
>>> import torch
>>> import torch.nn as nn
>>> 
>>> input = torch.randn(1, 1, 8)
>>> input
tensor([[[ 1.6188, -0.0436,  1.8603,  0.9043,  0.1372,  0.6567, -0.5700,
           0.8480]]])
>>> 
>>> m = nn.AdaptiveMaxPool1d(5)
>>> m
AdaptiveMaxPool1d(output_size=5)
>>> 
>>> output = m(input)
>>> output
tensor([[[1.6188, 1.8603, 0.9043, 0.6567, 0.8480]]])
>>> output.size()
torch.Size([1, 1, 5])
```

在定义`AdaptiveMaxPool1d`对象时确定固定输出大小即可

### 二维示例

二维操作和一维操作一样，设置输出大小即可

```
>>> input = torch.randn((1, 1, 8, 8))
>>> m = nn.AdaptiveMaxPool2d((3, 3))
>>> output = m(input)
>>> output.size()
torch.Size([1, 1, 3, 3])
>>> output
tensor([[[[1.4030, 2.3893, 1.1493],
          [0.8610, 1.9903, 0.9673],
          [1.1998, 1.9903, 1.9642]]]])
```

## AdaptiveAvgPool

参考：[自适应平均池化层](https://blog.zhujian.life/posts/ba337bfa.html)