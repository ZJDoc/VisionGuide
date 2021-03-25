
# [c++11][stl]queue

`c++`提供了队列的实现：[queue](http://www.cplusplus.com/reference/queue/queue/)，实现先进先出（`first-in first-out, FIFO`）功能

## 创建队列

引入头文件`queue`，创建时指定数据类型：

```
#include <queue>

queue<int> q;
```

## 队列功能

`queue`提供了如下常用功能实现：

* empty()：判断队列是否问空，为空返回`true`，不为空返回`false`
* size()：返回队列长度
* front()：返回队头（第一个出队）数据
* back()：返回队尾（第一个入队）数据
* push(value_type&& __x)：添加数据到队尾
* pop()：移除队头数据。注意，返回值为空

`c++11`提供了两个新特性：

* [swap](http://www.cplusplus.com/reference/queue/queue/swap/)：交换两个队列的值
* [emplace](http://www.cplusplus.com/reference/queue/queue/emplace/)：添加数据到队尾。这个新元素是就地（`in place`）构造的，它传递参数作为其构造函数的参数，可替换push操作

*参考：[C++11中emplace的使用](https://blog.csdn.net/u013700358/article/details/52623985)：emplace能通过参数构造对象，不需要拷贝或者移动内存，相比push能更好地避免内存的拷贝与移动，使容器插入元素的性能得到进一步提升*

## 实现

```
#include <iostream>
#include <queue>
using namespace std;

int main() {
    queue<int> q;
    // 队列大小
    cout << q.size() << endl;
    // 队列是否为空
    cout << q.empty() << endl;

    q.push(3);
    q.push(4);
    q.emplace(5);

    // 队头元素
    cout << q.front() << endl;
    // 队尾元素
    cout << q.back() << endl;

    queue<int> s;
    s.push(3232);

    q.swap(s);
    cout << q.size() << endl;
    cout << q.empty() << endl;
}
```