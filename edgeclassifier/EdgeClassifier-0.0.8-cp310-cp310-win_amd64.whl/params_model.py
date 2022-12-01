import torch.nn as nn


class Model(nn.Module):
    def __init__(self, params: dict):
        super().__init__()
        self.layers = nn.ModuleList()
        self.use_dropout_per_layer = []

        self.dropout = nn.Dropout(params["dropout"])
        self.activation = params["activation"]
        self.softmax = nn.Softmax()

        for (in_size, out_size, use_dropout) in params["layers"]:
            self.layers.append(nn.Linear(in_size, out_size))
            self.use_dropout_per_layer.append(use_dropout)

    def forward(self, x):
        for i, (layer, use_dropout) in enumerate(zip(self.layers, self.use_dropout_per_layer)):
            x = layer(x)
            if use_dropout:
                x = self.dropout(x)
            if i != len(self.layers) - 1:
                x = self.activation(x)

        x = x.squeeze(1)
        # Use sigmoid or softmax depends on the output size?
        x = self.activation(x)
        return x
