
# LeNet-5定义

`LeNet-5`模型结构图所下所示：

![](./imgs/mnist.png)

* 输入层`INPUT`：`32x32`大小
* 卷积层`C1`：`6x28x28`大小，卷积核`5x5`
* 池化层`S2`：`6x14x14`大小，滤波器`2x2`
* 卷积层`C3`：`16x10x10`大小，卷积核`5x5`
* 池化层`S4`：`16x5x5`大小，滤波器`2x2`
* 卷积层`C5`：`120`大小，滤波器`5x5`
* 全连接层`F6`：`84`大小
* 输出层`OUTPUT`：`10`大小

## 类定义

```
# -*- coding: utf-8 -*-

import torch
import torch.nn as nn
import torch.nn.functional as F

class LeNet(nn.Module):
    """
    LeNet-5网络模型
    输入图像大小为1x32x32
    """

    def __init__(self):
        super(LeNet, self).__init__()
        # 卷积层
        # 1 input image channel, 6 output channels, 5x5 square convolution
        self.conv1 = nn.Conv2d(1, 6, (5, 5))
        # 池化层
        # Max pooling over a (2, 2) window
        self.pool2 = nn.MaxPool2d(2, 2)
        # If the size is a square you can only specify a single number
        # 如果滤波器是正方形，可以只输入一个数值
        self.conv3 = nn.Conv2d(6, 16, 5)
        # If the size is a square you can only specify a single number
        self.pool4 = nn.MaxPool2d(2)
        # 全连接层
        # an affine operation: y = Wx + b
        self.fc5 = nn.Linear(16 * 5 * 5, 120)
        self.fc6 = nn.Linear(120, 84)
        self.fc7 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool2(F.relu(self.conv1(x)))
        x = self.pool4(F.relu(self.conv3(x)))
        x = x.view(-1, self.num_flat_features(x))
        x = F.relu(self.fc5(x))
        x = F.relu(self.fc6(x))
        x = self.fc7(x)
        return x

    def num_flat_features(self, x):
        size = x.size()[1:]  # all dimensions except the batch dimension
        num_features = 1
        for s in size:
            num_features *= s
        return num_features


if __name__ == '__main__':
    net = LeNet()
    print(net)
```

结果如下：

```
LeNet(
  (conv1): Conv2d(1, 6, kernel_size=(5, 5), stride=(1, 1))
  (pool2): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
  (conv3): Conv2d(6, 16, kernel_size=(5, 5), stride=(1, 1))
  (pool4): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
  (fc5): Linear(in_features=400, out_features=120, bias=True)
  (fc6): Linear(in_features=120, out_features=84, bias=True)
  (fc7): Linear(in_features=84, out_features=10, bias=True)
)
```

## 调用

输入是一个4维向量，分别表示样本数量、通道数、高和宽

$$\left(N, C_{i n}, H_{i n}, W_{i n}\right)$$

输出是一个2维向量，分别表示样本数量和分类结果

$$ 
\left(N, C_{o u t}\right)
 $$

```
if __name__ == '__main__':
    net = LeNet()
    # print(net)
    inp = torch.randn(2, 1, 32, 32)
    print(inp.size())
    out = net.forward(inp)
    print(out)
    print(out.size())

torch.Size([2, 1, 32, 32])
tensor([[ 0.0248, -0.0205,  0.0697,  0.0797,  0.0734, -0.0455, -0.0684, -0.0488,
          0.1245, -0.1140],
        [ 0.0130, -0.0355,  0.0659,  0.0751,  0.0736, -0.0455, -0.0391, -0.0383,
          0.1408, -0.1173]], grad_fn=<AddmmBackward>)
torch.Size([2, 10])
```

## 相关阅读

* [LeNet5实现-numpy](https://blog.zhujian.life/posts/c300ea0f.html)
* [LeNet5实现-pytorch](https://blog.zhujian.life/posts/a2db6d6b.html)
* [[pytorch]训练一个简单的检测器](https://blog.zhujian.life/posts/5bfa4e56.html)