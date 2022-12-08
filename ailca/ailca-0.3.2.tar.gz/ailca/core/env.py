"""
Environment Variables
---------------------
This base module contains the environments variables of AILCA for framework configurations of the objects and modules.
The environmental variables are used to configure and transfer the datasets and the machine learning models.
This module must not be modified.
"""


# Mathematics
DECIMAL_POINT = 3                                           # Decimal point for numerical values
N_HIST_BINS = 10                                            # The number of bins in target and error distributions


# Basic data types
DTYPE_FVEC = 'feature vector'                               # Numerical value
DTYPE_FORM = 'chemical formula'                             # Chemical formula
DTYPE_IMG = 'image data'                                    # Image data
DTYPE_MSTRUCT = 'molecular structure'                       # Molecular structure
DTYPE_CSTRUCT = 'crystal structure'                         # Crystal structure


# Representation method of chemical formula
REP_FORM_COMPACT = 'compact'                                # Compact representation
REP_FORM_CONTENT = 'content'                                # Content-Based representation


# Imputation methods for missing input features
IMPUTE_MEAN = 'impute_mean'                                 # Fill empty value by mean
IMPUTE_ZERO = 'impute_zero'                                 # Fill empty value by zero
IMPUTE_KNN = 'impute_knn'                                   # Fill empty value by k-nearest neighbor data.


# Source Library of Machine Learning Algorithms
LIB_SKLEARN = 'Scikit-Learn'                                # Scikit-Learn
LIB_PYTORCH = 'PyTorch'                                     # PyTorch


# Abbreviations of machine learning algorithms
ALG_LR = 'linear_reg'
ALG_LASSO = 'lasso'
ALG_DCTR = 'tree_reg'
ALG_SYMR = 'sym_reg'
ALG_KRR = 'ridge_reg'
ALG_KNNR = 'knn_reg'
ALG_SVR = 'svr'
ALG_GPR = 'gpr'
ALG_GBTR = 'gbtr'
ALG_FNN = 'fnn'
ALG_FCNN = 'fcnn'
ALG_ATE = 'autoencoder'
ALG_CNN = 'cnn'
ALG_RESNET18 = 'resnet_18'
ALG_RESNET34 = 'resnet_34'
ALG_RESNET101 = 'resnet_101'
ALG_DENSENET121 = 'densenet_121'
ALG_GCN = 'gcn'
ALG_GAT = 'gat'
ALG_GIN = 'gin'
ALG_ECCNN = 'eccnn'
ALG_CGCNN = 'cgcnn'
ALG_TFGNN = 'tfgnn'
ALG_MULTIMODAL = 'multimodal_nn'


ALG_CNNS = [
    ALG_RESNET18,
    ALG_RESNET34,
    ALG_RESNET101,
    ALG_DENSENET121
]

ALG_GNNS = [
    ALG_GCN,
    ALG_GAT,
    ALG_GIN,
    ALG_ECCNN,
    ALG_CGCNN,
    ALG_TFGNN
]

ALG_NAMES = {
    ALG_LR: 'Linear Regression',
    ALG_LASSO: 'Lasso',
    ALG_DCTR: 'Decision Tree Regression',
    ALG_SYMR: 'Symbolic Regression',
    ALG_KRR: 'Kernel Ridge Regression',
    ALG_KNNR: 'K-Nearest Neighbor Regression',
    ALG_SVR: 'Support Vector Regression',
    ALG_GPR: 'Gaussian Process Regression',
    ALG_GBTR: 'gbtr',
    ALG_FNN: 'Feedforward Neural Network',
    ALG_FCNN: 'Fully-Connected Neural Network',
    ALG_ATE: 'Autoencoder',
    ALG_CNN: 'Convolutional Neural Network',
    ALG_RESNET18: 'Residual Network 18',
    ALG_RESNET34: 'Residual Network 34',
    ALG_RESNET101: 'Residual Network 101',
    ALG_DENSENET121: 'Densely Connected Convolutional Network 121',
    ALG_GCN: 'Graph Convolutional Network',
    ALG_GAT: 'Graph Attention Network',
    ALG_GIN: 'Graph Isomorphism Network',
    ALG_ECCNN: 'Edge-Conditioned Convolutional Neural Network',
    ALG_CGCNN: 'Crystal Graph Convolutional Neural Network',
    ALG_TFGNN: 'Transformer Graph Neural Network',
    ALG_MULTIMODAL: 'Multimodal Network'
}

# Machine learning algorithms for each source library.
ALGS_SKLEARN = [
    ALG_LR,
    ALG_LASSO,
    ALG_DCTR,
    ALG_SYMR,
    ALG_KRR,
    ALG_KNNR,
    ALG_SVR,
    ALG_GPR,
    ALG_GBTR
]
ALGS_PYTORCH = [
    ALG_FNN,
    ALG_FCNN,
    ALG_ATE,
    ALG_CNN,
    ALG_RESNET18,
    ALG_RESNET34,
    ALG_RESNET101,
    ALG_DENSENET121,
    ALG_GCN,
    ALG_GAT,
    ALG_GIN,
    ALG_ECCNN,
    ALG_CGCNN,
    ALG_TFGNN,
    ALG_MULTIMODAL
]


# Source libraries of machine learning algorithms
SRC_SKLEARN = 'scikit_learn'
SRC_PYTORCH = 'pytorch'


# Gradient descent optimizers
GD_SGD = 'sgd'                                              # Stochastic gradient descent method
GD_ADADELTA = 'adadelta'                                    # AdaDelta optimizer
GD_RMSPROP = 'rmsprop'                                      # Root mean square propagation
GD_ADAM = 'adam'                                            # Adam optimizer


# Loss function
LOSS_MAE = 'mae'                                            # Mean absolute error
LOSS_MSE = 'mse'                                            # Mean squared error
LOSS_SMAE = 'smae'                                          # Smooth mean absolute error


# Activation function
ACT_FUNC_SIGMOID = 'sigmoid'                                # Sigmoid activation
ACT_FUNC_TANH = 'tanh'                                      # Hyperbolic tangent activation
ACT_FUNC_RELU = 'relu'                                      # Rectified linear unit activation
ACT_FUNC_SOFTPLUS = 'softplus'                              # Softplus activation
ACT_FUNC_PRELU = 'prelu'                                    # Parametric rectified linear unit activation


# Readout methods for graph neural networks
READOUT_MEAN = 'mean'                                       # Mean-based readout
READOUT_SUM = 'sum'                                         # Sum-based readout
READOUT_ATTN = 'attn'                                       # Attention-based readout


# Hyper-parameter optimization methods
HPARAM_OPT_GRID = 'grid'                                    # Grid search
HPARAM_OPT_BAYES = 'bayes'                                  # Bayesian optimization
HPARAM_OPT_GA = 'ga'                                        # Genetic algorithm
