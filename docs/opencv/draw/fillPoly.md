
# [掩码]绘制多边形

进行多边形的绘制和填充

## 示例程序

```
import cv2
import numpy as np

img = cv2.imread('box.png')

# binary mask
coordinates = []
coordinate = np.array([[[100, 100], [300, 100], [200, 200], [100, 200]]])
coordinate2 = np.array([[[100, 100], [300, 200], [100, 300], [100, 200]]])
print(coordinate.shape)
print(coordinate2.shape)
coordinates.append(coordinate)
coordinates.append(coordinate2)

mask = np.zeros(img.shape[:2], dtype=np.int8)
mask = cv2.fillPoly(mask, coordinates, 255)

# 掩码实现
image = cv2.add(img, np.zeros(np.shape(img), dtype=np.uint8), mask=mask)

cv2.imshow('mask', mask)
cv2.imshow('image', image)
cv2.waitKey(0)
```

## 出错

```
cv2.error: OpenCV(4.4.0) /tmp/pip-req-build-f9hglo4e/opencv/modules/imgproc/src/drawing.cpp:2395: error: (-215:Assertion failed) p.checkVector(2, CV_32S) >= 0 in function 'fillPoly'
```

**注意：每个多边形坐标点数组大小为(1, 4, 2)，其数据格式为np.int**

## 相关阅读

* [python opencv cv2在图片中画mask掩码/掩膜](https://blog.csdn.net/xjtdw/article/details/107073396)
* [cv2.fillConvexPoly()与cv2.fillPoly()填充多边形](https://www.cnblogs.com/Ph-one/p/12082692.html)