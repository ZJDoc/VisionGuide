
# pytest

[pytest](https://docs.pytest.org/en/stable/)是一个测试工具

## 安装

```
# anaconda套件里好像自带了
$ pip install -U pytest
$ pytest --version
This is pytest version 4.0.2, imported from /home/zj/software/anaconda/anaconda3/lib/python3.7/site-packages/pytest.py
setuptools registered plugins:
  pytest-remotedata-0.3.1 at /home/zj/software/anaconda/anaconda3/lib/python3.7/site-packages/pytest_remotedata/plugin.py
  pytest-openfiles-0.3.1 at /home/zj/software/anaconda/anaconda3/lib/python3.7/site-packages/pytest_openfiles/plugin.py
  pytest-doctestplus-0.2.0 at /home/zj/software/anaconda/anaconda3/lib/python3.7/site-packages/pytest_doctestplus/plugin.py
  pytest-arraydiff-0.3 at /home/zj/software/anaconda/anaconda3/lib/python3.7/site-packages/pytest_arraydiff/plugin.py
```

## 测试命令

不同于[unittest](https://docs.python.org/3/library/unittest.html)，`pytest`仅需使用`assert`语句就可以完成测试表达式，检测过程中`pytest`的高级断言反省（`advanced assertion introspection`）机制会处理中间过程

### 测试值

```
# 测试返回值是否正确
# content of test_assert1.py
def f():
    return 3


def test_function():
    assert f() == 4
```

也可以指定`assert`命令返回的信息：

```
$ assert a % 2 == 0, "value was odd, should be even"
```

### 测试异常

使用`pytest.raise`作为上下文管理器进行异常的验证

```
# 最简单的方式
import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```

使用关键字`message`指定一个自定义失败信息

```
>>> with raises(ZeroDivisionError, message="Expecting ZeroDivisionError"):
        pass
```

使用关键字`match`配置指定异常，可以使用正则表达式

```
import pytest

def myfunc():
    raise ValueError("Exception 123 raised")

def test_match():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc()
```

同时可以将捕获异常设置为对象，常用属性包括`.type/.value/.traceback`

```
def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:

        def f():
            f()

        f()
    assert "maximum recursion" in str(excinfo.value)
```

```
# 打印
print(excinfo.type)
print(excinfo.value)
# 结果
<class 'RecursionError'>
maximum recursion depth exceeded    
```

## 测试文件

### 搜索路径规范

`pytest`会依据以下规范进行测试文件搜索：

* 如果没有参数指定，会搜索[testpaths](https://docs.pytest.org/en/latest/reference.html#confval-testpaths)（*如果有配置*）和当前目录。另外，可以使用命令行参数组合任意的目录、文件名和节点
* 递归到目录，除非它们匹配[norecursedirs](https://docs.pytest.org/en/latest/reference.html#confval-norecursedirs)
* 在这些目录中搜索`test_*.py`或`*_test.py`文件，通过它们的[测试包名](https://docs.pytest.org/en/latest/goodpractices.html#test-package-name)导入（参考`pytest`导入机制）
* 从测试文件中搜索以下测试项:
    * 类定义以外带`test`前缀的测试函数或方法
    * 带`Test`前缀的类定义（没有`__init__`函数）中带`test`前缀的测试函数或方法

同时可以自定义测试路径，参考[Changing standard (Python) test discovery](https://docs.pytest.org/en/latest/example/pythoncollection.html)

在`python`模块中，`pytest`也会使用标准的`unittest.testcase`子类化技术发现测试文件

### pytest导入机制

不同的文件布局下导入的测试模块不一致

**文件和目录布局一**

```
root/
|- foo/
   |- __init__.py
   |- conftest.py
   |- bar/
      |- __init__.py
      |- tests/
         |- __init__.py
         |- test_foo.py
```

**文件和目录布局二**

```
root/
|- foo/
   |- conftest.py
   |- bar/
      |- tests/
         |- test_foo.py
```

执行测试命令

```
$ pytest root/
```

对于布局一而言，因为`foo/bar/tests`目录均包含`__init__.py`文件，所以它们都是`python`模块，所以对于测试文件`test_foo.py`而言，其模块名为`foo.bar.tests.test_foo`；对于`conftest.py`而言，其模块名为`foo.conftest`

对于布局二而言，没有一个目录包含`__init__.py`文件，所以对于测试文件`test_foo.py`，其模块名为`test_foo`；对于测试文件`conftest.py`，其模块名为`conftest`

**所以布局二的测试文件名不能相同，否则会出错**

## 文件布局

`pytest`支持两种常见布局

### 应用和测试分离

如果有许多测试文件，可以将应用文件和测试文件分离在不同目录下：

```
setup.py
mypkg/
    __init__.py
    app.py
    view.py
tests/
    test_app.py
    test_view.py
    ...
```

这种布局有如下优势：

* 在执行`pip install ...`之后，可以对已安装应用进行测试
* 在执行`pip install --editable ..`之后，可以在本地副本上进行测试（`Your tests can run against the local copy with an editable install after executing pip install --editable ..`）
* 如果根路径没有`setup.py`文件，执行`python -m pytest`同样能将根路径导入`sys.path`，对本地副本进行直接测试

**改进一**

上述文件布局有一个缺陷在于测试文件都作为顶级模块进行导入（因为没有包），所以要求所有测试文件的文件名都不相同，或者可以修改如下：

```
setup.py
mypkg/
    ...
tests/
    __init__.py
    foo/
        __init__.py
        test_view.py
    bar/
        __init__.py
        test_view.py
```

**改进二**

经过改进一后，模块名包含了包名：`tests.foo.test_view/tests.bar.test_view`，此时存在另一个问题，因为将根目录导入了`sys.path`，所以顺带把应用文件也载入了内存，所以无法测试已安装版本，在应用目录外加一个`src`包即可解决问题，修改如下：

```
setup.py
src/
    mypkg/
        __init__.py
        app.py
        view.py
tests/
    __init__.py
    foo/
        __init__.py
        test_view.py
    bar/
        __init__.py
        test_view.py
```

### 测试在应用目录内

测试文件也可以放置在应用目录内：

```
setup.py
mypkg/
    __init__.py
    app.py
    view.py
    test/
        __init__.py
        test_app.py
        test_view.py
        ...
```

执行时使用参数`--pyargs`

```
pytest --pyargs mypkg
```

`pytest`将发现`mypkg`的安装位置并收集测试。如果要测试已安装版本，采用布局一中的改进方式（用`src`文件夹）

## 检测

`pytest`可以检测单个测试文件，也可以同时检测多个测试文件

### pytest vs. python -m pytest

```
# 命令一
$ pytest [...]
# 命令二
$ python -m pytest [...]
```

上述两种执行方式等价，除了命令二会将当前目录添加在`sys.path`中

## 相关阅读

* [Installation](https://docs.pytest.org/en/latest/getting-started.html)
* [The writing and reporting of assertions in tests](https://docs.pytest.org/en/latest/assert.html)
* [pytest import mechanisms and sys.path/PYTHONPATH](https://docs.pytest.org/en/latest/pythonpath.html#pytest-import-mechanisms-and-sys-path-pythonpath)
* [Conventions for Python test discovery](https://docs.pytest.org/en/latest/goodpractices.html#conventions-for-python-test-discovery)
* [Choosing a test layout / import rules](https://docs.pytest.org/en/latest/goodpractices.html#choosing-a-test-layout-import-rules)
* [Calling pytest through python -m pytest](https://docs.pytest.org/en/latest/usage.html#calling-pytest-through-python-m-pytest)
