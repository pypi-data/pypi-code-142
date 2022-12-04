import numpy as np
import pandas as pd

#pandas读取Excel文件,分析工作消费存款省份学历的关系
income = pd.read_excel('./income.xlsx')
print(income)
print('-'*50)

#标准差:能反映一个数据集的离散程度


#标准化数据：离差标准化，标准差标准化，小数定标标准化数据

#离差标准化
def MinMaxScale(data):
    data = (data-data.min())/(data.max()-data.min())
    return data

#对工资和消费做离差标准化
#按照工资和消费进行横轴axis=1拼接
data_M = pd.concat([MinMaxScale(income['工资']),MinMaxScale(income['消费'])],axis=1)
print(data_M.head(5)) #查看前5行的数据
print('-'*50)

#标准差标准化:能够排除掉因省份学历等的不同造成的工资和消费不同
def StandarScaler(data):
    data = (data-data.mean())/data.std()#数据减去均值除以标准差
    return data

#对工资和消费做标准差标准化
data_S = pd.concat([StandarScaler(income['工资']),StandarScaler(income['消费'])],axis=1)
print(data_S.head(5)) #查看前5行的数据
print('-'*50)

#小数定标标准化数据
#data.abs().max()表示绝对值的最大值； np.ceil()向正无穷取整
def DecimalScaler(data):
    j = np.ceil(np.log10(data.abs().max()))
    data = data/(10**j)
    return data

#对工资和消费做标准差标准化
data_D = pd.concat([DecimalScaler(income['工资']),DecimalScaler(income['消费'])],axis=1)
print(data_D.head()) #查看前5行的数据

