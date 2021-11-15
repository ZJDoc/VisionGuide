
# Monkey Patch

## 动态替换

今天听到一个很有意思的术语 - `Monkey Patch`，意思是在程序运行过程中替换某一模块实现，而不是在磁盘上替换相应的代码文件。

>The definition of the term varies depending upon the community using it. In Ruby,[2] Python,[3] and many other dynamic programming languages, the term monkey patch only refers to dynamic modifications of a class or module at runtime, motivated by the intent to patch existing third-party code as a workaround to a bug or feature which does not act as desired. Other forms of modifying classes at runtime have different names, based on their different intents. For example, in Zope and Plone, security patches are often delivered using dynamic class modification, but they are called hot fixes.[citation needed]

除了`Monkey Patch`之外，还有相类似的名字，比如`Hot Fixes（热修复）`等等。

其实仔细一想，在脚本语言（比如`Python`）中，动态替换类、属性或者函数的操作非常普遍。

## 相关阅读

* [Monkey patch](https://en.wikipedia.org/wiki/Monkey_patch)
* [What is monkey patching?](https://stackoverflow.com/questions/5626193/what-is-monkey-patching)
* [关于Monkey Patch猴子补丁](https://www.cnblogs.com/robert871126/p/10107258.html)