
# [empty_cache]清空显存

查看工程源码时发现在训练完成后，测试模型之前调用了函数[torch.cuda.empty_cache()](https://pytorch.org/docs/stable/cuda.html#torch.cuda.empty_cache)

```
logger.info('Start evaluating...')
torch.cuda.empty_cache()  # speed up evaluating after training finished
do_evaluation(cfg, model, distributed=args.distributed)
```

其作用是释放缓存分配器当前持有的所有未占用的缓存内存，以便这些内存可以在其他GPU应用程序中使用，并在`nvidia-smi`中可见

## 使用

对于何时使用该函数清空缓存内存，参考：

[About torch.cuda.empty_cache()](https://discuss.pytorch.org/t/about-torch-cuda-empty-cache/34232)

[What is torch.cuda.empty_cache do and where should i add it?](https://discuss.pytorch.org/t/what-is-torch-cuda-empty-cache-do-and-where-should-i-add-it/40975)

[Why does torch.cuda.empty_cache() make the GPU utilization near 0 and slow down the training time?](https://discuss.pytorch.org/t/why-does-torch-cuda-empty-cache-make-the-gpu-utilization-near-0-and-slow-down-the-training-time/65196)

[pytorch GPU显存释放的问题？](https://www.zhihu.com/question/68509057/answer/566619040)

并不推荐在实现中频繁调用该函数。仅在显存不足时进行调用即可