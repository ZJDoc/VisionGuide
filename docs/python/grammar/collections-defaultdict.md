
# [collections][defaultdict]更安全的dict

`defaultdict`支持`dict`的用法，并且提供了更加安全的设置

## 默认值设置

`defaultdict`内置了一个工厂函数，当访问不存在的键时，会自动生成一个内置类型的对象

```
# 设置内置类型为int
from collections import defaultdict

if __name__ == '__main__':
    a = defaultdict(int)
    print(a)
    # 当访问不存在键`a`时，得到0
    print(a['a'])
################# 输出
defaultdict(<class 'int'>, {})
0
```

## 相关阅读

* [是时候用 defaultdict 和 Counter 代替 dictionary 了](https://zhuanlan.zhihu.com/p/68407137)

* [1-2 collections中deque,defaultdict,OrderedDict](https://www.jianshu.com/p/291bb5641c56)

* [Python 3 collections.defaultdict() 与 dict的使用和区别](https://www.cnblogs.com/herbert/archive/2013/01/09/2852843.html)
