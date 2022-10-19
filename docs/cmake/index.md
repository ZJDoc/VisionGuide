
# 引言

不知不觉已经写了好多的`CMakeLists.txt`文件，对于基本的`CMake`语法也有了简单的理解和使用，记录一下常用的内容。

* [最小实现](./minimum.md)
* [结构优化](./optimization.md)
* [配置OpenCV](./opencv.md)


1. 配置opencv的几种方式：直接引用头文件和库文件（调试阶段是否可以额外引用源文件）；引用opencv提供的opencv.cmake文件


各大库提供的opencv.cmake文件是如何配置的

rpath的作用：build_with_rpath或者install_with_rpath

流程控制：IF语句使用

条件表达式：匹配、比较等命令

环境变量设置 set

打印消息 message(status/error/xxx)不同级别

如何判断当前所属环境：

1. 系统名称：Android/Linux/Win32/Win64
2. 系统所使用处理器：x86/arm

引用库和链接库的几种方式：include_libriries/find_library/set_target_libriry/target_link_libraries

include .cmake文件

创建动态库/静态库/可执行文件

设定调试和正式发布

交叉编译和正常编译的区别

ldd、LD_LIBRARY_PATH和xxx的使用

通配符使用，比如*.cpp

安装路径的配置：install(targets/files xxx destination xxx)

增加前缀

设置编译器：比如gcc g++路径，c++标准

指定工程名 以及 最小使用cmake版本