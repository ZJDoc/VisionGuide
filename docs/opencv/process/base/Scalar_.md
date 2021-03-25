
# [Scalar_]4维向量

`OpenCV`常用`Scalar`保存像素值

## 声明

头文件声明：`#include <opencv2/core/types.hpp>`

头文件位置：`/path/to/opencv4/opencv2/core/types.hpp`

## 解析

`OpenCV`定义了一个模板类，其派生自`4`维向量

```
template<typename _Tp> class Scalar_ : public Vec<_Tp, 4>
{
public:
    //! default constructor
    Scalar_();
    Scalar_(_Tp v0, _Tp v1, _Tp v2=0, _Tp v3=0);
    Scalar_(_Tp v0);

    Scalar_(const Scalar_& s);
    Scalar_(Scalar_&& s) CV_NOEXCEPT;

    Scalar_& operator=(const Scalar_& s);
    Scalar_& operator=(Scalar_&& s) CV_NOEXCEPT;

    template<typename _Tp2, int cn>
    Scalar_(const Vec<_Tp2, cn>& v);

    //! returns a scalar with all elements set to v0
    static Scalar_<_Tp> all(_Tp v0);

    //! conversion to another data type
    template<typename T2> operator Scalar_<T2>() const;

    //! per-element product
    Scalar_<_Tp> mul(const Scalar_<_Tp>& a, double scale=1 ) const;

    //! returns (v0, -v1, -v2, -v3)
    Scalar_<_Tp> conj() const;

    //! returns true iff v1 == v2 == v3 == 0
    bool isReal() const;
};
```

最多可以保存`4`个值，定义类对象时需要输入至少两个数值

### 操作

* 对对象或两个对象进行乘/除操作
* 计算`L2`范数

等等

### 别名

定义了一个双精度类型别名`Scalar`

```
typedef Scalar_<double> Scalar;
```

## 示例

```
#include <iostream>
#include <opencv2/opencv.hpp>
#include <opencv2/core/types.hpp>

int main() {
    cv::Scalar s1(1, 2);
    cv::Scalar s2(0.23, 3.2, 11.13);

    std::cout << s1 << std::endl;
    std::cout << s2 << std::endl;

    cv::Scalar s3 = s1 + s2;                           // 加法
    std::cout << s3 << std::endl;

    cv::Scalar s4 = s1 - s2;                           // 减法
    std::cout << s4 << std::endl;

    std::cout << cv::norm(s1) << std::endl;            // L2范数

    std::cout << (s1 * 3) << std::endl;                // 乘以一个因子
}
```

运行结果

```
[1, 2, 0, 0]
[0.23, 3.2, 11.13, 0]
[1.23, 5.2, 11.13, 0]
[0.77, -1.2, -11.13, 0]
2.23607
[3, 6, 0, 0]
```

## 相关阅读

* [Detailed Description](https://docs.opencv.org/4.1.0/d1/da0/classcv_1_1Scalar__.html#details)