# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:38:09 2023

@author: Atharv
"""

# 1 Write a Pandas program to replace the 'qualify' column 
# contains the values 'yes' and 'no' with True and False
import pandas as pd
import numpy as np
exam_data = {'name': ['Ram', 'Sham', 'Krishna', 'Ramkrishna', 'Shubhendu', 'Mahesh', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df=pd.DataFrame(exam_data,index=labels)
df
df['qualify'] = df['qualify'].replace({'yes': True, 'no': False})
df


#2. Q2Write a Python program to plot two or more lines  
# with different styles.

import matplotlib.pyplot as plt
plt.plot([1,5,6,4],linestyle='dotted')
plt.plot([3,4,5,6],linestyle='dashdot')
plt.show()

# Q.3 Create an array[1,2,3] write L1 and L2 norm value for it
import numpy as np
from numpy.linalg import norm
a=np.array([1,2,3])
l1=norm(a,1)
print(l1)
#vector L2 norm
l2=norm(a)
l2


#Q.4 Write a NumPy program create
# [[1, 0], [1, 2]] square array and  compute the determinant
#  of a given square array. 
import numpy.linalg as n

a=np.array([[1,0],[1,2]])
n.det(a)

# Q.5 Write a Python function to find the kth smallest 
# element in a list.

def k_smallest(lst,k):
    a=sorted(lst)
    return a[k-1]

lst=[3,4,5,67,11,6,7]
k=4
k_smallest(lst, k)
        
