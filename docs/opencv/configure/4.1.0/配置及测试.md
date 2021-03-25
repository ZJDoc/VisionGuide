
# [Ubuntu 16.04][Anaconda3]OpenCV-4.1.0配置及测试

## 环境变量

编辑`~/.bashrc`

```
# opencv4.1.0
export OpenCV_DIR=/home/zj/opencv/opencv-4.1.0/install
export PKG_CONFIG_PATH=${OpenCV_DIR}/lib/pkgconfig
export CMAKE_PREFIX_PATH=${OpenCV_DIR}
```

## 查询

```
$ pkg-config --cflags opencv4
-I/home/zj/opencv/opencv-4.1.0/install/include/opencv4/opencv -I/home/zj/opencv/opencv-4.1.0/install/include/opencv4
$ pkg-config --libs opencv4
-L/home/zj/opencv/opencv-4.1.0/install/lib -lopencv_gapi -lopencv_stitching -lopencv_aruco -lopencv_bgsegm -lopencv_bioinspired -lopencv_ccalib -lopencv_dnn_objdetect -lopencv_dpm -lopencv_face -lopencv_freetype -lopencv_fuzzy -lopencv_hdf -lopencv_hfs -lopencv_img_hash -lopencv_line_descriptor -lopencv_quality -lopencv_reg -lopencv_rgbd -lopencv_saliency -lopencv_stereo -lopencv_structured_light -lopencv_phase_unwrapping -lopencv_superres -lopencv_optflow -lopencv_surface_matching -lopencv_tracking -lopencv_datasets -lopencv_text -lopencv_dnn -lopencv_plot -lopencv_videostab -lopencv_video -lopencv_xfeatures2d -lopencv_shape -lopencv_ml -lopencv_ximgproc -lopencv_xobjdetect -lopencv_objdetect -lopencv_calib3d -lopencv_features2d -lopencv_highgui -lopencv_videoio -lopencv_imgcodecs -lopencv_flann -lopencv_xphoto -lopencv_photo -lopencv_imgproc -lopencv_core
```

## 测试

`CMakeLists.txt`文件如下：

```
cmake_minimum_required(VERSION 2.8)
project( DisplayImage )
add_definitions(-std=c++11)

find_package( OpenCV REQUIRED )
MESSAGE("OpenCV version: ${OpenCV_VERSION}")
include_directories( ${OpenCV_INCLUDE_DIRS} )

add_executable( DisplayImage DisplayImage.cpp )
target_link_libraries( DisplayImage ${OpenCV_LIBS} )
```

源文件`DisplayImage.cpp`如下：

```
#include <stdio.h>
#include <opencv2/opencv.hpp>
using namespace cv;

int main(int argc, char** argv )
{
	if ( argc != 2 )
	{
	    printf("usage: DisplayImage.out <Image_Path>\n");
	    return -1;
	}
	Mat image;
	image = imread( argv[1], 1 );
	if ( !image.data )
	{
	    printf("No image data \n");
	    return -1;
	}
	namedWindow("Display Image", WINDOW_AUTOSIZE );
	imshow("Display Image", image);
	waitKey(0);
	return 0;
}
```

实现如下：

```
$ ls
CMakeLists.txt  DisplayImage.cpp  lena.jpg
# 配置
$ cmake .
-- The C compiler identification is GNU 5.4.0
-- The CXX compiler identification is GNU 5.4.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found OpenCV: /home/zj/opencv/opencv-4.1.0/install (found version "4.1.0") 
OpenCV version: 4.1.0
-- Configuring done
-- Generating done
-- Build files have been written to: /home/zj/opencv/test/cmake_test
# 编译
$ make
Scanning dependencies of target DisplayImage
[ 50%] Building CXX object CMakeFiles/DisplayImage.dir/DisplayImage.cpp.o
[100%] Linking CXX executable DisplayImage
[100%] Built target DisplayImage
# 执行
$ ./DisplayImage lena.jpg 
```