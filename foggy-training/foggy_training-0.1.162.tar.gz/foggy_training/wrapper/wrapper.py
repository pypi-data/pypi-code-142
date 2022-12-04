from sklearn.base import BaseEstimator, ClassifierMixin


class ClassificationWrapper(BaseEstimator, ClassifierMixin):

    def __init__(self, model_fun: callable, trainer_fun: callable):
        self.model_fun = model_fun
        self.trainer_fun = trainer_fun

    def fit(self, X, y, X_val=None, y_val=None, **kwargs):
        self.model_ = self.model_fun()
        self.trainer_ = self.trainer_fun()
        inputs = prepare_inputs(dataset, ['x'], 'y')
        train_dl = config.data.get_dataloader(inputs['train'], shuffle=True)
        val_dl = config.data.get_dataloader(inputs['test'], shuffle=False)




