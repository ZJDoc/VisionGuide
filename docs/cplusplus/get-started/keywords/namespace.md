
# [c++11]namespace

参考：

[Name visibility](http://www.cplusplus.com/doc/tutorial/namespaces/)

[Namespaces (C++)](https://docs.microsoft.com/en-us/cpp/cpp/namespaces-cpp?view=vs-2019#inline-namespaces-c-11)

[Namespaces](https://en.cppreference.com/w/cpp/language/namespace)

为了解决实体（`entity`）命名冲突（`name collision`）的问题，`c++`提出了`命名空间`（或称为`名称空间`），将具有全局作用域（`global scope`）的命名实体分组为更窄的命名空间作用域（`namespace scope`）。命令空间范围内的所有标识符（类型、函数、变量等）都是彼此可见，没有限定。命名空间之外的标识符可以使用每个标识符的完全限定名访问成员

## 语法

### 声明namespace

```
namespace identifier
{
  named_entities
}
```

使用关键字`namespace`指定命名空间，指定空间名称`identifier`，命名实体`named_entities`是一组变量、类型和函数

* 在外部访问命名空间中的对象需要加上范围运算符`::`

```
identifier::named_entity
```

* 可以在不同文件、不同位置多次定义同一个命名空间，里面的对象在同一个作用域内

* 命名空间可以嵌套定义

* 通常会将函数、类的声明和实现放置在两个文件中（头文件`.h`和源文件`.cpp`），如果在命名空间中定义函数声明，那么需要在函数实现代码加入完全限定符，类定义同样如此

### 示例一

声明命名空间`aaa`和`bbb`，声明相同变量名`x`和`y`，并访问

```
namespace aaa {
    int x;
    int y;

    void he() {
        cout << "hello zj" << endl;
    }
}

namespace bbb {
    char x;
    char y;
}

int main() {

    aaa::x = 3;
    cout << aaa::x << endl;

    bbb::x = '4';
    cout << bbb::x << endl;

    return 0;
}
```

结果

```
3
4
```

**使用命名空间可以有效解决名称冲突**

### 示例二

分离定义命名空间`aaa`

```
namespace aaa {
    int x;
    char y;
}

namespace aaa {
    void he() {
        cout << "hello aaa" << endl;
    }
}

int main() {

    aaa::x = 3;
    cout << aaa::x << endl;

    aaa::y = '4';
    cout << aaa::y << endl;

    aaa::he();

    return 0;
}
```

结果

```
3
4
hello aaa
```

### 示例三

头文件操作：在命名空间`zj`中声明函数`hello`和定义类`Te`

源文件操作：实现函数和类

```
# named.h
#ifndef FIRST_NAMED_H
#define FIRST_NAMED_H

#include <iostream>

namespace zj {
    void hello();

    class Te {
    public:
        Te();

        void hi();
    };
}

#endif //FIRST_NAMED_H

# named.cpp
#include "named.h"

void zj::hello() {

}

// 构造器
zj::Te::Te() {}

void zj::Te::hi() {

}
```

### 命名空间std

`c++`标准库中所有的实体（`变量、类型、常量和函数`）都定义在命名空间`std`中

## using

关键字`using`可以将名称引入当前声明区域，从而避免限定名称的需要

### 操作using

有`3`种方式可以访问`std`里面的对象，以`cout`为例：

方式一

```
#include <iostream>

std::cout << "hello cout";
```

不使用关键字`using`，使用完全受限的名称访问命名空间

方式二：

```
#include <iostream>
using namespace std;

cout << "hello cout";
```

使用关键字组合`using namespace`可以将整个命名空间`std`加入当前作用域

方式三

```
#include <iostream>
using std::cout;

cout <<"hello cout";
```

使用关键字`using`将`std`中的`cout`对象引入当前作用域，所以在接下来的操作中不需要加上限定符`std::`。不过访问`std`中的其他对象还是需要限定符

### 为什么尽量不要使用using namespace std？

网上一直有关于命名空间的讨论 - [为什么尽量不要使用using namespace std？](https://www.zhihu.com/question/26911239)

有很多意见哈，主要意见还是说不要把整个命名空间引入当前作用域，因为这违反了命名空间的初衷，所以还是尽量使用方式一和方式二进行操作

*头文件中的代码应始终使用完全限定的命名空间名称*

## 嵌套 vs. 内联

### 嵌套命名空间

可以定义嵌套命名空间，内部的命名空间可以直接访问外部命名空间的标识符，而外部命名空间必须使用限定符访问内部的命名空间

### 示例四

定义3层嵌套命名空间

```
namespace aaa {
    int x;
    int y;

    namespace bbb {
        void he() {
            x = 3;
            cout << x << endl;
        }

        namespace ccc {
            void hi() {
                he();
                cout << x << endl;
            }
        }
    }
}

int main() {
    aaa::bbb::ccc::hi();

    return 0;
}
```

结果

```
3
3
```

### 内联命名空间

内联命名空间是`c++11`的新特性。相比较于嵌套命名空间，内联命名空间的成员可直接看成外部空间的成员

可以使用内联命名空间作为版本控制机制来管理对库公共接口的更改。例如，可以创建单个父命名空间，并将接口的每个版本封装到嵌套在父命名空间中的自己的命名空间中。保存最新版本或首选版本的命名空间被限定为内联，因此被公开，就好像它是父命名空间的直接成员一样。调用`Parent::Class`的客户端代码将自动绑定到新代码。喜欢使用旧版本的客户机仍然可以通过使用具有该代码的嵌套命名空间的完全限定路径来访问它

### 示例五

```
namespace Test {
    namespace old_ns {
        std::string Func() { return std::string("Hello from old"); }
    }

    inline namespace new_ns {
        std::string Func() { return std::string("Hello from new"); }
    }

    std::string hi() {
        return Func();
    }
}

int main() {
    cout << Test::Func() << endl;
    cout << Test::hi() << endl;

    return 0;
}
```

结果

```
Hello from new
Hello from new
```

## 命名空间别名

参考：[Namespace aliases](https://en.cppreference.com/w/cpp/language/namespace_alias)

对于多重嵌套或者长字符的命名空间，可以使用别名方便访问。语法如下：

```
namespace new_name = current_name; 
```

### 示例六

在命名空间`aaa`内部设置命名空间`bbb`，可以使用限定符进行嵌套访问，也可以设置命名空间别名

```
namespace aaa {
    int x;
    char y;

    namespace bbb {
        void he() {
            cout << "hello aaa" << endl;
        }
    }
}

int main() {
    aaa::bbb::he();

    namespace aaabbb = aaa::bbb;

    aaabbb::he();

    return 0;
}
```

结果:

```
hello aaa
hello aaa
```

## 匿名或未命名空间

如果创建一个匿名空间（或称为未命名空间，`anonymous or unnamed namespace`），那么同一文件中的所有代码都可以看到未命名命名空间中的标识符，但标识符以及命名空间本身在该文件外部不可见

### 示例七

```
namespace {
    namespace old_ns {
        std::string Func() { return std::string("Hello from old"); }
    }

    inline namespace new_ns {
        std::string Func() { return std::string("Hello from new"); }
    }

    std::string hi() {
        return Func();
    }
}

int main() {
    cout << Func() << endl;
    cout << hi() << endl;
    cout << old_ns::Func() << endl;

    return 0;
}
```

结果

```
Hello from new
Hello from new
Hello from old
```