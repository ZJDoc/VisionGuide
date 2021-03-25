# -*- coding: utf-8 -*-

"""
@date: 2020/4/30 下午2:52
@file: compose.py
@author: zj
@description: 组合实现多种图像预处理
"""

import torchvision.transforms as transforms
from PIL import Image
import matplotlib.pyplot as plt

if __name__ == '__main__':
    src = Image.open('../data/lena.jpg')

    # 预处理顺序如下：
    # 1. 按较短边缩放
    # 2. 随机裁剪224x224
    # 3. 随机水平翻转
    # 4. 随机颜色抖动：亮度、对比度、饱和度、色调
    transform = transforms.Compose([
        transforms.Resize(224),
        transforms.RandomCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ColorJitter(brightness=0.1, contrast=0.1, saturation=0.1, hue=0.1),
        transforms.ToTensor(),
        transforms.RandomErasing(),
        transforms.ToPILImage()
    ])

    cols = 3
    rows = 3
    for i in range(rows):
        for j in range(cols):
            plt.subplot(rows, cols, i * cols + j + 1)
            plt.imshow(transform(src))
            plt.axis('off')
    plt.show()
