
# [OpenCV]Anaconda配置

有两种方式在`Anaconda`中配置`OpenCV`

1. 配置本地`OpenCV`源码编译的`python`包
2. `conda`安装（**推荐**）

## 在Anaconda中配置源码编译的opencv-python包

参考[[Ubuntu 16.04][Anaconda3]OpenCV-4.1.0安装](https://zj-image-processing.readthedocs.io/zh_CN/latest/opencv/[Ubuntu%2016.04][Anaconda3]OpenCV-4.1.0%E5%AE%89%E8%A3%85.html)，编译`OpenCV`源码后得到`python`包

参考[[Ubuntu 16.04][Anaconda3][Python3.6]OpenCV-3.4.2源码安装](https://zj-image-processing.readthedocs.io/zh_CN/latest/opencv/[Ubuntu%2016.04][Anaconda3][Python3.6]OpenCV-3.4.2%E6%BA%90%E7%A0%81%E5%AE%89%E8%A3%85.html)，将`python`包放置在`anaconda`指定位置

## conda安装

参考：

[OpenCV Linux Anaconda 源码安装](https://blog.csdn.net/u012005313/article/details/52985203)

[conda 安装指定版本的指定包](https://blog.csdn.net/weixin_37251044/article/details/79274202)

使用上述操作能够使用`python-opencv`，但是存在一个问题就是使用`PyCharm`时没有代码提示了。所以最好还是使用`conda`工具进行`opencv`安装

`conda`默认源下的`opencv`版本比较低，没有最新版本

```
$ conda search opencv
Loading channels: done
# Name                       Version           Build  Channel             
opencv                         3.3.1  py27h17fce66_0  pkgs/main           
opencv                         3.3.1  py27h61133dd_2  pkgs/main 
...
...
```

而使用源`conda-forge`能够得到最新版本的`OpenCV`，登录[conda-forge/packages/opencv](https://anaconda.org/conda-forge/opencv/files?sort=time&sort_order=desc&page=3)查询

```
$ conda search -c conda-forge opencv | grep 4.1.0
opencv                         4.1.0  py27h3aa1047_5  conda-forge         
opencv                         4.1.0  py27h3aa1047_6  conda-forge         
opencv                         4.1.0  py27h4a2692f_2  conda-forge 
...
...
```

下载指定版本的`python-opencv`

```
$ conda install -c conda-forge opencv=4.1.0 
```

## 后续问题

`PyCharm`使用`opencv`时，通过第一种方式安装无法得到代码提示，而通过第二种方式安装就可以，到底是为什么呢?

可能猜测：是不是`debug/release`关系