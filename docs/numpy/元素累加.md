
# [numpy]元素累加

`Numpy`提供了函数`cumsum`用于元素累加操作

```
import numpy as np

if __name__ == '__main__':
    data = np.arange(10)
    print(data)

    res = np.cumsum(data)
    print(res)
################### 输出
[0 1 2 3 4 5 6 7 8 9]
[ 0  1  3  6 10 15 21 28 36 45]
```