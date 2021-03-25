
# main

参考：[Main function](https://en.cppreference.com/w/cpp/language/main_function)

`main`函数是所有`C`和`C++`程序的执行起点

## 语法

参考：[Argument Definitions](https://docs.microsoft.com/en-us/cpp/cpp/argument-definitions?view=vs-2019)

```
int main () { body } 
int main (int argc, char *argv[]) { body } 
```

* `argc(argument count)`：包含后面参数`argv`数组的计数，`argc`参数始终大于或等于`1`
* `argv(argument vector)`：字符串数组，表示程序输入的命令行参数。按照惯例，`argv[0]`是用来调用程序的命令，`argv[1]`是第一个命令行参数，依此类推，直到`argv[argc]=null`

`argc`和`argv`的名称是任意的，并且使用指针表示数组同样有效：`int main（int ac，char**av）`

## 限制

参考：[main Function Restrictions](https://docs.microsoft.com/en-us/cpp/cpp/main-function-restrictions?view=vs-2019)

在`C++`编程中`main`函数有以下限制：

1. 不能被重载（`overloaded`）
2. 不能声明为内联（`inline`）
3. 不能声明为`static`
4. 不能传递其地址
5. 不能被调用

## 打印命令行参数

参考：[How to parse command line parameters.](http://www.cplusplus.com/articles/DEN36Up4/)

```
int main(int argc, char **argv) {
    // Walk through list of strings until a NULL is encountered.
    for (int i = 0; argv[i] != nullptr; ++i) {
        cout << i << ": " << argv[i] << "\n";
    }
}
```

输入：

```
$ ./first hi zj
```

结果：

```
0: ./first
1: hi
2: zj
```

## 启动注意事项

参考：[Additional Startup Considerations](https://docs.microsoft.com/en-us/cpp/cpp/additional-startup-considerations?view=vs-2019)

在`C++`中，对象构造（`constructor`）和析构（`destructor`）涉及执行用户代码（`executing user code`）。因此，重要的是要了解哪些初始化发生在进入`main`之前，哪些析构函数在退出`main`之后被调用

在进入`main`之前进行以下初始化：

1. 静态数据的默认初始化为零。在执行任何其他代码（包括运行时初始化）之前，所有没有显式初始值设定项的静态数据都设置为零。静态数据成员必须显式定义
2. 在翻译单元中初始化全局静态对象。这可能发生在进入`main`之前，也可能发生在对象所在的翻译单元中的任何函数或对象首次使用之前