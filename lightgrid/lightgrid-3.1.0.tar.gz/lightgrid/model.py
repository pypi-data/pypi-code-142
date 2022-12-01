import time
import json
import warnings
import random as rd

def R2_score(y_pred, y_val):
    """
    Function to get R2-score
    :param y_pred: predict sequence
    :param y_val: real sequence
    :return: R2_score
    """
    total1 = 0
    for i in range(len(y_val)):
        total1 = total1 + y_val[i]
    total2 = 0
    total3 = 0
    for i in range(len(y_val)):
        total2 = total2 + (y_val[i] - total1/len(y_val)) ** 2
        total3 = total3 + (y_val[i] - y_pred[i]) ** 2
    r2 = 1 - total3/total2
    return r2

def succe_percent(y_pred, y_val):
    """
    Function to get success percent
    :param y_pred: predict sequence
    :param y_val: real sequence
    :return:  success percent
    """
    customCount = 0
    for i in range(len(y_pred)):
        if y_pred[i] == y_val[i]:
            customCount = customCount + 1
    denominator = len(y_pred)
    return (customCount / denominator)

def timer(func):
    """
    Annotation to get  function run time
    :return:  function run time
    """
    def count_time(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print('lightgrid run time:{:.5f}s'.format(end_time - start_time))
    return count_time

def ramdon_sample(seed,maxSize,scale):
    """
    Function to get random data index 
    :param seed: random seed
    :param maxSize: data max length
    :scale: train and test data spilt scale
    :return:  test data index ; train data index
    """
    rd.seed(seed)
    res1 = rd.sample(range(0,maxSize),int(maxSize*scale))
    res2 = [elem for elem in  range(0,maxSize) if elem not in res1]
    return res1,res2

def param_check(paramList):
    """
    Function to check "paramList" and "crossParamList"
    :param paramList: param to be checked
    :return:  check result
    """
    delKey = []
    for key in paramList.keys():
        if len(paramList[key]) == 0:
            delKey.append(key)
    for key in delKey:
        paramList.pop(key, None)
    return paramList

def param_autofull(className):
    """
    Function to auto fill param accord to model
    :param className: model name
    :return:"paramList" and "crossParamList"
    """
    className = str(className)
    if className == 'DecisionTreeClassifier':
        paramList = {
                     'criterion': ['gini','entropy'],
                     'splitter':['best','random'],
                    }
        crossParamList= {
                     'max_depth':[10,20,30,40,50,60,70,80,90,100],
                     'min_samples_split':[2,4,6,8,10,12,14,16,18,20],
                     'min_samples_leaf':[1,3,5,7,9,11,13,15,17,19],
                     }
        return paramList,crossParamList
    if className == 'KNeighborsClassifier':
        paramList = {
                     'n_neighbors':[1,2,3,4,5,6,7,8,9],
                     'algorithm':['auto', 'ball_tree', 'kd_tree','brute'],
                     'leaf_size':[10,20,30,40,50,60,70,80,90]
                     }
        crossParamList= {}
        return paramList,crossParamList
    if className == 'SVC':
        paramList = {
                     'C': [1e3, 5e3, 1e4, 5e4, 1e5],
                     'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1],
                     'kernel':['linear','poly','rbf'],
                     'shrinking':[True,False]
                    }
        crossParamList= {}
        return paramList,crossParamList
    if className == 'XGBClassifier':
        paramList = {
                     'subsample': [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],
                     'scale_pos_weight':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],
                    }
        crossParamList ={
                     'max_depth':[10,20,30,40,50,60,70,80,90,100],
                     'colsample_bytree':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],
                     'min_child_weight':[0,2,4,6,8,10,12,14,16,18,20],
                    }
        return paramList,crossParamList

    return {},{}

def param_split(className,param_grid):
    """
    Function to auto classify param to "paramList" and "crossParamList"
    :param className: model name
    :param param_grid: param to be classified
    :return:"paramList" and "crossParamList"
    """
    className = str(className)
    if className == 'DecisionTreeClassifier':
        paramList = {
                     'criterion': param_grid['criterion'] if 'criterion' in param_grid.keys() else [],
                     'splitter':param_grid['splitter'] if 'splitter' in param_grid.keys() else [],
                    }
        crossParamList= {
                     'max_depth':param_grid['max_depth'] if 'max_depth' in param_grid.keys() else [],
                     'min_samples_split':param_grid['min_samples_split'] if 'min_samples_split' in param_grid.keys() else [],
                     'min_samples_leaf':param_grid['min_samples_leaf'] if 'min_samples_leaf' in param_grid.keys() else [],
                     }
        return paramList,crossParamList
    if className == 'KNeighborsClassifier':
        paramList = {
                     'n_neighbors':param_grid['n_neighbors'] if 'n_neighbors' in param_grid.keys() else [],
                     'algorithm':param_grid['algorithm'] if 'algorithm' in param_grid.keys() else [],
                     'leaf_size':param_grid['leaf_size'] if 'leaf_size' in param_grid.keys() else []
                     }
        crossParamList= {}
        return paramList,crossParamList
    if className == 'SVC':
        paramList = {
                     'C': param_grid['C'] if 'C' in param_grid.keys() else [],
                     'shrinking':param_grid['shrinking'] if 'shrinking' in param_grid.keys() else []
                    }
        crossParamList= {
                     'gamma': param_grid['gamma'] if 'gamma' in param_grid.keys() else [],
                     'kernel':param_grid['kernel'] if 'kernel' in param_grid.keys() else [],
                    }
        return paramList,crossParamList
    if className == 'XGBClassifier':
        paramList = {
                     'subsample': param_grid['subsample'] if 'subsample' in param_grid.keys() else [],
                     'scale_pos_weight':param_grid['scale_pos_weight'] if 'scale_pos_weight' in param_grid.keys() else [],
                    } 
        crossParamList ={
                     'max_depth':param_grid['max_depth'] if 'max_depth' in param_grid.keys() else [],
                     'colsample_bytree':param_grid['colsample_bytree'] if 'colsample_bytree' in param_grid.keys() else [],
                     'min_child_weight':param_grid['min_child_weight'] if 'min_child_weight' in param_grid.keys() else [],
                    }
        return paramList,crossParamList

    return {},{}
    
def paramIterator(dictValues, resList, dictKeys, jude=True):
    """
    Procedure to get dictionary parameter collection
    :param dictValues: dcitionary values list(IN)
    :param dictKeys: dcitionary keys list (IN)
    :param jude: recursive termination condition(IN)
    :param resList:  dictionary parameter collection(OUT)
    """
    if jude: dictValues = [[[i] for i in dictValues[0]]] + dictValues[1:]
    if len(dictValues) > 2:
        for i in dictValues[0]:
            for j in dictValues[1]:
                paramIterator([[i + [j]]] + dictValues[2:], resList, dictKeys, False)
    elif len(dictValues) == 2:
        for i in dictValues[0]:
            for j in dictValues[1]:
                resList.append(dict(zip(dictKeys, i + [j])))


class lightgrid():

    def __init__(self,
                 function,
                 param_grid = {},
                 optimal_fun='succe_percent',
                 valid_times = 10,
                 random_seed = 10,
                 scale = 0.2,
                 silent=False,
                 save_model=False):
        
        """auto adjust parameter  . author YSW

        Parameters
        ----------
        :param function: you should input a class name such as : test
        :param param_grid: features assemble . type as dict ,such as {'a':[1,2,3]}
        :param optimal_fun: optimal function ,option invoke 'R2_score' or 'succe_percent'
        :param valid_times: valid times
        :param random_seed: random seed
        :param scale: train and test data spilt scale
        :param silent: boolean,Whether to output logs during program operation
        :param save_model: boolean,save model or not

        Examples
        --------
        >>> from sklearn.tree import DecisionTreeClassifier 
        >>> from sklearn.datasets import load_breast_cancer
        >>> import lightgrid
        >>> data = load_breast_cancer()
        >>> x_train = data['data']
        >>> y_train = data['target']
        >>> 
        >>> lightgrid = lightgrid.lightgrid(DecisionTreeClassifier)
        >>> lightgrid.fit(x_train, y_train)
        >>> lightgrid.bst_param
        ...                             
        ...
        {'max_depth': 10,'min_samples_split': 2,'min_samples_leaf': 3,'splitter': 'random'}
        """

        super(lightgrid, self).__init__()
        self.function = function
        self.param_grid = param_grid
        self.optimal_fun = optimal_fun
        self.valid_times = int(valid_times)
        self.random_seed = random_seed
        self.scale = scale
        self.silent = silent
        self.save_model = save_model
        
        self.paramList = {}
        self.crossParamList = {}
        self.bst_param = None
        

        if (optimal_fun != 'R2_score') and (optimal_fun != 'succe_percent'):
            raise ValueError('optimal_fun is not exist')     
        if valid_times < 1:
            raise ValueError('valid_times should be greater than 0. You entered' + str(valid_times))
        if scale <= 0 or scale >= 1 :
            raise ValueError('scale should be greater than 0 and less than 1. You entered' + str(scale))
        if (silent is not True) and (silent is not False):
            raise ValueError('silent should be a boolean value. You entered' + str(silent))
        if (save_model is not True) and (save_model is not False):
            raise ValueError('save_model should be a boolean value. You entered' + str(save_model))
            
    @timer
    def fit(self, data, target):
        print(self.function.__name__)
        bst_param = {}
        err_log = {}
        
        if len(list(self.param_grid)) == 0:
            # param auto full
            self.paramList,self.crossParamList = param_autofull(self.function.__name__)
        else:
            # param auto catagorize
            self.paramList,self.crossParamList = param_split(self.function.__name__,self.param_grid)
            
        # param final check
        self.paramList = param_check(self.paramList)
        self.crossParamList = param_check(self.crossParamList)
        
        # ordinal  search
        for key in self.paramList.keys():            
            sr_flag = 0
            param_flag = 0
            for value in self.paramList[key]:
                try:
                    param = {}
                    param[key] = value
                    model = self.function(**param)

                    sr = 0
                    for i in range(self.valid_times):
                        res1,res2 = ramdon_sample(self.random_seed+i,data.shape[0],self.scale)
                        x_train = data[res2,:]
                        y_train = target[res2]
                        x_val = data[res1,:]
                        y_val = target[res1]
                        model.fit(x_train, y_train)
                        y_pred = model.predict(x_val)
                        sr = sr + globals()[self.optimal_fun](y_pred, y_val)
                    sr = sr/self.valid_times

                    if not self.silent:
                        print('[lightgrid]  ordinal test key:' + str(key) + '  value:' + str(value) +
                              '  score:' + str(sr))
                    if sr > sr_flag:
                        sr_flag = sr
                        param_flag = value
                except Exception as e:
                    print('[lightgrid]  error come in where key=' + str(key) + ' and value =' + str(value) + ' ,exception : ' + str(e))
                    err_log['key:' + str(key) + ' value:' + str(value)] = 'exception:' + str(e)
                    continue
            bst_param[key] = param_flag

        # crossed  search
        if len(list(self.crossParamList.keys())) > 1:
            print(self.crossParamList.items())
            param_flag = {}
            resList = []
            paramIterator(list(self.crossParamList.values()), resList, list(self.crossParamList.keys()))
            
            print(resList)
            sr_flag = 0
            for i in range(len(resList)):
                try:
                    model = self.function(**resList[i])
                    sr = 0
                    for j in range(self.valid_times):
                        res1,res2 = ramdon_sample(self.random_seed+j,data.shape[0],self.scale)
                        x_train = data[res2,:]
                        y_train = target[res2]
                        x_val = data[res1,:]
                        y_val = target[res1]
                        model.fit(x_train, y_train)
                        y_pred = model.predict(x_val)
                        sr = sr + globals()[self.optimal_fun](y_pred, y_val)
                    sr = sr / self.valid_times

                    if not self.silent:
                        print('[lightgrid]  crossed test dict: ' + str(resList[i]) + '  score:' + str(sr))
                    if sr > sr_flag:
                        sr_flag = sr
                        param_flag = resList[i]
                except Exception as e:
                    print('[lightgrid]  error come in where dict= ' + str(resList[i]) + ' ,exception:' + str(e))
                    err_log['dict:' + str(resList[i])] = 'exception:' + str(e)
                    continue
        else:    
            sr_flag = 0
            param_flag = 0
            key = [key for key in self.crossParamList.keys()][0]
            for value in self.crossParamList[key]:
                try:
                    param = {}
                    param[key] = value
                    model = self.function(**param)

                    sr = 0
                    for i in range(self.valid_times):
                        res1,res2 = ramdon_sample(self.random_seed+i,data.shape[0],self.scale)
                        x_train = data[res2,:]
                        y_train = target[res2]
                        x_val = data[res1,:]
                        y_val = target[res1]
                        model.fit(x_train, y_train)
                        y_pred = model.predict(x_val)
                        sr = sr + globals()[self.optimal_fun](y_pred, y_val)
                    sr = sr/self.valid_times

                    if not self.silent:
                        print('[lightgrid]  ordinal test key:' + str(key) + '  value:' + str(value) +
                              '  score:' + str(sr))
                    if sr > sr_flag:
                        sr_flag = sr
                        param_flag = value
                except Exception as e:
                    print('[lightgrid]  error come in where key=' + str(key) + ' and value =' + str(value) + ' ,exception : ' + str(e))
                    err_log['key:' + str(key) + ' value:' + str(value)] = 'exception:' + str(e)
                    continue
            param_flag = {key: param_flag}
        
        bst_param = {**bst_param, **param_flag}
        self.bst_param = bst_param

        if err_log == {}:
            print('[lightgrid]  everything is OK')
            if self.save_model:
                tf = open("./lightgrid.json", "w")
                json.dump(self.bst_param, tf)
                tf.close()
                print('[lightgrid]  model saved success')
        else:
            tf = open("./errlog.json", "w")
            json.dump(err_log, tf)
            tf.close()
            warnings.warn('[lightgrid]  exception has occured , detail in errlog.json')
        return