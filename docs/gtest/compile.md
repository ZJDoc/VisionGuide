
# 编译

在`Ubuntu`环境下使用`CMake`编译`Google Test`

## 编译

第一步，下载源码（切换到发布版本）

```
git clone https://github.com/google/googletest.git
cd googletest
git checkout -b release-1.12.1 release-1.12.1
```

第二步，编译静态库

```
mkdir build && cd build && cmake .. && make -j8
```

得到的静态库位于`/path/to/build/lib/`路径下

```
libgmock.a  libgmock_main.a  libgtest.a  libgtest_main.a
```

## 使用

`CMakeLists.txt`

```text
cmake_minimum_required(VERSION 3.20)
project(GTestDemo)

set(CMAKE_CXX_STANDARD 17)

include_directories(/home/zj/repos/googletest/googletest/include)
link_directories(/home/zj/repos/googletest/build/lib)
set(gtest_lib libgmock.a  libgmock_main.a  libgtest.a  libgtest_main.a)

add_executable(GTestDemo main.cpp)
target_link_libraries(GTestDemo ${gtest_lib} pthread)
```

`main.cpp`

```c++
#include "gtest/gtest.h"
#include <iostream>

int sum(int a, int b) {
  return a + b;
}

TEST(TestDemo, First) {
  int res = sum(3, 5);

  EXPECT_EQ(res, 8);
}

int main(int argc, char *argv[]) {
  ::testing::InitGoogleTest(&argc, argv);
  int res = RUN_ALL_TESTS();

  std::cout << "Hello, World!" << std::endl;
  return 0;
}
```

实现结果：

```
[==========] Running 1 test from 1 test suite.
[----------] Global test environment set-up.
[----------] 1 test from TestDemo
[ RUN      ] TestDemo.First
[       OK ] TestDemo.First (0 ms)
[----------] 1 test from TestDemo (0 ms total)

[----------] Global test environment tear-down
[==========] 1 test from 1 test suite ran. (0 ms total)
[  PASSED  ] 1 test.
Hello, World!

Process finished with exit code 0
```

## 相关阅读

* [Quickstart: Building with CMake](http://google.github.io/googletest/quickstart-cmake.html)