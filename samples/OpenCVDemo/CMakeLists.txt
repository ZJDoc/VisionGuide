cmake_minimum_required(VERSION 3.24)
project(OpenCVDemo)

set(CMAKE_CXX_STANDARD 17)

# set opencv
get_filename_component(ABSOLUTE_OpenCV_DIR ./3rdparty/opencv ABSOLUTE)
IF (CMAKE_SYSTEM_NAME MATCHES "Linux")
    set(OpenCV_DIR ${ABSOLUTE_OpenCV_DIR}/lib/cmake/opencv4)
ELSEIF (CMAKE_SYSTEM_NAME MATCHES "Windows")
    set(OpenCV_DIR ${ABSOLUTE_OpenCV_DIR})
ENDIF ()
find_package(OpenCV REQUIRED)

MESSAGE("OpenCV version: ${OpenCV_VERSION}")
MESSAGE("OpenCV OpenCV_INCLUDE_DIRS: ${OpenCV_INCLUDE_DIRS}")
MESSAGE("OpenCV OpenCV_LIBS: ${OpenCV_LIBS}")


add_executable(OpenCVDemo main.cpp)
target_link_libraries(OpenCVDemo ${OpenCV_LIBS})
