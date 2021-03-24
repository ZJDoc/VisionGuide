
# [pip]更新国内镜像源

有两种方式配置国内镜像源：

1. 参数配置
2. 文件配置

## 参数配置

添加`-i`参数，指定国内镜像源

```
$ pip install <软件名> -i https://pypi.tuna.tsinghua.edu.cn/simple
```

可选的有

```
阿里云http://mirrors.aliyun.com/pypi/simple/ 
中国科技大学https://pypi.mirrors.ustc.edu.cn/simple/
豆瓣(douban)http://pypi.douban.com/simple/ 
清华大学https://pypi.tuna.tsinghua.edu.cn/simple/ 
中国科学技术大学http://pypi.mirrors.ustc.edu.cn/simple/
```

## 文件配置

修改配置文件`~/.pip/pip.conf`，添加

```
[global]
index-url = https://pypi.doubanio.com/simple
trusted-host = pypi.doubanio.com
```

## 相关阅读

* [python - pip换源，更换pip源到国内镜像](https://blog.csdn.net/xuezhangjun0121/article/details/81664260)
* [Python pip 修改镜像源为豆瓣源](https://www.douban.com/note/672475302/)