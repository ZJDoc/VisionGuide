
# void类型

## void类型

参考：

[The void type](https://docs.microsoft.com/en-us/cpp/cpp/cpp-type-system-modern-cpp?view=vs-2019#the-void-type)

[void (C++)](https://docs.microsoft.com/en-us/cpp/cpp/void-cpp?view=vs-2019)

`void`类型有两个用处

1. 作为函数返回值类型，表示不返回一个值
2. 定义在函数参数列表，表示该函数没有任何参数
3. 使用`void *`作为指针，可以指向任何类型的变量

```
#include <iostream>

using std::cout;
using std::endl;

void f(void *a) {
    int *b = (int *) a;
    cout << sizeof(b) << endl;
    cout << sizeof(*b) << endl;

    cout << *b << endl;
}


int main() {

    int a = 3;
    f(&a);

    return 0;
}
```

结果

```
8
4
3
```

`void *`可以指向任何类型的指针（除了`const`和`volatile`声明的），但是如果想要使用具体的变量值必须重新经过转换

`void`指针同样可以指向函数，但是不能是类成员

## C++规范

1. 尽量避免使用`void`指针，其涉及到类型安全
2. 设置函数无参数，使用`f()`代替`f(void)`