# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 15:13:46 2023

@author: Atharv Joshi
"""
import pandas as pd
import matplotlib.pyplot as plt

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

# we can check the scale of the Univ dataframe which is between 0 and 1

b=df_norm.describe()
# we can observe that the min() value is 0 and that of max value is 1 after 
# Normalizaion

#For visualzing the cluster of  the above dataframe we  have to draw
# Dendodron first then we cluster the datapoints

from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch

# linkage function give the hierarchical and Agglomotive clustering
 

z=linkage(df_norm,method='complete',metric='euclidean')

plt.figure(figsize=(15,8))
plt.title('Hierarchical Clustering')
plt.xlabel('Index')
plt.ylabel('Disance')
#sch is help to draw 
sch.dendrogram(z,leaf_rotation=0,leaf_font_size=10)
plt.show()


#appying agglomerative clustering choose 3 as a cluster from dendogram

# In dedrogram is not show the clustering it only shows how many clusters are there

from sklearn.cluster import AgglomerativeClustering
h_complete=AgglomerativeClustering(n_clusters=3,linkage='complete',affinity='euclidean').fit(df_norm)

#apply labels to the cluster
h_complete.labels_
# so these all are in the form of array we have to convert the Series
cluster_labels=pd.Series(h_complete.labels_)

Univ['clust']=cluster_labels

#We want to realocate the column 7 to 0

Univ1=Univ.iloc[:,[7,1,2,3,4,5,6]]

Univ1.iloc[:,2:].groupby(Univ1.clust).mean()

# we convert it into csv
Univ1.to_csv('University.csv',encoding='utf-8')

import os
os.getcwd()

