import torch
import os
from ..models import create_model


def save_model(model, name="model.pth"):
    os.makedirs(os.path.dirname(name), exist_ok=True)
    torch.save(model.state_dict(), name)
    print(f"Saved PyTorch Model State to {name}")


def load_model(model_name, classes, path, pretrained=False):
    model = create_model(name=model_name, classes=classes,
                         pretrained=pretrained)
    model.load_state_dict(torch.load(path))
    return model
