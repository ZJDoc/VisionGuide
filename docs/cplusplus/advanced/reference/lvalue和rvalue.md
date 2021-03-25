
# [c++11][c++17]lvalue和rvalue

参考：

[Lvalues and Rvalues (C++)](https://docs.microsoft.com/en-us/cpp/cpp/lvalues-and-rvalues-visual-cpp?view=vs-2019)

[Lvalue Reference Declarator: &](https://docs.microsoft.com/en-us/cpp/cpp/lvalue-reference-declarator-amp?view=vs-2019)

[Rvalue Reference Declarator: &&](https://docs.microsoft.com/en-us/cpp/cpp/rvalue-reference-declarator-amp-amp?view=vs-2019)

每个`C++`表达式都有一个类型，并且属于一个值类别。值类别是编译器在表达式计算期间创建、复制和移动临时对象时必须遵循的规则的基础

`C++17`标准定义表达式值类别如下：

* `glvalue`是一个表达式，其计算结果确定对象、位字段或函数的标识
* `prvalue`是一个表达式，它的计算初始化对象或位字段，或计算运算符的操作数的值，由其出现的上下文指定
* `xvalue`是一个`glvalue`，它表示一个对象或位字段，其资源可以重用（通常是因为它接近其生命周期的末尾）。示例：涉及`rvalue`（8.3.2）的某些类型的表达式生成`xvalue`，例如对返回类型为右值引用的函数的调用或对右值引用类型的强制转换
* `lvalue`不是`xvalue`，是`glvalue`
* `rvalue`是`prvalue`或者`xvalue`

![](https://docs.microsoft.com/en-us/cpp/cpp/media/value_categories.png?view=vs-2019)

`lvalue`有一个程序可以访问的地址。`lvalue`表达式的示例包含变量名，包括常量变量、数组元素、返回左值引用的函数调用、位字段、联合和类成员

`prvalue`表达式没有程序可以访问的地址。`prvalue`表达式的示例包括文本、返回非引用类型的函数调用以及在表达式计算期间创建但只能由编译器访问的临时对象

`xvalue`表达式有一个地址，该地址不再可被程序访问，但可用于初始化提供对表达式访问的右值引用。示例包括返回`rvalue`的函数调用，以及数组或对象是`rvalue`的数组下标、成员和指向成员表达式的指针

## lvalue引用声明符

左值引用用于获取对象地址，但其操作和对象一样，可看成对象的另一个名称。语法如下：

```
type-id & cast-expression
```

左值引用声明由可选的说明符列表和引用声明符组成。引用必须初始化且不能更改

其地址可以转换为给定指针类型的任何对象也可以转换为类似的引用类型，比如char类型对象地址可以转换成`char *`，同样的也可转换成`char &`

左值引用声明符和取地址符有差别，当`&`前面是一个类型名时，其作为左值引用；否则，作为取地址符

### 示例

声明一个`Person`类对象`myFriend`，声明一个左值引用`rFriend`。对象的操作会影响`rFriend`，同样`rFriend`的操作会改变对象

```
struct Person {
    char *Name;
    short Age;
};

int main() {
    // Declare a Person object.
    Person myFriend;

    // Declare a reference to the Person object.
    Person &rFriend = myFriend;

    // Set the fields of the Person object.
    // Updating either variable changes the same object.
    myFriend.Name = "Bill";
    rFriend.Age = 40;

    // Print the fields of the Person object to the console.
    cout << rFriend.Name << " is " << myFriend.Age << endl;
}
```

## rvalue引用声明符

右值引用（`&&`）是对右值表达式的引用，语法如下：

```
type-id && cast-expression
```

左值引用和右值引用在语法和语义上相似，但它们遵循的规则有所不同

### 移动语义

移动语义（`move semantics`）允许通过代码实现对象之间的资源转移（比如动态分配的内存）。移动语义起作用的原因是因为它能够使用其他地方不能引用的临时对象进行资源传输

在类中实现移动语义，通常要提供一个移动构造器（编译器不自动提供，必须自定义），以及一个移动赋值构造器（`operator=`，可选）。如果输入对象为`rvalue`，那么复制和赋值操作将自动利用移动语义

之前对`operator+`的每个调用都会分配并返回一个新的临时字符串对象（右值）。`operator+`不能将一个字符串附加到另一个字符串，因为它不知道源字符串是`lvalue`还是`rvalue`。如果源字符串都是`lvalue`，那么它们可能在程序的其他地方被引用，因此不能修改。通过使用右值引用，可以修改`operator+`以获取右值，而右值不能在程序中的其他地方引用。因此，`operator+`现在可以将一个字符串附加到另一个字符串。这可以显著减少字符串类必须执行的动态内存分配的数量

为了更好地理解移动语义，请考虑将元素插入`vector`。如果超出了`vector`对象的容量，则`vector`对象必须为其元素重新分配内存，然后将每个元素复制到另一个内存位置，为插入的元素腾出空间。当插入操作复制一个元素时，它会创建一个新元素，调用复制构造函数将数据从上一个元素复制到新元素，然后销毁上一个元素。移动语义使您能够直接移动对象，而不必执行昂贵的内存分配和复制操作

为了利用向量示例中的移动语义，可以编写一个移动构造函数来将数据从一个对象移动到另一个对象

### 完美转发

完美转发（`perfect forwarding`）减少了对重载（`overloaded`）函数的需要，并有助于避免转发问题。当编写一个以引用为参数的通用函数，并将这些参数传递（或转发）给另一个函数时，可能会发生转发问题。例如，如果泛型函数采用`const&`类型的参数，则被调用函数无法修改该参数的值。如果泛型函数接受类型为`T&`的参数，则不能使用右值（例如临时对象或整型文本）调用该函数。通常，为了解决这个问题，您必须提供通用函数的重载版本，它为每个参数同时使用`T&`和`const&`。因此，重载函数的数量随着参数数量呈指数增长。右值引用使得一个版本即可接受任意参数，并将其转发给另一个函数，就像直接调用了另一个函数一样

### 示例

声明了四种类型（`W、X、Y和Z`）。每种类型的构造函数都采用`const`和非`const lvalue`引用的不同组合作为其参数

```
struct W
{
   W(int&, int&) {}
};

struct X
{
   X(const int&, int&) {}
};

struct Y
{
   Y(int&, const int&) {}
};

struct Z
{
   Z(const int&, const int&) {}
};
```

使用模板创建通用的对象构造函数

```
// 指定对象类型，参数类型
template <typename T, typename A1, typename A2>
T* factory(A1& a1, A2& a2)
{
   return new T(a1, a2);
}
// 调用一
int a = 4, b = 5;
W* pw = factory<W>(a, b);
// 调用二
Z* pz = factory<Z>(2, 2);
```

使用调用二会出错，因为不匹配模板定义，函数`factory`将可修改的`lvalue`引用作为其参数，但使用`rvalues`调用它

以往解决方式是写一个重载版本，使用`const A&`作为参数。而使用右值引用作为模板参数可以实现一个模板函数即可

```
template <typename T, typename A1, typename A2>
T* factory(A1&& a1, A2&& a2)
{
    // std::forward函数的目的是将工厂函数的参数转发给模板类的构造函数
   return new T(std::forward<A1>(a1), std::forward<A2>(a2));
}
```