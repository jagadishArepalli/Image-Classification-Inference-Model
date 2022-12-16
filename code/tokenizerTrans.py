import torch
import torchvision
import torch.nn as nn
import numpy as np
import torch.nn.functional as F

class Tokenizer(nn.Module):
    def __init__(self, L, CT, C, head=16, groups=16, dynamic=False, input_channels=256):
        super(Tokenizer , self).__init__()
        self.feature = nn.Conv2d(input_channels, C, kernel_size=1)
        if not dynamic :
            self.conv_token_coef = nn.Conv2d(C, L, kernel_size=1) 
        else:
            self.conv_query = nn.Conv1d(CT, C, kernel_size=1) 
            self.conv_key = nn.Conv2d(C, C, kernel_size=1, groups=groups)
        self.conv_value = nn.Conv2d(C, C,kernel_size=1, groups=groups)
        self.head = head
        self.dynamic = dynamic
        self.C = C

    def forward(self, feature, tokens=0):
        N, C, H, W = feature.shape
        if C != self.C:
            feature = self.feature(feature)
        if not self.dynamic : 
            token_coef = self.conv_token_coef(feature)
            N, L, H, W = token_coef.shape
            token_coef = token_coef.view(N, 1, L, H * W)
            token_coef = token_coef.permute(0, 1, 3, 2) 
            token_coef = token_coef / np.sqrt(feature.shape[1])
        else: 
            L = tokens.shape[2]
            T_a, T_b = tokens[:, :, :L // 2], tokens[:, :, L // 2:] 
            query = self.conv_query(T_a)
            N, C, L_a = query.shape
            query = query.view(N, self.head, C // self.head, L_a) 
            N, C, H, W = feature.shape
            key = self.conv_key(feature).view(N, self.head, C // self.head, H * W) 
            token_coef = torch.Tensor.matmul(key.permute(0, 1, 3, 2), query) 
            token_coef = token_coef / np.sqrt(C / self.head)
        N, C, H, W = feature.shape
        token_coef = F.softmax(token_coef , dim=2)
        value = self.conv_value(feature).view(N, self.head, C // self.head, H * W) 
        tokens = torch.Tensor.matmul(value, token_coef).view(N, C, -1)
        tokens = tokens.view(N, L, C)
        return feature, tokens