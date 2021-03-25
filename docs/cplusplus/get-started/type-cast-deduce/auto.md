
# [c++11]auto

参考：

[auto (C++)](https://docs.microsoft.com/en-us/cpp/cpp/auto-cpp?view=vs-2019)

[placeholder type specifiers](https://en.cppreference.com/w/cpp/language/auto)

## 定义

关键字`auto`是`c++11`新增的，其目的是用于自动类型推断。语法如下：

```
auto declarator initializer;
```

`auto`本身不是类型，它是一个类型占位符。它能够指导编译器根据声明变量的初始化表达式或`lambda`表达式参数进行类型推断

使用`auto`代替固定类型声明有以下优点：

* 鲁棒性：即使表达式的类型会更改也能工作，比如函数返回不同类型
* 高性能：能够保证不会发生类型转换
* 易用性：不需要关心拼写困难或打字错误
* 高效率：使得编码更有效率

以下情况可能需要使用固定类型：

1. 只有某一类型能够起作用
2. 表达式模板辅助类型，比如`(valarray+valarray)`

网上也有关于`auto`的讨论：[如何评价 C++ 11 auto 关键字？](https://www.zhihu.com/question/35517805)

## 示例

```
# BEFORE
float getSum(int A, float B) {
    return A + B;
}

int main(int argc, char *argv[]) {
    float sum = getSum(2, 33.33);

    vector<int> src;
    src.emplace_back(1);
    src.emplace_back(4);
    src.emplace_back(3);
    for (vector<int>::iterator it = src.begin(); it != src.end(); it++) {
        cout << *it << " ";
    }
}

# AFTER
...
    auto sum = getSum(2, 33.33);
    ...
    for (auto it = src.begin(); it != src.end(); it++) {
        cout << *it << " ";
    }
```