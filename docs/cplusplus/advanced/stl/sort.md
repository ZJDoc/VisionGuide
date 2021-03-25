
# [stl]sort

参考：[详细解说 STL 排序(Sort) ](http://www.cppblog.com/mzty/archive/2005/12/15/1770.aspx)

`STL`库提供了排序算法的实现，其中一个就是[std::sort](http://www.cplusplus.com/reference/algorithm/sort/?kw=sort)

函数`sort`默认按**升序**进行排序，也可以自定义比较算子

## 头文件

```
#include <algorithm>
```

## 熟悉

```
// sort algorithm example
#include <iostream>     // std::cout
#include <algorithm>    // std::sort
#include <vector>       // std::vector

bool myfunction(int i, int j) { return (i < j); }

bool greater_than(int i, int j) {
    return i > j;
}

struct myclass {
    bool operator()(int i, int j) { return (i < j); }
} myobject;

void zprint(std::vector<int> myvector) {
    for (int n:myvector) {
        std::cout << ' ' << n;
    }
    std::cout << '\n';
}

int main() {
    int myints[] = {32, 71, 12, 45, 26, 80, 53, 33};
   c++/multiple definition of
    std::vector<int> myvector(myints, myints + 8);               // 32 71 12 45 26 80 53 33

    // using default comparison (operator <):
    std::sort(myvector.begin(), myvector.begin() + 4);           //(12 32 45 71)26 80 53 33

    zprint(myvector);

    // using function as comp
    std::sort(myvector.begin() + 4, myvector.end(), myfunction); // 12 32 45 71(26 33 53 80)

    zprint(myvector);

    // using object as comp
    std::sort(myvector.begin(), myvector.end(), myobject);     //(12 26 32 33 45 53 71 80)

    zprint(myvector);

    sort(myvector.begin(), myvector.end(), greater_than);

    zprint(myvector);

    return 0;
}
```

结果

```
 12 32 45 71 26 80 53 33
 12 32 45 71 26 33 53 80
 12 26 32 33 45 53 71 80
 80 71 53 45 33 32 26 12
```

## 性能

参考：[排序 0 - 前言](https://blog.csdn.net/u012005313/article/details/78162666)

平均时间复杂度为`O(NlogN)`，是不稳定排序（*稳定排序参考[stable_sort](http://www.cplusplus.com/stable_sort)*）