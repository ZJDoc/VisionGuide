#include <iostream>

#include "opencv2/opencv.hpp"

int main() {
  // 读取图片
  cv::Mat image = cv::imread("../lena.jpg");
  if (image.empty()) {
    std::cout << "无法读取图片，请确保文件路径正确" << std::endl;
    return -1;
  }

  // 获取图片的尺寸
  int width = image.cols;
  int height = image.rows;

  // 计算中心裁剪的区域
  int x = width / 4;          // 裁剪区域的左上角 x 坐标
  int y = height / 4;         // 裁剪区域的左上角 y 坐标
  int cropWidth = width / 2;  // 裁剪区域的宽度
  int cropHeight = height / 2;// 裁剪区域的高度

  // 裁剪图片
  cv::Rect cropRegion(x, y, cropWidth, cropHeight);
  cv::Mat croppedImage = image(cropRegion);

  // 显示原始图片和裁剪后的图片
  cv::imshow("原始图片", image);
  cv::imshow("裁剪后的图片", croppedImage);
  cv::waitKey(0);

  // 保存裁剪后的图片
  cv::imwrite("../cropped_lena.jpg", croppedImage);

  std::cout << "Hello, World!" << std::endl;
  return 0;
}
