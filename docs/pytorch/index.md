
# 引言

之前操作过`torch`，是一个`lua`编写的深度学习训练框架，后来`facebook`发布了`pytorch`，使用`python`语言进行开发

[pytorch](https://pytorch.org/)是在`torch`的基础上发展而来的，它继承了许多内容，包括各种包的命名和类的定义，比如张量(`tensor`)


## 目标

* 替代`Numpy`进行`GPU`运算
* 提供最大灵活性和速度的深度学习平台

## 安装

参考：[Start Locally](https://pytorch.org/get-started/locally/)

指定版本/操作系统/安装方式/`python`语言/`cuda`版本

当前配置:

* `PyTorch Stable(1.0)`
* `Ubuntu 16.04`
* `Anacodna3 `
* `Python 3.6`
* `CUDA 10.0`

安装命令如下:

    $ conda install pytorch torchvision cudatoolkit=9.0 -c pytorch

## 加载`torch`

命令行方式

    $ python
    Python 3.6.8 |Anaconda, Inc.| (default, Dec 30 2018, 01:22:34) 
    [GCC 7.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import torch
    >>> torch.__version__
    '1.0.1.post2'
    >>> 

文件方式

    from __future__ import print_function
    import torch