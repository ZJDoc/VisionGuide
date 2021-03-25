# -*- coding: utf-8 -*-

"""
@date: 2020/5/2 下午2:41
@file: find_lr.py
@author: zj
@description: 发现最高学习率
"""

import math
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


def find_lr(data_loader, model, criterion, optimizer, device, init_value=1e-8, final_value=10., beta=0.98):
    num = len(data_loader) - 1
    mult = (final_value / init_value) ** (1 / num)
    lr = init_value
    optimizer.param_groups[0]['lr'] = lr
    avg_loss = 0.
    best_loss = 0.
    batch_num = 0
    losses = []
    log_lrs = []
    for inputs, labels in data_loader:
        batch_num += 1
        print('{}: {}'.format(batch_num, lr))

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
            return log_lrs, losses

        # Record the best loss
        if smoothed_loss < best_loss or batch_num == 1:
            best_loss = smoothed_loss

        # Store the values
        losses.append(smoothed_loss)
        log_lrs.append(math.log10(lr))

        # Do the SGD step
        loss.backward()
        optimizer.step()

        # Update the lr for the next step
        lr *= mult
        optimizer.param_groups[0]['lr'] = lr
    return log_lrs, losses


if __name__ == '__main__':
    device = util.get_device()
    # device = torch.device('cpu')

    data_loader = load_data()
    num_classes = 100
    for name in ['squeezenet']:
        model = SqueezeNet(num_classes=num_classes)
        model.eval()
        # print(model)
        model = model.to(device)

        criterion = SmoothLabelCritierion(label_smoothing=0.1)
        optimizer = optim.Adam(model.parameters(), lr=1e-8)

        log_lrs, losses = find_lr(data_loader, model, criterion, optimizer, device,
                                  init_value=1e-8, final_value=10., beta=0.98)
        util.plot(log_lrs, losses)
