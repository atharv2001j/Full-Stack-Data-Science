# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 20:22:50 2023

@author: Atharv Joshi 
"""

'''
Business Objective:
    
Maximize: The Flight distance

Minimize: The travelling cost

constraints: The data privacy and resources
'''
'''
Nominal Data Type:

ID#: Customer's identification number.

Continuous Data Type:

Balance: Customer's balance.
Qual_miles: Number of miles qualified by the customer.
Bonus_miles: Number of bonus miles earned by the customer.
Bonus_trans: Number of bonus transactions made by the customer.
Flight_miles_12mo: Number of flight miles in the last 12 months.
Flight_trans_12: Number of flight transactions in the last 12 months.
Days_since_enroll: Number of days since the customer enrolled.

Ordinal Data Type:

cc1_miles: Miles earned by the customer with credit card 1.
cc2_miles: Miles earned by the customer with credit card 2.
cc3_miles: Miles earned by the customer with credit card 3.
Award?: Whether the customer was awarded or not.



'''
#######################################################
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

df=pd.read_excel('EastWestAirLines.xlsx')
df

#EDA for the dataset

df.head()

df.shape
#the dataset contain totally 3999 rows and 12 columns

df.columns

a=df.describe()
#It is observe that the difference between mean and median is small 
# but there is scale difference in the standard deviation 

#Check the datatype of columns
df.dtypes
#we observed that the all the columns are of the integer type
# check the relation between the columns so we draw the heatmap

corr=df.corr()
sns.heatmap(corr)
# we observe that the heatmap having the same colour at diagonal so it
# indicate that the data is arranged in particular pattern and it is almost
# Normally distributted

# To understand the more about data we plot the pairplot

sns.pairplot(df)

#we observe that the most of the columns are corelate with each other
# we drae the histogram for all the columns for checking the normalzation

sns.histplot(df.Balance,kde=True)
#Data is right skew
sns.histplot(df.Qual_miles,kde=True)
#Data is normally distributed
sns.histplot(df.cc1_miles,kde=True)
#data is bi_model
#from above we conclude that there is skewness in data

sns.boxplot(df)
# There is an outlier present in the Balance and the Bonus_miles
#There is  a large scale in between mean and the Standard Deviation so we 
# normalize it

def norm_fun(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

#It normalize the all the columns and make values between 0 and 1
#apply above function to the dataframe
df_norm=norm_fun(df)

df_norm.columns
sns.histplot(df_norm.Balance,kde=True)
v=df_norm.describe()
# we see that the mean and median values are same so the data is norrmally
#distributed
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

