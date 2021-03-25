
# [Point_]坐标点的保存和使用

经常需要对图像坐标点进行操作，`OpenCV`提供了类`Point_`来保存`x/y`坐标

## 声明

头文件声明如下：`#include <opencv2/core/types.hpp>`

头文件位置：`/path/to/include/opencv4/opencv2/core/types.hpp`

## 解析

类定义如下：

```
template<typename _Tp> class Point_
{
public:
    typedef _Tp value_type;

    //! default constructor
    Point_();
    Point_(_Tp _x, _Tp _y);
    Point_(const Point_& pt);
    Point_(Point_&& pt) CV_NOEXCEPT;
    Point_(const Size_<_Tp>& sz);
    Point_(const Vec<_Tp, 2>& v);

    Point_& operator = (const Point_& pt);
    Point_& operator = (Point_&& pt) CV_NOEXCEPT;
    //! conversion to another data type
    template<typename _Tp2> operator Point_<_Tp2>() const;

    //! conversion to the old-style C structures
    operator Vec<_Tp, 2>() const;

    //! dot product
    _Tp dot(const Point_& pt) const;
    //! dot product computed in double-precision arithmetics
    double ddot(const Point_& pt) const;
    //! cross-product
    double cross(const Point_& pt) const;
    //! checks whether the point is inside the specified rectangle
    bool inside(const Rect_<_Tp>& r) const;
    _Tp x; //!< x coordinate of the point
    _Tp y; //!< y coordinate of the point
};
```

定义了两个变量`x`和`y`，同时允许执行以下操作：

```
pt1 = pt2 + pt3;                               # 加法
pt1 = pt2 - pt3;                               # 减法
pt1 = pt2 * a;                                 # 乘以固定数
pt1 = a * pt2;
pt1 = pt2 / a;                                 # 除以固定数
pt1 += pt2;
pt1 -= pt2;
pt1 *= a;
pt1 /= a;
double value = norm(pt); // L2 norm            # L2范数
pt1 == pt2;                                    # 比较两个点是否相等
pt1 != pt2;
```

### 别名

类`Point_`是一个模板，所以可以在定义类对象时指定数据类型，比如`int/float/double`。`OpenCV`也提供了一些常用数据类型别名

```
typedef Point_<int> Point2i;                   # 整型点
typedef Point2i Point;
typedef Point_<float> Point2f;                 # 浮点型点
typedef Point_<double> Point2d;                # 双精度浮点型点
```

### 类型转换

浮点数`Point`可以转换成整数`Point`，其通过四舍五入方式进行转换

## 示例

```
#include <iostream>
#include <opencv2/opencv.hpp>
#include <opencv2/core/types.hpp>

int main() {
    cv::Point2i pt2i(2, 3);
    cv::Point2f pt2f(2.2, 3.6);

    std::cout << pt2i << std::endl;
    std::cout << pt2f << std::endl;

    cv::Point2f pt = static_cast<cv::Point2f>(pt2i) + pt2f;         // 加法
    std::cout << pt << std::endl;

    pt2i = pt2f;                                                    // 类型转换
    std::cout << pt2i << std::endl;

    std::cout << cv::norm(pt2i) << std::endl;                       // L2范数
}
```

执行结果

```
[2, 3]
[2.2, 3.6]
[4.2, 6.6]
[2, 4]
4.47214
```

## 类似结构

类似的数据结构还包括`3`维点（`Point3_`）、大小（`Size_`）、`2`维矩阵（`Rect_`）等等

## 相关阅读

* [Detailed Description](https://docs.opencv.org/4.1.0/db/d4e/classcv_1_1Point__.html#details)