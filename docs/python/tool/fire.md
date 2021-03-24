
# [fire]自动生成命令行界面

[fire](https://github.com/google/python-fire)是一个自动生成命令行界面的`Python`库

## 简介

`Python Fire`是一个库，用于从任何`Python`对象中自动生成命令行界面（`CLIs`）

* `Python Fire`是一种在`Python`中创建命令行界面的简单方法
* `Python Fire`是开发和调试`Python`代码的有用工具
* `Python Fire`有助于探索现有代码或将其他人的代码转换成`CLI`
* `Python Fire`使`Bash`和`Python`之间的转换更加容易
* `Python Fire`通过设置需要导入和创建的模块和变量来设置`REPL`，使得使用`Python REPL`变得更加容易

## 安装

```
# 方式一
$ pip install fire
# 方式二
$ conda install fire -c conda-forge
# 方式三
$ git clone https://github.com/google/python-fire.git
$ cd python-fire
$ python setup.py install
```

## 示例一：`fire.Fire()`

编写`Python`文件如下：

```
import fire


def hi(name='World'):
    """
    就是hi
    :param name: 谁
    :return: Hi 谁
    """
    return "Hi %s!" % name


def hello(name="World"):
    """
    就是hello
    :param name: 谁
    :return: Hello 谁
    """
    return "Hello %s!" % name


if __name__ == '__main__':
    fire.Fire()
```

直接调用`fire.Fire()`将会把整个模块载入命令行。执行测试代码如下：

```
$ python te_fire.py
NAME
    te_fire.py

SYNOPSIS
    te_fire.py GROUP | COMMAND

GROUPS
    GROUP is one of the following:

     fire
       The Python Fire module.

COMMANDS
    COMMAND is one of the following:

     hi
       就是hi

     hello
       就是hello
```

可以执行两个函数：`hi`和`hello`

```
$ python te_fire.py hi
Hi World!
$ python te_fire.py hello
Hello World!
```

可以输入参数

```
$ python te_fire.py hello zj
Hello zj!
(base) zj@zj-ThinkPad-T470p:~/test/TEST$ python te_fire.py hi zj
Hi zj!
```

## 示例二：`fire.Fire(<fn>)`

可以指定载入命令行的函数

```
。。。
if __name__ == '__main__':
    fire.Fire(hi)
```

此时命令行模式下直接设置为函数`hi`的调用

```
$ python te_fire.py 
Hi World!
```

## 示例三：`fire.Fire(<object>)`

`fire`不仅可以作用于函数，也可以作用于对象。定义模块文件如下：

```
import fire


class Calculator(object):

    def add(self, x, y):
        return x + y

    def multiply(self, x, y):
        return x * y


if __name__ == '__main__':
    calculator = Calculator()
    fire.Fire(calculator)
```

定义了一个`Calculator`类。首先声明一个对象，然后调用`fire.Fire`函数，这样就可以在命令行中使用该对象的函数的了

```
$ python te_fire.py
NAME
    te_fire.py

SYNOPSIS
    te_fire.py COMMAND

COMMANDS
    COMMAND is one of the following:

     add

     multiply
$ python te_fire.py multiply 3 1 
3
$ python te_fire.py add 3 1 
4
```

## 更多示例

参考：[The Python Fire Guide](https://github.com/google/python-fire/blob/master/docs/guide.md)