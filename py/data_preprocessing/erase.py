# -*- coding: utf-8 -*-

"""
@date: 2020/5/1 上午10:09
@file: erase.py
@author: zj
@description: 
"""

import torchvision.transforms as transforms
from PIL import Image
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['simhei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def plot(src, dst, dst2):
    f = plt.figure()

    plt.subplot(311)
    h, w = src.size
    plt.title('原图 (w,h)=(%d, %d)' % (h, w))
    plt.imshow(src),  # plt.axis('off')

    plt.subplot(312)
    h, w = dst.size
    plt.title('随机擦除1 (w,h)=(%d, %d)' % (h, w))
    plt.imshow(dst),  # plt.axis('off')

    plt.subplot(313)
    h, w = dst2.size
    plt.title('随机擦除2 (w,h)=(%d, %d)' % (h, w))
    plt.imshow(dst2),  # plt.axis('off')

    plt.show()


if __name__ == '__main__':
    src = Image.open('../data/butterfly.jpg')

    # 随机擦除1
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.RandomErasing(),
        transforms.ToPILImage()
    ])
    dst = transform(src)

    # 随机擦除2
    transform2 = transforms.Compose([
        transforms.ToTensor(),
        transforms.RandomErasing(),
        transforms.ToPILImage()
    ])
    dst2 = transform2(src)

    plot(src, dst, dst2)
