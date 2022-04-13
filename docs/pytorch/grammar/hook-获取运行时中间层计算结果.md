
# [Hook]获取运行时中间层计算结果

可以通过`Hook`机制获取模型中间层结果，包括前向和后向计算：

* [register_forward_hook(hook)](https://pytorch.org/docs/master/generated/torch.nn.Module.html#torch.nn.Module.register_forward_hook)
* [register_full_backward_hook(hook)](https://pytorch.org/docs/master/generated/torch.nn.Module.html#torch.nn.Module.register_full_backward_hook)

还有其他注册方法啥的。。。以`register_forward_hook`为例：

```
import torch
import torchvision.models as models


def hook_fn(module, input, output):
    print(module)
    print(len(input), input[0].shape)
    print(len(output), output[0].shape, output[1].shape)
    # print(output[0])
    # print(output[1])


if __name__ == '__main__':
    m = models.resnet50(pretrained=False, num_classes=1000)
    for name, module in m.named_modules():
        # print(name, type(module))

        if name == 'layer1.1.conv2':
            module.register_forward_hook(hook_fn)
    # print(m)

    data = torch.randn(2, 3, 224, 224)
    outputs = m(data)
    print(outputs.shape)
```

注意：`register_forward_hook`可以获取得到输入数据和输出数据，只有输出数据修改是有效的，因为它运行在`forward()`方法之后。如果想要修改输入数据，可以找找其他`hook`函数


```
        r"""Registers a forward hook on the module.

        The hook will be called every time after :func:`forward` has computed an output.
        It should have the following signature::

            hook(module, input, output) -> None or modified output

        The input contains only the positional arguments given to the module.
        Keyword arguments won't be passed to the hooks and only to the ``forward``.
        The hook can modify the output. It can modify the input inplace but
        it will not have effect on forward since this is called after
        :func:`forward` is called.

        Returns:
            :class:`torch.utils.hooks.RemovableHandle`:
                a handle that can be used to remove the added hook by calling
                ``handle.remove()``
        """
```

## 相关阅读

* [How to register forward hooks for each module](https://discuss.pytorch.org/t/how-to-register-forward-hooks-for-each-module/43347)