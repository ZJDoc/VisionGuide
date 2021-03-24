
# [py3.6][f-strings]字符串连接

最近接触到一种新的字符串连接方式：[f-strings](https://www.python.org/dev/peps/pep-0498/#how-to-denote-f-strings)。这是从`Python3.6`开始的一个新的语法糖

## 实现

```
str_demo = f'balabala {TEXT} balabala'
```

在字符串引号前面添加前缀`f`，在字符串内部的大括号里面添加前面定义的变量`TEXT`。在编译期间，`Python`解释器会自动解析该字符串的连接操作，此操作类似于之前的`str.format()`方法

## 示例

```
>>> text='abcd'
>>> text
'abcd'
>>> f'this is {text}'
'this is abcd'
>>> 
>>> num=100
>>> f'num is {num}'
'num is 100'
```