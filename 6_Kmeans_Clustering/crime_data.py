# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 19:19:16 2023

@author: Atharv Joshi
"""
# Problem Statement :
'''
3.	Analyze the information given in the following 
‘Crime’ to create clusters of persons falling
 in the same type. Refer to crime_data.csv
'''
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
########################################################################
# EDA
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# we import the dataset excel file
df=pd.read_csv("crime_data.csv") 
df
#################################################################
#1.column
df.columns

#In this dataset there are 5 column and 
#all  column has the nominal data except Unnamed :0
#######################
#2.shape
df.shape    
# in the Insurance Dataset has 50 records and 5 column
#######################
# Now we count the number of the datapoint in the age clomun
df['Unnamed: 0'].value_counts()
'''
Alabama           1
Pennsylvania      1
Nevada            1
New Hampshire     1
New Jersey        1
New Mexico        1
New York          1
North Carolina    1
North Dakota      1
Ohio              1
Oklahoma          1
Oregon            1
Rhode Island      1
Alaska            1
South Carolina    1
South Dakota      1
Tennessee         1
Texas             1
Utah              1
Vermont           1
Virginia          1
Washington        1
West Virginia     1
Wisconsin         1
Nebraska          1
Montana           1
Missouri          1
Mississippi       1
Arizona           1
Arkansas          1
California        1
Colorado          1
Connecticut       1
Delaware          1
Florida           1
Georgia           1
Hawaii            1
Idaho             1
Illinois          1
Indiana           1
Iowa              1
Kansas            1
Kentucky          1
Louisiana         1
Maine             1
Maryland          1
Massachusetts     1
Michigan          1
Minnesota         1
Wyoming           1
Name: Unnamed: 0, dtype: int64
'''
##########################################
#Check the datatype of columns
df.dtypes
'''
Unnamed: 0     object
Murder        float64
Assault         int64
UrbanPop        int64
Rape          float64
dtype: object
'''
###########################################
# Find the missing values from the dataset
a=df.isnull()
a.sum()
#There is no null value in the dataset 
##########################################
# plot the scatter plot to understand the behaviour of the columns andrelation between them
df.plot(kind='scatter', x='Murder', y='Assault') ;
plt.show()


df.plot(kind='scatter', x='Murder', y='UrbanPop') ;
plt.show()
# the datapoints are more scatter than the above 
##########################################
#2-D  Scatter Plot
sns.set_style("whitegrid");
sns.FacetGrid(df, hue="Unnamed: 0", height=4) \
   .map(plt.scatter, "Murder", "Rape") \
   .add_legend();
plt.show();
# The count of murder after the rape is more below 25
###############################################
#To understand the relation between the columns we plot a pairplot
sns.pairplot(df)
# From the pairplot we clearly understand that the data is more sactter
# with the all columns 
################################################
# Outlier detection /Boxplot
sns.boxplot(df)
# It will shows that there is an outlier present for the column
#Rape
####################################################
# five Number Summary
v=df.describe()
# There is scale difference in mean and meadian and also the standarsd 
# deviation is also high
##################################################
# Outlier Treatment
#we can calclaute the IQR

IQR=df['Rape'].quantile(0.75)-df['Rape'].quantile(0.25)

#have observation that the IQR in the variable explore
#no becaue the IQR are in the capaitalluze letter
#treated as constant
IQR

lower_limit=df['Rape'].quantile(0.25)-1.5*IQR    #make the lower limit value as 0 not the negative
lower_limit         
upper_limit=df['Rape'].quantile(0.75)+1.5*IQR 
upper_limit 

#Replacement Technique
df_replace=pd.DataFrame(np.where(df['Rape']>upper_limit,upper_limit,np.where(df['Rape']<lower_limit,lower_limit,df['Rape'])))
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
d=pd.read_csv("crime_data.csv")
d.describe()
a=d.describe()

#intialize the scalar
scalar=StandardScaler()
df=scalar.fit_transform(d.iloc[:,1:])
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
d['clust']=mb
d.head()
d=d.iloc[:,[5,0,1,2,3,4]]
d
d.iloc[:,2:8].groupby(d.clust).mean()
d.to_csv('Kmeans_crime.csv',encoding='utf-8')
import os
os.getcwd()

