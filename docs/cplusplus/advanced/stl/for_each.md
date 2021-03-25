
# [c++11][stl]for_each

参考：[std::for_each](http://www.cplusplus.com/reference/algorithm/for_each/?kw=for_each)

使用`for_each`函数对指定范围内的数值逐个进行函数操作

最常用的就是遍历操作

```
#include <iostream>     // std::cout
#include <algorithm>    // std::for_each
#include <vector>       // std::vector

void myfunction(int i) {  // function:
    std::cout << ' ' << i;
}

struct myclass {           // function object type:
    void operator()(int i) { std::cout << ' ' << i; }
} myobject;

int main() {
    std::vector<int> myvector;
    myvector.emplace_back(10);
    myvector.emplace_back(20);
    myvector.emplace_back(30);

    std::cout << "myvector contains:";
    for_each(myvector.begin(), myvector.end(), myfunction);
    std::cout << '\n';

    // or:
    std::cout << "myvector contains:";
    for_each(myvector.begin(), myvector.end(), myobject);
    std::cout << '\n';

    return 0;
}
```