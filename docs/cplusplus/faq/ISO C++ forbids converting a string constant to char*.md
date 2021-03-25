
# warning: ISO C++ forbids converting a string constant to 'char*' [-Wwrite-strings]

测试如下代码时遇到上述问题

```
    char *pArray[] = {"apple", "pear", "banana", "orange", "pineApple"};
    for (int i = 0; i < sizeof(pArray) / sizeof(*pArray); i++) {
        std::cout << pArray[i] << std::endl;
    }
```

```
 warning: ISO C++ forbids converting a string constant to ‘char*’ [-Wwrite-strings]
```

参考[warning: ISO C++ forbids converting a string constant to 'char*' [-Wwrite-strings]](https://blog.csdn.net/creambean/article/details/89459858)

`C++11`禁止将字符串常量赋值给`char*`类型，解决方式之一就是将`char*`设置为`const char*`