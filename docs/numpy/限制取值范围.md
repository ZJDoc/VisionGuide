
# [numpy][clip]限制取值范围

>clip(a, a_min, a_max, out=None, **kwargs)

将数组取值限制为给定最小值和最大值之间

```
>>> import numpy as np
>>> 
>>> a = np.arange(5)
>>> a
array([0, 1, 2, 3, 4])
>>> np.clip(a, 2, 3)
array([2, 2, 2, 3, 3])
>>> a = np.arange(12).reshape(3,4)
>>> a
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>> np.clip(a, 3, 9)
array([[3, 3, 3, 3],
       [4, 5, 6, 7],
       [8, 9, 9, 9]])
```