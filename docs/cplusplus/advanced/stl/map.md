
# [c++11][stl]map

参考：[std::map](http://www.cplusplus.com/reference/map/map/)

`map`是存储键/值对的关联容器

## 头文件

```
#include <map>
```

## 使用

```
#include <map>

template<typename T, typename U>
void forward_print(std::map<T, U> maps) {
//    for (auto it = maps.begin(); it != maps.end(); ++it)
//        std::cout << it->first << " => " << it->second << ' ';

    for (auto &x:maps) {
        std::cout << x.first << " => " << x.second << ' ';
    }
    std::cout << std::endl;
}

int main() {
    // 创建
    std::map<int, int> maps;
    // 添加
    for (int i = 0; i < 10; i++) {
        maps.emplace(i, i + 1);
    }
    forward_print(maps);

    // 修改
    // 第二个位置，从0开始
    maps[1] = 444;
    forward_print(maps);

    // 删除
    // 先查找再删除
    std::map<int, int>::iterator it = maps.find(3);
    maps.erase(it);
    // 按键删除
    maps.erase(4);
    forward_print(maps);
    // 删除所有
    maps.clear();
    std::cout << "size: " << maps.size() << std::endl;
    std::cout << "isEmpty: " << maps.empty() << std::endl;
}
```