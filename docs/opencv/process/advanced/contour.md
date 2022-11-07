
# 轮廓检测

## 引言

定位具体物体的轮廓形状。首先需要将图像转换成为二值图像，常用的方式是

* `BGR -> GRAY -> THRESH -> FILTER`

然后就可以针对边缘信息进行物体定位，首先绘制出轮廓，然后将使用矩形框进行定位。关键函数如下：

* `C++`
    * [cv::getStructuringElement](https://docs.opencv.org/4.x/d4/d86/group__imgproc__filter.html#gac342a1bb6eabf6f55c803b09268e36dc)
    * [cv::morphologyEx](https://docs.opencv.org/3.4/d4/d86/group__imgproc__filter.html#ga67493776e3ad1a3df63883829375201f)
    * [cv::findContour](https://docs.opencv.org/3.4/d3/dc0/group__imgproc__shape.html#ga17ed9f5d79ae97bd4c7cf18403e1689a)
    * [cv::boundingRect](https://docs.opencv.org/3.4/d3/dc0/group__imgproc__shape.html#ga103fcbda2f540f3ef1c042d6a9b35ac7)

## 相关阅读

* [Morphological Transformations](https://docs.opencv.org/3.4/d4/d76/tutorial_js_morphological_ops.html)
* [Extract horizontal and vertical lines by using morphological operations](https://docs.opencv.org/4.x/dd/dd7/tutorial_morph_lines_detection.html)
* [边缘检测，框出物体的轮廓(使用opencv-python)](https://zhuanlan.zhihu.com/p/38739563)