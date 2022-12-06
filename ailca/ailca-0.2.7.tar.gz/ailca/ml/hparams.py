import numpy
import optuna
from typing import Tuple
from itertools import product
from mealpy.utils.problem import Problem
from mealpy.evolutionary_based.GA import SingleGA
from ailca.ml.util import *
from ailca.data.base import Dataset
from ailca.data.util import get_data_loader


class HparamOptProblem(Problem):
    def __init__(self, model, dataset, param_space, **kwargs):
        if model is not None:
            self.model = model
            self.init_state_dict = deepcopy(self.model.state_dict()) if isinstance(self.model, PyTorchModel) else None
            self.dataset_train, self.dataset_val = dataset.split(ratio_train=0.8)
            self.param_space = param_space
            self.n_hparams = len(self.param_space)
            self.hparam_names = list()
            self.lb = list()
            self.ub = list()
            self.n_vals = list()

            for hparam in self.param_space.keys():
                self.hparam_names.append(hparam)
                self.lb.append(numpy.min(self.param_space[hparam]))
                self.ub.append(numpy.max(self.param_space[hparam]))
                self.n_vals.append(len(self.param_space[hparam]))

            super().__init__(self.lb, self.ub, minmax='min', **kwargs)

    def __to_categorical(self, sol):
        _sol = numpy.empty(sol.shape[0])

        for i in range(0, sol.shape[0]):
            vals = self.param_space[self.hparam_names[i]]
            _sol[i] = vals[numpy.argmin(numpy.abs(vals - sol[i]))]

        return _sol

    def run_model(self, hparams):
        if isinstance(self.model, SKLearnModel):
            _model = SKLearnModel(alg_id=self.model.alg_id, **hparams)
            _model.fit(self.dataset_train)
            preds = _model.predict(self.dataset_val)
        else:
            batch_size = hparams['batch_size'] if 'batch_size' in hparams.keys() else 64
            grad_name = hparams['gradient_method'] if 'gradient_method' in hparams.keys() else 'adam'
            init_lr = hparams['init_lr'] if 'init_lr' in hparams.keys() else 1e-3
            l2_reg = hparams['l2_reg'] if 'l2_reg' in hparams.keys() else 1e-6
            loss_name = hparams['loss_func'] if 'loss_func' in hparams.keys() else 'mae'

            self.model.load_state_dict(deepcopy(self.init_state_dict))
            loader_train = get_data_loader(self.dataset_train, batch_size=batch_size, shuffle=True)
            optimizer = get_optimizer(self.model, gradient_method=grad_name, init_lr=init_lr, l2_reg=l2_reg)
            loss_func = get_loss_func(loss_func=loss_name)

            for n in range(0, 100):
                _ = self.model.fit(loader_train, optimizer, loss_func)
            preds = self.model.predict(self.dataset_val)

        return mae(self.dataset_val.y, preds)

    def generate_position(self, lb=None, ub=None):
        pos = list()

        for i in range(0, self.n_hparams):
            rand_idx = numpy.random.randint(0, self.n_vals[i])
            pos.append(self.param_space[self.hparam_names[i]][rand_idx])

        return numpy.array(pos)

    def amend_position(self, position=None, lb=None, ub=None):
        return self.__to_categorical(numpy.clip(position, lb, ub))

    def fit_func(self, sol):
        _sol = self.__to_categorical(sol)
        opt_hparams = dict()

        for i in range(0, self.n_hparams):
            if isinstance(self.param_space[self.hparam_names[i]][0], int):
                opt_hparams[self.hparam_names[i]] = int(_sol[i])
            else:
                opt_hparams[self.hparam_names[i]] = float(_sol[i])

        return self.run_model(opt_hparams)


__problem = HparamOptProblem(None, None, None)


def __hparam_opt_grid():
    keys, vals = zip(*__problem.param_space.items())
    combs = [dict(zip(keys, p)) for p in product(*vals)]
    best_hparams = None
    best_score = -1e+8

    for hparams in combs:
        score = __problem.run_model(hparams)

        if score > best_score:
            best_hparams = hparams
            best_score = score

    return best_hparams, best_score


def __obj_bayes(trial):
    opt_hparams = dict()

    for hparam in __problem.param_space.keys():
        opt_hparams[hparam] = trial.suggest_categorical(hparam, __problem.param_space[hparam])

    return __problem.run_model(opt_hparams)


def __hparam_opt_bayes():
    skopt_kwargs = {
        'base_estimator': 'GP',
        'n_random_starts': 10,
        'acq_func': 'EI'
    }
    optuna.logging.set_verbosity(optuna.logging.ERROR)
    sampler = optuna.integration.SkoptSampler(skopt_kwargs=skopt_kwargs)
    study = optuna.create_study(direction='minimize', sampler=sampler)
    study.optimize(__obj_bayes, n_trials=10)

    return study.best_params, study.best_value


def __hparam_opt_ga():
    opt = SingleGA(epoch=10, pop_size=20)
    hp, best_score = opt.solve(problem=__problem)
    best_hparams = dict()

    for i in range(0, __problem.n_hparams):
        best_hparams[__problem.hparam_names[i]] = hp[i]

        if isinstance(__problem.param_space[__problem.hparam_names[i]][0], int):
            best_hparams[__problem.hparam_names[i]] = int(hp[i])

    return best_hparams, best_score


def optimize_hparams(model: Model,
                     dataset: Dataset,
                     param_space: dict,
                     opt_method: str = HPARAM_OPT_GRID) -> Tuple[dict, float]:
    """
    Optimize hyperparameters of the prediction model in a given parameter space ``param_space``.
    It returns the optimized hyperparameters and the prediction error of the prediction model with the optimized hyperparameters.
    This function supports the following three search methods: Grid Search, Bayesian Optimization, and Metaheuristics.

    :param model: (*Model*) Prediction model.
    :param dataset: (*Dataset*) Dataset for the hyperparameter optimization.
    :param param_space: (*dict*) Dictionary of the paris (hyperparamter, candidate values).
    :param opt_method: (*str*) Search method for the hyperparameter optimization (*default* = ``HPARAM_OPT_GRID``).
    :return: (*Tuple[dict, float]*) Optimized hyperparameters and prediction error on the optimized hyperparameters.
    """

    # Define a hyperparameter optimization problem.
    global __problem
    __problem = HparamOptProblem(model, dataset, param_space)

    # Optimize the hyperparameters in the parameter space.
    if opt_method == HPARAM_OPT_GRID:
        return __hparam_opt_grid()
    elif opt_method == HPARAM_OPT_BAYES:
        return __hparam_opt_bayes()
    elif opt_method == HPARAM_OPT_GA:
        return __hparam_opt_ga()
    else:
        raise KeyError('Unknown hyper-parameter optimization method \'{}\' was given.'.format(opt_method))
