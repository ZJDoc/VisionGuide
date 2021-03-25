
# [vconcat][hconcat]按行合并以及按列合并

`OpenCV`提供了多种方式进行矩阵的合并

## 函数解析

主要函数包括

1. [vconcat](https://docs.opencv.org/4.0.1/d2/de8/group__core__array.html#ga744f53b69f6e4f12156cdde4e76aed27)：垂直连接，按行合并
2. [hconcat](https://docs.opencv.org/4.0.1/d2/de8/group__core__array.html#gaf9771c991763233866bf76b5b5d1776f)：水平连接，按列合并

### vconcat

```
CV_EXPORTS void vconcat(const Mat* src, size_t nsrc, OutputArray dst);
CV_EXPORTS void vconcat(InputArray src1, InputArray src2, OutputArray dst);
CV_EXPORTS_W void vconcat(InputArrayOfArrays src, OutputArray dst);
```

* `src`：输入矩阵的数组或向量。所有矩阵必须具有相同的列数和相同的深度
* `nsrc`：`src`中的矩阵数
* `src2`：用于垂直连接的第二个输入数组
* `dst`：输出数组

### hconcat

```
CV_EXPORTS void hconcat(const Mat* src, size_t nsrc, OutputArray dst);
CV_EXPORTS void hconcat(InputArray src1, InputArray src2, OutputArray dst);
CV_EXPORTS void hconcat(InputArray src1, InputArray src2, OutputArray dst);
CV_EXPORTS_W void hconcat(InputArrayOfArrays src, OutputArray dst);
```

参数和`vconcat`类似

## 示例

以下操作按行合并示例，按列合并操作类似

### 示例一

```
cv::Mat matArray[] = {cv::Mat(1, 4, CV_8UC1, cv::Scalar(1)),
                    cv::Mat(1, 4, CV_8UC1, cv::Scalar(2)),
                    cv::Mat(1, 4, CV_8UC1, cv::Scalar(3)),};
cv::Mat out;
cv::vconcat(matArray, 3, out);
cout << out << endl;
// out
[  1,   1,   1,   1;
   2,   2,   2,   2;
   3,   3,   3,   3]
```

### 示例二

```
cv::Mat_<float> A = (cv::Mat_<float>(3, 2) << 1, 7, 2, 8, 3, 9);
cv::Mat_<float> B = (cv::Mat_<float>(3, 2) << 4, 10, 5, 11, 6, 12);
cv::Mat C;
cv::vconcat(A, B, C);
cout << C << endl;
// out
[1, 7;
 2, 8;
 3, 9;
 4, 10;
 5, 11;
 6, 12]
```

### 示例三

```
std::vector<cv::Mat> matrices = {cv::Mat(1, 4, CV_8UC1, cv::Scalar(1)),
                                    cv::Mat(1, 4, CV_8UC1, cv::Scalar(2)),
                                    cv::Mat(1, 4, CV_8UC1, cv::Scalar(3)),};
cv::Mat out;
cv::vconcat(matrices, out);
cout << out << endl;
// out
[  1,   1,   1,   1;
   2,   2,   2,   2;
   3,   3,   3,   3]
```

## 使用其他函数完成合并

* [opencv中Mat矩阵的合并与拼接](https://blog.csdn.net/birenxiaofeigg/article/details/88847446)

## 相关阅读

* [opencv中Mat矩阵的合并与拼接](https://blog.csdn.net/birenxiaofeigg/article/details/88847446)