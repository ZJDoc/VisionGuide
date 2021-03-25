
# [c++11][stl][shuffle]随机重排列

参考：[std::shuffle](http://www.cplusplus.com/reference/algorithm/shuffle/)

`c++`实现了`shuffle`函数用于随机重新排列指定范围内的元素，使用均匀随机数发生器

```
// shuffle algorithm example
#include <iostream>     // std::cout
#include <algorithm>    // std::shuffle
#include <array>        // std::array
#include <random>       // std::default_random_engine
#include <chrono>       // std::chrono::system_clock

int main() {
    std::array<int, 5> foo{1, 2, 3, 4, 5};

    // obtain a time-based seed:
    long seed = std::chrono::system_clock::now().time_since_epoch().count();

    shuffle(foo.begin(), foo.end(), std::default_random_engine(seed));

    std::cout << "shuffled elements:";
    for (int &x: foo) std::cout << ' ' << x;
    std::cout << '\n';

    return 0;
}
```