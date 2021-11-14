
# Ubuntu编译

## 实现步骤

```
$ git clone https://github.com/libjpeg-turbo/libjpeg-turbo.git
$ cd /path/to/libjpeg-turbo
# 编译、配置和安装
$ mkdir build
$ cd build
$ cmake -G"Unix Makefiles" -DCMAKE_INSTALL_PREFIX=../install ../
$ make -j8
$ make install
```

## 相关阅读

* [Building libjpeg-turbo](https://github.com/libjpeg-turbo/libjpeg-turbo/blob/main/BUILDING.md)