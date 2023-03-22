cmake_minimum_required(VERSION 3.16)
project(Exec VERSION 0.1.0 LANGUAGES C CXX)

set(CMAKE_C_STANDARD ${CMAKE_C_STANDARD})
set(CMAKE_CXX_STANDARD 17)
MESSAGE(STATUS "CMAKE_C_STANDARD: ${CMAKE_C_STANDARD}")
MESSAGE(STATUS "CMAKE_CXX_STANDARD: ${CMAKE_CXX_STANDARD}")

# 设置C++编译器
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -pipe -std=c99")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -pipe -std=c++17")
MESSAGE(STATUS "CMAKE_C_FLAGS: ${CMAKE_C_FLAGS}")
MESSAGE(STATUS "CMAKE_CXX_FLAGS: ${CMAKE_CXX_FLAGS}")

file(GLOB_RECURSE FILES_RECURSE . "*.cc")
MESSAGE(STATUS "FILES_RECURSE: ${FILES_RECURSE}")

include_directories(../libs/common)
include_directories(../libs/ma)
include_directories(../libs/mb)

add_executable(${BUILD_MAIN} ${FILES_RECURSE})
#target_link_libraries(main PRIVATE MA MB COMMON)
target_link_libraries(${BUILD_MAIN} PRIVATE ${BUILD_MA} ${BUILD_MB} ${BUILD_COMMON})
