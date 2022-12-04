from typing import Any, Callable, Literal
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import numpy as np
import torch
from .method import OrdinaryLeastSquares, GradientDescent, ParticleSwarmOptimization

Method = Literal['ols', 'gd', 'pso']


class Regression:
    """The Regression Interface
    Defines the necessary methods to implement additional regression models.
    """

    def __init__(self, loss: Any, method: Method, **kwargs: Any) -> None:
        """Initialization

        Args:
            loss (torch.nn.Loss): A loss defined in pyTorch.
            method (Method): Method could be OLS, GD or PSO.
        """
        pass

    @property
    def coeff_(self):
        """Return the coefficients of the regression model
        """
        pass

    @property
    def intercept_(self):
        """Return the intercept of the regression model
        """
        pass

    def get_method(self, model: Callable[[torch.Tensor], torch.Tensor], loss: Any, method: Literal['ols', 'gd', 'pso'], **kwargs: Any):
        params = {'ols': kwargs.get('ols', {}),
                  'gd': kwargs.get('gd', {}),
                  'pso': kwargs.get('pso', {})}

        self.__method_factory = {
            'ols': OrdinaryLeastSquares,
            'gd': GradientDescent,
            'pso': ParticleSwarmOptimization
        }
        return self.__method_factory[method](model, loss, **params[method])

    def fit(self, X: np.ndarray, Y: np.ndarray) -> None:
        """Fit the X and Y to the model.

        Args:
            X (np.ndarray): Training instances.
            Y (np.ndarray): Training labels.
        """
        pass

    def predict(self, X: np.ndarray) -> torch.Tensor:
        """Predict given a test set.

        Args:
            X (np.ndarray): Test instances.

        Returns:
            torch.Tensor: Predicted values.
        """
        pass

    def rmse(self, Y_true: torch.Tensor, Y_predicted: torch.Tensor) -> float:
        """The RMSE metric between ground truth and predicted values.

        Args:
            Y_true (torch.Tensor): Ground truth
            Y_predicted (torch.Tensor): Predicted values

        Returns:
            float: RMSE value
        """
        mse = mean_squared_error(
            Y_true.detach().numpy(), Y_predicted.detach().numpy())
        return np.sqrt(mse)

    def r2_score(self, Y_true: torch.Tensor, Y_predicted: torch.Tensor) -> float:
        """R2 Score of the model.

        Args:
            Y_true (torch.Tensor): Ground truth
            Y_predicted (torch.Tensor): Predicted values

        Returns:
            float: R2 Score value
        """
        return r2_score(Y_true.detach().numpy(), Y_predicted.detach().numpy())

    def mae(self, Y_true: torch.Tensor, Y_predicted: torch.Tensor) -> float:
        """The MAE metric between ground truth and predicted values.

        Args:
            Y_true (torch.Tensor): Ground truth
            Y_predicted (torch.Tensor): Predicted values

        Returns:
            float: MAE value
        """
        return mean_absolute_error(Y_true.detach().numpy(), Y_predicted.detach().numpy())


class LinearRegression(Regression):
    def __init__(self, loss: Any, method: Method, **kwargs: Any) -> None:
        super(LinearRegression, self).__init__(loss, method, **kwargs)
        self.method = self.get_method(self.model, loss, method, **kwargs)

    @property
    def coeff_(self):
        return torch.flatten(self.W)[1:].tolist()

    @property
    def intercept_(self):
        return torch.flatten(self.W)[:1].tolist()

    def model(self, X: torch.Tensor, W: torch.Tensor):
        return X @ W.t().double()

    def fit(self, X: np.ndarray, Y: np.ndarray) -> None:
        ones = torch.ones(X.shape[0], 1)
        X = torch.cat((ones, torch.tensor(X)), 1)
        Y = torch.tensor(Y)
        self.W = self.method.learn(X, Y)

    def predict(self, X: np.ndarray) -> torch.Tensor:
        ones = torch.ones(X.shape[0], 1)
        X = torch.cat((ones, torch.tensor(X)), 1)
        return self.model(X, self.W)
