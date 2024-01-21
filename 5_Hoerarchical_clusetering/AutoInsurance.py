# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 16:38:43 2023

@author: Atharv Joshi
"""
'''
Business Objective:

Minimize: The customer queries and the concepts

Maximize: Annual  revenue

Contraints: data Privacy
'''

'''
Customer: nominal
State: nominal
Response: nominal
Coverage: nominal
Education: Nominal
EmploymentStatus: Nominal
Gender: Nominal
Location Code: Nominal
Marital Status: Nominal
Policy Type: Nominal
policy:Nominal
Renew Offer Type: Nominal
Sales Channel: nominal
Vehicle Class: Nominal
Vehicle Size: Nominal
Effective To Date: Nominal
Income: Continuous
Monthly Premium Auto: Continuous
Months Since Last Claim: Continuous
Months Since Policy Inception: Continuous
Number of Open Complaints: Continuous
Number of Policies: Continuous
Total Claim Amount: Continuous
'''
###################################################
# EDA
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# we import the dataset excel file
df=pd.read_csv("AutoInsurance.csv") 
df
########################
df.columns
#######################
df.shape
#The dataset contain 9134 rows and 24 columns
######################
df.State.value_counts()
'''
California    3150
Oregon        2601
Arizona       1703
Nevada         882
Washington     798
Name: State, dtype: int64
'''
#####################
df.dtypes
#The dataset contain mixed types of data i.e nominal and ordinal 
#####################
#Check if there is null value or not
a=df.isnull()
a.sum()
#####################
# plot a scatter plot of numeric data 
df.plot(kind='scatter', x='Number of Policies', y='Total Claim Amount') ;
plt.show()
# maximum customer taken 1,2 or 5 number of policies 
df.plot(kind='scatter', x='Income', y='Total Claim Amount') ;
plt.show()
#The customer having income more than 10000 have taken the AutoInsurance
########################
#2-D  Scatter Plot

sns.set_style("whitegrid");
sns.FacetGrid(df, hue="Income", height=4) \
   .map(plt.scatter, "Monthly Premium Auto", "Total Claim Amount") \
   .add_legend();
plt.show();

# From this we observed that the data points are closed to each other
# and show some relation with one another

#############################
#To understand the relation between the columns we plot a pairplot
sns.pairplot(df)
#The data  is not properly arranged and data is scatter
#############################
#Finding an Outlier
sns.boxenplot(df)
#There is an outlier for the column Income and Customer Lifetime value

###########################
#Five Number Summary 
a=df.describe()
# For some columns there is a scale difference in mean and median and also
# the standard deviation is also high for the some columns
############################
# Outlier Treatment
#we can calclaute the IQR

IQR=df['Income'].quantile(0.75)-df['Income'].quantile(0.25)

#have observation that the IQR in the variable explore
#no becaue the IQR are in the capaitalluze letter
#treated as constant
IQR

lower_limit=df['Income'].quantile(0.25)-1.5*IQR    #make the lower limit value as 0 not the negative
lower_limit         
upper_limit=df['Income'].quantile(0.75)+1.5*IQR 
upper_limit 
#Replacement Technique
df_replace=pd.DataFrame(np.where(df['Income']>upper_limit,upper_limit,np.where(df['Income']<lower_limit,lower_limit,df['Income'])))
df_replace

# if the value is lower than the lower limit ie is it has oulier
#so make it as the lower limit value  to that entry 
#if the value is greater than the upper limit ie is it has outlier
#so make it upper limit value to it 
#other wise make it as the same  for that columns
sns.boxplot(df_replace[0])


#For the Customer Lifetime value
IQR=df['Customer Lifetime Value'].quantile(0.75)-df['Customer Lifetime Value'].quantile(0.25)

#have observation that the IQR in the variable explore
#no becaue the IQR are in the capaitalluze letter
#treated as constant
IQR

lower_limit=df['Customer Lifetime Value'].quantile(0.25)-1.5*IQR    #make the lower limit value as 0 not the negative
lower_limit         
upper_limit=df['Customer Lifetime Value'].quantile(0.75)+1.5*IQR 
upper_limit 
#Replacement Technique
df_replace=pd.DataFrame(np.where(df['Customer Lifetime Value']>upper_limit,upper_limit,np.where(df['Customer Lifetime Value']<lower_limit,lower_limit,df['Customer Lifetime Value'])))
df_replace

# if the value is lower than the lower limit ie is it has oulier
#so make it as the lower limit value  to that entry 
#if the value is greater than the upper limit ie is it has outlier
#so make it upper limit value to it 
#other wise make it as the same  for that columns
sns.boxplot(df_replace[0])
df_new=pd.get_dummies(df)
df_new.columns
v=df_new.drop(df_new.loc[:,'Customer_AA10041':],axis=1)
# There is scale difference in columns so we normalize or standardized it
#Whenever there is mixed data we use normalizaion 

def norm_fun(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

#It normalize the all the columns and make values between 0 and 1
#apply above function to the dataframe
df_norm=norm_fun(v)

df_norm

# we can check the scale of the df dataframe which is between 0 and 1

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