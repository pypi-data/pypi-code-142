""" Main file to access the package aryzer """

import pandas as pd
import numpy as np

from aryzer import aryzer

if __name__ == '__main__':
    dtypes = {'#': np.int32, 'text': 'string', 'title': 'string', 'labels': 'string'}
    df = pd.read_csv('./data/221201_training_data.csv',
                     delimiter=',',
                     quotechar='"',
                     encoding='utf-8',
                     dtype=dtypes)
    str_series = pd.Series(df['labels'].values, dtype="string").str.split(',', expand=True)
    count_of_topics = str_series.apply(pd.Series.value_counts).sum(axis=1)
    print(count_of_topics.describe())
    aryzer.create_overview_of_categories(count_of_topics)
