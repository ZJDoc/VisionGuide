
# 问题解答

## 问题一：OSError: [Errno 12] Cannot allocate memory

参考：

[死亡Error：OSError: [Errno 12] Cannot allocate memory](https://blog.csdn.net/breeze210/article/details/99679048)

[OSError: [Errno 12] Cannot allocate memory. But memory usage is actually normal](https://discuss.pytorch.org/t/oserror-errno-12-cannot-allocate-memory-but-memory-usage-is-actually-normal/56027)

执行`PyTorch`程序，发生内存不足错误

* 内存查询

监视内存，查看是否是内存不足

```
# 打开两个窗口，分别查看CPU内存和显卡内存
# 每隔1秒查询一次
$ watch -n 1 free -m
$ wathc -n 1 nvidia-smi
```

* num_workers

确实不是因为内存不足，那么修改`DataLoader`的`num_workers`为`0`，再重新运行即可

```
        num_workers (int, optional): how many subprocesses to use for data
            loading. ``0`` means that the data will be loaded in the main process.
            (default: ``0``)
```

## 问题二：Process finished with exit code 137 (interrupted by signal 9: SIGKILL) 

前几天突然遇到这个问题：

```
Process finished with exit code 137 (interrupted by signal 9: SIGKILL) 
```

程序启动后被系统`KILLED`，在网上找了资料，发现是说内存不足的问题

查询内存使用情况，发现大多数内存都被缓存占据了

```
$ free -h
              total        used        free      shared  buff/cache   available
Mem:            62G         13G        450M        308M         49G         48G
Swap:          7.6G        4.2G        3.4G
```

* 额外阅读

[Process finished with exit code 137 in PyCharm](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.set_start_method)

[multiprocessing.set_start_method(method)](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.set_start_method)

[Semaphore leaks in dataloader](https://github.com/pytorch/pytorch/issues/11727)

## 问题三：RuntimeError: CUDA error: initialization error

参考：[RuntimeError: CUDA error: initialization error](https://blog.csdn.net/yyhaohaoxuexi/article/details/90718501)

>不可在DataLoader或DataSet内将任何数据放到CUDA上，而是等到程序运行出DataLoader之后（也就是到了train里的时候）将数据放到CUDA上。

## 问题四：RuntimeError: invalid argument 0: Sizes of tensors must match except in dimension 0

参考：[12 invalid argument 0: Sizes of tensors must match except in dimension 1. Got 14 and 13 in dimension 0 at /home/prototype/Downloads/pytorch/aten/src/THC/generic/THCTensorMath.cu:83](https://oldpan.me/archives/pytorch-conmon-problem-in-training)

调用`DataSet`的`__getitem__`方法返回的`image`数据维度应该一致