import torch.nn
import torch_geometric.data
from typing import Union
from torch.utils.data import DataLoader
from torch_geometric.data import Batch
from torch_geometric.nn import Sequential
from torch_geometric.nn.norm import LayerNorm
from torch_geometric.nn.conv import GCNConv, GATConv, GINConv, NNConv, CGConv, TransformerConv
from torch_geometric.nn.glob import global_mean_pool, global_add_pool
from ailca.core.sys import is_gpu_runnable
from ailca.data.base import Dataset
from ailca.ml.base import PyTorchModel
from ailca.ml.nn import *
from ailca.ml.fnn import FCLayer


class GNNLayer(Layer):
    """
    A base class for the network layers of graph neural networks.
    """

    def __init__(self,
                 node_aggr_scheme: str,
                 dim_in_node: int,
                 dim_out: int,
                 dim_in_edge: int = None,
                 layer_norm: bool = False,
                 act_func: str = None):
        super(GNNLayer, self).__init__()
        self.__node_aggr_scheme = node_aggr_scheme
        self.__edge_aggr = False if dim_in_edge is None else True
        self._dim_in_node = dim_in_node
        self._dim_out = dim_out
        self._dim_in_edge = dim_in_edge
        self._layer_norm = layer_norm
        self._act_func = act_func

        if self.__node_aggr_scheme == ALG_GCN:
            self._modules.append((GCNConv(dim_in_node, dim_out), 'x, edge_index -> x'))
        elif self.__node_aggr_scheme == ALG_GAT:
            self._modules.append((GATConv(dim_in_node, dim_out), 'x, edge_index -> x'))
        elif self.__node_aggr_scheme == ALG_GIN:
            fcn = torch.nn.Linear(dim_in_node, dim_out)
            self._modules.append((GINConv(fcn), 'x, edge_index -> x'))
        elif self.__node_aggr_scheme == ALG_ECCNN:
            fce = torch.nn.Sequential(torch.nn.Linear(dim_in_edge, 64),
                                      torch.nn.ReLU(),
                                      torch.nn.Linear(64, dim_in_node * dim_out))
            self._modules.append((NNConv(dim_in_node, dim_out, fce), 'x, edge_index, edge_attr -> x'))
        elif self.__node_aggr_scheme == ALG_CGCNN:
            self._modules.append((CGConv(dim_in_node, dim_in_edge), 'x, edge_index, edge_attr -> x'))
        elif self.__node_aggr_scheme == ALG_TFGNN:
            self._modules.append((TransformerConv(dim_in_node, dim_out, edge_dim=dim_in_edge),
                                  'x, edge_index, edge_attr -> x'))
        else:
            raise AssertionError('Unknown node aggregation scheme \'{}\' was given.'.format(self.__node_aggr_scheme))

        if layer_norm:
            self._modules.append((LayerNorm(dim_out), 'x -> x'))

        if act_func is not None:
            self._modules.append(get_act_func(act_func))

    @property
    def node_aggr_scheme(self):
        return self.__node_aggr_scheme

    @property
    def dim_in_node(self):
        return self._dim_in_node

    @property
    def dim_in_edge(self):
        return self._dim_in_edge

    @property
    def edge_aggr(self):
        return self.__edge_aggr

    @property
    def layer_norm(self):
        return self._layer_norm

    @property
    def act_func(self):
        return self._act_func


class GNN(PyTorchModel):
    def __init__(self,
                 alg_id: str,
                 aggr_layers: list,
                 pred_layers: list,
                 readout_method: str = None,
                 node_emb_layers: list = None):
        super(GNN, self).__init__(alg_id)
        self.__edge_aggr = aggr_layers[0].edge_aggr
        self._aggr_layers = aggr_layers_to_sequential(aggr_layers, self.__edge_aggr)
        self._pred_layers = layers_to_sequential(pred_layers)
        self._node_emb_layers = None if node_emb_layers is None else layers_to_sequential(node_emb_layers)
        self._readout_method = readout_method
        self._dim_out = pred_layers[-1].dim_out

        aggr_layer_info = list()
        for layer in aggr_layers:
            aggr_layer_info.append({
                'node_aggr_scheme': layer.node_aggr_scheme,
                'dim_in_node': layer.dim_in_node,
                'dim_out': layer.dim_out,
                'dim_in_edge': layer.dim_in_edge,
                'layer_norm': layer.layer_norm,
                'act_func': layer.act_func
            })

        pred_layer_info = list()
        for layer in pred_layers:
            pred_layer_info.append({
                'dim_in': layer.dim_in,
                'dim_out': layer.dim_out,
                'batch_norm': layer.batch_norm,
                'act_func': layer.act_func
            })

        if node_emb_layers is None:
            node_emb_layer_info = None
        else:
            node_emb_layer_info = list()
            for layer in node_emb_layers:
                node_emb_layer_info.append({
                    'dim_in': layer.dim_in,
                    'dim_out': layer.dim_out,
                    'batch_norm': layer.batch_norm,
                    'act_func': layer.act_func
                })

        self._model_info = {
            'alg_id': self.alg_id,
            'alg_name': self.alg_name,
            'alg_src': self.alg_src,
            'readout_method': self._readout_method,
            'aggr_layers': aggr_layer_info,
            'pred_layers': pred_layer_info,
            'node_emb_layers': node_emb_layer_info,
            'dim_out': self.dim_out
        }

    def _readout(self,
                 node_embs: torch.Tensor,
                 batch_idx: torch.Tensor) -> torch.Tensor:
        if self._readout_method == READOUT_MEAN:
            return global_mean_pool(node_embs, batch_idx)
        elif self._readout_method == READOUT_SUM:
            return global_add_pool(node_embs, batch_idx)
        else:
            raise AssertionError('Unknown readout method {}.'.format(self._readout_method))

    def forward(self,
                x: Union[Batch, torch_geometric.data.Data]) -> torch.Tensor:
        # Feature embedding layer(s).
        if self._node_emb_layers is not None:
            node_feats = self._node_emb_layers(x.x)
        else:
            node_feats = x.x

        # Node aggregation layer(s).
        if self.__edge_aggr:
            h = self._aggr_layers(node_feats, x.edge_index, x.edge_attr)
        else:
            h = self._aggr_layers(node_feats, x.edge_index)

        # Readout.
        if self._readout_method is not None:
            if isinstance(x, Batch):
                batch = x.batch
            else:
                batch = torch.zeros(h.shape[0], dtype=torch.long)

                if is_gpu_runnable():
                    batch = batch.cuda()

            h = self._readout(h, batch)

        # Prediction layer(s).
        out = self._pred_layers(h)

        return out

    def fit(self,
            data_loader: DataLoader,
            optimizer: torch.optim.Optimizer,
            loss_func: torch.nn.Module) -> float:
        self.train()
        train_loss = 0

        for batch, y in data_loader:
            if is_gpu_runnable():
                batch = batch.cuda()
                y = y.cuda()

            y_p = self(batch)
            loss = loss_func(y_p, y)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            train_loss += loss.detach().item()

        return train_loss / len(data_loader)

    def predict(self,
                x: Union[torch_geometric.data.Data, Dataset]) -> torch.Tensor:
        self.eval()

        if isinstance(x, torch_geometric.data.Data):
            _x = x
        else:
            _x = Batch.from_data_list(x.x)

        with torch.no_grad():
            if is_gpu_runnable():
                return self(_x.cuda()).cpu()
            else:
                return self(_x)


class GCN(GNN):
    def __init__(self,
                 aggr_layers: list = None,
                 pred_layers: list = None,
                 dim_in_node: int = None,
                 dim_out: int = None,
                 readout_method: str = None):
        if aggr_layers is None:
            if dim_in_node is None or dim_out is None:
                raise AssertionError('For auto-configuration, dimensionalities of the input and target'
                                     'data must be provided by \'dim_in_node\' and \'dim_out\'.')

            aggr_layers = [
                GNNLayer(node_aggr_scheme=ALG_GCN, dim_in_node=dim_in_node, dim_out=256,
                         layer_norm=False, act_func=ACT_FUNC_PRELU),
                GNNLayer(node_aggr_scheme=ALG_GCN, dim_in_node=256, dim_out=256,
                         layer_norm=False, act_func=ACT_FUNC_PRELU),
                GNNLayer(node_aggr_scheme=ALG_GCN, dim_in_node=256, dim_out=256,
                         layer_norm=False, act_func=ACT_FUNC_PRELU)
            ]
            pred_layers = [
                FCLayer(dim_in=256, dim_out=256, batch_norm=True, act_func=ACT_FUNC_PRELU),
                FCLayer(dim_in=256, dim_out=128, batch_norm=True, act_func=ACT_FUNC_PRELU),
                FCLayer(dim_in=128, dim_out=dim_out)
            ]

        super(GCN, self).__init__(ALG_GCN, aggr_layers, pred_layers, readout_method)


class GAT(GNN):
    def __init__(self,
                 aggr_layers: list = None,
                 pred_layers: list = None,
                 dim_in_node: int = None,
                 dim_out: int = None,
                 readout_method: str = None):
        if aggr_layers is None:
            if dim_in_node is None or dim_out is None:
                raise AssertionError('For auto-configuration, dimensionalities of the input and target'
                                     'data must be provided by \'dim_in_node\' and \'dim_out\'.')

            aggr_layers = [
                GNNLayer(node_aggr_scheme=ALG_GAT, dim_in_node=dim_in_node, dim_out=256,
                         layer_norm=False, act_func=ACT_FUNC_PRELU),
                GNNLayer(node_aggr_scheme=ALG_GAT, dim_in_node=256, dim_out=256,
                         layer_norm=False, act_func=ACT_FUNC_PRELU),
                GNNLayer(node_aggr_scheme=ALG_GAT, dim_in_node=256, dim_out=256,
                         layer_norm=False, act_func=ACT_FUNC_PRELU)
            ]
            pred_layers = [
                FCLayer(dim_in=256, dim_out=256, batch_norm=True, act_func=ACT_FUNC_PRELU),
                FCLayer(dim_in=256, dim_out=128, batch_norm=True, act_func=ACT_FUNC_PRELU),
                FCLayer(dim_in=128, dim_out=dim_out)
            ]

        super(GAT, self).__init__(ALG_GAT, aggr_layers, pred_layers, readout_method)


class GIN(GNN):
    def __init__(self,
                 aggr_layers: list = None,
                 pred_layers: list = None,
                 dim_in_node: int = None,
                 dim_out: int = None,
                 readout_method: str = None):
        if aggr_layers is None:
            if dim_in_node is None or dim_out is None:
                raise AssertionError('For auto-configuration, dimensionalities of the input and target'
                                     'data must be provided by \'dim_in_node\' and \'dim_out\'.')

            aggr_layers = [
                GNNLayer(node_aggr_scheme=ALG_GIN, dim_in_node=dim_in_node, dim_out=256,
                         layer_norm=False, act_func=ACT_FUNC_PRELU),
                GNNLayer(node_aggr_scheme=ALG_GIN, dim_in_node=256, dim_out=256,
                         layer_norm=False, act_func=ACT_FUNC_PRELU),
                GNNLayer(node_aggr_scheme=ALG_GIN, dim_in_node=256, dim_out=256,
                         layer_norm=False, act_func=ACT_FUNC_PRELU)
            ]
            pred_layers = [
                FCLayer(dim_in=256, dim_out=256, batch_norm=True, act_func=ACT_FUNC_PRELU),
                FCLayer(dim_in=256, dim_out=128, batch_norm=True, act_func=ACT_FUNC_PRELU),
                FCLayer(dim_in=128, dim_out=dim_out)
            ]

        super(GIN, self).__init__(ALG_GIN, aggr_layers, pred_layers, readout_method)


class ECCNN(GNN):
    def __init__(self,
                 aggr_layers: list = None,
                 pred_layers: list = None,
                 dim_in_node: int = None,
                 dim_in_edge: int = None,
                 dim_out: int = None,
                 readout_method: str = None):
        if aggr_layers is None:
            if dim_in_node is None or dim_out is None:
                raise AssertionError('For auto-configuration, dimensionalities of the input and target'
                                     'data must be provided by \'dim_in_node\', \'dim_in_edge\', and \'dim_out\'.')

            aggr_layers = [
                GNNLayer(node_aggr_scheme=ALG_ECCNN, dim_in_node=dim_in_node, dim_in_edge=dim_in_edge, dim_out=128,
                         layer_norm=False, act_func=ACT_FUNC_PRELU),
                GNNLayer(node_aggr_scheme=ALG_ECCNN, dim_in_node=128, dim_in_edge=dim_in_edge, dim_out=64,
                         layer_norm=False, act_func=ACT_FUNC_PRELU),
                GNNLayer(node_aggr_scheme=ALG_ECCNN, dim_in_node=64, dim_in_edge=dim_in_edge, dim_out=64,
                         layer_norm=False, act_func=ACT_FUNC_PRELU)
            ]
            pred_layers = [
                FCLayer(dim_in=64, dim_out=128, batch_norm=True, act_func=ACT_FUNC_PRELU),
                FCLayer(dim_in=128, dim_out=128, batch_norm=True, act_func=ACT_FUNC_PRELU),
                FCLayer(dim_in=128, dim_out=dim_out)
            ]

        super(ECCNN, self).__init__(ALG_ECCNN, aggr_layers, pred_layers, readout_method)


class CGCNN(GNN):
    def __init__(self,
                 node_emb_layers: list = None,
                 aggr_layers: list = None,
                 pred_layers: list = None,
                 dim_in_node: int = None,
                 dim_in_edge: int = None,
                 dim_out: int = None,
                 readout_method: str = None):
        if aggr_layers is None:
            if dim_in_node is None or dim_out is None:
                raise AssertionError('For auto-configuration, dimensionalities of the input and target'
                                     'data must be provided by \'dim_in_node\', \'dim_in_edge\', and \'dim_out\'.')

            node_emb_layers = [
                FCLayer(dim_in=dim_in_node, dim_out=256, batch_norm=True, act_func=ACT_FUNC_PRELU)
            ]
            aggr_layers = [
                GNNLayer(node_aggr_scheme=ALG_CGCNN, dim_in_node=256, dim_in_edge=dim_in_edge, dim_out=256,
                         layer_norm=False, act_func=ACT_FUNC_PRELU),
                GNNLayer(node_aggr_scheme=ALG_CGCNN, dim_in_node=256, dim_in_edge=dim_in_edge, dim_out=256,
                         layer_norm=False, act_func=ACT_FUNC_PRELU),
                GNNLayer(node_aggr_scheme=ALG_CGCNN, dim_in_node=256, dim_in_edge=dim_in_edge, dim_out=256,
                         layer_norm=False, act_func=ACT_FUNC_PRELU)
            ]
            pred_layers = [
                FCLayer(dim_in=256, dim_out=256, batch_norm=True, act_func=ACT_FUNC_PRELU),
                FCLayer(dim_in=256, dim_out=128, batch_norm=True, act_func=ACT_FUNC_PRELU),
                FCLayer(dim_in=128, dim_out=dim_out)
            ]

        super(CGCNN, self).__init__(ALG_CGCNN, aggr_layers, pred_layers, readout_method, node_emb_layers)


class TFGNN(GNN):
    def __init__(self,
                 aggr_layers: list = None,
                 pred_layers: list = None,
                 dim_in_node: int = None,
                 dim_in_edge: int = None,
                 dim_out: int = None,
                 readout_method: str = None):
        if aggr_layers is None:
            if dim_in_node is None or dim_out is None:
                raise AssertionError('For auto-configuration, dimensionalities of the input and target'
                                     'data must be provided by \'dim_in_node\', \'dim_in_edge\', and \'dim_out\'.')

            aggr_layers = [
                GNNLayer(node_aggr_scheme=ALG_TFGNN, dim_in_node=dim_in_node, dim_in_edge=dim_in_edge, dim_out=256,
                         layer_norm=False, act_func=ACT_FUNC_PRELU),
                GNNLayer(node_aggr_scheme=ALG_TFGNN, dim_in_node=256, dim_in_edge=dim_in_edge, dim_out=256,
                         layer_norm=False, act_func=ACT_FUNC_PRELU),
                GNNLayer(node_aggr_scheme=ALG_TFGNN, dim_in_node=256, dim_in_edge=dim_in_edge, dim_out=256,
                         layer_norm=False, act_func=ACT_FUNC_PRELU)
            ]
            pred_layers = [
                FCLayer(dim_in=256, dim_out=256, batch_norm=True, act_func=ACT_FUNC_PRELU),
                FCLayer(dim_in=256, dim_out=128, batch_norm=True, act_func=ACT_FUNC_PRELU),
                FCLayer(dim_in=128, dim_out=dim_out)
            ]

        super(TFGNN, self).__init__(ALG_TFGNN, aggr_layers, pred_layers, readout_method)


def aggr_layers_to_sequential(list_layers: list,
                              contain_edge_feats: bool) -> Sequential:
    metadata = 'x, edge_index, edge_attr' if contain_edge_feats else 'x, edge_index'
    listed_layers = list()

    for layer in list_layers:
        for module in layer.tolist():
            listed_layers.append(module)

    return Sequential(metadata, listed_layers)
