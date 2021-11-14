
# libjpeg-turbo概述

[libjpeg-turbo](https://github.com/libjpeg-turbo/libjpeg-turbo)是一个图像编解码库，专门支持JPEG数据的编码和解码操作，支持不同平台和不同颜色空间，相比于`libjpeg`库加速了`2x~6x`，据说也比`OpenCV`快。

使用`libjpeg-turbo`可以进行`jpeg`图像的解析，获取字节数据以及宽/高等信息，可以作为`OpenCV`的替代（*因为相对而言编译和使用更加简单*）

* 官网地址：[libjpeg-turbo/libjpeg-turbo](https://github.com/libjpeg-turbo/libjpeg-turbo)
* 示例程序：[libjpeg-turbo/tjexample.c ](https://github.com/libjpeg-turbo/libjpeg-turbo/blob/main/tjexample.c)

本地示例实现位于`libjpeg/`