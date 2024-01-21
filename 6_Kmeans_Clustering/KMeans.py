# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 09:17:48 2023

@author: Atharv Joshi
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
#let us try to understand first how k means works for two
#dimensional data
#for that, generate random numbers in the range 0 and 1
#and write uniform probability of 1/50
X = np.random.uniform(0,1,50)
Y = np.random.uniform(0,1,50)
#create a empty dataframe with 0 rows and 2 columns
df_xy = pd.DataFrame(columns=["X","Y"])
df_xy.X=X
df_xy.Y=Y
df_xy.plot(x="X",y="Y",kind="scatter")
model1=KMeans(n_clusters=3).fit(df_xy)
'''
With data X and Y, apply Kmeans model,
generate scatter plot
with scale/font=10
'''
model1.labels_
df_xy.plot(x="X",y='Y',c=model1.labels_,kind='scatter',s=10,cmap=plt.cm.coolwarm)
Univ1 =pd.read_excel('University_Clustering.xlsx')
a=Univ1.describe()

# there is one columns State which is not affect onn the data so we dropi

Univ=Univ1.drop(["State"],axis=1)

# There is scale difference in columns so we normalize or standardized it
#Whenever there is mixed data we use normalizaion 

def norm_fun(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

#It normalize the all the columns and make values between 0 and 1
#apply above function to the dataframe
df_norm=norm_fun(Univ.iloc[:,1:])

# what will be the ideal clusetr 0,1,or 2

TWSS=[]
k=list(range(2,8))
for i in k:
    kmeans=KMeans(n_clusters=i)
    kmeans.fit(df_norm)
    
    TWSS.append(kmeans.inertia_)
    
    '''
    kmeans inertia also known as sum odf sqares methos
    .It measures all the datapoints from the centroid of the point.
    it differentiate between observed value and predicted value
    '''
    
TWSS
# Plot a elbow curve
plt.plot(k,TWSS,'ro-')
plt.xlabel('No of clusers')
plt.ylabel('Total within SS')

model=KMeans(n_clusters=3)
model.fit(df_norm)
model.labels_
mb=pd.Series(model.labels_)
Univ['clust']=mb
Univ.head()
Univ=Univ.iloc[:,[7,0,1,2,3,4,5,6]]
Univ
Univ.iloc[:,2:8].groupby(Univ.clust).mean()
Univ.to_csv('Kmeans_university.csv',encoding='utf-8')
import os
os.getcwd()

    
