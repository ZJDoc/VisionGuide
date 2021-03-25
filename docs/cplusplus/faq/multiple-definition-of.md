
# multiple definition of

## 问题描述

新建头文件`macro.h`，添加全局变量

    #ifndef C_MACRO_H
    #define C_MACRO_H

    #include <iostream>
    using namespace std;

    // 人脸检测模型路径
    string FACE_CASCADE_PATH = "../../models/haarcascade_frontalface_default.xml";

    #endif //C_MACRO_H

编译时出错

    CMakeFiles/c__.dir/OpencvDetect.cpp.o:(.bss+0x0): multiple definition of `WINDOWS_NAME[abi:cxx11]'
    CMakeFiles/c__.dir/main.cpp.o:(.bss+0x0): first defined here

## 问题解析

头文件被多次引用，导致重复定义

解决：设置成常量，添加`const`关键字

    const string FACE_CASCADE_PATH = "../../models/haarcascade_frontalface_default.xml";