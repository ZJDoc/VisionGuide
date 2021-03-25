
# [Conv][Pool]实现原理

## 实现

`PyTorch`关于卷积层和池化层的实现参考：

* [Conv2d](https://pytorch.org/docs/master/nn.html#conv2d)
* [MaxPool2d](https://pytorch.org/docs/master/nn.html#maxpool2d)

## 原理

之前一直觉得卷积层和池化层的计算如下所示：

$$
n_{out} = (n_{in}−F+2P)/S+1 (卷积层)\\
n_{out} = (n_{in}−F)/S+1 (池化层)
$$

* $n_{out}$表示输出维度的特征数
* $n_{in}$表示输入维度的特征数
* $F$表示卷积核大小
* $P$表示零填充大小
* $S$表示步长

最近发现`PyTorch`并没有严格按照上述公式实现，其实现参考[A guide to convolution arithmetic for deeplearnin](https://arxiv.org/pdf/1603.07285.pdf)中$2.4$节以及第$3$节所示

$$
n_{out} = \left \lfloor  \frac {n_{in} + 2p - k}{s} \right \rfloor + 1 (卷积层) 
$$

$$
n_{out} = \left \lfloor  \frac {n_{in} - k}{s} \right \rfloor + 1 (池化层)
$$

使用了一个向下取整（`floor`）计算，所以在`PyTorch`实现中，不同输入大小（比如`224`和`227`）能够得到相同大小的输出