import torch
import torch.nn as nn
import numpy as np
import json
import os
import pytorch_lightning as pl


class MeanMaxPooling(nn.Module):
    """
    [B, S, E] -> [B, 2*E]
    """
    def __init__(self, axis=1, dropout=0.0):
        super().__init__()
        self.axis = axis
        self.dropout = nn.Dropout(p=dropout)

    def forward(self, inputs, valid_length=None):
        """
        :param inputs: Tensor, shape [batch_size, seq_len, embedding_dim]
        :param valid_length: None or Tensor, valid len of token in the sequence with shape [batch_size]
        :return: Tensor, shape [batch_size, 2 * embedding_dim]
        """
        # TODO: broadcast indexing to mean over first vl
        mean_out = torch.mean(inputs, dim=self.axis) if valid_length is None \
            else torch.sum(inputs, dim=self.axis) / valid_length.add(1E-7).unsqueeze(1)
        max_out = torch.max(inputs, dim=self.axis).values
        outputs = torch.cat((mean_out, max_out), dim=1)
        outputs = self.dropout(outputs)
        return outputs


class Whitening:
    def __init__(self, vecs, n_components=248):
        super().__init__()
        self.vecs = vecs
        self.n_components = n_components
    
    def compute_kernel_bias(self, axis=0, keepdims=True):
        mu = self.vecs.mean(axis=axis, keepdims=keepdims)
        cov = np.cov(self.vecs.T)
        u, s, vh = np.linalg.svd(cov)
        W = np.dot(u, np.diag(1 / np.sqrt(s)))
        return W[:, :self.n_components], -mu

    def transform_and_normalize(self, kernel=None, bias=None):
        if not (kernel is None or bias is None):
            vecs = (self.vecs + bias).dot(kernel)
        return vecs / (self.vecs**2).sum(axis=1, keepdims=True)**0.5
