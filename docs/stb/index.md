
# 引言

最近发现一个非常实用的单文件库：[ nothings/stb](https://github.com/nothings/stb)，仅需加入单个头文件即可完成图像加载（*获取字节流以及对应的宽/高/通道数等信息*）、图像保存等操作。

图像处理相关的操作包括：

* `image loader`: [stb_image.h](https://github.com/nothings/stb/blob/master/stb_image.h)
* `image writer`: [stb_image_write.h](https://github.com/nothings/stb/blob/master/stb_image_write.h)
* `image resizer`: [stb_image_resize.h](https://github.com/nothings/stb/blob/master/stb_image_resize.h)

## 操作

下载`stb`仓库，将对应头文件加入自己工程，使用如下语法引入该头文件：

```
#define STB_IMAGE_IMPLEMENTATION
#include "stb_image.h"
```

## 示例

查看目录：`stb/`