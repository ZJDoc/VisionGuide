
# 模型转换

## ONNX -> MNN

```shell
./MNNConvert -f ONNX --modelFile XXX.onnx --MNNModel XXX.mnn --bizCode biz
```

正确性校验

```shell
python ../tools/script/fastTestOnnx.py mobilenetv2-7.onnx # 模型转换后推理并与ONNXRuntime结果对比
```

## MNN -> .h

```shell
xxd -i xxx.mnn xxx.h
```

## 相关阅读

* [模型转换工具](https://mnn-docs.readthedocs.io/en/latest/tools/convert.html)