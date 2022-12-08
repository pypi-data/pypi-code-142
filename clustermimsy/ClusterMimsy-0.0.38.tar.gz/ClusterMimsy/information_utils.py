import pandas as pd
from itertools import combinations
from sklearn.metrics import mutual_info_score
import matplotlib.pyplot as plt
import numpy as np

def get_mutual_information_data_frame_from_data_frame(dataframe):

  # Create the dataframe to be returned
  mutual_information_dataframe = pd.DataFrame(index = dataframe.columns,
                                       columns = dataframe.columns)
  

  # Fill diagonal (entropy of each column)
  for column in dataframe.columns:
    column_entropy = mutual_info_score(dataframe[column], dataframe[column])
    mutual_information_dataframe[column][column] = column_entropy
  
  # Fill off-diagonals (mutual information)
  all_column_combinations = list(combinations(dataframe.columns,2))
  for column_combination in all_column_combinations:
    column_1, column_2 = column_combination
    _mi = mutual_info_score(dataframe[column_1], dataframe[column_2])
    mutual_information_dataframe[column_1][column_2] = _mi
    mutual_information_dataframe[column_2][column_1] = _mi
  
  return mutual_information_dataframe


plot_mutual_information_default_kwargs = {
    'ha': "center",
    'va': "center",
    'color': "black"
    
}

def plot_mutual_information(mutual_information_dataframe,
                            annotate = True,
                            cmap='Oranges',
                            annotation_kwargs = plot_mutual_information_default_kwargs):
  fig, ax = plt.subplots()
  im = ax.imshow(mutual_information_dataframe.astype('float'), cmap=cmap)
  ax.set_xticks(np.arange(len(mutual_information_dataframe.columns)))
  ax.set_yticks(np.arange(len(mutual_information_dataframe.columns)))
  ax.set_xticklabels(mutual_information_dataframe.columns)
  ax.set_yticklabels(mutual_information_dataframe.columns)

  # Rotate the tick labels and set their alignment.
  plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
          rotation_mode="anchor")

  if annotate:
    for i in range(len(mutual_information_dataframe.columns)):
        for j in range(len(mutual_information_dataframe.columns)):
          ax.text(i,j, round(mutual_information_dataframe.iloc[i,j],2), **annotation_kwargs)
          