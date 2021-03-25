
# [benchmark]训练加速

阅读工程源码时发现了一种加速训练的方法：

```
if torch.cuda.is_available():
        # This flag allows you to enable the inbuilt cudnn auto-tuner to
        # find the best algorithm to use for your hardware.
        torch.backends.cudnn.benchmark = True
```

## 原理

因为存在多种卷积实现算法，所以设置`true`将会启动内置`cudnn auto-tuner`，帮助寻找最优的计算算法，从而实现加速目的。其前提条件是每次输入的尺寸固定，如果不固定，那么找到的加速算法不一定适合不同大小的输入计算，不会得到加速效果

## 测试

参考：[torch.backends.cudnn.benchmark ?!](https://zhuanlan.zhihu.com/p/73711222)

## 相关阅读

* [What does torch.backends.cudnn.benchmark do?](https://discuss.pytorch.org/t/what-does-torch-backends-cudnn-benchmark-do/5936)

* [Can you use torch.backends.cudnn.benchmark = True after resizing images?](https://discuss.pytorch.org/t/can-you-use-torch-backends-cudnn-benchmark-true-after-resizing-images/40659)
