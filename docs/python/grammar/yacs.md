
# [yacs]YAML文件读取

使用[yacs](https://github.com/rbgirshick/yacs)实现`YAML`文件的读取

## 安装

```
$ pip install yacs
```

## 配置

首先创建一个配置文件，通常命名为`config.py`或者`defaults.py`

```
# my_project/config.py
from yacs.config import CfgNode as CN


_C = CN()

_C.SYSTEM = CN()
# Number of GPUS to use in the experiment
_C.SYSTEM.NUM_GPUS = 8
# Number of workers for doing things
_C.SYSTEM.NUM_WORKERS = 4

_C.TRAIN = CN()
# A very important hyperparameter
_C.TRAIN.HYPERPARAMETER_1 = 0.1
# The all important scales for the stuff
_C.TRAIN.SCALES = (2, 4, 8, 16)


def get_cfg_defaults():
  """Get a yacs CfgNode object with default values for my_project."""
  # Return a clone so that the defaults will not be altered
  # This is for the "local variable" use pattern
  return _C.clone()

# Alternatively, provide a way to import the defaults as
# a global singleton:
# cfg = _C  # users can `from config import cfg`
```

* `YAML`采用树型结构保存信息
    * 每个根节点必须创建一个新对象，比如`_C = CN()、_C.SYSTEM = CN()、_C.TRAIN = CN()`
    * 每个叶子结点用来保存信息，比如`_C.SYSTEM.NUM_GPUS = 8`
* 上述配置文件中预先设置了一些配置参数，比如设置`SYSTEM=CN()`，设置`SYSTEM.NUM_GPUS = 8`。这些可以根据实际情况添加或者删除

创建一个`YAML`测试文件`experiment.yaml`

```
# my_project/experiment.yaml
SYSTEM:
  NUM_GPUS: 2
TRAIN:
  SCALES: (1, 2)
```

**Note：在读取本地`YAML`文件时，必须在配置文件中预先设置相应的参数。比如在`experiment.yaml`中设置了根节点`SYSTEM`，以及叶子节点`NUM_GPU`，那么必须再`config.py`中进行预设置**

## 文件读取

有两种使用方式

1. 全局单例模式（`global singleton`）
2. 局部变量模式（`local variable`）

### global singleton

修改上述配置文件如下：

```
# my_project/config.py
from yacs.config import CfgNode as CN


_C = CN()

_C.SYSTEM = CN()
# Number of GPUS to use in the experiment
_C.SYSTEM.NUM_GPUS = 8
# Number of workers for doing things
_C.SYSTEM.NUM_WORKERS = 4

_C.TRAIN = CN()
# A very important hyperparameter
_C.TRAIN.HYPERPARAMETER_1 = 0.1
# The all important scales for the stuff
_C.TRAIN.SCALES = (2, 4, 8, 16)

# Alternatively, provide a way to import the defaults as
# a global singleton:
cfg = _C  # users can `from config import cfg`
```

创建`main.py`，读取配置信息如下：

```
from config import cfg                                              --------------- 直接使用预定义的对象即可

if __name__ == "__main__":
    cfg.merge_from_file("experiment.yaml")
    cfg.freeze()
    # print(cfg)

    print(cfg.SYSTEM.NUM_GPUS)
####################### 输出
SYSTEM:
  NUM_GPUS: 2
  NUM_WORKERS: 4
TRAIN:
  HYPERPARAMETER_1: 0.1
  SCALES: (1, 2)
2
```

**Note：完成配置信息读取后最好调用函数`freeze()`防止进一步修改**

### local variable

其配置文件修改如下：

```
# my_project/config.py
from yacs.config import CfgNode as CN


_C = CN()

_C.SYSTEM = CN()
# Number of GPUS to use in the experiment
_C.SYSTEM.NUM_GPUS = 8
# Number of workers for doing things
_C.SYSTEM.NUM_WORKERS = 4

_C.TRAIN = CN()
# A very important hyperparameter
_C.TRAIN.HYPERPARAMETER_1 = 0.1
# The all important scales for the stuff
_C.TRAIN.SCALES = (2, 4, 8, 16)


def get_cfg_defaults():
  """Get a yacs CfgNode object with default values for my_project."""
  # Return a clone so that the defaults will not be altered
  # This is for the "local variable" use pattern
  return _C.clone()
```

为每个局部变量创建一个副本。读取文件如下：

```
from config import get_cfg_defaults  # local variable usage pattern, or:

if __name__ == "__main__":
    cfg = get_cfg_defaults()
    cfg.merge_from_file("experiment.yaml")
    cfg.freeze()
    # print(cfg)

    print(cfg.SYSTEM.NUM_GPUS)
####################### 输出
2
```

## 命令行重载

`yacs`同样支持命令行参数输入的配置信息。示例如下：

```
cfg.merge_from_file("experiment.yaml")
# Now override from a list (opts could come from the command line)
opts = ["SYSTEM.NUM_GPUS", 8, "TRAIN.SCALES", "(1, 2, 3, 4)"]
cfg.merge_from_list(opts)
```

上述代码功能如下：

1. 调用函数`merge_from_file`读取`experiment.yaml`配置信息
2. 读取命令行信息`opts`，配置了叶子节点`NUM_GPUS`和`SCALES`
3. 调用函数`merge_from_list`读取`opts`配置信息