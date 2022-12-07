import numpy as np
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

def root_mean_squared_error(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))


def print_metrics(y_train, y_pred_train, y_test, y_pred_test):
    print('Train RMSE value   : %.3f ' % root_mean_squared_error(y_train, y_pred_train))
    print('Train MSE value    : %.3f ' % mean_squared_error(y_train, y_pred_train))
    print('Train R2 value     : %.3f ' % r2_score(y_train, y_pred_train))
    print('Train MAE value    : %.3f ' % mean_absolute_error(y_train, y_pred_train))
    print('---------------------------')
    print('Test RMSE value    : %.3f ' % root_mean_squared_error(y_test, y_pred_test))
    print('Test MSE value     : %.3f ' % mean_squared_error(y_test, y_pred_test))
    print('Test R2 value      : %.3f ' % r2_score(y_test, y_pred_test))
    print('Test MAE value     : %.3f ' % mean_absolute_error(y_test, y_pred_test))