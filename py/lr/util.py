# -*- coding: utf-8 -*-

"""
@date: 2020/5/2 下午2:47
@file: util.py
@author: zj
@description: 
"""

import os
import torch
import matplotlib.pyplot as plt


def get_device():
    return torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')


def check_dir(data_dir):
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)


def save_model(model, model_save_path):
    # 保存最好的模型参数
    check_dir('./models')
    torch.save(model.state_dict(), model_save_path)


def topk_accuracy(output, target, topk=(1,)):
    """
    计算前K个。N表示样本数，C表示类别数
    :param output: 大小为[N, C]，每行表示该样本计算得到的C个类别概率
    :param target: 大小为[N]，每行表示指定类别
    :param topk: tuple，计算前top-k的accuracy
    :return: list
    """
    assert len(output.shape) == 2 and output.shape[0] == target.shape[0]
    maxk = max(topk)
    batch_size = target.size(0)

    _, pred = output.topk(maxk, 1, largest=True, sorted=True)
    pred = pred.t()
    correct = pred.eq(target.view(1, -1).expand_as(pred))

    res = []
    for k in topk:
        correct_k = correct[:k].view(-1).float().sum(0)
        res.append(correct_k.mul_(100.0 / batch_size))
    return res


def plot(log_lrs, losses):
    # x_major_locator = MultipleLocator(1)
    # ax = plt.gca()
    # ax.xaxis.set_major_locator(x_major_locator)
    fig = plt.figure()

    plt.title('loss-lr')
    plt.xlabel('learning rate (log scale)')
    plt.ylabel('loss (smoothed)')
    plt.plot(log_lrs, losses)

    plt.savefig('./loss-lr.png')
    plt.show()


def plot_loss_lr(res_dict):
    fig = plt.figure()

    plt.xlabel('iteration')
    plt.ylabel('loss (smoothed)')
    for k, v in res_dict.items():
        losses = v['loss']
        plt.plot(losses, label=k)
    plt.legend()
    plt.savefig('./loss-lr.png')
    plt.show()


def save_png(title, res_dict):
    # x_major_locator = MultipleLocator(1)
    # ax = plt.gca()
    # ax.xaxis.set_major_locator(x_major_locator)
    fig = plt.figure()

    plt.title(title)
    for name, res in res_dict.items():
        for k, v in res.items():
            x = list(range(len(v)))
            plt.plot(v, label='%s-%s' % (name, k))

    plt.legend()
    plt.savefig('%s.png' % title)
