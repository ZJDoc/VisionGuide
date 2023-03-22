cmake_minimum_required(VERSION 3.16)
project(SubModules)

set(CMAKE_INSTALL_PREFIX ${CMAKE_SOURCE_DIR}/install)
MESSAGE(STATUS "CMAKE_INSTALL_PREFIX: ${CMAKE_INSTALL_PREFIX}")

set(BUILD_COMMON COMMON)
set(BUILD_MA MA)
set(BUILD_MB MB)

set(BUILD_MAIN main)

add_subdirectory(libs)
add_subdirectory(tests)
add_subdirectory(exec)

install(TARGETS ${BUILD_COMMON} ${BUILD_MA} ${BUILD_MB} ${BUILD_MAIN}
		RUNTIME DESTINATION bin
		LIBRARY DESTINATION lib
		ARCHIVE DESTINATION lib)