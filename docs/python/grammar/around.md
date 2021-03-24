
# [around]四舍五入

函数[np.around](https://numpy.org/doc/1.18/reference/generated/numpy.around.html)能够对数据执行四舍五入操作

## 定义

>numpy.around(a, decimals=0, out=None)[source]

* `a`：输入数据，可以是单个数字，或者列表/数组
* `decimals`：保留几位小数。默认不保留小数

## 示例

```
# 单个数字
>>> np.around(3.33)
3.0
# 数组
>>> a = np.random.randn(3)
>>> a
array([ 0.02557499, -0.05847877, -1.53689999])
>>> 
>>> np.around(a)
array([ 0., -0., -2.])
# 保留2位小数
>>> np.around(a, decimals=2)
array([ 0.03, -0.06, -1.54])
```