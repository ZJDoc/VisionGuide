
# 打包和分发Python程序

最新示例：[ zjykzj/python-setup.py](https://github.com/zjykzj/python-setup.py)

## 内容列表

* 相关术语介绍
* 打包和分发流程
    * 创建`setup.py`
    * 打包`Python Package`
    * 注册`pypi`帐号
    * 上传`Python Package`
    * 安装`Python Package`
* 进阶
    * 免密上传
    * 配置版本号
    * 配置依赖库
    * 配置命令行脚本
    * 创建徽章
* 最终版本
    * 实现打包、上传和`GIT`标签一条龙服务
* 问题

## 相关术语介绍

* 库
    * [setuptools](https://setuptools.readthedocs.io/en/latest/setuptools.html#)：新一代打包和分发`Python Packages`的工具（之前是`distutils`）
* 命令行工具
    * [twine](https://twine.readthedocs.io/en/latest/)：上传构建文件的工具
    * [pip](https://pip.pypa.io/en/stable/)：安装`Python`包的工具，从`pypi`或者其他软件仓库中下载包并安装
* 文件
    * `setup.py`：在项目根目录创建，指定包以及环境信息
* 仓库
    * [pypi](https://pypi.org/)：全称为`The Python Package Index`，`Python`编程语言的在线软件仓库

## 打包和分发流程

创建示例工程`python-setup`，其文件架构如下：

```
.
├── lib
│   ├── __init__.py
│   └── tools
│       ├── cli.py
│       └── __init__.py
├── README.md
└── setup.py
```

### 创建setup.py

在`setup.py`上编写相应的打包信息，其文件内容如下：

```
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-setup",  # Replace with your own username
    version="0.0.1",
    author="zj",
    author_email="wy163zhuj@163.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zjZSTU/python-setup.py.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
```

* `name`：工程名
* `version`：版本号
* `author`：作者
* `author_email`：邮箱
* `description`：工程短描述
* `long_description`：长描述，直接使用`README.md`
* `url`：在线仓库地址
* `packages`：打包文件，有两种选择
    * 自定义：格式为`packages=['xx', 'xx']`，指定要打包的包目录
    * [find_packages()](https://setuptools.readthedocs.io/en/latest/setuptools.html#using-find-packages)：打包所有包目录（就是有`__init__.py`的文件夹），可以通过参数`exclude`排除指定文件，比如`find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])`
* `classifiers`：字符串列表，描述了包类别
* `python_requires`：指定`Python`版本

### 打包Python Package

执行如下命令

```
$ python setup.py sdist bdist_wheel
```

将会创建`3`个文件夹：`build、dist`和`python_setup.egg-info`，打包程序位于`dist`目录下：

```
python_setup-0.0.1-py3-none-any.whl
python-setup-0.0.1.tar.gz
```

### 注册pypi帐号

在`pypi`上注册帐号：[Create an account on PyPI](https://pypi.org/account/register/)

### 上传Python Package

安装上传工具

```
pip install twine
```

上传Python Packages

```
twin upload dist/*
```

输入注册的用户名和密码即可，上传完成后，可以在[个人工程页面](https://pypi.org/manage/projects/)查看

### 安装Python Package

#### 使用pip命令

使用`pip`命令进行安装，有两种方式

##### 在线下载并安装

```
pip install python_setup
```

升级已安装包

```
pip install --upgrade python_setup
```

安装指定包

```
pip install python_setup==x.x.x
```

卸载包

```
pip uninstall python_setup
```

##### 安装本地包

```
pip install python_setup-0.0.1-py3-none-any.whl
```

#### 使用setuptools

```
python setup.py install
```

## 进阶

### 免密上传

`pypi`官网推荐使用`API Token`的方式进行免密登录：[How can I use API tokens to authenticate with PyPI?](https://pypi.org/help/#apitoken)，实现后发现会出现错误，参考[pypi上传问题](https://pypi.org/manage/account/)，编辑文件`.pypirc`

```
$ vim ~/.pypirc
[distutils]
index-servers=pypi

[pypi]
repository:https://upload.pypi.org/legacy/
username:用户名
password:密码
```

### 配置版本号

在`lib/__init__.py`中设置版本信息

```
# This line will be programatically read/write by setup.py.
# Leave them at the bottom of this file and don't touch them.
__version__ = "0.1.0"
```

在`setup.py`中解析该文件，获取版本号

```
import os


def get_version():
    init_py_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "lib", "__init__.py")
    init_py = open(init_py_path, "r").readlines()
    version_line = [l.strip() for l in init_py if l.startswith("__version__")][0]
    version = version_line.split("=")[-1].strip().strip("'\"")

    return version

。。。
。。。

setuptools.setup(
    。。。
    version=get_version(),
    。。。
```

### 配置依赖库

类似于`requirements.txt`，在安装`Python`包时同时下载安装相关的依赖库，使用`python_requires`属性设置，比如

```
python_requires=[
    "yacs >= 0.1.7",
    "opencv_contrib_python >= 4.2.0",
    "numpy >= 1.17.2"
]
```

### 配置命令行脚本

新建文件`lib/tools/cli.py`

```
from lib.src.hello import print_hello

def main():
    print_hello()

if __name__ == '__main__':
    main()
```

修改`setup.py`，添加属性`entry_points`

```
    entry_points={
        'console_scripts': [
            # 注意，不要添加.py后缀
            # print_hello就是命令
            'print_hello = lib.tools.cli:main'
        ]
    },
```

重新打包并安装

```
$ python setup.py sdist bdist_wheel
$ pip install dist/python_setup-0.1.0-py3-none-any.whl
```

即可在全局命令行中执行命令`print_hello`

```
$ print_hello 
Hello python-setup.py
```

其地址位于`/bin`目录下

```
$ which print_hello 
/home/zj/anaconda3/bin/print_hello
$ file `which print_hello`
/home/zj/anaconda3/bin/print_hello: Python script, ASCII text executable
$ cat `which print_hello`
#!/home/zj/anaconda3/bin/python
# -*- coding: utf-8 -*-
import re
import sys

from python_setup.tools.cli import main

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
```

### 创建徽章

参考[自定义徽章](https://zjdoc-gitguide.readthedocs.io/zh_CN/latest/readme/badge/)，为`pypi`项目创建徽章

## 最终版本

参考[navdeep-G/setup.py](https://github.com/navdeep-G/setup.py/blob/master/setup.py)实现打包、上传以及`GIT`标签一条龙服务。修改`setup.py`如下：

### 新增类UploadCommand

```
import shutil
import sys

class UploadCommand(setuptools.Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            here = os.path.abspath(os.path.dirname(__file__))
            self.status('Removing previous builds…')
            shutil.rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(get_version()))
        os.system('git push --tags')

        sys.exit()
```

执行如下功能：

1. 删除已有的`dist`文件夹
2. 打包：`python setup.py sdist bdist_wheel --universal`
3. 上传到`Pypi`软件仓库：`twine upload dist/*`
4. 打标签：`git tag v{}`
5. 上传到远程`Git`仓库：`git push --tags`

### 更新setuptools.setup

```
setuptools.setup(
    ...
    ...
    cmdclass={
        'upload': UploadCommand,
    },
)
```

### 执行

使用如下命令即可完成打包、上传和贴标签一条龙服务了

```
$ python setup.py upload 
```

## 问题

### Filename or contents already exists

参考：[Why am I getting a "Filename or contents already exists" or "Filename has been previously used" error?](https://pypi.org/help/#file-name-reuse)

`pypi`规定指定文件名的`python`包只能上传一次，即使删除也不能重复上传

### ModuleNotFoundError

安装完`Python`包后，执行命令行工具经常会出现`ModuleNotFoundError`错误

```
$ print_hello 
Traceback (most recent call last):
  File "/home/zj/anaconda3/bin/print_hello", line 6, in <module>
    from lib.tools.cli.py import main
ModuleNotFoundError: No module named 'lib.tools.cli.py'; 'lib.tools.cli' is not a package
```

这是因为`lib`这个库有冲突，最好选择一个独特的包名，比如`lib -> python_setup`

### pip没有办法更新到最新版本

我就遇到了这个问题，想了很久觉得是因为我配置了国内`pip`镜像源，所以没办法马上下载到最新的版本

## 相关阅读

* [1. An Introduction to Distutils](https://docs.python.org/3/distutils/introduction.html#a-simple-example)

* [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)

* [Getting Started With setuptools and setup.py](https://pythonhosted.org/an_example_pypi_project/setuptools.html)

* [facebookresearch/detectron2](https://github.com/facebookresearch/detectron2)

* [Python中, 使用setup.py和console_scripts参数创建安装包和shell命令](https://blog.csdn.net/lslxdx/article/details/73131664)