
# [itertools][product]嵌套循环

可迭代对象输入的笛卡儿积。大致相当于生成器表达式中的嵌套循环

##  product(A, B)

等同于`((x,y) for x in A for y in B)`

```
>>> from itertools import product
>>> import numpy a snp
>>> a = np.arange(3)
>>> b = np.arange(5, 9)
>>> a
array([0, 1, 2])
>>> b
array([5, 6, 7, 8])
>>> ((x, y) for x in a for y in b)
<generator object <genexpr> at 0x7fb108a9fed0>
>>> list(((x, y) for x in a for y in b))
[(0, 5), (0, 6), (0, 7), (0, 8), (1, 5), (1, 6), (1, 7), (1, 8), (2, 5), (2, 6), (2, 7), (2, 8)]
>>> product(a,b)
<itertools.product object at 0x7fb106b1b4b0>
>>> list(product(a,b))
[(0, 5), (0, 6), (0, 7), (0, 8), (1, 5), (1, 6), (1, 7), (1, 8), (2, 5), (2, 6), (2, 7), (2, 8)]
```

## product(A, repeat=2)

等同于`product(A, A)`，也就是`((x, y) for x in A for y in A)`

```
>>> product(a, a)
<itertools.product object at 0x7fb106b1b4b0>
>>> list(product(a, a))
[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
>>> list(product(a, repeat=2))
[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
```

## 相关阅读

* [product](https://docs.python.org/zh-cn/3.7/library/itertools.html#itertools.product)