import torch
from torch.nn.functional import relu
from torch.utils.data import DataLoader
from torch.nn import ModuleList
from ailca.core.env import *
from ailca.core.sys import is_gpu_runnable
from ailca.data.multimodal import MultimodalDataset
from ailca.ml.base import PyTorchModel
from ailca.data.util import get_data_loader


class MultimodalNet(PyTorchModel):
    def __init__(self,
                 nets: list,
                 dim_out: int):
        super(MultimodalNet, self).__init__(ALG_MULTIMODAL)
        self.__nets = nets
        self.__net_modules = ModuleList(nets)
        self.__dim_out_nets = sum([net.dim_out for net in self.__nets])
        self.fc1 = torch.nn.Linear(self.__dim_out_nets, 256)
        self.fc2 = torch.nn.Linear(256, dim_out)

        if is_gpu_runnable():
            for i in range(0, len(self.__nets)):
                self.__nets[i] = self.__nets[i].cuda()

        net_info = list()
        for net in nets:
            net_info.append(net.model_info)

        self._model_info = {
            'alg_id': self.alg_id,
            'alg_name': self.alg_name,
            'alg_src': self.alg_src,
            'nets': net_info,
            'dim_out': dim_out
        }

    def forward(self,
                x: list) -> torch.Tensor:
        h = list()
        for i in range(0, len(self.__nets)):
            h.append(self.__net_modules[i](x[i]))

        h = torch.hstack(h)
        h = relu(self.fc1(h))
        out = self.fc2(h)

        return out

    def fit(self,
            data_loader: DataLoader,
            optimizer: torch.optim.Optimizer,
            loss_func: torch.nn.Module):
        # Set the model to the training mode.
        self.train()

        # Initialize training loss.
        train_loss = 0

        # Train the machine learning model for each mini-batch.
        for x, y in data_loader:
            # Move the data from CPU to GPU if GPU is runnable.
            if is_gpu_runnable():
                for i in range(0, len(x)):
                    x[i] = x[i].cuda()
                y = y.cuda()

            # Predict target values for the input data.
            y_p = self(x)

            # Calculate the training loss for the mini-batch.
            loss = loss_func(y_p, y)

            # Optimize the model parameters.
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            # Accumulate the training loss.
            train_loss += loss.item()

        return train_loss / len(data_loader)

    def predict(self,
                dataset: MultimodalDataset) -> torch.Tensor:
        # Set the model to the evaluation model.
        self.eval()

        preds = list()
        data_loader = get_data_loader(dataset, batch_size=64, shuffle=False)

        with torch.no_grad():
            for x, _ in data_loader:
                if is_gpu_runnable():
                    for i in range(0, len(x)):
                        x[i] = x[i].cuda()

                    preds.append(self(x).cpu())
                else:
                    preds.append(self(x))

        return torch.vstack(preds)
