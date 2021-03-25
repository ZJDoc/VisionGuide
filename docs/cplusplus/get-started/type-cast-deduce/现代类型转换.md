
# [c++11][cast]现代类型转换

参考：

[Casting](https://docs.microsoft.com/en-us/cpp/cpp/casting?view=vs-2019)

[Casting Operators](https://docs.microsoft.com/en-us/cpp/cpp/casting-operators?view=vs-2019)

现代`C++`编程更推荐使用`C++`风格转换方式，因为其在某些情况下类型安全性显著提高，并且更明确地表达编程意图

常用的有以下3种：

1. `dynamic_cast`
2. `static_cast`
3. `const_cast`

## dynamic_cast

参考：[dynamic_cast Operator](https://docs.microsoft.com/en-us/cpp/cpp/dynamic-cast-operator?view=vs-2019)

```
dynamic_cast < type-id > ( expression )
```

其作用是将操作数`expression`转换成`type-id`类型

* `new_type`：是一个类的指针或者引用，或者指向`void`的指针
* `expression`：其类型必须是指针（如果`new_type`是指针的话），否则是一个`l_value`（如果`new_type`是引用的话）

如果强制转换成功，`dynamic_cast`将返回一个新类型的值；如果强制转换失败，并且`new_type`是指针类型，则返回该类型的空指针（也就是`0`）；如果强制转换失败，`new_type`是引用类型，则返回`0`

`dynamic_cast`执行编译时检查和运行时检查，适用于多态类型的数据转换，比如基类和派生类之间的转换

## static_cast

参考：[static_cast Operator](https://docs.microsoft.com/en-us/cpp/cpp/static-cast-operator?view=vs-2019)

```
static_cast <type-id> ( expression )
```

`static_cast`没有运行时类型检查，出现错误时会返回原指针，好像没有错一样，所以不像`dynamic_cast`那样安全

```
typedef unsigned char BYTE;

enum scast {
    AA,
    BB,
    CC
};


void f() {
    char ch;
    int i = 65;
    float f = 2.5;
    double dbl;

    // int to char
    ch = static_cast<char>(i);
    // float to double
    dbl = static_cast<double>(f);
    // char to unsigned char
    i = static_cast<BYTE>(ch);

    scast s = AA;
    // enum to int
    cout << static_cast<int>(s) << endl;
    // int to enum
    s = static_cast<scast >(2);
    cout << s << endl;
}
```

### static_cast vs. dynamic_cast

* `dynamic_cast`转换更安全，但`dynamic_cast`只对指针或引用有效，同时运行时类型检查是一个开销
* `static_cast`不执行运行时检查，其安全性弱于`dynamic_cast`，适用于非多态类型的数据转换，比如整数和浮点数的转换，以及整数和枚举值的转换

```
class B {};

class D : public B {};

void f(B* pb, D* pd) {
   D* pd2 = static_cast<D*>(pb);   // Not safe, D can have fields
                                   // and methods that are not in B.

   B* pb2 = static_cast<B*>(pd);   // Safe conversion, D always
                                   // contains all of B.
}
```

## const_cast

```
const_cast <type-id> (expression)
```

其作用是移除对象的`const/volatile/__unaligned`属性。比如将`const`常量转换成常量

```
class CCTest {
public:
    void setNumber(int);

    void printNumber() const;

private:
    int number;
};

void CCTest::setNumber(int num) { number = num; }

void CCTest::printNumber() const {
    std::cout << "\nBefore: " << number;
    const_cast< CCTest * >( this )->number--;
    std::cout << "\nAfter: " << number;
}

int main() {
    CCTest X;
    X.setNumber(8);
    X.printNumber();
}
```

本来在类`CCTest`中，设置`printNumber`为`const`函数，不能在其中修改对象值

通过const_cast的使用，将`this`的类型从`const CCTest *`修改为`CCTest *`，这样就能够修改对象值了。结果如下

```
Before: 8
After: 7
```