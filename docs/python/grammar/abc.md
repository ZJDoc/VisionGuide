
# [抽象基类]abc

`python`提供了[abc](https://docs.python.org/zh-cn/3/library/abc.html?highlight=decorator)模块用于抽象基类的创建

## 简单实现

* 创建一个抽象基类`Person`，定义抽象方法`print`
* 创建子类`Men`和`Women`，实现抽象方法`print`

```
# -*- coding: utf-8 -*-

# @Time    : 19-6-12 上午11:02
# @Author  : zj

from abc import ABCMeta
from abc import abstractmethod


class Person(metaclass=ABCMeta):

    @abstractmethod
    def print(self):
        pass


class Men(Person):

    def print(self):
        print("men")


class Women(Person):

    def print(self):
        print('women')


if __name__ == '__main__':
    b = Men()
    c = Women()

    print(type(Person))
    print(type(b))
    print(type(c))
```

在上面代码中，使用`abc.ABCMeta`作为抽象基类的元类，使用装饰器`@abstractmethod`声明抽象方法

## ABC

类`ABC`是`abc`模块中定义的类，其继承了元类`ABCMeta`，可以作为辅助类使用标准方式进行类定义，上面的抽象基类可改写成

```
class Person(ABC):

    @abstractmethod
    def print(self):
        pass
```

## 抽象基类特性

1. 无法实例化抽象基类
    ```
    TypeError: Can't instantiate abstract class Person with abstract methods print
    ```
2. 无法实例化未重写抽象方法的子类
    ```
    TypeError: Can't instantiate abstract class Men with abstract methods print
    ```

## 什么是元类

元类就是定义类的类。在面向对象思想中，所有类都是对象，包括定义的类

默认情况下，[type](https://docs.python.org/zh-cn/3/library/functions.html?highlight=type#type)是所有的类的元类

## 小结

元类/抽象基类的出现进一步完善了`python`面向对象特性

*这些思想在`Java`中已经有了实现*

## 相关阅读

* [使用元类](https://www.liaoxuefeng.com/wiki/1016959663602400/1017592449371072)

* [What are metaclasses in Python?](https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python)
