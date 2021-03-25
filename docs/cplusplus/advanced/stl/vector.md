
# [c++11][stl]vector

参考：[std::vector](http://www.cplusplus.com/reference/vector/vector/)

`vector`是序列容器，它是可以改变大小的数组

## 头文件

```
#include <vector>
```

## 把一个vector追加到另一个vector

参考：[Vector 把一个vector追加到另一个vector](https://blog.csdn.net/Fly_as_tadpole/article/details/82710781)

```
std::vector<int> src;
std::vector<int> dest;
dest.insert(dest.end(), src.begin(), src.end());
```

## 使用

```
#include <vector>

void forward_print(std::vector<int> vecs) {
//    for (auto it = vecs.cbegin(); it != vecs.cend(); ++it) {
//        std::cout << " " << *it;
//    }
//    std::cout << std::endl;

    for (auto &x: vecs) {
        std::cout << " " << x;
    }
    std::cout << std::endl;
}

void backward_print(std::vector<int> vecs) {
    for (auto it = vecs.crbegin(); it != vecs.crend(); ++it) {
        std::cout << " " << *it;
    }
    std::cout << std::endl;
}

int main() {
    // 创建
    std::vector<int> vectors;
    // 添加
    for (int i = 0; i < 10; i++) {
        vectors.emplace_back(i + 1);
    }
    forward_print(vectors);

    // 插入
    // 第二个位置
    vectors.emplace(vectors.begin() + 1, 333);
    forward_print(vectors);

    // 修改
    // 第二个位置，从0开始
    vectors.at(1) = 444;
    forward_print(vectors);

    // 删除
    // 最后一个位置
    vectors.pop_back();
    forward_print(vectors);
    // 删除第3个
    vectors.erase(vectors.begin() + 2);
    forward_print(vectors);
    // 删除所有
    vectors.clear();
    std::cout << "size: " << vectors.size() << std::endl;
}
```