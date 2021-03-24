
# [xmltodict]读取XML文件

之前学习过使用包[xml.etree.cElementTree](./[python]读取XML文件.md)来读取`XML`文件，今天发现一个新的包[xmltodict](https://pypi.org/project/xmltodict/)，将`XML`文件转换成字典形式进行读取

## 安装

```
$ conda install xmltodict
```

## 关键函数

解析给定的`XML`输入并将其转换为字典

```
def parse(xml_input, encoding=None, expat=expat, process_namespaces=False,
          namespace_separator=':', disable_entities=True, **kwargs):
```

参数`xml_input`为字符串（`XML`文件，不是文件名）或者文件对象

输入字典，生成`XML`文件字符串

```
def unparse(input_dict, output=None, encoding='utf-8', full_document=True,
            short_empty_elements=False,
            **kwargs):
```

## 示例

输入一个`xml`格式字符串，使用函数`parse`解析成字典；使用函数`unparse`将字典解析成`xml`格式字符串

```
import xmltodict

xxxml_str = "<source><database>OK HAHAHA</database></source>"

xml_parse_dict = xmltodict.parse(xxxml_str)
print(xml_parse_dict)
print(xml_parse_dict['source']['database'])

dict_unparse_xml = xmltodict.unparse(xml_parse_dict)
print(dict_unparse_xml)
# 输出
OrderedDict([('source', OrderedDict([('database', 'OK HAHAHA')]))])
OK HAHAHA
<?xml version="1.0" encoding="utf-8"?>
<source><database>OK HAHAHA</database></source>
```

还可以使用`parse`函数直接解析文件对象

```
import xmltodict

with open('./data/image-localization-dataset/training_images/eggplant_36.xml', 'rb') as f:
    xml_parse_dict = xmltodict.parse(f)
    print(xml_parse_dict)
```