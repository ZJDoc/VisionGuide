# -*- coding: utf-8 -*-

"""
@date: 2020/5/2 下午11:11
@file: find_wd.py
@author: zj
@description: 
"""

import torch.optim as optim
from torch.utils.data import DataLoader
import torchvision.transforms as transforms
from torchvision.datasets import CIFAR100
from torchvision.models import SqueezeNet

from lr import util
from lr.SmoothLabelCriterion import SmoothLabelCritierion


def load_data(data_root_dir='../data/'):
    train_transform = transforms.Compose([
        transforms.Resize(256),
        transforms.RandomCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ColorJitter(brightness=0.1, contrast=0.1, saturation=0.1, hue=0.1),
        transforms.ToTensor(),
        transforms.RandomErasing(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])

    data_set = CIFAR100(data_root_dir, train=True, download=True, transform=train_transform)
    data_loader = DataLoader(data_set, batch_size=96, shuffle=True, num_workers=8)
    return data_loader


def find_wd(data_loader, model, criterion, optimizer, device, beta=0.98):
    num = len(data_loader) - 1
    avg_loss = 0.
    best_loss = 0.
    batch_num = 0
    losses = []
    for inputs, labels in data_loader:
        batch_num += 1

        # As before, get the loss for this mini-batch of inputs/outputs
        inputs = inputs.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)

        # Compute the smoothed loss
        avg_loss = beta * avg_loss + (1 - beta) * loss.item()
        smoothed_loss = avg_loss / (1 - beta ** batch_num)

        # Stop if the loss is exploding
        if batch_num > 1 and smoothed_loss > 4 * best_loss:
            return losses

        # Record the best loss
        if smoothed_loss < best_loss or batch_num == 1:
            best_loss = smoothed_loss

        # Store the values
        losses.append(smoothed_loss)

        # Do the SGD step
        loss.backward()
        optimizer.step()

    return losses


if __name__ == '__main__':
    device = util.get_device()
    # device = torch.device('cpu')

    data_loader = load_data()
    num_classes = 100

    res_dict = dict()
    for weight_decay in [0, 1e-3, 1e-4, 1e-5]:
        # for weight_decay in [3e-5, 1e-4, 3e-4]:
        model = SqueezeNet(num_classes=num_classes)
        model.eval()
        # print(model)
        model = model.to(device)

        criterion = SmoothLabelCritierion(label_smoothing=0.1)
        optimizer = optim.Adam(model.parameters(), lr=3e-4, weight_decay=weight_decay)

        losses = find_wd(data_loader, model, criterion, optimizer, device)
        res_dict[str(weight_decay)] = {'loss': losses}
        print('{} done'.format(weight_decay))
    util.plot_loss_lr(res_dict)
    print('done')
