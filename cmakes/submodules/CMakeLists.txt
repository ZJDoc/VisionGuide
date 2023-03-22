cmake_minimum_required(VERSION 3.16)
project(SubModules)

set(BUILD_COMMON COMMON)
set(BUILD_MA MA)
set(BUILD_MB MB)

add_subdirectory(libs)
add_subdirectory(tests)
add_subdirectory(exec)