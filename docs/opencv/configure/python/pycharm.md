
# [PyCharm]解码opencv python库

`opencv`源码编译得到的`python`库仅是一个`.so`文件，在`vscode`中编辑代码时无法跳转到内部，但是在`pycharm`中可以查看函数头和常量定义

进入(`Ctrl+B`)之后发现是一个`__init__.py`文件，存储`python_stubs`路径下

    /home/zj/.PyCharm2018.3/system/python_stubs/-1678504091/cv2/__init__.py

上网查找了许久，参考

[pycharm的python_stubs](https://blog.csdn.net/u013128262/article/details/81491009)

[PyCharm, what is python_stubs?](https://stackoverflow.com/questions/24266114/pycharm-what-is-python-stubs)

`pycharm`自己解码了`cv2.so`文件，生成了类头文件以便更好的编程