# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 11:08:49 2020

@author: Q Mo
"""
# =============================================================================
# this part is still in development
# =============================================================================

import matplotlib.pyplot as plt
import sys
sys.path.append('../..')
from matgen_rester import MatgenError

DOS =['s','p','d','f']

def get_data_set():
  
  with open('../result','r') as f:
    dataset={}
    label = ''
    x_data = []
    y_data = []
    for line in f:
      data = line[0:-1].strip().split(' ')
      while '' in data:
        data.remove('')
      
      if data in DOS:
          dataset[label] = x_data,y_data
          label = data
          x_data = []
          y_data = []
      elif (len(data) == 1) and (data.contains('=')):
        continue
      print(data)
      if(len(data) != 2):
        raise MatgenError.MatgenError("file data error, can't get data")
      x_data.append(data[0])
      y_data.append(data[1])
    return dataset

def draw(data):      
  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.set(xlim=[0.5,4.5],ylim=[-2,80],title='an test axes',
         ylabel='Y-Axis',xlabel='X-Axis')
  
  plt.plot(data[0], data[1], color='lightblue', linewidth=3)
  plt.show()

if __name__=="__main__":
  print(get_data_set())