
# [c++11][stl]find

参考：[std::find](http://www.cplusplus.com/reference/algorithm/find/)

`C++`提供了丰富的查询函数

* `find`
* `find_end`
* `find_first_of`
* `find_if`
* `find_if_not`

## find_if

参考：[std::find_if](http://www.cplusplus.com/reference/algorithm/find_if/)

函数`find_if`发现指定范围内（不包含最后一个位置）是否存在数值符合条件

如果存在，返回第一个符合条件的迭代器；如果不存在，返回最后一个值的迭代器

```
// find_if example
#include <iostream>     // std::cout
#include <algorithm>    // std::find_if
#include <vector>       // std::vector

bool IsOdd(int i) {
    return ((i % 2) == 1);
}

int main() {
    std::vector<int> myvector;

    myvector.push_back(10);
    myvector.push_back(25);
    myvector.push_back(40);
    myvector.push_back(55);

    std::vector<int>::iterator it = std::find_if(myvector.begin(), myvector.end(), IsOdd);
    std::cout << "The first odd value is " << *it << '\n';

    return 0;
}
```