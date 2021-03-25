# -*- coding: utf-8 -*-

"""
@date: 2020/4/30 下午4:22
@file: SmoothLabelCriterion.py
@author: zj
@description: 
"""

import torch
import torch.nn as nn


class SmoothLabelCritierion(nn.Module):
    """
    TODO:
    1. Add label smoothing
    2. Calculate loss
    """

    def __init__(self, label_smoothing=0.0):
        super(SmoothLabelCritierion, self).__init__()
        self.label_smoothing = label_smoothing
        self.LogSoftmax = nn.LogSoftmax(dim=1)

        # When label smoothing is turned on, KL-divergence is minimized
        # If label smoothing value is set to zero, the loss
        # is equivalent to NLLLoss or CrossEntropyLoss.
        if label_smoothing > 0:
            self.criterion = nn.KLDivLoss(reduction='batchmean')
        else:
            self.criterion = nn.NLLLoss()
        self.confidence = 1.0 - label_smoothing

    def _smooth_label(self, num_tokens):

        one_hot = torch.randn(1, num_tokens)
        one_hot.fill_(self.label_smoothing / (num_tokens - 1))
        return one_hot

    def _bottle(self, v):
        return v.view(-1, v.size(2))

    def forward(self, dec_outs, labels):
        # Map the output to (0, 1)
        scores = self.LogSoftmax(dec_outs)
        # n_class
        num_tokens = scores.size(-1)

        gtruth = labels.view(-1)
        if self.confidence < 1:
            tdata = gtruth.detach()
            one_hot = self._smooth_label(num_tokens)
            if labels.is_cuda:
                one_hot = one_hot.cuda()
            tmp_ = one_hot.repeat(gtruth.size(0), 1)
            tmp_.scatter_(1, tdata.unsqueeze(1), self.confidence)
            gtruth = tmp_.detach()
        loss = self.criterion(scores, gtruth)
        return loss


if __name__ == '__main__':
    outputs = torch.randn((1, 10))
    targets = torch.ones(1).long()
    print(outputs)
    print(targets)

    tmp = SmoothLabelCritierion(label_smoothing=0.1)
    loss = tmp.forward(outputs, targets)
    print(loss)

    tmp = nn.CrossEntropyLoss()
    loss = tmp.forward(outputs, targets)
    print(loss)

    print(1 / 10)
