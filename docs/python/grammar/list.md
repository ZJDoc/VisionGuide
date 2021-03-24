
# [list]排序

## 定义

```
list.sort(cmp=None, key=None, reverse=False)
```

* `cmp`：指定排序方法
* `key`：指定比较元素
* `reverse`：排序规则：`True`表示降序，`False`表示升序

## 示例一

```
import random

if __name__ == '__main__':
    a = random.sample(range(10), 3)
    print(a)

    # 降序
    a.sort(reverse=True)
    print(a)
    # 升序
    a.sort()
    print(a)
######################3 输出
[8, 1, 5]
[8, 5, 1]
[1, 5, 8]
```

## 示例二

列表中包含列表，按子列表中指定元素进行排序

```
import random

if __name__ == '__main__':
    a = [random.sample(range(10), 3), random.sample(range(10), 3), random.sample(range(10), 3)]
    print(a)

    # 按子列表中最后一个元素进行排序
    a.sort(key=lambda x: x[2], reverse=True)
    print(a)
######################## 输出
[[0, 9, 5], [0, 2, 6], [5, 7, 0]]
[[0, 2, 6], [0, 9, 5], [5, 7, 0]]
```

## 示例三

列表中包含字典，按字典中指定元素进行排序。其操作和示例二类似

```
a.sort(key=lambda x: x['指定key'], reverse=True)
```

## 相关阅读

* [Python List sort()方法](https://www.runoob.com/python/att-list-sort.html)