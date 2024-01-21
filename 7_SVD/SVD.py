# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 15:22:54 2023

@author: Atharv Joshi
"""
import numpy as np
import pandas as pd
from scipy.linalg import svd
from numpy import array

A=array([[1,0,0,0,2],[0,0,3,0,0],[0,0,0,0,0],[0,4,0,0,0]])
print(A)

#SVD
U,d,Vt=svd(A)

print(U)
print(d)
print(Vt)

print(np.diag(d))

##############################################
#Try on Dataset
df=pd.read_excel('University_Clustering.xlsx')
df.head()

data=df.iloc[:,2:]
data

from sklearn.decomposition import TruncatedSVD
svd=TruncatedSVD(n_components=3)
svd.fit(data)

result=pd.DataFrame(svd.transform(data))
result.head()
result.columns="pc0",'pc1','pc2'
result.head()

#Scatter plot
import matplotlib.pyplot as plt
plt.scatter(x=result.pc0,y=result.pc1)
