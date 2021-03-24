
# [pnno]转换json/dict数据为voc-xml

需要将标注数据保存为`VOC XML`格式，在网上查了一些资料。有多种方式可以实现，下面使用[martinblech/xmltodict](https://github.com/martinblech/xmltodict)将`json/dict`保存为`xml`文件

## 函数定义

### parse

使用`parse`读取`xml`文件，保存为`dict`数据

```
def parse(xml_input, encoding=None, expat=expat, process_namespaces=False,
          namespace_separator=':', disable_entities=True, **kwargs):
```

* `xml_input`：`xml`文件路径或者`file-like object`

### unparse

使用`unparse`将`dict`数据保存为`xml`文件

```
def unparse(input_dict, output=None, encoding='utf-8', full_document=True,
            short_empty_elements=False,
            **kwargs):
```

* `input_dict`：字典数据
* `output`：默认为`None`，则函数将转换后的`xml`数据字符串返回；如果设置文件路径，则保存在本地

## 示例

参考：[python中xml和json数据相互转换](https://blog.csdn.net/qq_33196814/article/details/99992771)

## 集成

使用工具[ zjykzj/pnno](https://github.com/zjykzj/pnno)自动转换生成`VOC`格式`xml`文件

## 相关阅读

* [Convert JSON to XML in Python](https://stackoverflow.com/questions/8988775/convert-json-to-xml-in-python/19474571)
* [Python – JSON to XML](https://www.geeksforgeeks.org/python-json-to-xml/)
* [How to convert JSON to XML using Python](https://www.codespeedy.com/how-to-convert-json-to-xml-using-python/)