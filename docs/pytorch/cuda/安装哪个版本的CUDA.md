
# 安装哪个版本的CUDA

## 问题

今天运行`Detectron2`时遇到一个问题

```
...
...
RuntimeError: CUDA error: invalid device function
段错误 (核心已转储)
```

在仓库上查找到相应的`Issue`：[RuntimeError: CUDA error: invalid device function ROIAlign_forward_cuda #62](https://github.com/facebookresearch/detectron2/issues/62)

原因在于`CUDA`和`cudatoolkit`版本不一致的关系

## 解析

使用`nvidia-smi`和`nvcc --version`查询得到的`cuda`版本并不一致

```
$ nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2018 NVIDIA Corporation
Built on Sat_Aug_25_21:08:01_CDT_2018
Cuda compilation tools, release 10.0, V10.0.130
#########################################
$ nvidia-smi 
Sun Jun 14 20:58:31 2020       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 440.36       Driver Version: 440.36       CUDA Version: 10.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce GTX 108...  Off  | 00000000:01:00.0  On |                  N/A |
| 54%   71C    P2   174W / 250W |   7268MiB / 11175MiB |    100%      Default |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|    0      1710      G   /usr/lib/xorg/Xorg                           124MiB |
|    0      6739      C   python                                      7131MiB |
+-----------------------------------------------------------------------------+
```

参考：[nvidia-smi 和 nvcc 结果的版本为何不一致](https://blog.csdn.net/ljp1919/article/details/102640512)

>其实是因为CUDA 有两种API，分别是 运行时 API 和 驱动API，即所谓的 Runtime API 与 Driver API。
nvidia-smi 的结果除了有 GPU 驱动版本型号，还有 CUDA Driver API的型号，这里是 10.0。而nvcc的结果是对应 CUDA Runtime API

## 解决

之前依据的是`nvidia-smi`查询的结果，重新安装`PyTorch`

```
conda install pytorch torchvision cudatoolkit=10.0 -c pytorch
```

再次编译`Detectron2`，问题解决