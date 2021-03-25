
# [c++11][stl]array

从`c++11`开始`stl`库新增了一个容器[std::array](http://www.cplusplus.com/reference/array/array/)，它实现的是数组功能，同时集成了一些通用的容器操作

## 概述

`array`是固定大小的序列容器：它们按严格线性序列排列持有特定数量的元素

在`array`内部不保留除其包含的元素以外的任何数据（甚至不保留其大小，这是一个模板参数，在编译时固定）。它在存储大小方面与用括号语法（`[]`）声明的普通数组一样有效。这个类只向它添加一个成员和全局函数层，这样数组就可以用作标准容器

与其他标准容器不同，数组具有固定的大小，并且不通过分配器管理其元素的分配：它们是封装固定大小元素数组的聚合类型。因此，它们不能动态地展开或收缩（有关可以展开的类似容器，请参见[vector](http://www.cplusplus.com/vector)）

零大小的数组是有效的，但不应取消对它们的引用（成员的`front、back和data`）

与标准库中的其他容器不同，交换两个数组容器是一种线性操作，涉及单独交换范围中的所有元素，这通常是一种效率较低的操作。另一方面，这允许迭代器到两个容器中的元素保持其原始容器关联

数组容器的另一个独特特征是，它们可以被视为[tuple](http://www.cplusplus.com/tuple)对象：`<array> header`重载了`get`函数，就像它是一个元组一样访问数组的元素，以及专用的[tuple-size](http://www.cplusplus.com/tuple_size)和[tuple-element](http://www.cplusplus.com/tuple_element)类型

### 模板

```
template < class T, size_t N > class array;
```

* `T`表示包含元素类型
* `N`表示数组大小

### 创建数组

```
# include <array>

std::array<int,5> myarray = { 2, 16, 77, 34, 50 };
```

## 元素访问

和原来的括号语法定义的数组一样，可以进行取值赋值操作

```
int main() {
    std::array<int, 10> myarray;
    std::cout << myarray.empty() << std::endl;

    for (int i = 0; i < 3; i++) {
        myarray[i] = i * i;
    }

    for (int i = 0; i < 3; i++) {
        std::cout << myarray[i] << " ";
    }

    std::cout << std::endl;

    std::cout << myarray.size() << std::endl;
    std::cout << myarray.empty() << std::endl;

    return 0;
}
```

结果

```
0
0 1 4 
10
0
```

* 函数`empty`用于判断数组大小是否为`0`
* 函数`size`用于计算数组大小

`array`还提供了以下函数用于访问元素：

* [at](http://www.cplusplus.com/reference/array/array/at/)：返回指定位置元素的引用, 可以取值也可以赋值
* [front](http://www.cplusplus.com/reference/array/array/front/)：返回对数组容器中第一个元素的引用，可以取值也可以赋值
* [back](http://www.cplusplus.com/reference/array/array/back/)：返回数组容器中最后一个元素的引用，可以取值也可以赋值
* [data](http://www.cplusplus.com/reference/array/array/data/)：获取数据指针，可用于数组赋值操作

```
#include <iostream>
#include <array>
#include <cstring>

int main() {
    const char *cstr = "Test string.";
    std::array<char, 12> charray;

    std::memcpy(charray.data(), cstr, 12);

    std::cout << charray.data() << '\n';

    std::cout << charray.at(3) << std::endl;
    std::cout << charray.front() << std::endl;
    std::cout << charray.back() << std::endl;

    return 0;
}
```

结果：

```
Test string.
t
T
.
```

## 迭代器功能

`array`对象除了正常的取值赋值操作外，还支持迭代器功能（*这也表明可以调用`stl sort`函数*）

```
// sort algorithm example
#include <iostream>     // std::cout
#include <algorithm>    // std::sort
#include <array>

bool myfunction(int i, int j) { return (i < j); }

bool greater_than(int i, int j) {
    return i > j;
}

struct myclass {
    bool operator()(int i, int j) { return (i < j); }
} myobject;

template<size_t SIZE>
void zprint(std::array<int, SIZE> myarray) {
    for (auto it = myarray.begin(); it != myarray.end(); ++it)
        std::cout << ' ' << *it;
//    for (int n:myarray) {
//        std::cout << ' ' << n;
//    }
    std::cout << '\n';
}

int main() {
    std::array<int, 8> myarray = {32, 71, 12, 45, 26, 80, 53, 33};

    // using default comparison (operator <):
    std::sort(myarray.begin(), myarray.begin() + 4);           //(12 32 45 71)26 80 53 33

    zprint(myarray);

    // using function as comp
    std::sort(myarray.begin() + 4, myarray.end(), myfunction); // 12 32 45 71(26 33 53 80)

    zprint(myarray);

    // using object as comp
    std::sort(myarray.begin(), myarray.end(), myobject);     //(12 26 32 33 45 53 71 80)

    zprint(myarray);

    std::sort(myarray.begin(), myarray.end(), greater_than);

    zprint(myarray);

    return 0;
}
```

**注意：`array`对象作为函数参数时需要设置模板参数**

## 修改器

* [std::array::swap](http://www.cplusplus.com/reference/array/array/swap/)：交换两个相同类型，相同大小的数组内容
* [std::array::fill](http://www.cplusplus.com/reference/array/array/fill/)：使用指定值赋值array所有位置

```
int main() {
    std::array<int, 5> first = {10, 20, 30, 40, 50};
    std::array<int, 5> second = {11, 22, 33, 44, 55};

    first.swap(second);

    std::cout << "first:";
    for (int &x : first) std::cout << ' ' << x;
    std::cout << '\n';

    std::cout << "second:";
    for (int &x : second) std::cout << ' ' << x;
    std::cout << '\n';

    first.fill(1);
    std::cout << "fill:";
    for (int &x:first) std::cout << ' ' << x;
    std::cout << std::endl;

    return 0;
}
```

结果

```
first: 11 22 33 44 55
second: 10 20 30 40 50
fill: 1 1 1 1 1
```

## 二维数组

二维数组定义比较繁琐，参考[【C++ STL应用与实现】5: 如何使用std::array (since C++11) ](https://elloop.github.io/c++/2015-12-23/learning-using-stl-5-std-array)，给出了二维数组定义以及2种初始化方式

### 定义

通过嵌套方式定义二维数组

```
std::array<std::array<int, COLS>, ROWS> array
```

里面定义了列数，外面定义了行数

### 初始化方式

有两种初始化方式，一是直接输入数据进行初始化，二是创建一维数组进行初始化

### 实现

```
#include <iostream>
#include <array>

using std::cout;
using std::endl;
using std::array;

template<size_t COLS, size_t ROWS>
void PrintMatrix(std::array<std::array<int, COLS>, ROWS> arr) {
    for (const auto &ary : arr) {
        for (const auto &item : ary) {
            cout << item << " ";
        }
        cout << endl;
    }
}

int main() {
    // like plain 2D array
    array<array<int, 5>, 5> mat1 = {
            1, 2, 3, 4, 5,
            1, 2, 3, 4, 5,
            1, 2, 3, 4, 5,
            1, 2, 3, 4, 5,
            1, 2, 3, 4, 5,
    };

    // construct with 1D arys.
    array<int, 3> ary = {1, 2, 3};
    array<array<int, 3>, 5> mat2 = {ary, ary, ary, ary, ary};

    // just like plain 2D array, but can commit some value some each div.
    array<array<int, 5>, 5> mat3 = {
            array<int, 5>{1, 2, 3, 4, 5},
            array<int, 5>{1, 2, 3, 4},
            array<int, 5>{1, 2, 3},
            array<int, 5>{1, 2,},
            array<int, 5>{1,}
    };

    cout << "mat1" << endl;
    PrintMatrix(mat1);

    cout << "mat2" << endl;
    PrintMatrix(mat2);

    cout << "mat3" << endl;
    PrintMatrix(mat3);
}
```

### 指针赋值

利用指针对二维数组进行赋值操作

```
#include <iostream>
#include <cstring>
#include <array>

using std::cout;
using std::endl;
using std::array;

typedef int TYPE;
#define NUM 9

int main() {
    TYPE arcs[NUM][NUM] = {
            {0,  10, -1, -1, -1, 11, -1, -1, -1},
            {10, 0,  18, -1, -1, -1, 16, -1, 12},
            {-1, 18, 0,  22, -1, -1, -1, -1, 8},
            {-1, -1, 22, 0,  20, -1, 24, 16, 21},
            {-1, -1, -1, 20, 0,  26, -1, 7,  9},
            {11, -1, -1, -1, 26, 0,  17, -1, -1},
            {-1, 16, -1, 24, -1, 17, 0,  19, -1},
            {-1, -1, -1, 16, 7,  -1, 19, 0,  -1},
            {-1, 12, 8,  21, -1, -1, -1, -1, 0}
    };

    int i = 0;
    array<array<TYPE, NUM>, NUM> arrs = {};
    for (auto &ary:arrs) {
        memcpy(&ary, arcs[i], sizeof(TYPE) * 9);
        i++;
    }

    for (auto ary:arrs) {
        for (auto item : ary) {
            cout << " " << item;
        }
        cout << endl;
    }
}
```