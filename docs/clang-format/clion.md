
# CLion配置

## 配置文件

将`.clang-format`放置到`CLion`工程根路径

## CLion配置

* 点击菜单栏`File->Settings->Editor->Code Style`，打开`ClangFormat`设置

修改`C++`文件后使用快捷命令`ctrl+alt+L`即进行格式化操作

## 错误

```
Error reading /home/zj/repos/VisionGuide/samples/GTestDemo/.clang-format:97:4: Invalid argument - unknown key 'Delimiter
```

当前解决方案：注释掉该选项

```
#RawStringFormats:
#  - Delimiter:       pb
#    Language:        TextProto
#    BasedOnStyle:    google
```