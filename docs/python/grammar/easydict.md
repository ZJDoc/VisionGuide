
# [easydict]访问属性的方式来访问字典

[EasyDict](https://github.com/makinacorpus/easydict)提供了一种更便捷的方式来访问键值对，像访问属性一样来访问

## 安装

```
$ pip install easydict
```

## 示例一：解析Dict

```
from easydict import EasyDict as edict

if __name__ == '__main__':
    d = edict({'foo': 3, 'bar': {'x': 1, 'y': 2}})
    print(d)

    print(d.foo)
    # 可以递归调用
    print(d.bar)
    print(d.bar.x)
################# 输出
{'foo': 3, 'bar': {'x': 1, 'y': 2}}
3
{'x': 1, 'y': 2}
1
```

## 示例二：解析Json

`EasyDict`同样能够解析`Json`格式内容

```
from easydict import EasyDict as edict
from simplejson import loads
import pprint

if __name__ == '__main__':
    j = """{
    "Buffer": 12,
    "List1": [
        {"type" : "point", "coordinates" : [100.1,54.9] },
        {"type" : "point", "coordinates" : [109.4,65.1] },
        {"type" : "point", "coordinates" : [115.2,80.2] },
        {"type" : "point", "coordinates" : [150.9,97.8] }
    ]
    }"""

    pprint.pprint(j)
    json_j = loads(j)
    pprint.pprint(json_j)
    d = edict(json_j)
    print(d.Buffer)
    print(d.List1[2].type)
####################### 输出
('{\n'
 '    "Buffer": 12,\n'
 '    "List1": [\n'
 '        {"type" : "point", "coordinates" : [100.1,54.9] },\n'
 '        {"type" : "point", "coordinates" : [109.4,65.1] },\n'
 '        {"type" : "point", "coordinates" : [115.2,80.2] },\n'
 '        {"type" : "point", "coordinates" : [150.9,97.8] }\n'
 '    ]\n'
 '    }')
{'Buffer': 12,
 'List1': [{'coordinates': [100.1, 54.9], 'type': 'point'},
           {'coordinates': [109.4, 65.1], 'type': 'point'},
           {'coordinates': [115.2, 80.2], 'type': 'point'},
           {'coordinates': [150.9, 97.8], 'type': 'point'}]}
12
point
```