# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 19:19:16 2023

@author: Atharv Joshi
"""
# Problem Statement :
'''
3.	Analyze the information given in the following 
‘Insurance Policy dataset’ to create clusters of persons falling
 in the same type. Refer to Insurance Dataset.csv
'''
''' This is column present in the Insurance Dataset.csv

premiums paid- It is monthly paid amount
age- age of insurance holder
Day to renew-remaining days to renew the insurance
claimed made-money return to insurance holder
Income-Income of the holder
'''
########################################################################
# EDA
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# we import the dataset excel file
df=pd.read_csv("Insurance Dataset.csv") 
df
#################################################################
#1.column
df.columns

#In this dataset there are 5 column and 
#all  column has the nominal data
#######################
#2.shape
df.shape    
# in the Insurance Dataset has 100 records and 5 column
#######################
# Now we count the number of the datapoint in the age clomun
df['Age'].value_counts()
'''
Out[18]: 
45    8
44    7
34    6
32    5
56    5
42    4
49    4
48    4
26    3
50    3
41    3
27    3
23    3
53    3
70    3
67    3
46    3
35    3
30    3
28    3
69    3
63    2
58    2
59    2
62    2
52    2
82    2
54    2
36    2
77    1
39    1
Name: Age, dtype: int64
'''
##########################################
#Check the datatype of columns
df.dtypes
'''
Premiums Paid      int64
Age                int64
Days to Renew      int64
Claims made      float64
Income             int64
dtype: object
'''
###########################################
# Find the missing values from the dataset
a=df.isnull()
a.sum()
#There is no null value in the dataset 
##########################################
# plot the scatter plot to understand the behaviour of the columns andrelation between them
df.plot(kind='scatter', x='Age', y='Claims made') ;
plt.show()
# from the scatter plot we observe that the insurance claime age group
# ranges from the 25 to 55

df.plot(kind='scatter', x='Income', y='Age') ;
plt.show()
# the age groupbelow 60 is most of the earning group
##########################################
#2-D  Scatter Plot
sns.set_style("whitegrid");
sns.FacetGrid(df, hue="Age", height=4) \
   .map(plt.scatter, "Premiums Paid", "Claims made") \
   .add_legend();
plt.show();
#This will clesrly give us the age group and the insurance claime

sns.set_style("whitegrid");
sns.FacetGrid(df, hue="Age", height=4) \
   .map(plt.scatter, "Premiums Paid", "Income") \
   .add_legend();
plt.show();
###############################################
#To understand the relation between the columns we plot a pairplot
sns.pairplot(df)
# From the pairplot we clearly understand that the data is more sactter
# with the all columns except the Claime made
################################################
# Outlier detection /Boxplot
sns.boxplot(df)
# It will shows that there is an outlier present for the column
# Premiumns paid and Caime made
####################################################
# five Number Summary
v=df.describe()
# There is scale difference in mean and meadian and also the standarsd 
# deviation is also high
##################################################
# Outlier Treatment
#we can calclaute the IQR

IQR=df['Premiums Paid'].quantile(0.75)-df['Premiums Paid'].quantile(0.25)

#have observation that the IQR in the variable explore
#no becaue the IQR are in the capaitalluze letter
#treated as constant
IQR

lower_limit=df['Premiums Paid'].quantile(0.25)-1.5*IQR    #make the lower limit value as 0 not the negative
lower_limit         
upper_limit=df['Premiums Paid'].quantile(0.75)+1.5*IQR 
upper_limit 

#Replacement Technique
df_replace=pd.DataFrame(np.where(df['Premiums Paid']>upper_limit,upper_limit,np.where(df['Premiums Paid']<lower_limit,lower_limit,df['Premiums Paid'])))
df_replace

# if the value is lower than the lower limit ie is it has oulier
#so make it as the lower limit value  to that entry 
#if the value is greater than the upper limit ie is it has outlier
#so make it upper limit value to it 
#other wise make it as the same  for that columns
sns.boxplot(df_replace[0])

#####################################################
# Standardization 
# the data is numeric so we will perform the standardization technique
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
d=pd.read_csv("Insurance Dataset.csv")
d.describe()
a=d.describe()

#intialize the scalar
scalar=StandardScaler()
df=scalar.fit_transform(d)
dataset=pd.DataFrame(df)
res=dataset.describe()

#####################################################
# Model Building
# what will be the ideal clusetr 0,1,or 2
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

TWSS=[]
k=list(range(2,8))
for i in k:
    kmeans=KMeans(n_clusters=i)
    kmeans.fit(dataset)
    
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
model.fit(dataset)
model.labels_
mb=pd.Series(model.labels_)
type(mb)
df['clust']=mb
df.head()
df=df.iloc[:,[5,0,1,2,3,4]]
df
df.iloc[:,2:8].groupby(df.clust).mean()
df.to_csv('Kmeans_Insurance.csv',encoding='utf-8')
import os
os.getcwd()

