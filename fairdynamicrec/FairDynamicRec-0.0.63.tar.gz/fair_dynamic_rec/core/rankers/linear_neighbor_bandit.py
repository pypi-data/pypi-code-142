import numpy as np
from .abstract_ranker import AbstractRanker

class NeighborUCB(AbstractRanker):
    def __init__(self, config, dataObj, parameters=None):
        super(NeighborUCB, self).__init__(config, dataObj)
        self.n_samples = np.zeros(dataObj.n_users)
        self.n_clicks = np.zeros(dataObj.n_users)
        self.prng = np.random.RandomState(seed=config.seed)
        self.sigma = float(parameters["sigma"]["value"]) if "sigma" in parameters else 1.0

        self.l = int(parameters["latent_dim"]["value"]) if "latent_dim" in parameters else 0
        self.lambda_1 = float(parameters["lambda1"]["value"]) if "lambda1" in parameters else 1.0
        self.lambda_2 = float(parameters["labmda2"]["value"]) if "lambda2" in parameters else 1.0
        self.alpha_a = float(parameters["alpha_a"]["value"]) if "alpha_a" in parameters else 1.0
        self.alpha_u = float(parameters["alpha_u"]["value"]) if "alpha_u" in parameters else 1.0

        self.V = np.zeros((self.dataObj.n_items, self.l))
        self.k = 0
        self.contextual_var = bool(
            parameters["contextual_variable"]["value"]) if "contextual_variable" in parameters else False
        if self.contextual_var:
            self.X = self.dataObj.feature_data['train_item_topical_features']
            self.k = self.X.shape[1]
            self.XV = np.concatenate((self.X, self.V), axis=1)
            self.XV_optimal = np.concatenate((self.X, self.dataObj.feature_data['test_item_latent_features']), axis=1)
        else:
            self.XV = self.V
            self.XV_optimal = self.dataObj.feature_data['test_item_latent_features']
        self.Theta = np.zeros((self.dataObj.n_users, self.k + self.l))
        self.Theta_x = self.Theta[:, :self.k]
        self.Theta_v = self.Theta[:, self.k:]
        self.W = np.identity(n=self.dataObj.n_users)

        self.A = np.zeros(
            (self.dataObj.n_users, (self.k + self.l) * self.dataObj.n_users, (self.k + self.l) * self.dataObj.n_users))
        # self.A = np.zeros((self.dataObj.n_users, self.lambda_1 * np.identity(n=(self.k+self.l)*self.dataObj.n_users)))
        self.AInv = np.zeros(
            (self.dataObj.n_users, (self.k + self.l) * self.dataObj.n_users, (self.k + self.l) * self.dataObj.n_users))
        # self.AInv = np.zeros((self.dataObj.n_users, self.lambda_1 * np.identity(n=(self.k + self.l) * self.dataObj.n_users)))
        identity = self.lambda_1 * np.identity(n=(self.k + self.l) * self.dataObj.n_users)
        for i in range(self.A.shape[0]):
            self.A[i] = identity
            self.AInv[i] = np.linalg.inv(self.A[i])  # np.zeros((self.k+self.l,self.k+self.l))
        self.b = np.zeros((self.dataObj.n_users, (self.k + self.l) * self.dataObj.n_users))

        self.C = np.zeros((self.dataObj.n_items, self.l, self.l))
        self.CInv = np.zeros((self.dataObj.n_items, self.l, self.l))
        for i in range(self.C.shape[0]):
            self.C[i] = self.lambda_2 * np.identity(n=self.l)
            self.CInv[i] = np.linalg.inv(self.C[i])  # np.zeros((self.k+self.l,self.k+self.l))
        self.d = np.zeros((self.dataObj.n_items, self.l))

        self.ill_matrix_counter = 0
        # for ill inverse
        self.AInv_tmp = np.zeros(
            (self.dataObj.n_users, (self.k + self.l) * self.dataObj.n_users, (self.k + self.l) * self.dataObj.n_users))
        self.b_tmp = np.zeros((self.dataObj.n_users, (self.k + self.l) * self.dataObj.n_users))
        self.CInv_tmp = np.zeros((self.dataObj.n_items, self.l, self.l))
        self.d_tmp = np.zeros((self.dataObj.n_items, self.l))