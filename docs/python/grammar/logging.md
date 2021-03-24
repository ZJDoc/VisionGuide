
# [logging]日志模块

`logging`是`python`的日志记录工具，从最简单的配置到高级自定义，包含了非常丰富的内容和实现。之前在工程中使用过它，记录过初级和高级使用

* [python logging - 初级](https://blog.csdn.net/u012005313/article/details/51581442)
* [python logging - 高级](https://blog.csdn.net/u012005313/article/details/51588317)

不过最近回看发现内容排版有一些杂乱，所以打算重新学习一下`logging`的使用

## 日志工具要求

打印日志是为了有效的输出足够多的信息，方便之后的调试。对于日志记录工具，需要实现以下几个功能：

1. 能够为每条日志设置级别信息
2. 能够格式化输出日志信息
3. 能够根据需要输出日志到不同目的地（比如控制台/文件）
4. 能够根据不同的目的地过滤日志（比如控制台仅需输出`warn`级别以上的日志）

## logging简介

`logging`模块提供了`4`个组件来完成上述的功能：

* [Logger](https://docs.python.org/2.7/library/logging.html#logging.Logger)：主对象，集成后续组件，提供使用接口
* [Formatter](https://docs.python.org/2.7/library/logging.html#formatter-objects)：格式化对象
* [Handler](https://docs.python.org/2.7/library/logging.handlers.html#module-logging.handlers)：处理程序，指定日志输出目的地
* [Filter](https://docs.python.org/2.7/library/logging.html#filter-objects)：过滤器，作用于`Handler`

如果仅需打印日志到控制台或者文件，`logging`已经集成了相应的组件；如果需要输出日志到多个目的地，那么需要自定义`Handler`进行操作

## 初级使用

### 分级别

`logging`日志分`５`个等级，通过对应的函数输出

|   等级   |                                                   解释                                                   |  对应函数  |
| :------: | :------------------------------------------------------------------------------------------------------: | :--------: |
|  DEBUG   |                                                 详细信息                                                 |  debug()   |
|   INFO   |                                            确认事情按预期进行                                            |   info()   |
| WARNING  | 表示发生了意想不到的事情，或者表示在不久的将来出现了一些问题(例如“磁盘空间不足”)。软件仍如预期的那样工作 | warning()  |
|  ERROR   |                                  由于更严重的问题，软件无法执行某些功能                                  |  error()   |
| CRITICAL |                                  严重错误，表明程序本身可能无法继续运行                                  | critical() |

通过函数[basicConfig](https://docs.python.org/2.7/library/logging.html#logging.basicConfig)指定输出日志级别

```
import logging
logging.basicConfig(filename='example.log', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
```

### 格式化

`logging`自带了很多的属性，可以用于格式化日志的打印，比如时间信息/等级信息/文件信息/进程信息/线程信息等等。默认的格式化日志为

```
>>> logging.BASIC_FORMAT
'%(levelname)s:%(name)s:%(message)s'
```

可以使用函数`basicConfig`进行配置

```
import logging
 
logging.basicConfig(format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', level=logging.DEBUG)
logging.debug("This is debug message")
# 输出
2016-06-03 09:20:53,565 ...
```

上述格式化语句中指定了时间、文件名、行数、日志等级以及日志信息

如果对时间格式（默认的时间/日期格式是`ISO8601`）有要求，可以通过函数`basicConfig`重新设置时间格式：

```
logging.basicConfig(format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', datefmt='%Y/%m/%d %I:%M:%S %p', level=logging.DEBUG)
# 输出
2016/06/03 09:20:53 PM
```

### 输出日志到不同目的地

默认情况下输出日志到控制台窗口，如果要输出到文件，可以通过函数`basicConfig`指定

```
logging.basicConfig(level=logging.DEBUG, filename='example.log')
```

默认情况下对文件进行添加日志操作，如果想要每次都重新从头开始写入文件，可以使用属性`filemode`进行设置

```
# 默认filemode='a'
logging.basicConfig(level=logging.DEBUG, filename='example.log', filemode='w')
```

## 高级使用

如果想要同时输出日志到控制台和文件，并且自定义不同输出的格式和过滤，需要新建组件对象进行配置

### Logger

自定义组件后需要绑定到日志记录器上，可以通过函数创建

```
def getLogger(name=None):
    """
    Return a logger with the specified name, creating it if necessary.

    If no name is specified, return the root logger.
    """
```

*如果不指定`name`，则使用根记录器*

默认记录器输出日志级别为`warning`，使用函数`setLevel`设置

```
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
```

### Handler

`logging`已经实现了多个`Handler`对象，指向不同的输出目的地

* `StreamHandler`：输出到控制台
* `FileHandler`：输出到文件

定义`Handler`对象，然后绑定到`Logger`对象，日志将会输出到不同目的地

```
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# 设置控制台处理程序
console_handler = logging.StreamHandler()
# 设置输出日志等级
console_handler.setLevel(logging.DEBUG)
logger.addHandler(console_handler)

# 设置文件处理程序，输出文件名为output.log，写入模式为重建文件写入（默认为添加文件写入）
file_handler = logging.FileHandler('output.log', mode='w')
file_handler.setLevel(logging.WARNING)
logger.addHandler(file_handler)

if __name__ == '__main__':
    logger.debug("hello world 1")
    logger.info("hello world 2")
    logger.warning("hello world 3")
    logger.error("hello world 4")
    logger.critical("hello world 5")
```

**注意：设置`Handler`对象后，`basicConfig`配置将失效，需要新建`Formatter`对象进行格式化**

### Formatter

新建`Formatter`对象，使用属性`fmt`指定输出日志的格式，使用属性`datefmt`指定日期格式

```
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# 可以设置多个formatter，绑定到不同的Handler
console_formatter = logging.Formatter(fmt='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                              datefmt='%Y/%m/%d %I:%M:%S %p')
file_formatter = logging.Formatter(fmt='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                              datefmt='%I:%M:%S %Y/%m/%d')

# 设置控制台处理程序
console_handler = logging.StreamHandler()
# 设置输出日志等级
console_handler.setLevel(logging.DEBUG)
# 绑定Formatter到Handler
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

# 设置文件处理程序，输出文件名为output.log，写入模式为重建文件写入（默认为添加文件写入）
file_handler = logging.FileHandler('output.log', mode='w')
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

if __name__ == '__main__':
    logger.debug("hello world 1")
    logger.info("hello world 2")
    logger.warning("hello world 3")
    logger.error("hello world 4")
    logger.critical("hello world 5")
```

控制台输出如下：

```
2020/01/14 02:25:18 PM logg.py[line:35] DEBUG hello world 1
2020/01/14 02:25:18 PM logg.py[line:36] INFO hello world 2
2020/01/14 02:25:18 PM logg.py[line:37] WARNING hello world 3
2020/01/14 02:25:18 PM logg.py[line:38] ERROR hello world 4
2020/01/14 02:25:18 PM logg.py[line:39] CRITICAL hello world 5
```

文件`output.log`输出如下：

```
02:25:18 2020/01/14 logg.py[line:37] WARNING hello world 3
02:25:18 2020/01/14 logg.py[line:38] ERROR hello world 4
02:25:18 2020/01/14 logg.py[line:39] CRITICAL hello world 5
```

## 封装

仓库[lufficc/SSD](https://github.com/lufficc/SSD)给出了一个`logging`模块的封装，实现控制台窗口和文件的同步写入

```
import logging
import os
import sys


def setup_logger(name, save_dir=None):
    logger = logging.getLogger(name)

    logger.propagate = False

    logger.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler(stream=sys.stdout)
    formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    if save_dir:
        fh = logging.FileHandler(os.path.join(save_dir, 'log.txt'), mode='a')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    return logger
```

## 问题：重复输出日志

使用上述封装后的`logging`函数

```
from automark.utils.logger import setup_logger

logger = setup_logger(__name__, save_dir=self.dst_dir)
logger.debug('加载xxx')
```

打印结果时会出现重复的输出

```
2020-07-11 10:53:44,198 xxxx DEBUG: 加载模型
2020-07-11 10:53:44,198-DEBUG: 加载模型
....
....
```

参考[https://stackoverflow.com/questions/19561058/](duplicate-output-in-simple-python-logging-configuration/19561320)后发现是因为子`logger`对象会传播到根`logger`对象，造成重复输出的想象，添加如下设置即可

```
 logger.propagate = False
```

## 进一步

`logging`模块还支持通过配置文件的方式进行日志的处理，参考[15.8. logging.config — Logging configuration](https://docs.python.org/2.7/library/logging.config.html#module-logging.config)

除了发送日志到控制台和文件外，`logging`模块还提供了许多`Handler`进行操作，参考[15.9. logging.handlers — Logging handlers](https://docs.python.org/2.7/library/logging.handlers.html#module-logging.handlers)

## 相关阅读

* [Basic Logging Tutorial](https://docs.python.org/2.7/howto/logging.html#basic-logging-tutorial)

* [Advanced Logging Tutorial](https://docs.python.org/2.7/howto/logging.html#advanced-logging-tutorial)

* [15.7. logging — Logging facility for Python](https://docs.python.org/2.7/library/logging.html#module-logging)
