#!/usr/bin/env python
# coding: utf-8

# In[11]:


import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score

def plot_roc_curve(test_y, prob,n=2):
    if(n>2):
        fpr = dict()
        tpr = dict()
        thr = dict()
        roc_auc = dict()
        for i in range(n):
            fpr[i], tpr[i], thr[i] = roc_curve(test_y[:,i], prob[:,i])
        plt.figure(figsize=(30, 15))
        a=1
        for idx, i in enumerate(range(n)):     
            plt.subplot(2,2,idx+1)
            plt.plot(fpr[i], tpr[i],color='red', label='ROC ')
            plt.plot([0, 1], [0, 1], color='green', linestyle='--')
            plt.xlabel('False Positive Rate')
            plt.ylabel('True Positive Rate')
            plt.title('Class %0.0f : Roc auc score: %f'%(idx,roc_auc_score(test_y[:,i], prob[:,i])))
            plt.legend()
        plt.show()

    else:
        
        fpr, tpr, thr = roc_curve(test_y, prob)
        plt.plot(fpr, tpr, color='red', label='ROC')
        plt.plot([0, 1], [0, 1], color='green', linestyle='--')
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('Roc auc score: %f'%(roc_auc_score(test_y, prob)))
        plt.legend()
        plt.show()


def plot_feature_importance(model, X, y = None,top_n=10):
        ft_importance_values = model.feature_importances_

        # 정렬과 시각화를 쉽게 하기 위해 series 전환
        ft_series = pd.Series(ft_importance_values, index = X.columns)
        ft_top=ft_series.sort_values(ascending=False)[:top_n]
        # 시각화
        plt.figure(figsize=(8,6))
        plt.title('Feature Importance Top 20')
        sns.barplot(x=ft_top, y=ft_top.index)
        plt.show()




