
# [c++11][stl]stack

`c++`提供了栈的实现：[queue](http://www.cplusplus.com/reference/queue/queue/)，实现后进先出（`last-in first-out, LIFO`）功能

## 创建栈

引入头文件`stack`，创建时指定数据类型：

```
#include <stack>

stack<int> s;
```

## 栈功能

`stack`提供了如下常用功能实现：

* empty()：判断栈是否问空，为空返回`true`，不为空返回`false`
* size()：返回栈长度
* top()：返回栈顶数据
* push(value_type&& __x)：插入数据到栈顶
* pop()：移除栈顶数据。注意，返回值为空

`c++11`提供了两个新特性：

* [swap](http://www.cplusplus.com/reference/stack/stack/swap/)：交换两个栈的值
* [emplace](http://www.cplusplus.com/reference/stack/stack/emplace/)：添加数据到栈顶。这个新元素是就地（`in place`）构造的，它传递参数作为其构造函数的参数，可替换push操作

*参考：[C++11中emplace的使用](https://blog.csdn.net/u013700358/article/details/52623985)：emplace能通过参数构造对象，不需要拷贝或者移动内存，相比push能更好地避免内存的拷贝与移动，使容器插入元素的性能得到进一步提升*


## 实现

```
    stack<int> s;
    // 栈大小
    cout << s.size() << endl;
    // 栈是否为空
    cout << s.empty() << endl;

    s.push(3);
    s.push(4);
    s.emplace(5);

    // 栈顶元素
    cout << s.top() << endl;

    stack<int> s2;
    s2.push(3232);

    s2.swap(s);
    cout << s.size() << endl;
    cout << s.empty() << endl;
    cout << s.top() << endl;
}
```