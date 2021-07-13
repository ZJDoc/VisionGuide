
# 问题解答

## 问题一：[pip]python: bad interpreter

* 问题描述

使用`pip`命令安装`python`库时发现了如下错误

```
$ pip install imgaug
-bash: /home/zj/anaconda3/envs/cv2/bin/pip: /home/zj/anaconda3/envs/cv/bin/python: bad interpreter: No such file or directory
```

* 问题解析

使用`Anaconda`配置`Python`开发环境，除了`base`环境外还创建了一个新的环境`cv`，后来想要配置另一套环境，就直接在`envs`环境下复制了`cv`，重命名为`cv2`，把`cv`环境给删除了

在`cv2`环境下能够正常的运行`Python`程序，但是使用`pip`安装新库时发现了如上错误

* 解决方案

所以还是需要使用`Anaconda`提供的`clone`命令进行环境移植

另外在网上找到一种解决方法，就是在执行`pip`命令时指定使用哪个`python`

```
$ pythoh -m pip install imgaug
```

## 问题二：AttributeError: module 'scipy.misc' has no attribute 'imread'

* 问题描述

```
AttributeError: module 'scipy.misc' has no attribute 'imread'
```

* 问题解析

`scipy`版本过高

* 解决方案

```
$ pip install scipy==1.2.1
```

* 参考

[解决AttributeError: module 'scipy.misc' has no attribute 'imread'报错问题](https://blog.csdn.net/fu6543210/article/details/103515909)

## 问题三：OSError: image file is truncated (24 bytes not processed)

* 问题描述

使用`PIL Image`读取图片时出现如下错误：

```
```

* 问题解析

从提示信息来看，是因为图片文件太大了，`PIL Image`默认不支持大图片读取

* 解决方案

参考：

[OSError: image file is truncated (X bytes not processed)错误处理](https://blog.csdn.net/hzs3237259/article/details/108188323)

[OSError: image file is truncated (28 bytes not processed)](https://www.cnblogs.com/yqpy/p/11362350.html)

在文件头添加

```
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
```

## 问题四：AttributeError: module 'ssl' has no attribute 'PROTOCOL_TLSv1' 

* 问题描述：

使用`Miniconda`安装`Python`环境，完成后使用`conda/pip`安装时均出现错误

* 问题解决：

```
$ sudo apt install openssl
```

* 相关阅读

[AttributeError: module 'ssl' has no attribute 'PROTOCOL_TLSv1' #1029](https://github.com/pyca/pyopenssl/issues/1029)