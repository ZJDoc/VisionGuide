
# [setup.py]保存额外数据

使用`setuptools`打包`Python`包时，需要加入额外数据，比如图片、文档、压缩包等等。其配置方式参考：

有多种方式可以实现：

1. 配置属性`package_data`
2. 配置属性`data_files`
3. 编辑文件`MANIFEST.in`

## package_data

### 实现

其编辑方式如下：

```
setuptools.setup(
    ...
    ...
    package_data={'目录名': ['文件一', '文件二']},
    ...
    ...
}
```

通过键值对的方式指定要添加的文件

1. 如果同一目录下有多个子文件夹的文件，可以使用列表的方式保存在同一键下
2. 可以使用通配符的方式指定相同格式的文件，比如`*.jpg`

注意：其根目录为`setup.py`所在路径

### 示例

参考：[ zjykzj/zlogo ](https://github.com/zjykzj/zlogo)

```
setuptools.setup(
    name=NAME,  # Replace with your own username
    version=get_version(),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
    packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_data={'zlogo': ['tool/logo', 'config/*. logorc']},                 <----------------- 这里
    classifiers=CLASSIFIERS,
    python_requires=PYTHON_REQUIRES,
    entry_points={
        'console_scripts': [
            CONSOLE_SCRIPTS
        ]
    },
    cmdclass={
        'upload': UploadCommand,
    },
)
```

## 相关阅读

* [2.6. Installing Package Data](https://docs.python.org/3/distutils/setupscript.html#installing-package-data)
* [2.7. Installing Additional Files](https://docs.python.org/3/distutils/setupscript.html#installing-additional-files)
* [4.1. Specifying the files to distribute](https://docs.python.org/3/distutils/sourcedist.html#specifying-the-files-to-distribute)
