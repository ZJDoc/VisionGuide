
# 基础语法

* 具体示例可以查看：[grammar](../../cmakes/grammar/)

## 打印信息

```text
message([<mode>] "message text" ...)
```

* [Log a message.](https://cmake.org/cmake/help/latest/command/message.html?highlight=message)

## 文件操作

```text
# 获取文件
file({GLOB | GLOB_RECURSE} <out-var> [...] [<globbing-expr>...])
# 获取当前目录中的所有.cc文件
file(GLOB FILES . "*.cc")
# 递归获取当前目录中所有的.cc文件和.txt文件
file(GLOB_RECURSE FILES_RECURSE . "*.cc" "*.txt")
```

* [File manipulation command.](https://cmake.org/cmake/help/latest/command/file.html?highlight=file#command:file)