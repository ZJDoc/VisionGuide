
# size_t

参考：

[size_t](http://www.cplusplus.com/reference/cstddef/size_t/?kw=size_t)

[std::size_t](https://en.cppreference.com/w/cpp/types/size_t)

无符号整数值，可作为基本无符号整数类型的别名

它是一种能够以字节表示任何对象大小的类型：`size_t`是`sizeof`运算符返回的类型，在标准库中广泛用于表示大小和计数

```
#include <cstddef>
#include <iostream>
#include <array>
 
int main()
{
    std::array<std::size_t,10> a;
    for (std::size_t i = 0; i != a.size(); ++i)
        a[i] = i;
    for (std::size_t i = a.size()-1; i < a.size(); --i)
        std::cout << a[i] << " ";
}
```