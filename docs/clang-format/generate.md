
# 配置文件

## 安装

首先安装`clang-format`

```shell
sudo apt install clang-format
```

## 配置

执行如下命令，生成`Google`风格`C++`配置文件：

```shell
clang-format -style=google -dump-config > .clang-format
```

生成得到`YAML`格式配置文件`.clang-format`

## 修改

修改部分选项，更符合个人需求：

1. `tab`宽度从`8`修改为`4`

```
#TabWidth:        8
TabWidth:        4
```

2. `indent`宽度从`2`修改为`4`

```
#IndentWidth:     2
IndentWidth:     4
```