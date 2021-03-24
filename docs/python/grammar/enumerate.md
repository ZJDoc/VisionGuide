
# [enumerate]遍历

## 使用

```
class enumerate(object)
 |  enumerate(iterable, start=0)
 |  
 |  Return an enumerate object.
 |  
 |    iterable
 |      an object supporting iteration
```

遍历可迭代对象，同时返回数组下标和值

```
>>> import numpy as np
>>> a = np.arange(30, 40)
>>> a
array([30, 31, 32, 33, 34, 35, 36, 37, 38, 39])
>>> for idx, item in enumerate(a, 0):
...     print(idx, item)
... 
0 30
1 31
2 32
3 33
4 34
5 35
6 36
7 37
8 38
9 39
```

可以指定起始位置下标值（**Note：仅改变下标起始值，仍旧会完整遍历数组**）

```
>>> for idx, item in enumerate(a, 10):
...     print(idx, item)
... 
10 30
11 31
12 32
13 33
14 34
15 35
16 36
17 37
18 38
19 39
```

## 相关阅读

* [Python enumerate() 函数](https://www.runoob.com/python/python-func-enumerate.html)