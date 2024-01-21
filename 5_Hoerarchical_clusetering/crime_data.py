# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 22:16:32 2023

@author: Atharv Joshi
"""
'''
Business Objective:
    
Maximize: The accuracy

Minimize: The count of crime

Contraints: The Resource and data manupulation
'''

'''
Continuous Data Type:

Murder: The number of murder cases in a given location.
Assault: The number of assault cases in a given location.
Rape: The number of rape cases in a given location.

Ordinal Data Type:

UrbanPop: The level of urban population in a given location. This could be categorized as ordinal if it represents different levels of urbanization (e.g., small town, medium-sized city, large city).
'''
#######################################################
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('crime_data.csv')
df
#EDA
df.shape
#The DataFrame contain an 50 rows and 5 columns 
df.dtypes
#The datatype of all coloum is of type int and float
df.columns

df.describe()
#The mean and median are near approximatly same so we say that the data 
# is normally distributed

# for more detail we plot the heatmap for relation between the columns
corr=df.corr()
sns.heatmap(corr)
#The hetmap shows the diagonl colour are same and the data is arranged 
# in particular patern and data is normalized one

#For more deail understanding we plot the pairplot to understand the 
# relationship between the columns and data 

sns.pairplot(df)
# we observe that thhe columns shows the relationship among themselves and
# the datapoints are also scatter 

#There is scale diffrence in the range of column so we have to normalize it 
# so we create a normalize function

def norm_fun(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

df_norm=norm_fun(df.iloc[:,1:])
df_norm

# It will map the values in the range from 0 and 1

df_norm.describe()

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

#appying agglomerative clustering choose 1 as a cluster from dendogram

# In dedrogram is not show the clustering it only shows how many clusters are there

from sklearn.cluster import AgglomerativeClustering
h_complete=AgglomerativeClustering(n_clusters=2,linkage='complete',affinity='euclidean').fit(df_norm)

#apply labels to the cluster
h_complete.labels_
# so these all are in the form of array we have to convert the Series
cluster_labels=pd.Series(h_complete.labels_)

df['clust']=cluster_labels
df

#rearrange the all the columns 
df1=df.iloc[:,[5,1,2,3,4]]

