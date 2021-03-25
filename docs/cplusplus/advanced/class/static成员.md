
# static成员

参考：[Static Members (C++)](https://docs.microsoft.com/en-us/cpp/cpp/static-members-cpp?view=vs-2019)

类可以包含静态成员数据和成员函数。当一个数据成员声明为静态时，该类的所有对象只维护一个数据副本

静态数据成员不是给定类类型的对象的一部分。因此，静态数据成员的声明不被视为定义。数据成员在类作用域中声明，但定义在文件作用域中执行。这些静态成员具有外部链接。以下示例说明了这一点：

## 使用

可以引用静态数据成员而不引用类类型的对象

```
long nBytes = BufferedOutput::bytecount;
```

也可以通过类对象引用

```
BufferedOutput Console;
long nBytes = Console.bytecount;
```

## 访问规则

静态数据成员受类成员访问规则的约束。对于私有定义的静态数据成员而言，只允许类成员函数和友元函数进行私有访问。例外情况是，不管静态数据成员的访问限制如何，都必须在文件作用域中定义它们。如果要显式初始化数据成员，则必须为该定义提供初始值设定项