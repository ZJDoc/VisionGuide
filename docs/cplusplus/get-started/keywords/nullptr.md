
# [c++11]nullptr

参考：[nullptr](https://docs.microsoft.com/en-us/cpp/cpp/nullptr?view=vs-2019)

`std::nullptr`是类型`std::nullptr_t`的空指针常量，可以转换成任何原始指针类型

之前通常使用`NULL`或者`0`来表示空指针，这有可能造成编译错误。从`c++11`开始推荐使用常量`std::nullptr`

## 示例一

参考：[std::nullptr_t](https://en.cppreference.com/w/cpp/types/nullptr_t)

```
void f(int *pi) {
    std::cout << "Pointer to integer overload\n";
}

void f(double *pd) {
    std::cout << "Pointer to double overload\n";
}

void f(std::nullptr_t nullp) {
    std::cout << "null pointer overload\n";
}

int main() {
    int *pi;
    double *pd;

    f(pi);
    f(pd);
    f(nullptr);  // would be ambiguous without void f(nullptr_t)
//    f(0);  // ambiguous call: all three functions are candidates
//    f(NULL); // ambiguous if NULL is an integral null pointer constant
    // (as is the case in most implementations)
}
```

定义了三个重载函数，分别使用`int/double/nullptr_t`作为参数类型。如果输入`0`或者`NULL`作为参数，会存在二义性（`ambiguous`），因为均符合这`3`个重载函数

## 示例二

参考：[nullptr, the pointer literal](https://en.cppreference.com/w/cpp/language/nullptr)

`std::nullptr`能够输入模板函数，而`0`和`NULL`会发生错误

```
template<class F, class A>
void Fwd(F f, A a) {
    f(a);
}

void g(int *i) {
    std::cout << "Function g called\n";
}

int main() {
    g(NULL);           // Fine
    g(0);              // Fine

    Fwd(g, nullptr);   // Fine
//  Fwd(g, NULL);  // ERROR: No function g(int)
}
```