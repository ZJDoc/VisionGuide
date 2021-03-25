
# 特征/特征检测/特征描述

`OpenCV`提供了一篇很好的文章来介绍什么是特征、特征检测以及特征描述符：[Understanding Features](https://docs.opencv.org/master/df/d54/tutorial_py_features_meaning.html)

## 什么是特征

对计算机视觉而言，特征就是图像中的一部分区域

## 什么是好的特征

好的特征就是从该区域向图像任何方向移动时，其内容会发现最大的变化，比如角特征（`corner features`）或者斑点特征（`blob features`）

## 什么是特征检测

发现这些图像特征的方法就是特征检测（`Feature Detection`）

## 什么是特征描述

如何用计算机语言描述图像特征所在区域，使得计算机可以在其他图像上发现相同的特征，这一方法称为特征描述（`Feature Description`）

## 小结

* 好的特征 = 图像中最独特的区域
* 特征检测 = 发现图像中的特征
* 特征描述 = 发现不同图像中相同的特征

之后就可以进行图像对齐、图像分类、图像检测等任务了