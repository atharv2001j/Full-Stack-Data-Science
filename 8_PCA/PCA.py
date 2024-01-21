# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 16:24:54 2023

@author: Atharv Joshi
"""

import pandas as pd
import numpy as np

uni1=pd.read_excel('University_Clustering.xlsx')
uni1

uni1.describe()

uni1.info()
uni=uni1.drop(['State'],axis=1)

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale

#Considering only numeric data

uni.data=uni.iloc[:,1:]

#Normalize the numeric data
uni_normal=scale(uni.data)
uni_normal

pca=PCA(n_components=6)
pca_values=pca.fit_transform(uni_normal)

#The amount of variance that each PCA explain

var=pca.explained_variance_ratio_
var

#Commulative Variance
var1=np.cumsum(np.round(var,decimals=4)*100)
var1

#Variance plot for PCA component obtained
plt.plot(var1,color='red')
#PCA Scores
pca_values

pca_data=pd.DataFrame(pca_values)
pca_data.columns='comp0','comp1','comp2','comp3','comp4','comp5'

final=pd.concat([uni.Univ,pca_data.iloc[:,0:3]],axis=1)

#Visualize the dataframe
ax=final.plot(x='comp0',y='comp1',kind='scatter',figsize=(12,8))
final[['comp0','comp1','Univ']].apply(lambda x:ax.text(*x),axis=1)
