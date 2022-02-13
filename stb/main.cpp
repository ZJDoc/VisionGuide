#include <iostream>

#define STB_IMAGE_IMPLEMENTATION
#include "stb_image.h"
#define STB_IMAGE_WRITE_IMPLEMENTATION
#include "stb_image_write.h"

int main() {
    const char *file_name = "../assets/mnist_0.png";

    // 分别获取宽 / 高 / 通道数
    int x, y, n;
    // 返回的data是一个字节数组，包含了解析的图像像素值
    unsigned char *data = stbi_load(file_name, &x, &y, &n, 0);
    std::cout << "width: " << x << " height: " << y << " channels: " << n << std::endl;

    // 写入文件，按保存格式选择
//    JPEG does ignore alpha channels in input data; quality is between 1 and 100.
//    Higher quality looks better but results in a bigger image.
    stbi_write_jpg("../assets/mnist_0_write_jpg.jpg", x, y, n, data, 100);
//    For PNG, "stride_in_bytes" is the distance in bytes from the first byte of
//    a row of pixels to the first byte of the next row of pixels.
    stbi_write_png("../assets/mnist_0_write_png.png", x, y, n, data, 0);

    // 释放字节数组
    stbi_image_free(data);

    std::cout << "Hello, World!" << std::endl;
    return 0;
}
