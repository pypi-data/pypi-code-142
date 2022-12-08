import os
import json
from copy import deepcopy
from ailca.core.operation import flatten_lists
from ailca.data.util import get_data_loader
from ailca.data.multimodal import MultimodalDataset
from ailca.ml.base import Model, SKLearnModel
from ailca.ml.fnn import *
from ailca.ml.cnn import *
from ailca.ml.gnn import *
from ailca.ml.multimodal import MultimodalNet


class MLResult:
    def __init__(self,
                 model: Model,
                 dataset_train: Dataset,
                 dataset_test: Dataset = None):
        self.model = model
        self.dataset_train = dataset_train
        self.dataset_test = dataset_test

    def save(self,
             dir_name: str):
        """
        Save machine learning results.

        :param dir_name: (*str*) The name of the directory to store machine learning results.
        """

        # Make a directory to store machine learning results.
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

        # Store metadata of the prediction model.
        exp_info = dict()
        exp_info['model_info'] = self.model.model_info

        # Store metadata of the dataset.
        if isinstance(self.dataset_train, MultimodalDataset):
            exp_info['dataset_info'] = list()
            for i in range(0, len(self.dataset_train.datasets)):
                exp_info['dataset_info'].append(self.dataset_train.datasets[i].metadata)
        else:
            exp_info['dataset_info'] = self.dataset_train.metadata

        # Store the machine learning results on the training dataset.
        preds_train = self.model.predict(self.dataset_train)
        exp_info['mae_train'] = mae(self.dataset_train.y, preds_train)
        exp_info['r2_train'] = r2_score(self.dataset_train.y, preds_train)

        # Store the machine learning results on the test dataset if it is available.
        if self.dataset_test is not None:
            exp_info['preds_test'] = self.model.predict(self.dataset_test)
            exp_info['mae_test'] = mae(self.dataset_test.y, exp_info['preds_test'])
            exp_info['r2_test'] = r2_score(self.dataset_test.y, exp_info['preds_test'])
            exp_info['targets_test'] = self.dataset_test.y.flatten().tolist()
            exp_info['preds_test'] = exp_info['preds_test'].flatten().tolist()

        # Save the JSON file to store the metadata.
        with open(dir_name + '/exp_info.json', 'w') as f:
            json.dump(exp_info, f)

        # Save the model parameters.
        self.model.save(dir_name + '/pred_model.pt')


def get_optimizer(model: PyTorchModel,
                  gradient_method: str,
                  init_lr: float = 1e-3,
                  l2_reg: float = 1e-6) -> torch.optim.Optimizer:
    """
    Get a gradient-based optimizer to fit the model parameters of neural networks.

    :param model: (*PyTorchModel*) A model to be optimized.
    :param gradient_method: (*str*) A name of the gradient method.
    :param init_lr: (*float, optional*) Initial learning rate of the gradient-based optimizer (*default* = 1e-6).
    :param l2_reg: (*float, optional*) L2 regularization coefficient to prevent the overfitting problem.
    :return: (*torch.optim.Optimizer*) A gradient-based optimizer.
    """

    if gradient_method == GD_SGD:
        return torch.optim.SGD(model.parameters(), lr=init_lr, weight_decay=l2_reg, momentum=0.9)
    elif gradient_method == GD_ADADELTA:
        return torch.optim.Adadelta(model.parameters(), lr=init_lr, weight_decay=l2_reg)
    elif gradient_method == GD_RMSPROP:
        return torch.optim.RMSprop(model.parameters(), lr=init_lr, weight_decay=l2_reg)
    elif gradient_method == GD_ADAM:
        return torch.optim.Adam(model.parameters(), lr=init_lr, weight_decay=l2_reg)
    else:
        raise AssertionError('Unknown gradient method {} was given.'.format(gradient_method))


def get_loss_func(loss_func: str) -> Union[torch.nn.L1Loss, torch.nn.MSELoss, torch.nn.SmoothL1Loss]:
    """
    Get a loss function object to run the gradient-based optimizers.

    :param loss_func: (*str*) A name of the loss function.
    :return: (*Union[torch.nn.L1Loss, torch.nn.MSELoss, torch.nn.SmoothL1Loss]*) A loss function object.
    """

    if loss_func == LOSS_MAE:
        return torch.nn.L1Loss()
    elif loss_func == LOSS_MSE:
        return torch.nn.MSELoss()
    elif loss_func == LOSS_SMAE:
        return torch.nn.SmoothL1Loss()
    else:
        raise AssertionError('Unknown loss function {} was given.'.format(loss_func))


def mae(targets: torch.Tensor,
        preds: torch.Tensor) -> float:
    """
    Calculate mean absolute error (MAE) of the given ``targets`` and ``preds``.

    :param targets: (*torch.Tensor*) Target values.
    :param preds: (*torch.Tensor*) Predicted values.
    :return: (*float*) Calculated mean absolute error.
    """

    return torch.mean(torch.abs(targets - preds)).item()


def rmse(targets: torch.Tensor,
         preds: torch.Tensor) -> float:
    """
    Calculate root-mean-square error (RMSE) of the given ``targets`` and ``preds``.

    :param targets: (*torch.Tensor*) Target values.
    :param preds: (*torch.Tensor*) Predicted values.
    :return: (*float*) Calculated root-mean-square error.
    """

    return torch.sqrt(torch.mean((targets - preds)**2)).item()


def r2_score(targets: torch.Tensor,
             preds: torch.Tensor) -> float:
    """
    Calculate r2-score (coefficient of determination) of the given ``targets`` and ``preds``.

    :param targets: (*torch.Tensor*) Target values.
    :param preds: (*torch.Tensor*) Predicted values.
    :return: (*float*) Calculated r2-score.
    """

    target_mean = torch.mean(targets)
    ss_tot = torch.sum((targets - target_mean)**2)
    ss_res = torch.sum((targets - preds)**2)

    return (1 - ss_res / ss_tot).item()


def k_fold_cross_validation(k_folds: list,
                            model: Model,
                            batch_size: int = 64,
                            gradient_method: str = 'adam',
                            loss_func: str = 'mae',
                            init_lr: float = 1e-3,
                            l2_reg: float = 1e-6,
                            n_epochs: int = 300,
                            random_seed: int = 0) -> dict:
    """

    :param k_folds:
    :param model:
    :param batch_size:
    :param gradient_method:
    :param loss_func:
    :param init_lr:
    :param l2_reg:
    :param n_epochs:
    :param random_seed:
    :return: (*dict*) A dictionary
    """

    scores = list()
    idx_test = list()
    preds = list()
    targets = list()
    tooltips = list()
    eval_results = dict()

    for k in range(0, len(k_folds)):
        dataset_train, dataset_test = k_folds[k]

        if isinstance(model, SKLearnModel):
            _model = deepcopy(model)
            _model.fit(dataset_train)
            preds_test = _model.predict(dataset_test)
        elif isinstance(model, PyTorchModel):
            min_loss_val = 1e+8
            dataset_train, dataset_val = dataset_train.split(ratio_train=0.8, random_seed=random_seed)
            loader_train = get_data_loader(dataset_train, batch_size=batch_size, shuffle=True)
            init_state_dict = deepcopy(model.state_dict())
            best_state_dict = None

            model.load_state_dict(deepcopy(init_state_dict))
            optimizer = get_optimizer(model, gradient_method=gradient_method, init_lr=init_lr, l2_reg=l2_reg)
            criterion = get_loss_func(loss_func=loss_func)

            for n in range(0, n_epochs):
                _ = model.fit(loader_train, optimizer, criterion)
                preds_val = model.predict(dataset_val)
                loss_val = criterion(preds_val, dataset_val.y)

                if loss_val < min_loss_val:
                    best_state_dict = deepcopy(model.state_dict())
                    min_loss_val = loss_val

            model.load_state_dict(best_state_dict)
            preds_test = model.predict(dataset_test)
            scores.append(criterion(preds_test, dataset_test.y).item())
        else:
            raise KeyError('Unknown source library \'{}\' of the prediction model.'.format(model.alg_src))

        idx_test.append(dataset_test.idx_data)
        preds.append(preds_test)
        targets.append(dataset_test.y)
        tooltips.append(dataset_test.tooltips)

    preds = torch.vstack(preds)
    targets = torch.vstack(targets)
    eval_results['idx_test'] = flatten_lists(idx_test)
    eval_results['preds_test'] = preds.flatten().tolist()
    eval_results['targets_test'] = targets.flatten().tolist()
    eval_results['tooltips_test'] = flatten_lists(tooltips)
    eval_results['mae_test'] = mae(targets, preds)
    eval_results['rmse_test'] = rmse(targets, preds)
    eval_results['r2_test'] = r2_score(targets, preds)

    return eval_results


def load_exp_info(path_exp_file: str) -> dict:
    with open(path_exp_file, 'r') as f:
        return json.loads(f.read())


def load_model(model_info: Union[str, dict],
               path_model_file: str = None) -> Model:
    if isinstance(model_info, str):
        with open(model_info, 'r') as f:
            _model_info = json.loads(f.read())
    else:
        _model_info = model_info

    if _model_info['alg_id'] == ALG_MULTIMODAL:
        nets = [__config_model(info) for info in _model_info['nets']]
        model = MultimodalNet(nets=nets, dim_out=_model_info['dim_out']).init()
    else:
        model = __config_model(_model_info)

    if path_model_file is None:
        model.load(_model_info['path_model_file'])
    else:
        model.load(path_model_file)

    return model


def __config_model(model_info: dict) -> Model:
    if model_info['alg_src'] == SRC_SKLEARN:
        model = SKLearnModel(model_info['alg_id'], **model_info['hparams'])
    else:
        alg_id = model_info['alg_id']

        if alg_id == ALG_FCNN:
            layers = [FCLayer(c['dim_in'], c['dim_out'], c['batch_norm'], c['act_func'])
                      for c in model_info['layers']]
            model = FCNN(layers)
        elif alg_id == ALG_RESNET18:
            model = ResNet18(model_info['dim_out'])
        elif alg_id == ALG_RESNET34:
            model = ResNet34(model_info['dim_out'])
        elif alg_id == ALG_RESNET101:
            model = ResNet101(model_info['dim_out'])
        elif alg_id == ALG_DENSENET121:
            model = DenseNet121(model_info['dim_out'])
        elif alg_id in ALG_GNNS:
            aggr_layers = [GNNLayer(c['node_aggr_scheme'], c['dim_in_node'], c['dim_out'],
                                    c['dim_in_edge'], c['layer_norm'], c['act_func'])
                           for c in model_info['aggr_layers']]
            pred_layers = [FCLayer(c['dim_in'], c['dim_out'], c['batch_norm'], c['act_func'])
                           for c in model_info['pred_layers']]

            if alg_id == ALG_GCN:
                model = GCN(aggr_layers, pred_layers, readout_method=model_info['readout_method'])
            elif alg_id == ALG_GAT:
                model = GAT(aggr_layers, pred_layers, readout_method=model_info['readout_method'])
            elif alg_id == ALG_GIN:
                model = GIN(aggr_layers, pred_layers, readout_method=model_info['readout_method'])
            elif alg_id == ALG_ECCNN:
                model = ECCNN(aggr_layers, pred_layers, readout_method=model_info['readout_method'])
            elif alg_id == ALG_CGCNN:
                node_emb_layers = [FCLayer(c['dim_in'], c['dim_out'], c['batch_norm'], c['act_func'])
                                   for c in model_info['node_emb_layers']]
                model = CGCNN(node_emb_layers, aggr_layers, pred_layers, readout_method=model_info['readout_method'])
            elif alg_id == ALG_TFGNN:
                model = TFGNN(aggr_layers, pred_layers, readout_method=model_info['readout_method']).init()
            else:
                raise KeyError('Unknown algorithm identifier: \'{}\''.format(alg_id))
        else:
            raise KeyError('Unknown algorithm identifier: \'{}\''.format(alg_id))

        model.init()

    return model
