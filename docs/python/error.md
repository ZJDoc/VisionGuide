
# ERROR

## 问题一：[pip]python: bad interpreter

## 问题

使用`pip`命令安装`python`库时发现了如下错误

```
$ pip install imgaug
-bash: /home/zj/anaconda3/envs/cv2/bin/pip: /home/zj/anaconda3/envs/cv/bin/python: bad interpreter: No such file or directory
```

## 解析

使用`Anaconda`配置`Python`开发环境，除了`base`环境外还创建了一个新的环境`cv`，后来想要配置另一套环境，就直接在`envs`环境下复制了`cv`，重命名为`cv2`，把`cv`环境给删除了

在`cv2`环境下能够正常的运行`Python`程序，但是使用`pip`安装新库时发现了如上错误

## 解决

所以还是需要使用`Anaconda`提供的`clone`命令进行环境移植

另外在网上找到一种解决方法，就是在执行`pip`命令时指定使用哪个`python`

```
$ pythoh -m pip install imgaug
```