
# [numpy]数据保存和加载

`numpy`提供了函数`savetxt`和`loadtxt`进行数据的保存和加载

## 函数解析

使用函数[numpy.savetxt](https://numpy.org/devdocs/reference/generated/numpy.savetxt.html?highlight=savetxt#numpy-savetxt)将数组写入文件

```
@array_function_dispatch(_savetxt_dispatcher)
def savetxt(fname, X, fmt='%.18e', delimiter=' ', newline='\n', header='',
            footer='', comments='# ', encoding=None):
```

* `fname`：保存文件名，可以是`.txt/.csv`
* `X`：一维或二维数组
* `fmt`：格式化结果，默认为`%.18e`，则数值`23`保存为`2.300000000000000000e+02`
* `delimiter`：分隔符，默认为空字符，可设置为空格或者逗号等等
* `newline`：每行数值如何结尾，默认为换行符
* `header`：写入文件开头，默认为空
* `footer`：写入文件末尾，默认为空

使用函数[loadtxt](https://numpy.org/devdocs/reference/generated/numpy.loadtxt.html?highlight=loadtxt#numpy.loadtxt)从文件读取数组

```
@set_module('numpy')
def loadtxt(fname, dtype=float, comments='#', delimiter=None,
            converters=None, skiprows=0, usecols=None, unpack=False,
            ndmin=0, encoding='bytes', max_rows=None):
```

* `fname`：文件名
* `dtype`：读取类型，默认为`float`
* `delimiter`：分隔符

## 示例

写入和读取一个二维数组，保存为`.csv`文件

```
# -*- coding: utf-8 -*-

"""
@author: zj
@file:   main.py
@time:   2020-01-26
"""

import numpy as np

if __name__ == '__main__':
    # 分隔符使用空格
    delimiter = ' '
    # 文件名
    file_name = 'np.csv'
    # 创建二维数组
    data = np.random.randn(2, 4)
    print('data:', data)
    # 保存数据
    np.savetxt(file_name, data, fmt='%.4f', delimiter=delimiter)
    # 解析数组
    res = np.loadtxt(file_name, delimiter=delimiter)
    print('res:', res)
```

文件保存如下：

```
0.7206 -0.8134 -0.6305 0.1064
0.0843 0.9964 1.5460 0.8704
```

输出结果如下：

```
data: [[ 0.72061082 -0.81343968 -0.63050239  0.10642858]
 [ 0.08428892  0.99644281  1.54604727  0.87040002]]
res: [[ 0.7206 -0.8134 -0.6305  0.1064]
 [ 0.0843  0.9964  1.546   0.8704]]
```

## 如何将float数组转换成int数组

因为默认数组保存为`float`格式，所以读取文件时得到的也是浮点型数组，转换成整型格式需要额外使用函数`astype`，而不是设置`dtype`属性

```
# 解析数组
res = np.loadtxt(file_name, delimiter=delimiter).astype(np.int)
print('res:', res)
# 输出结果如下
data: [[ -6.47453318   0.63819837 -12.63992178   7.79347093]
 [  0.97600354   5.12906234  -0.49724709  -2.01769487]]
res: [[ -6   0 -12   7]
 [  0   5   0  -2]]
```