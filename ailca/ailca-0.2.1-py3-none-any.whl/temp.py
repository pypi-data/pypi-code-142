import numpy
from mealpy.evolutionary_based import GA


# def fit_func(y):
#     return numpy.sum(y**2)
#
# prob = {
#     'fit_func': fit_func,
#     'lb': [-1, -2, -3],
#     'ub': [100, 10, 1],
#     'minmax': 'min'
# }
# ga = GA.BaseGA(prob, epoch=100, pop_size=50)
# sol, score = ga.solve()
# print(sol)
# print(score)

from mealpy.utils.problem import Problem


class DOP(Problem):
    def __init__(self, hparams, dataset, **kwargs):
        self.hparams = hparams
        self.dataset = dataset
        self.n_hparams = len(self.hparams)
        self.hparam_names = list()
        self.lb = list()
        self.ub = list()
        self.n_vals = list()

        for hparam in self.hparams.keys():
            self.hparam_names.append(hparam)
            self.lb.append(numpy.min(self.hparams[hparam]))
            self.ub.append(numpy.max(self.hparams[hparam]))
            self.n_vals.append(len(self.hparams[hparam]))

        super().__init__(self.lb, self.ub, minmax='min', **kwargs)

    def __to_categorical(self, sol):
        _sol = numpy.empty(sol.shape[0])

        for i in range(0, sol.shape[0]):
            vals = self.hparams[self.hparam_names[i]]
            _sol[i] = vals[numpy.argmin(numpy.abs(vals - sol[i]))]

        return _sol

    def generate_position(self, lb=None, ub=None):
        pos = list()

        for i in range(0, self.n_hparams):
            rand_idx = numpy.random.randint(0, self.n_vals[i])
            pos.append(self.hparams[self.hparam_names[i]][rand_idx])

        return numpy.array(pos)

    def amend_position(self, position=None, lb=None, ub=None):
        return self.__to_categorical(numpy.clip(position, lb, ub))

    def fit_func(self, sol):
        _sol = self.__to_categorical(sol)

        return numpy.sum(sol**2)


hparams = {
    'n_estimators': [100, 200, 300, 400, 500, 600, 700],
    'max_depth': [3, 4, 5, 6, 7, 8, 9]
}
dop = DOP(hparams=hparams, dataset=None)
from mealpy.swarm_based import PSO
pso = PSO.OriginalPSO(epoch=100, pop_size=50)
b, s = pso.solve(problem=dop)
print(b)
print(s)
