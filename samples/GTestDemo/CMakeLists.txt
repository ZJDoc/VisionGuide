cmake_minimum_required(VERSION 3.20)
project(GTestDemo)

set(CMAKE_CXX_STANDARD 17)

include_directories(/home/zj/repos/googletest/googletest/include)
link_directories(/home/zj/repos/googletest/build/lib)
set(gtest_lib libgmock.a libgmock_main.a libgtest.a libgtest_main.a)

add_executable(GTestDemo gtest_main.cpp gtest_two.cpp)
target_link_libraries(GTestDemo ${gtest_lib} pthread)
