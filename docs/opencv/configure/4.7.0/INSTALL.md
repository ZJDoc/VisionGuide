
# 4.7.0安装

目前OpenCV最新版本是[OpenCV 4.7.0](https://github.com/opencv/opencv/releases/tag/4.7.0)，前几天尝试编译了一下，发觉比之前更加简单了，记录一下

## 安装文档

* [OpenCV installation overview](https://docs.opencv.org/4.7.0/d0/d3d/tutorial_general_install.html)
* [OpenCV configuration options reference](https://docs.opencv.org/4.7.0/db/d05/tutorial_config_reference.html)
* [Installation in Linux](https://docs.opencv.org/4.7.0/d7/d9f/tutorial_linux_install.html)

## 安装操作

官网给出的安装流程如下：

```shell
# Install minimal prerequisites (Ubuntu 18.04 as reference)
sudo apt update && sudo apt install -y cmake g++ wget unzip
# Download and unpack sources
wget -O opencv.zip https://github.com/opencv/opencv/archive/4.x.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.x.zip
unzip opencv.zip
unzip opencv_contrib.zip
# Create build directory and switch into it
mkdir -p build && cd build
# Configure
cmake -DOPENCV_EXTRA_MODULES_PATH=../opencv_contrib-4.x/modules ../opencv-4.x
# Build
cmake --build .
```

在Configure阶段，我增加了一些安装选项，包括安装路径、Python安装等

```shell
cmake -D CMAKE_INSTALL_PREFIX=../install \
                -D OPENCV_EXTRA_MODULES_PATH=../opencv_contrib/modules \
                -D BUILD_opencv_python3=ON \
                -D PYTHON3_EXECUTABLE=~/anaconda3/bin/python \
                -D PYTHON_LIBRARIES=~/anaconda3/lib \
                -D PYTHON_INCLUDE_DIRS=~/anaconda3/include \
                ..
```

然后执行编译和安装

```shell
cmake --build . && make -j12
```