
# Tensor

参考：[WHAT IS PYTORCH?](https://pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html#sphx-glr-beginner-blitz-tensor-tutorial-py)

`Tensor`(张量)是`pytorch`最重要的数据结构,类似与`numpy`库中的`ndarray`,能够实现多维数据的加/减/乘/除以及更加复杂的操作

* 创建`tensor`
* 重置大小
* 加/减/乘/除
* 矩阵运算
* 访问单个元素
* `in_place`操作
* `numpy`格式转换
* `cuda tensor`

## 函数查询

[TORCH](https://pytorch.org/docs/stable/torch.html)

[TORCH.TENSOR](https://pytorch.org/docs/stable/tensors.html#torch-tensor)

## 创建tensor

创建一个`5`行`3`列的`tensor`

    # 赋值为0
    torch.zeros(5, 3)
    # 赋值为1
    x = torch.ones(5, 3)
    y = x.new_ones(5)
    z = torch.ones_like(x)
    # 未初始化
    torch.empty(5, 3)
    # 赋值均匀分布的随机数,大小在[0,1)
    torch.rand(5, 3)
    torch.randn_like(5, 3)

也可以转换列表为`tensor`

    torch.tensor([[i+j for i in range(3)] for j in range(5)])
    # 结果
    tensor([[0, 1, 2],
            [1, 2, 3],
            [2, 3, 4],
            [3, 4, 5],
            [4, 5, 6]])

或者使用函数`arange`

    # 创建一个连续列表
    torch.arange(2, 10)
    # 结果
    tensor([3, 4, 5, 6, 7, 8, 9])

或者复制其他`tensor`

    # 复制张量的大小一致
    w=torch.ones(3,2)
    w.copy_(x)

### 设置数据类型

在创建`tensor`的同时设置数据类型,比如

    torch.zeros(5, 3, dtype=torch.float)
    # 或
    torch.tensor([[1 for i in range(3)] for j in range(5)], dtype=torch.float)

常用数据类型包括

* `torch.float`
* `torch.double`

### 获取大小

    $ x = tensor.zeros(5, 3)
    $ x.size()
    torch.Size([5, 3])

`torch.Size`类型实际上是一个元组(`tuple`),可以执行所有元组操作

## 重置大小

使用函数[torch.Tensor.view](https://pytorch.org/docs/stable/tensors.html#torch.Tensor.view)可以重置大小

    # 重建4x4数组
    x = torch.randn(4, 4)
    # 重置大小为16
    y = x.view(16)
    # 重置大小为2x8
    z = x.view(-1, 8) # 输入-1值，那么该维度大小会参考其他维度
    # 输出
    $ print(x.size(), y.size(), z.size())
    torch.Size([4, 4]) torch.Size([16]) torch.Size([2, 8])

或者使用函数[torch.Tensor.reshape](https://pytorch.org/docs/stable/torch.html#torch.reshape)

## 加/减/乘/除

进行加/减/乘/除的张量大小相同,在对应位置上进行操作

    x = torch.ones(2, 3)
    y = torch.randn(2, 3)
    # 加
    re = torch.add(x, y)
    # 减 x - y
    re = torch.sub(x, y)
    # 乘
    re = torch.mul(x, y)
    # 除 x / y
    re = torch.div(x,y)

也可以使用参数`out`来复制结果

    # 设置同样大小数组
    re = torch.empty(2, 3)
    # 加法
    torch.add(x, y, out=re)

## 矩阵运算

    # 转置
    x = torch.ones(2,3) # 生成一个2行3列
    y = x.t()           # 得到一个3行2列

## 访问单个元素

可以执行类似`Numpy`数组的取值操作

    x = torch.tensor([x for x in range(6)])
    print(x)
    # 取值
    print(x[0])
    # 切片
    print(x[:3])
    # 结果
    tensor([0, 1, 2, 3, 4, 5])
    tensor(0)
    tensor([0, 1, 2])

使用函数`item()`将单个`tensor`转换成数值(标量,`scalar`)

    print(x[3].item())
    3

## `in_place`操作

`tensor`可以执行`in_place`操作,只需要在函数末尾添加下划线

    # 加
    x.add_(y)
    # 减
    x.sub_(y)
    # 转置
    x.t_()

## `numpy`格式转换

`torch`支持`tensor`和`numpy`数组的转换

`tensor`转换为`numpy`

    a = torch.ones(5)
    b = a.numpy()

`numpy`转换成`tensor`

    import numpy as np
    a = np.ones(5)
    b = torch.from_numpy(a)

除了`CharTensor`以外,`CPU`上的其他`Tensor`都支持和`Numpy`的转换

**注意：转换前后的数组共享底层内存，改变会同时发生**

## `cuda tensor`

利用`CUDA`调用`GPU`进行`tensor`运算,需要使用函数`to`进行`GPU`和`CPU`的转换

    x = torch.tensor(5)
    if torch.cuda.is_available():                # 测试cuda是否有效
        device = torch.device("cuda")            # 生成一个cuda对象
        y = torch.ones_like(x, device=device)    # 直接在GPU中创建y
        x = x.to(device)                         # 转换CPU数据到GPU中，也可直接使用函数`.to("cuda")`
        z = x + y                                # GPU运算
        print(x)
        print(y)
        print(z)
        print(z.to('cpu', torch.double))         # 转换数据到CPU，同时转换类型