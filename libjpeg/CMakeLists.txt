cmake_minimum_required(VERSION 3.20)
project(libjpeg)

set(CMAKE_CXX_STANDARD 11)

set(CMAKE_PREFIX_PATH /home/zj/opencv/opencv-4.2.0/install)
find_package(OpenCV REQUIRED)
# 打印OpenCV版本
MESSAGE("OpenCV version: ${OpenCV_VERSION}")
# 添加include地址
include_directories(${OpenCV_INCLUDE_DIRS})


include_directories(/home/zj/repos/libjpeg-turbo/install/include)
link_directories(/home/zj/repos/libjpeg-turbo/install/lib)

add_executable(libjpeg main.cpp)
target_link_libraries(libjpeg libturbojpeg.so ${OpenCV_LIBS})
#target_link_libraries(CImgDemo -lpthread -lX11)


