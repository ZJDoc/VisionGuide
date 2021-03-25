
# [c++11]cv限定符

关键字`const`和`volatile`统称为`cv`限定符（`cv qualifiers`）

## const

参考：[const (C++)](https://docs.microsoft.com/en-us/cpp/cpp/const-cpp?view=vs-2019)

语法如下：

```
const declaration ;
member-function const ;
```

### 声明值

用于数据声明时，`const`关键字指定对象或变量不可修改。`c++`使用`const`声明代替`#define`预处理器指令进行常量定义

```
int main() {
   const int i = 5;
   i = 10;   // error: assignment of read-only variable ‘i’
   i++;   // error: assignment of read-only variable ‘i’
}
```

#### 数组大小

在`c++`编程中，可使用`const`声明变量作为数组大小

```
const int maxarray = 255;
char store_char[maxarray];  // allowed in C++; not allowed in C
```

#### const指针

参考：[C++中指针常量和常量指针的区别](https://www.cnblogs.com/lizhenghn/p/3630405.html)

`const`指针就是常量指针，即指针指向的是常量，这个常量指的是指针的值（地址），而不是地址指向的值

* 指向`const`常量的指针可以重新赋值，即指针能够指向另一个地址
* 指向`const`常量的指针只能赋值给同样声明为`const`常量的指针，两者指向同一个地址
* 使用常量指针作为函数参数能够避免函数体中参数被修改

```
void f(const char *te) {
    te = "asdfadsf";

    cout << te << endl;
}

int main() {
    const char *te = "asdfa";
    const char *ttee = te;
    te = "13414";

    cout << ttee << endl;
    f(te);
    cout << te << endl;
}
```

结果：

```
asdfa         // 两个指针指向同一个地址
asdfadsf      // 指针地址可修改
13414         // 函数参数不可修改
```

#### const对象

如果对象声明为`const`，则只能调用`const`成员函数

```
class Cls {
public:
    Cls(int a, char b) : a(a), b(b) {}

    void setA(int a);

    void setA(int a) const;

private:
    int a;
    char b;
};

void Cls::setA(int a) {
    this->a = a;
    cout << this->a << endl;
}

void Cls::setA(int a) const {
    cout << "const " << a << endl;
}

int main() {
    const Cls cls(1, 'c');
    cls.setA(33);

    Cls cls2(2, 'd');
    cls2.setA(11);
}
```

### 声明成员函数

声明成员函数为`const`，表示该函数为只读函数（即常量成员函数），不会修改调用对象

常量成员函数（`constant member function`）无法修改任何非静态数据成员和调用任何非常量成员函数

示例如下：

```
class Cls {
public:
    void setA(int a) const;
}

void Cls::setA(int a) const {
    cout << "const " << a << endl;
}
```

### c vs. c++

`c`语言中，`const`拥有外部链接，所以文件声明如下：

```
const int i=2; // 源文件初始化
extern const int i; // 其他模块使用
```

`c++`语言中，`const`拥有内部链接，所以必须显式添加`extern`关键字：

```
extern const int i=2; // 源文件初始化
extern const int i; // 其他模块使用
```

如果想要在`c`文件中调用`c++ const`变量，需要初始化如下：

```
extern “C” const int x=10;
```

*所以`c`语言中，常量通常定义在源文件；`c++`语言中，常量也可定义在头文件中*

## constexpr

参考：[constexpr (C++)](https://docs.microsoft.com/en-us/cpp/cpp/constexpr-cpp?view=vs-2019)

`constexpr`是`c++11`提出的关键字，意为常量表达式（`constant expression`）

`constexpr`除了`const`的功能外，还可用于函数和构造器声明，表示其值或返回值是常量

`constexpr`整数值可用于替代需要`const`整数的任何位置，例如模板参数和数组声明中。当一个值可以在编译时而不是在运行时计算时，它可以帮助您的程序更快地运行，并且使用更少的内存

### constexpr变量

`const`变量和`constexpr`变量的主要区别在于前者的初始化可在运行时推导，而后者必须在编译时完成初始化

* 如果变量具有`literal`类型并已初始化，则可以使用`constexpr`声明该变量。如果初始化是由构造函数执行的，则必须将该构造函数声明为`constexpr`
* 如果引用的对象已由常量表达式初始化，并且在初始化期间调用的任何隐式转换也是常量表达式，则可以将引用声明为`constexpr`
* `constexpr`变量或函数的所有声明都必须具有`constexpr`说明符

### constexpr函数

`constexpr`函数可以在编译时计算其返回值。例如初始化`constexpr`变量或提供非类型模板参数。当其参数为`constexpr`值时，`constexpr`函数生成编译时常量。当使用非`constexpr`参数调用时，或者在编译时不需要它的值时，它在运行时像常规函数一样生成一个值（*这种双重行为使您不必编写同一函数的`constexpr`和`non constexpr`版本*）

**`constexpr`函数或构造函数是隐式内联的**

以下规则适用于`constexpr`函数：

* `constexpr`函数必须只接受和返回`literal`类型
* `constexpr`函数可以是递归的
* 它不能是`virtual`的。如果封闭类具有任何`virtual`基类，则不能将构造函数定义为`constexpr`
* 函数体可以定义为`=default`或`=delete`
* 函数体不能包含`goto`语句或`try`块
* 非`constexpr`模板的显式专用化可以声明为`constexpr`
* `constexpr`模板的显式专用化不必也是`constexpr`

#### const vs. constexpr

参考：[C++ const 和 constexpr 的区别？](https://www.zhihu.com/question/35614219)

`const`未区分编译期常量和运行期常量，`constexpr`表示编译期可计算

在 `C` 里面，`const` 很明确只有「只读」一个语义，不会混淆。`C++` 在此基础上增加了「常量」语义，也由 `const` 关键字来承担，引出来一些奇怪的问题。`C++11` 把「常量」语义拆出来，交给新引入的 `constexpr` 关键字

在 `C++11` 以后，建议凡是「常量」语义的场景都使用 `constexpr`，只对「只读」语义使用 `const`

示例如下：

```
// constexpr 声明factorial可以参与编译期的运算
constexpr int factorial(int n) {
    return n <= 1 ? 1 : (n * factorial(n - 1));
}

int main() {
    std::cout << "4! = " << factorial(4) << endl; // computed at compile time

    volatile int k = 4; // disallow optimization using volatile
    std::cout << k << "! = " << factorial(k) << '\n'; // computed at run time
}
```

## volatile

参考：

[C 和 C++ 的 volatile 关键字为什么给编程者造成了如此大的误解？](https://www.zhihu.com/question/66896665)

[深入理解C++中的volatile关键字](https://www.xuebuyuan.com/3180923.html)

* 阻止编译器调整操作`volatile`变量的指令顺序，提供对特殊地址的稳定访问
* 阻止编译器为了提高速度将一个变量缓存到寄存器内而不写回，生成对应代码直接存取原始内存地址