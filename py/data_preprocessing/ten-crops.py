# -*- coding: utf-8 -*-

"""
@date: 2020/4/30 下午3:16
@file: ten-crops.py
@author: zj
@description: 
"""

import torch
import torchvision.transforms as transforms
from PIL import Image
import matplotlib.pyplot as plt
from torchvision.models import alexnet
from torchvision.datasets import CIFAR10
from torch.utils.data import Dataset
from torch.utils.data import DataLoader


def plot(src, dsts):
    f = plt.figure()

    cols = 3
    rows = 2

    plt.subplot(rows, cols, 1)
    plt.title('src')
    plt.imshow(src)

    for i in range(rows):
        for j in range(cols):
            if (i * cols + j) == 5:
                break

            plt.subplot(rows, cols, i * cols + j + 2)
            plt.imshow(dsts[i * cols + j])

    plt.show()


def draw_five_crop():
    src = Image.open('../data/butterfly.jpg')

    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.FiveCrop(224),  # this is a list of PIL Images
    ])

    dsts = transform(src)
    print(len(dsts))
    plot(src, dsts)


if __name__ == '__main__':
    src = Image.open('../data/butterfly.jpg')

    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.FiveCrop(224),  # this is a list of PIL Images
        transforms.Lambda(lambda crops: torch.stack([transforms.ToTensor()(crop) for crop in crops])),
        transforms.Lambda(lambda crops: torch.stack(
            [transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))(crop) for crop in crops])),
        # returns a 4D  tensor
    ])

    # # for 测试
    model = alexnet()
    data_set = CIFAR10('./data', download=True)
    data_loader = DataLoader(data_set, batch_size=8, shuffle=True, num_workers=8)

    # # In your test loop you can do the following:
    inputs, target = next(iter(data_loader))  # input is a 5d tensor, target is 2d
    N, N_crops, C, H, W = inputs.size()
    result = model(inputs.view(-1, C, H, W))  # fuse batch size and ncrops
    result_avg = result.view(N, N_crops, -1).mean(1)  # avg over crops
