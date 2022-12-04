from typing import Any, Callable
import torch
from torchswarm.swarmoptimizer import SwarmOptimizer


class Method:
    def __init__(self, model: Callable[[torch.Tensor], torch.Tensor], criterion: Any, verbose: bool, **kwargs: Any) -> None:
        self. criterion = criterion
        self.model = model
        pass

    def learn(self, X: torch.Tensor, Y: torch.Tensor) -> torch.Tensor:
        pass


class OrdinaryLeastSquares(Method):
    def __init__(self, model: Callable[[torch.Tensor], torch.Tensor], criterion: Any, verbose: bool = False, **kwargs: Any) -> None:
        super(OrdinaryLeastSquares, self).__init__(
            model, criterion, verbose, **kwargs)
        self.use_inbuilt_matmul = kwargs.get('use_inbuilt_matmul', False)

    def matmul(self, X: torch.Tensor, Y: torch.Tensor) -> torch.Tensor:
        Xr, Xc = X.shape
        Yr, Yc = Y.shape
        result = torch.zeros((Xr, Yc))
        assert Xc == Yr
        for i in range(Xr):
            result[i] = (X[i].unsqueeze(-1)*Y).sum(dim=0)
        return result

    def learn(self, X: torch.Tensor, Y: torch.Tensor) -> torch.Tensor:
        if self.use_inbuilt_matmul:
            print("Using in-built matrix multiplication")
            self.W = torch.inverse(X.t() @ X) @ X.t() @ Y
            return self.W.t()
        else:
            X_tX = self.matmul(X.t(), X)
            inv_X_tX = torch.inverse(X_tX)
            inv_X_tXX_t = self.matmul(inv_X_tX, X.t())

            self.W = self.matmul(inv_X_tXX_t, Y)
            return self.W.t()


class GradientDescent(Method):
    def __init__(self, model: Callable[[torch.Tensor], torch.Tensor], criterion: Any, epochs: int = 20_000, learning_rate: float = 0.001, verbose: bool = False) -> None:
        super(GradientDescent, self).__init__(model, criterion, verbose)
        self.epochs = epochs
        self.learning_rate = learning_rate
        self.verbose = verbose

    def learn(self, X: torch.Tensor, Y: torch.Tensor) -> torch.Tensor:
        self.features = X.shape[1]
        self.W = torch.randn(1, self.features, requires_grad=True)
        for i in range(self.epochs):
            Y_predicted = self.model(X, self.W)
            loss = self.criterion(Y, Y_predicted)
            loss.backward()
            with torch.no_grad():
                self.W -= self.W.grad * self.learning_rate
                # Set the gradients to zero
                self.W.grad.zero_()
            if self.verbose:
                print(f"Epoch {i}/{self.epochs}: Loss: {loss.item()}")
        return self.W


class ParticleSwarmOptimization(Method):
    def __init__(self, model: Callable[[torch.Tensor], torch.Tensor], criterion: Any, epochs: int = 1_00, swarm_size: int = 1_00, verbose: bool = False) -> None:
        super(ParticleSwarmOptimization, self).__init__(
            model, criterion, verbose)
        self.swarm_size = swarm_size
        self.epochs = epochs
        self.verbose = verbose

    def learn(self, X: torch.Tensor, Y: torch.Tensor) -> torch.Tensor:
        class Evaluation:
            def __init__(self, model: Callable[[torch.Tensor], torch.Tensor], criterion: Any) -> None:
                self.model = model
                self.criterion = criterion

            def evaluate(self, W: Any):
                Y_predicted = self.model(X, W.t())
                return self.criterion(Y_predicted, Y)

        self.features = X.shape[1]
        pso = SwarmOptimizer(self.features, self.swarm_size,
                             swarm_optimizer_type="rotated_exponentially_weighted", max_iterations=self.epochs)
        pso.optimize(Evaluation(self.model, self.criterion))

        self.W = pso.run(verbosity=self.verbose).gbest_position.t()
        return self.W
