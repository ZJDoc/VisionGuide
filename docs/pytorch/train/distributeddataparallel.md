
# [DistributedDataParallel]分布式训练

## 概述

`PyTorch`官网教程上提供了[分布式训练](https://pytorch.org/tutorials/beginner/dist_overview.html)文档，不过说的不是很清楚。在网上找了另外一个参考：[Distributed data parallel training in Pytorch](https://pytorch.org/tutorials/beginner/dist_overview.html)，里面并没有介绍具体的实现原理，不过给出了清晰的实例。还参考了以下资源：

* [tczhangzhi/pytorch-distributed](https://github.com/tczhangzhi/pytorch-distributed)
* [Getting Started with Distributed Data Parallel](https://pytorch.org/tutorials/intermediate/ddp_tutorial.html#skewed-processing-speeds)
* [[pytorch]单多机下多GPU下分布式负载均衡训练 ](https://www.cnblogs.com/wildkid1024/p/13155377.html)
* [pytorch 分布式计算 你们都遇到过哪些 坑/bug？](https://www.zhihu.com/question/351342218)
* [Writing Distributed Applications with PyTorch](https://pytorch.org/tutorials/intermediate/dist_tuto.html#collective-communication)

示例位于：[ zjykzj/pytorch-distributed ](https://github.com/zjykzj/pytorch-distributed)，完整实现可参考：[ZJCV/ZCls ](https://github.com/ZJCV/ZCls)

## 原理

共有两种类型的分布式训练：

* 模型分布
* 数据分布

`PyTorch`提供了两种类型的实现，不过当前使用的是数据分布实现，`PyTorch`实现了两种方式：

* `DataParallel`
* `DistributedDataParallel`

前者使用单进程模式，虽然实现很简单，但是其将所有`GPU`的运算结果汇集到主`GPU`进行计算，会出现多`GPU`负载不均衡问题；后者对每个`GPU`执行单个进程，所有进程在各自`GPU`内计算完成`loss`后，将`loss`汇集到主`GPU`进行计算，大大减缓了负载不均衡的问题。当前使用的是`DistributedDataParallel`

简单的说，`DistributedDataParallel`使用了`All-Reduce`技术：

* 首先每个`GPU`各有一个进程，每个进程里面有自己的数据加载器、模型、优化器和学习率调度器
* 首先所有`GPU`各自加载同一个模型，所有模型对象进行相同的初始化
* 将数据集按`GPU`个数进行切分，每个`GPU`载入不同的数据进行前向计算和梯度计算
* 通过[ring allreduce](https://www.zhihu.com/question/57799212)方式，`GPU`之间相互通信以平均由不同`GPU`计算的梯度，将平均梯度应用于各自GPU模型的反向传播以获得新权重

通过平均梯度方式，保证每个`GPU`上的模型参数在整个训练过程中保持一致，分布式训练相当于大批量的单`GPU`训练

## 复现

为了保证复现性，在训练时可以设置

```
import numpy as np
import torch

torch.manual_seed(0)
np.random.seed(0)

# 使用默认卷积算法
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False
```

在测试时

```
torch.manual_seed(0)
np.random.seed(0)

torch.backends.cudnn.deterministic = False
# 为模型的每个卷积层搜索最适合它的卷积实现算法
torch.backends.cudnn.benchmark = True
```

## 额外阅读

* [Is my DistributedDataParallel code correct? Why is DistributedDataParallel’s performance worse than nn.DataParallel?](https://discuss.pytorch.org/t/is-my-distributeddataparallel-code-correct-why-is-distributeddataparallels-performance-worse-than-nn-dataparallel/55614)
* [Setting visible devices with Distributed Data Parallel](https://discuss.pytorch.org/t/setting-visible-devices-with-distributed-data-parallel/93230)
* [torch.cuda.empty_cache() write data to gpu0 #25752](https://github.com/pytorch/pytorch/issues/25752)
* [Distributed training creates multiple processes in GPU0](https://discuss.pytorch.org/t/distributed-training-creates-multiple-processes-in-gpu0/77881)
* [Avoid keeping two copies of gradients (param.grad and buckets) in DDP](https://github.com/pytorch/pytorch/issues/37030)
* [Is it expected for DistributedDataParallel to use more memory on 1 GPU in a 1GPU:1process setup?](https://discuss.pytorch.org/t/is-it-expected-for-distributeddataparallel-to-use-more-memory-on-1-gpu-in-a-1gpu-1process-setup/77748)
* [Torch not able to utilize GPU ram properly](https://discuss.pytorch.org/t/torch-not-able-to-utilize-gpu-ram-properly/83245)
* [DDP taking up too much memory on rank 0](https://discuss.pytorch.org/t/ddp-taking-up-too-much-memory-on-rank-0/62443)
* [How to use SyncBatchNorm in nn.parallel.DistributedDataParallel with v1.1.0?](https://discuss.pytorch.org/t/how-to-use-syncbatchnorm-in-nn-parallel-distributeddataparallel-with-v1-1-0/51204)
* [Distributed: other ranks not waiting rank_0’s evaluation](https://discuss.pytorch.org/t/distributed-other-ranks-not-waiting-rank-0s-evaluation/78100)
* [Distributed Data Parallel with Multiple Losses](https://discuss.pytorch.org/t/distributed-data-parallel-with-multiple-losses/71648)
* [Average loss in DP and DDP](https://discuss.pytorch.org/t/average-loss-in-dp-and-ddp/93306)
* [DistributedDataParallel loss compute and backpropogation?](https://discuss.pytorch.org/t/distributeddataparallel-loss-compute-and-backpropogation/47205)
* [What is the differenc between cudnn.deterministic and .cudnn.benchmark?](https://discuss.pytorch.org/t/what-is-the-differenc-between-cudnn-deterministic-and-cudnn-benchmark/38054)
* [REPRODUCIBILITY](https://pytorch.org/docs/stable/notes/randomness.html)
* [What is the differenc between cudnn.deterministic and .cudnn.benchmark?](https://discuss.pytorch.org/t/what-is-the-differenc-between-cudnn-deterministic-and-cudnn-benchmark/38054/3)
