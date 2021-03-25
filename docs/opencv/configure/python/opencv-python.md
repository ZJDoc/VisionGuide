
# [opencv-python]编译与安装

仓库[skvark/opencv-python](https://github.com/skvark/opencv-python)配置了`Python OpenCV`包编译环境

相比较于自编译的`Python`实现，`skvark/opencv-python`有以下优点：

1. 可以通过`pip`方式安装预编译包
2. 编译得到的`cv2`文件能够提供相应的`Python`定义（*就是`PyCharm`编程时可以点击函数查看相关定义*）

其缺点就是实现速度比自编译包慢（参考[OpenCV-4.4.0安装](../4.4.0/安装.md)）

## pip安装

`skvark/opencv-python`提供了多种形式的预编译包

```
$ pip install opencv-python
$ pip install opencv-contrib-python
$ pip install opencv-python-headless
$ pip install opencv-contrib-python-headless
```

其中`*-contrib-*`表示包含了第三方模块，`*-headless`表示不包含`GUI`函数，适用于服务器版本`/Docker`版本

也可以指定版本安装，比如

```
$ pip install opencv-contrib-python==4.4.0.46
```

## 编译安装

当前想要通过加载中文字体，需要使用`freetype`库，`OpenCV`集成了该模块，不过在`skvark/opencv-python`中默认没有编译，需要自编译实现

1. 下载源码

```
git clone --recursive https://github.com/skvark/opencv-python.git
```

2. 设置`CMake`符号

```
export CMAKE_ARGS="-DWITH_FREETYPE=ON"
```

3. 设置第三方模块编译

```
export ENABLE_CONTRIB=1 
```

4. 编译

```
pip wheel . --verbose. 
```

编译完成后即可生成对应的`wheel -  opencv_contrib_python-4.4.0.46-cp37-cp37m-linux_x86_64.whl`

5. 安装

```
pip install opencv_contrib_python-4.4.0.46-cp37-cp37m-linux_x86_64.whl
```

## 问题一：xfeatures2d/boostdesc: Download failed: 28;"Timeout was reached"

参考[安装opencv时，xfeatures2d模块缺失boostdesc_bgm.i文件，下载超时问题](https://blog.csdn.net/sazass/article/details/108406518)

## 问题二： ippicv_2020_lnx_intel64_20191018_general.tgz

参考[ubuntu安装opencv无法下载IPPICV的问题 ippicv_2020_lnx_intel64_20191018_general.tgz](https://blog.csdn.net/gadwgdsk/article/details/107423625)