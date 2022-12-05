import timm
import torch
from torch import nn


# Define model
class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10)
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

    def model():
        device = "cuda" if torch.cuda.is_available() else "cpu"
        return NeuralNetwork().to(device)


def create_model(name, classes=None, pretrained=False):
    if name == "NeuralNetwork":
        model = NeuralNetwork.model()
    elif len(name):
        model = timm.create_model(
            name, num_classes=len(classes), pretrained=pretrained)
    return model
