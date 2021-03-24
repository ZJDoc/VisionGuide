
# [collections][deque]双向队列

`list`是单向队列，而`deque`是双向队列

## list方法

`deque`支持`list`常用的用法，包括

```
>>> from collections import deque
>>> a = deque(range(3))
>>> a
deque([0, 1, 2])
# 队尾添加
>>> a.append(4)
>>> a
deque([0, 1, 2, 4])
# 检索下标
>>> a.index(2)
2
# 队尾弹出
>>> a.pop()
4
>>> a
deque([0, 1, 2])
# 读取指定下标值
>>> a[2]
2
```

## deque方法

除此之外，`deque`还支持前向操作

```
appendleft(x) 头部添加元素
extendleft(iterable) 头部添加多个元素
popleft() 头部返回并删除
rotate(n=1) 旋转
maxlen 最大空间，如果是无边界的，返回None
```

## maxlen

`deque`支持有限长度

```
>>> a = deque(range(3), maxlen=3)
>>> a
deque([0, 1, 2], maxlen=3)
>>> a.append(4)
>>> a
deque([1, 2, 4], maxlen=3)
>>> a.appendleft(22)
>>> a
deque([22, 1, 2], maxlen=3)
```

当队列到达最大长度后，再次添加元素，会进行替换操作

## rotate

将序列队头/队尾元素进行移动

```
>>> a = deque(range(8))
>>> a
deque([0, 1, 2, 3, 4, 5, 6, 7])
# 将队尾元素向队头移动
>>> a.rotate(2)
>>> a
deque([6, 7, 0, 1, 2, 3, 4, 5])
# 将队头元素向队尾移动
>>> a.rotate(-2)
>>> a
deque([0, 1, 2, 3, 4, 5, 6, 7])
```

## 相关阅读

* [python3：deque和list的区别](https://blog.csdn.net/qq_34979346/article/details/83540389)

* [python list与deque在存储超大数组的区别](https://blog.csdn.net/qq_37887537/article/details/93722103)
