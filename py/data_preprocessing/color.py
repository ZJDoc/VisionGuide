# -*- coding: utf-8 -*-

"""
@date: 2020/4/30 下午2:41
@file: color.py
@author: zj
@description: 随机改变图像的亮度、对比度和饱和度
"""

import torchvision.transforms as transforms
from PIL import Image
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['simhei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def plot(src, dst, dst2, dst3, dst4):
    f = plt.figure()

    plt.subplot(231)
    plt.title('原图')
    plt.imshow(src), plt.axis('off')

    plt.subplot(232)
    plt.title('随机亮度')
    plt.imshow(dst), plt.axis('off')

    plt.subplot(233)
    plt.title('随机对比度')
    plt.imshow(dst2), plt.axis('off')

    plt.subplot(234)
    plt.title('随机饱和度')
    plt.imshow(dst3), plt.axis('off')

    plt.subplot(235)
    plt.title('随机色调')
    plt.imshow(dst4), plt.axis('off')

    plt.show()


if __name__ == '__main__':
    src = Image.open('../data/butterfly.jpg')

    # 随机改变亮度
    transform = transforms.Compose([
        transforms.ColorJitter(brightness=1)
    ])
    dst = transform(src)

    # 随机改变对比度
    transform2 = transforms.Compose([
        transforms.ColorJitter(contrast=1)
    ])
    dst2 = transform2(src)

    # 随机改变饱和度
    transform3 = transforms.Compose([
        transforms.ColorJitter(saturation=1)
    ])
    dst3 = transform3(src)

    # 随机改变色调
    transform4 = transforms.Compose([
        transforms.ColorJitter(hue=0.5)
    ])
    dst4 = transform4(src)

    plot(src, dst, dst2, dst3, dst4)
