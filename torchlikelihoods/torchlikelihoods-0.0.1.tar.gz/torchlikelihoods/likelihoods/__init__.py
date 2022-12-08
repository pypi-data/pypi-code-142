from .beta import BetaLikelihood
from .bernoulli import BernoulliLikelihood
from .continous_bernoulli import ContinousBernoulliLikelihood
from .categorical import CategoricalLikelihood
from .normal import NormalLikelihood
from .normal_mean import NormalMeanLikelihood


likelihood_dict = {
    'beta': BetaLikelihood,
    'ber': BernoulliLikelihood,
    'cb': ContinousBernoulliLikelihood,
    'cat': CategoricalLikelihood,
    'normal': NormalLikelihood,
    'normal1': NormalMeanLikelihood.create(1),
    'normal01': NormalMeanLikelihood.create(0.01),
    'normal001': NormalMeanLikelihood.create(0.001),
    'normal0001': NormalMeanLikelihood.create(0.0001)
}