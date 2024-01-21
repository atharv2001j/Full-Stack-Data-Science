# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 18:33:01 2023

@author: Lenovo
"""

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('boston_data.csv')
df
#######################################
plt.bar(df['age'],df['crim'])
plt.show()
######################################
df.rename({'crim':'CRIM','age':'AGE'},axis=1)
####################


df['age']
####################
df[['age','crim']]
#################
df.describe
####################
import numpy as np
arr1=np.array([1,2,34,45])
arr1.ndim
arr2=arr1.reshape(2,2)
arr2
arr3=np.power(arr2,3)
arr3
#####################
arr4=np.mod(arr1,arr1)
arr4
#####################
arr2=np.array([[1,2,3,4],[2,3,4,5]])
arr3=np.array([[3,4,5,6],[4,5,6,7]])
p=np.add(arr2,arr3)
p
######################
q=np.subtract(arr2,arr3)
q
############################
lst=[13,4,65,78,34,5]
for i,j in enumerate(lst,start=1):
    print(i,j)
######################
from itertools import combinations
for i in combinations(lst, 3):
    print(i)
#######################################




