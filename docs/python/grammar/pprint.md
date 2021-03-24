
# [pprint]更易读的打印

相比于`print`，`pprint`提供了更加易读的打印结果

## 使用

```
>>> import pprint
>>> stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
>>> stuff.insert(0, stuff)
>>> print(stuff)
[[...], 'spam', 'eggs', 'lumberjack', 'knights', 'ni']
>>> pprint.pprint(stuff)
[<Recursion on list with id=139827371606416>,
 'spam',
 'eggs',
 'lumberjack',
 'knights',
 'ni']
```

## 相关阅读

* [pprint — Data pretty printer](https://docs.python.org/3/library/pprint.html)

* [python中pprint模块](https://blog.csdn.net/ZEroJAVAson/article/details/88649650)
