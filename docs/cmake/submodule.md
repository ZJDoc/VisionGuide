
# 子模块

## 场景

一个完整的工程中存在多个子目录，分别保存有库文件、运行文件和测试文件。分别创建三个子模块：

1. 在库目录中创建动态库
2. 在运行文件中创建可执行程序，链接动态库
3. 在测试文件中创建gtest测试程序，链接动态库

## 相关阅读

* [CMake多模块的构建方式](https://www.leadroyal.cn/p/781/)
* [CMake应用：模块化及库依赖](https://zhuanlan.zhihu.com/p/373363335)
* [Subdirectories, spliting code in CMake](https://codeiter.com/en/posts/subdirectories-spliting-code-in-cmake)
* [CMake 管理多项目](https://zcteo.top/blog/CMake/002_CmakeMultiproject.html)
* [使用子工程CMake](https://sfumecjf.github.io/cmake-examples-Chinese/02-sub-projects/A-basic/)