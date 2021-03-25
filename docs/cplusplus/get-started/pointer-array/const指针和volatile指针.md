
# const指针和volatile指针

参考：[const and volatile Pointers](https://docs.microsoft.com/en-us/cpp/cpp/const-and-volatile-pointers?view=vs-2019)

## const

`const`可用于指针的两方面，一是指针所指对象值，二是指针存储地址值

### 常量指针

声明指针所指对象为`const`，即为常量指针，语法如下：

```
const char *p;
```

声明常量指针后可以赋值指针另一个对象地址，但是无法通过指针修改对象值（*可以通过对象本身进行修改*），比如

```
char a = 'A';
const char *p = &a;
//    *p = 'D'; // error, *p只读

cout << (void *) &a << endl;
cout << (void *) p << endl;

a = 'B';

cout << (void *) &a << endl;
cout << (void *) p << endl;

char b = 'C';
p = &b;

cout << (void *) &a << endl;
cout << (void *) p << endl;
cout << (void *) &b << endl;
```

### 指针常量

声明指针值（即指针存储地址）为`const`，即为指针常量，语法如下：

```
char const *p;
```

声明指针常量后可以通过指针修改对象值，但是无法赋值指针另一个对象地址。示例如下

```
char a = 'A';
char *const p = &a;

cout << (void *) &a << endl;
cout << (void *) p << endl;

a = 'B';

cout << (void *) &a << endl;
cout << (void *) p << endl;

cout << a << endl;
cout << *p << endl;

char b = 'C';
//    p = &b; // error，指针p存储的地址固定为a
```

### 常量指针 vs. 指针常量

1. 常量指针可看成对象的`const`类型，只能读取对象值而不能修改
2. 指针常量可看成对象的别名，其存储地址固定为初始对象地址

可同时声明指针为常量指针和指针常量

```
const char *const p = &a;
```

此时指针`p`可看成对象`a`的别名，同时不能通过`p`修改对象值

## volatile

`volatile`关键字的语法和`const`一样，可作用于所指对象或者指针存储地址

```
// 作用于对象
volatile char *vpch;
// 作用于指针地址
char * volatile pchv;
```

`volatile`关键字指定了可以通过用户应用程序中的操作以外的操作进行修改，对于在共享内存中声明可由多个进程或用于与中断服务例程通信的全局数据区域访问的对象非常有用

当对象声明为`volatile`时，每次程序访问编译器都将从存储器中获取对象值。这极大地减少了可能的优化。如果对象的状态无法预期时，这是确保可预测的程序性能的唯一途径