
# [Ubuntu 16.04][Anaconda3][OpenCV_Contrib 4.0.1]编译OpenCV4Android

`OpenCV4.0.1`中的人脸识别模块被移植到了`opencv_contrib`仓库,官网没有编译好的`OpenCV4Android`包,所以需要自己编译

前后大概花了两天时间,一个是需要配置许多依赖,另外一个是官网没有很好的提供对于编译选项的解释,导致多次编译错误

`OpenCV`在`2.x/3.x/4.x`的迭代中有了很多的改变,`NDK`同样也有改变,可能不再支持一些版本,或者指定一些版本工具

为了减少编译错误,当前使用最新的配置环境

## 源码下载

下载[OpenCV-4.0.1压缩包](https://opencv.org/releases.html)以及[OpenCV_Contrib仓库](https://github.com/opencv/opencv_contrib),

    $ wget https://github.com/opencv/opencv/archive/4.0.1.zip
    $ git clone https://github.com/opencv/opencv_contrib.git

*注意:切换opencv_contrib到4.0.1版本*

## 配置环境

当前操作系统:`Ubuntu 16.04`

`NDK:android-ndk-r18b`

`cmake:`

    $ cmake --version
    cmake version 3.14.0-rc3

    CMake suite maintained and supported by Kitware (kitware.com/cmake).

`ninja:`

    $ ninja --version
    1.8.2

`java:`

    $ java -version
    java version "1.8.0_201"
    Java(TM) SE Runtime Environment (build 1.8.0_201-b09)
    Java HotSpot(TM) 64-Bit Server VM (build 25.201-b09, mixed mode)

`ant:`

    $ ant -version
    Apache Ant(TM) version 1.10.5 compiled on July 10 2018

`python:`

    $ python --version
    Python 3.6.8 :: Anaconda, Inc.

同时设置环境变量

    # cmake
    export PATH=/home/zj/software/cmake/cmake-3.14.0-rc3-Linux-x86_64/bin:$PATH

    # ant
    export ANT_HOME=/home/zj/software/ant/apache-ant-1.10.5
    export PATH=$PATH:$ANT_HOME/bin

    ## android
    export ANDROID_NDK=/home/zj/Android/android-ndk-r18b
    export ANDROID_SDK=/home/zj/Android/Sdk
    export ANDROID_HOME=/home/zj/Android/Sdk

    # JAVA
    export JAVA_HOME=/home/zj/software/java/jdk1.8.0_201
    export CLASSPATH=.:$JAVA_HOME/lib:$JRE_HOME/lib:$CLASSPATH
    export PATH=$JAVA_HOME/bin:$JRE_HOME/bin:$PATH
    export JRE_HOME=$JAVA_HOME/jre

## 编译脚本

在`opencv-4.0.1/platforms/android`文件夹内有编译脚本`build_sdk.py`

    $ ./build_sdk.py --help 
    usage: build_sdk.py [-h] [--config CONFIG] [--ndk_path NDK_PATH]
                        [--sdk_path SDK_PATH]
                        [--extra_modules_path EXTRA_MODULES_PATH]
                        [--sign_with SIGN_WITH] [--build_doc] [--no_ccache]
                        [--force_copy] [--force_opencv_toolchain]
                        [work_dir] [opencv_dir]

    Build OpenCV for Android SDK

    positional arguments:
    work_dir              Working directory (and output)
    opencv_dir            Path to OpenCV source dir

    optional arguments:
    -h, --help            show this help message and exit
    --config CONFIG       Package build configuration
    --ndk_path NDK_PATH   Path to Android NDK to use for build
    --sdk_path SDK_PATH   Path to Android SDK to use for build
    --extra_modules_path EXTRA_MODULES_PATH
                            Path to extra modules to use for build
    --sign_with SIGN_WITH
                            Certificate to sign the Manager apk
    --build_doc           Build javadoc
    --no_ccache           Do not use ccache during library build
    --force_copy          Do not use file move during library build (useful for
                            debug)
    --force_opencv_toolchain
                                Do not use toolchain from Android NDK

执行脚本程序

    python build_sdk.py --config=ndk-18.config.py --extra_modules_path=/home/zj/opencv/opencv_contrib/modules --no_ccache /home/zj/opencv/opencv-4.0.1/build_android/ /home/zj/opencv/opencv-4.0.1

* 参数`config`指定了要编译的指令集,文件`ndk-18.config.py`是`opencv`自带的,里面指定了`armeabi-v7a/arm64-v8a/x86_64/x86`
* 参数`extra_modules_path`用于指定`opencv_contrib`的路径
* 参数`no_ccache`能够避免编译错误
* 还需要设置`work_dir`以及`opencv_dir`

**注意:如果没有在之前没有设置过`NDK`和`SDK`的环境变量,需要在执行脚本时添加**

    --ndk_path NDK_PATH ... --sdk_path SDK_PATH ...

使用该脚本能够实现`opencv4android`编译,但是还需要在里面修改一些参数

一个方面是禁止对于`Android`工程/服务的编译,因为这涉及到外网连接,常常会失败；另一个方面是为了编译`libopencv_java4.so`,需要打开一些开关

修改`build_sdk.py`中的`build_library`函数

    # 原先
    def build_library(self, abi, do_install):
        cmd = ["cmake", "-GNinja"]
        cmake_vars = dict(
            CMAKE_TOOLCHAIN_FILE=self.get_toolchain_file(),
            INSTALL_CREATE_DISTRIB="ON",
            WITH_OPENCL="OFF",
            WITH_IPP=("ON" if abi.haveIPP() else "OFF"),
            WITH_TBB="ON",
            BUILD_EXAMPLES="OFF",
            BUILD_TESTS="OFF",
            BUILD_PERF_TESTS="OFF",
            BUILD_DOCS="OFF",
            BUILD_ANDROID_EXAMPLES="OFF",
            INSTALL_ANDROID_EXAMPLES="OFF",
    )
    # 修改后
    def build_library(self, abi, do_install):
        cmd = ["cmake", "-GNinja"]
        cmake_vars = dict(
            CMAKE_TOOLCHAIN_FILE=self.get_toolchain_file(),
            INSTALL_CREATE_DISTRIB="ON",
            WITH_OPENCL="OFF",
            WITH_IPP=("ON" if abi.haveIPP() else "OFF"),
            WITH_TBB="ON",
            BUILD_EXAMPLES="OFF",
            BUILD_TESTS="OFF",
            BUILD_PERF_TESTS="OFF",
            BUILD_DOCS="OFF",
            BUILD_ANDROID_EXAMPLES="OFF",
            INSTALL_ANDROID_EXAMPLES="OFF",
            BUILD_ANDROID_SERVICE="OFF",
            CMAKE_BUILD_TYPE="RELEASE",
            BUILD_ZLIB="ON"
        )

### 编译问题

问题一:

    CMake Error: CMake was unable to find a build program corresponding to "Ninja".  CMAKE_MAKE_PROGRAM is not set.  You probably need to select a different build tool.

缺少`ninja`,下载安装

    conda install ninja

问题二:

    CMake Error at /home/zj/Android/android-ndk-r16b/build/cmake/android.toolchain.cmake:40 (cmake_minimum_required):
    CMake 3.6.0 or higher is required.  You are running version 3.5.1

下载[CMake](https://cmake.org/download/)源码编译安装

问题三:

    CMake Error at /home/zj/software/cmake/cmake-3.14.0-rc3-Linux-x86_64/share/cmake-3.14/Modules/CMakeTestCXXCompiler.cmake:53 (message):
    The C++ compiler

        "/home/zj/Android/android-ndk-r16b/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/bin/arm-linux-androideabi-g++"

    is not able to compile a simple test program.
    ...
    ...
    /bin/sh: 1: ccache: not found
    ninja: build stopped: subcommand failed.

问题四:编译完成后没有`libopencv_java.so`

参考:

[Building OpenCV4Android from source does not output libopencv_java.so](https://stackoverflow.com/questions/44593680/building-opencv4android-from-source-does-not-output-libopencv-java-so)

[creat libopencv_java.so from source](https://github.com/opencv/opencv/issues/7023)

这个没有很好理解,但是通过添加`CMAKE_BUILD_TYPE="RELEASE"`能够解决这个问题

## `cmake`解析

参考:[libc++](https://developer.android.com/ndk/guides/cpp-support?hl=zh-cn#libc)

执行`build_sdk.py`就能够实现`opencv4android`编译,里面调用了`cmake`进行构建,执行如下

    cmake -GNinja -DOPENCV_EXTRA_MODULES_PATH='/home/zj/opencv/opencv_contrib/modules' -DCMAKE_TOOLCHAIN_FILE='/home/zj/Android/android-ndk-r18b/build/cmake/android.toolchain.cmake' -DINSTALL_CREATE_DISTRIB='ON' -DWITH_OPENCL='OFF' -DWITH_IPP='OFF' -DWITH_TBB='ON' -DBUILD_EXAMPLES='OFF' -DBUILD_TESTS='OFF' -DBUILD_PERF_TESTS='OFF' -DBUILD_DOCS='OFF' -DBUILD_ANDROID_EXAMPLES='OFF' -DINSTALL_ANDROID_EXAMPLES='OFF' -DBUILD_ANDROID_SERVICE='OFF' -DCMAKE_BUILD_TYPE='RELEASE' -DBUILD_ZLIB='ON' -DANDROID_STL='c++_static' -DANDROID_ABI='arm64-v8a' -DANDROID_PLATFORM_ID='3' -DANDROID_TOOLCHAIN='clang' /home/zj/opencv/opencv-4.0.1

参数`CMAKE_TOOLCHAIN_FILE`指定了交叉编译的配置文件,使用的是`NDK`包里面的`android.toolchain.cmake`  

参数`ANDROID_STL`指定了编译用的标准库,这是因为`Android`自`NDK r18`以来指定了`c++_static`作为唯一可用的`STL`

## 相关参考

`OpenCV`提供了一个非正式的编译库:[master-contrib_pack-contrib-android/](https://pullrequest.opencv.org/buildbot/export/opencv_releases/master-contrib_pack-contrib-android/)

## 相关阅读

* [taka-no-me/android-cmake](https://blog.csdn.net/wuzuyu365/article/details/53708535)

* [Building OpenCV4Android from source code](https://github.com/davidmigloz/go-bees/wiki/Building-OpenCV4Android-from-source-code)

* [OpenCV移动端之CMake Android交叉编译](https://blog.csdn.net/xxboy61/article/details/80953288)

* [OpenCV4Android编译](http://blog.sina.com.cn/s/blog_602f87700102vdnw.html)
