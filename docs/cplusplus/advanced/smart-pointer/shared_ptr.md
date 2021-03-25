
# [c++11]shared_ptr

参考：[How to: Create and Use shared_ptr Instances](https://docs.microsoft.com/en-us/cpp/cpp/how-to-create-and-use-shared-ptr-instances?view=vs-2019)

多个`shared_ptr`实例可以同时拥有同一个原始指针。初始化一个`shared_ptr`对象后，可以复制它，通过函数值参数进行传递，也可以将它分配给其他`shared_ptr`对象。所有实例都指向同一个对象，并共享对一个`控制块`的访问，该`控制块`在添加实例、实例超出范围或重置实例时递增和递减引用计数（`reference count`）。当引用计数达到零时，控制块删除内存资源和自身。示例图如下：

![](./imgs/shared_ptr.png)

## 创建

有两种方式进行创建，一是使用`shared_ptr`构造器，二是使用辅助函数[make_shared](https://docs.microsoft.com/en-us/cpp/standard-library/memory-functions?view=vs-2019#make_shared)（推荐）

```
auto sp = std::shared_ptr<Example>(new Example(argument));
auto msp = std::make_shared<Example>(argument);
```

## 成员函数

参考：

[std::shared_ptr](http://www.cplusplus.com/reference/memory/shared_ptr/)

[shared_ptr class](https://docs.microsoft.com/en-us/cpp/standard-library/shared-ptr-class?view=vs-2019)

`shared_ptr`常用的成员函数包括：

* [get](http://www.cplusplus.com/reference/memory/shared_ptr/get/)：返回存储指针，如果为空返回`nullptr`
* [reset](http://www.cplusplus.com/reference/memory/shared_ptr/reset/)：删除当前对象管理的内存资源，并在对象中用`nullptr`代替存储指针
* [swap](http://www.cplusplus.com/reference/memory/shared_ptr/swap/)：交换两个`shared_ptr`对象保存的内容，包括指针和引用计数
* [use_count](http://www.cplusplus.com/reference/memory/shared_ptr/use_count/)：返回引用计数
* [unique](http://www.cplusplus.com/reference/memory/shared_ptr/unique/)：当前实例是否唯一拥有对象，等价于`user_count() == 1`
* [operator=](http://www.cplusplus.com/reference/memory/shared_ptr/operator=/)：赋值共享对象
* [operator bool](http://www.cplusplus.com/reference/memory/shared_ptr/operator%20bool/)：当前`shared_ptr`对象是否为空。等价于`get() != nullptr`

## 示例1

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

int main(int argc, char *argv[]) {
    auto sptr = std::make_shared<struct S>('a', 33);
    std::shared_ptr<struct S> sptr2(sptr);
    // 计数
    cout << sptr.use_count() << endl;
    // 修改对象信息
    sptr2->a = '3';
    print(*sptr);
    print(*sptr2);

    // 是否唯一拥有
    cout << sptr.unique() << endl;
}
```

## 函数调用

将`shared_ptr`输入到另一个函数需要注意以下信息：

1. 通过值传递。这将调用复制构造函数，增加引用计数，使得被调用方拥有`shared_ptr`实例。在这个操作中会有少量的开销，取决于传递的`shared_ptr`对象的数量。当调用方和被调用方之间的隐含或显式代码协定要求被调用方是所有者时，使用此选项
2. 通过引用或`const`引用传递。在这种情况下，引用计数不会递增，只要调用方不超出范围，被调用方就可以访问指针。或者，被调用方可以在代码内基于引用创建`shared_ptr`，成为共享所有者。当调用者不了解被调用者时，或者必须传递一个`shared_ptr`并且出于性能原因希望避免复制操作时，使用此选项
3. 将基础指针或引用传递给基础对象。这使被调用方能够使用该对象，但不能使其共享所有权或延长生存期。如果被调用者从原始指针创建一个`shared_ptr`，则新的`shared_ptr`独立于原始指针，并且不控制底层资源。当调用方和被调用方之间的约定明确指定调用方保留`shared_ptr`生存期的所有权时，使用此选项


当决定如何传递`shared_ptr`时，请确定被调用者是否必须共享基础资源的所有权。`owner`是一个对象或函数，它可以保持底层资源的活动状态。如果调用者必须保证被调用者可以将指针的寿命延长到其（函数）寿命之外，请使用第一个选项；如果不关心被调用者是否延长了生存期，那么通过引用传递并让被调用者复制它

如果必须让辅助函数访问底层指针，并且知道辅助函数将只使用指针并在调用函数返回之前返回，则该函数不必共享底层指针的所有权。它只需要在调用者的`shared_ptr`的生命周期内访问指针。在这种情况下，可以通过引用传递`shared_ptr`，或者将原始指针或引用传递给基础对象。通过这种方式提供了一个小的性能优势，也可以帮助您表达您的编程意图

有时，例如在`std::vector<shared_ptr<T>>`，可能必须将每个`shared_ptr`传递给`lambda`表达式体或命名函数对象。如果`lambda`或函数不存储指针，则通过引用传递`shared_ptr`，以避免为每个元素调用复制构造函数

## 数组

参考：[c++ shared_ptr到数组：应该使用它吗？](https://codeday.me/bug/20170605/24437.html)

使用`shared_ptr`创建动态数组需要自定义删除程序：

```
template<typename T>
struct array_deleter {
    void operator()(T const *p) {
        cout << "delete" << endl;
        delete[] p;
    }
};
```

使用如下：

```
int main() {
    // 创建整型数组
    std::shared_ptr<int> ints(new int[10], array_deleter<int>());
    for (int i = 0; i < 5; i++) {
        ints.get()[i] = i;
        cout << ints.get()[i] << endl;
    }

    ints.reset();

    cout << "end" << endl;
}
```

结果：

```
0
1
2
3
4
delete
end
```