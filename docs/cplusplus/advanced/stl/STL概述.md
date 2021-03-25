
# STL概述

`C++ STL(standard template library，标准模板库)`提供了许多高效的容器、算法和迭代器

## 容器

参考：

[Containers (Modern C++)](https://docs.microsoft.com/en-us/cpp/cpp/containers-modern-cpp?view=vs-2019)

[C++ Standard Library Containers](https://docs.microsoft.com/en-us/cpp/standard-library/stl-containers?view=vs-2019)

容器是用来管理某一类对象的集合。它们被实现为类模板，这允许在元素支持的类型中具有很大的灵活性。完整容器列表参考[Container class templates](http://www.cplusplus.com/reference/stl/)

容器可以分为三类：序列容器、关联容器和容器适配器

* 对于序列容器（`sequential container`），推荐使用`vector`
* 对于关联容器（`associate container`），推荐使用`map`

### 序列容器

序列容器能够维护指定的插入元素的顺序

* `vector`：其操作类似于数组，它是随机存取和连续存储的，长度是高度灵活的
* `array`：`array`容器具有`vector`的一些优点，但是长度不是灵活的
* `deque`：双端队列（`double-ended queue`）允许在容器开头和结尾的快速插入和删除。它具有向量的随机访问和柔性长度的优点，但不是连续的
* `list`：是一个双链接列表，它允许在容器中的任何位置进行双向访问、快速插入和快速删除，但不能随机访问容器中的元素
* `forward_list`：单链表，`list`的前向访问版本

### 关联容器

在关联容器中，元素以预定义的顺序插入，例如按升序排序。也可以使用无序的关联容器。关联容器可以分为两个子集：map和set

* `map`：也称为字典（`dictionary`），由键/值对（`key/value pair`）组成。键用于对序列排序，值与该键关联。例如，`map`可能包含表示文本中每个唯一单词的键和表示每个单词在文本中出现的次数的相应值。`map`的无序版本是[unordered_map](https://docs.microsoft.com/en-us/cpp/standard-library/unordered-map-class?view=vs-2019)
* `set`：单元素的升序排列容器，其值也是键。未排序版本称为[unordered_set](https://docs.microsoft.com/en-us/cpp/standard-library/unordered-set-class?view=vs-2019)

`map`和`set`都只允许将键或元素的一个实例插入到容器中。如果需要元素的多个实例，使用`multimap`和`multiset`。它们的未排序版本就是`unordered_multimap`和`unordered_multiset`

有序映射和集合支持双向迭代器（`bi-directional iterators`），它们的无序对应项支持正向迭代器（`forward iterators`）

### 容器适配器

容器适配器是序列容器和关联容器的变体，其简化了接口。容器适配器不支持迭代器

* `queue`：先进先出（`FIFO`）操作
* `stack`：后进先出（`LIFO`）操作
* `priority_queue`：最高值元素始终位于队列第一位

### 容器元素要求

* 通用要求是容器元素是可复制的。但是只要在操作中不涉及复制操作，也可以工作
* 析构函数不允许引发异常
* 对于有序关联容器而言，其对象必须定义了`public`比较运算符（`opeator<`）
* 容器上的某些操作可能还需要公共默认构造函数和公共等价运算符。例如，无序关联容器需要支持相等和散列

### 容器比较

所有容器均重载了`operator==`，可用于保存相同类型元素的相同类型容器之间的比较，比如`vector<string>`和`vector<string>`之间的比较

## 算法

参考：[Algorithms (Modern C++)](https://docs.microsoft.com/en-us/cpp/cpp/algorithms-modern-cpp?view=vs-2019)

`C++`实现了许多算法，常用的有以下几项：

1. 遍历算法：`for_each`
2. 搜索算法：`find_if/count_if/remove_if`
3. 排序算法：`sort/lower_bound/upper_bound`