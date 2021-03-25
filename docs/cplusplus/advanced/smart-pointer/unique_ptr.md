
# [c++11]unique_ptr

参考：[How to: Create and Use unique_ptr Instances](https://docs.microsoft.com/en-us/cpp/cpp/how-to-create-and-use-unique-ptr-instances?view=vs-2019)

## 规范

每个`unique_ptr`对象都是独立的，无法共享其保存的原始指针，这样能够简化程序逻辑的复杂度。其遵循以下规范：

1. 它不能复制到另一个`unique_ptr`对象，或者传递值到函数，或者任何需要复制操作的`C++`标准库算法
2. `unique_ptr`对象保存的指针可以被移动，即内存资源的所有权可以转移到另一个`unique_ptr`对象，原来的对象就不再拥有

下图演示了两个`unique_ptr`对象之间的资源转移

![](./imgs/unique_ptr.png)

将`unique_ptr`实例添加到`C++`标准库容器是有效的，因为`unique_ptr`的移动构造器（`move constructor`）消除了复制操作的需要

## 成员函数

参考：

[std::unique_ptr](http://www.cplusplus.com/reference/memory/unique_ptr/)

[unique_ptr Class](https://docs.microsoft.com/en-us/cpp/standard-library/unique-ptr-class?view=vs-2019#unique_ptr_operator_eq)

`unique_ptr`常用的成员函数包括：

* [get](http://www.cplusplus.com/reference/memory/unique_ptr/get/)：返回存储指针，如果为空返回`nullptr`
* [release](http://www.cplusplus.com/reference/memory/unique_ptr/release/)：释放存储指针的所有权。返回存储指针且在对象中使用`nullptr`代替
* [reset](http://www.cplusplus.com/reference/memory/unique_ptr/reset/)：删除当前对象管理的内存资源，并在对象中用`nullptr`代替存储指针
* [swap](http://www.cplusplus.com/reference/memory/unique_ptr/swap/)：交换两个`unique_ptr`对象保存的指针
* [operator bool](http://www.cplusplus.com/reference/memory/unique_ptr/operator%20bool/)：当前`unique_ptr`对象是否为空。等价于`get() != nullptr`

## 示例1

```
struct S {
    S(char a, int b) : a(a), b(b) {}

    char a;
    int b;
};

/**
 * @param ptr : lvalue引用方式
 */
void print(const struct S &ptr) {
    cout << ptr.a << " " << ptr.b << endl;
}

int main(int argc, char *argv[]) {
    std::unique_ptr<struct S> uptr(new struct S('c', 3));
    std::unique_ptr<struct S> uptr2(new struct S('d', 4));

    // 打印
    print(*uptr);
    print(*uptr2);

    // 转换信息
    uptr.swap(uptr2);

    // 调用原始指针打印
    struct S *ptr = uptr.get();
    struct S *ptr2 = uptr2.get();
    print(*ptr);
    print(*ptr2);

    // 重置智能指针
    uptr.reset();
    if (!uptr) {
        cout << "ptr is null" << endl;
    }

    // 释放智能指针
    ptr2 = uptr2.release();
    if (!uptr2) {
        cout << "ptr2 is null" << endl;
        print(*ptr2);
        delete (ptr2);
    }
}
```

结果：

```
c 3
d 4
d 4
c 3
ptr is null
ptr2 is null
c 3
```

## 辅助函数

`c++11`提供了以下函数来进行`unique_ptr`的操作

1. [std::make_unique](https://docs.microsoft.com/en-us/cpp/standard-library/memory-functions?view=vs-2019#make_unique)：使用`make_unique`辅助函数创建`unique_ptr`对象

2. `std::move`：移动一个`unique_ptr`保存的指针到另一个空的`unique_ptr`

## 示例2

```
struct S {
    S() : a(0), b(0) {}

    S(char a, int b) : a(a), b(b) {}

    char a;
    int b;
};

/**
 * @param ptr : lvalue引用方式
 */
void print(const struct S &ptr) {
    cout << ptr.a << " " << ptr.b << endl;
}

bool isNull(const struct S *ptr) {
    return ptr == nullptr;
}

int main(int argc, char *argv[]) {
    auto uptr = std::make_unique<struct S>('a', 2);
    std::unique_ptr<struct S> uptr2;

    // 打印
    print(*uptr);
    // 转移指针
    uptr2 = std::move(uptr);
    print(*uptr2);
    // 判空
    cout << isNull(uptr.get()) << endl;
    cout << isNull(uptr2.get()) << endl;

    // 创建数组，使用make_unique没有进行初始化
    auto arr = std::make_unique<struct S[]>(5);
    // 初始化
    for (int i = 0; i < 5; i++) {
        arr[i].a = i + '0';
        arr[i].b = i;

        print(arr[i]);
    }
}
```