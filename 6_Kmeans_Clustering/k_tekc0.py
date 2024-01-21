# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 19:37:37 2023

@author: Atharv Joshi
"""
'''
Nominal Data Type:

Customer ID: Customer's identification number.
Quarter: The quarter of the year.
Offer: The type of offer.
Internet Service: Type of internet service.
Internet Type: The type of internet connection.
Contract: The contract type.
Paperless Billing: Whether the customer prefers paperless billing.
Payment Method: The method of payment.

Continuous Data Type:

Count: Count of something (please provide context for a more precise categorization).
Number of Referrals: Number of referrals made by the customer.
Tenure in Months: Number of months the customer has been with the service.
Avg Monthly Long Distance Charges: Average monthly long-distance charges.
Avg Monthly GB Download: Average monthly gigabytes downloaded.
Monthly Charge: Monthly charge for the service.
Total Charges: Total charges incurred.
Total Refunds: Total refund amount.
Total Extra Data Charges: Total extra data charges.
Total Long Distance Charges: Total long-distance charges.
Total Revenue: Total revenue generated.

Ordinal Data Type:

Referred a Friend: Whether the customer referred a friend.
Phone Service: Type of phone service (e.g., yes, no).
Multiple Lines: Whether the customer has multiple phone lines.
Online Security: Whether the customer has online security.
Online Backup: Whether the customer has online backup.
Device Protection Plan: Whether the customer has a device protection plan.
Premium Tech Support: Whether the customer has premium tech support.
Streaming TV: Whether the customer has streaming TV.
Streaming Movies: Whether the customer has streaming movies.
Streaming Music: Whether the customer has streaming music.
Unlimited Data: Whether the customer has unlimited data.



'''
############################EDA##################################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_excel('Telco_customer_churn.xlsx')
df

###############################
df.shape
#he dataset contain total 7043 rows and 30 columns
###############################
df.columns
#The dataset contain mixed data columns i.e nominal and ordinal
###############################
df.head()

###############################
df['Internet Type'].value_counts()
'''
Fiber Optic    3035
DSL            1652
None           1526
Cable           830
Name: Internet Type, dtype: int64
'''
###############################
#Check if there is any missing values

a=df.isnull()
a.sum()
#There is no null value
###############################
#Check the datatypes of columns
df.dtypes
##############################
#Plot a pairplot to know the relation and behaviour of data
sns.pairplot(df)
# all datapoints are closely related to each other and some points we can divide
# ino the groups
###############################
# Plot a Boxplot to check the outlier present in the columns or not
sns.boxplot(df)
# There is an outlier present in the Total revenue and Total Long Distance

###############################
# Five number summary
a=df.describe()
# There is scale difference between the min and median and also the standard deviation
# for some columns is higher so it says that the datapoints are scatter from the 
# meadian
##############################
# Outlier Treatment
#we can calclaute the IQR

IQR=df['Total Revenue'].quantile(0.75)-df['Total Revenue'].quantile(0.25)

#have observation that the IQR in the variable explore
#no becaue the IQR are in the capaitalluze letter
#treated as constant
IQR

lower_limit=df['Total Revenue'].quantile(0.25)-1.5*IQR    #make the lower limit value as 0 not the negative
lower_limit         
upper_limit=df['Total Revenue'].quantile(0.75)+1.5*IQR 
upper_limit 

#Replacement Technique
df_replace=pd.DataFrame(np.where(df['Total Revenue']>upper_limit,upper_limit,np.where(df['Total Revenue']<lower_limit,lower_limit,df['Total Revenue'])))
df_replace

# if the value is lower than the lower limit ie is it has oulier
#so make it as the lower limit value  to that entry 
#if the value is greater than the upper limit ie is it has outlier
#so make it upper limit value to it 
#other wise make it as the same  for that columns
sns.boxplot(df_replace[0])
# same  for the second column
# Outlier Treatment
#we can calclaute the IQR

IQR=df['Total Long Distance Charges'].quantile(0.75)-df['Total Long Distance Charges'].quantile(0.25)

#have observation that the IQR in the variable explore
#no becaue the IQR are in the capaitalluze letter
#treated as constant
IQR

lower_limit=df['Total Long Distance Charges'].quantile(0.25)-1.5*IQR    #make the lower limit value as 0 not the negative
lower_limit         
upper_limit=df['Total Long Distance Charges'].quantile(0.75)+1.5*IQR 
upper_limit 

#Replacement Technique
df_replace=pd.DataFrame(np.where(df['Total Long Distance Charges']>upper_limit,upper_limit,np.where(df['Total Long Distance Charges']<lower_limit,lower_limit,df['Total Long Distance Charges'])))
df_replace

# if the value is lower than the lower limit ie is it has oulier
#so make it as the lower limit value  to that entry 
#if the value is greater than the upper limit ie is it has outlier
#so make it upper limit value to it 
#other wise make it as the same  for that columns
sns.boxplot(df_replace[0])

###################################
# # we are checking which column is not necserray or
# the column which is  numerical data  that can be place in the datframe
df1=df.drop(['Customer ID','Count', 'Quarter', 'Referred a Friend', 'Offer', 'Phone Service',
       'Multiple Lines', 'Contract','Paperless Billing','Payment Method'],axis=1) 
df1.columns
df1.dtypes
'''
Number of Referrals                    int64
Tenure in Months                       int64
Avg Monthly Long Distance Charges    float64
Internet Service                      object
Internet Type                         object
Avg Monthly GB Download                int64
Online Security                       object
Online Backup                         object
Device Protection Plan                object
Premium Tech Support                  object
Streaming TV                          object
Streaming Movies                      object
Streaming Music                       object
Unlimited Data                        object
Monthly Charge                       float64
Total Charges                        float64
Total Refunds                        float64
Total Extra Data Charges               int64
Total Long Distance Charges          float64
Total Revenue                        float64
dtype: object
'''
#The most of the datapoints having the datatype object and the data is of type nominal
# so we have to convert it into the numeric data
###################################
# Get Dummies
df_dummies=pd.get_dummies(df1)
df_dummies.columns

v=df_dummies.drop(['Device Protection Plan_No','Premium Tech Support_No','Online Security_No',
                 'Streaming TV_Yes','Streaming Movies_No','Streaming Music_Yes',
                 'Unlimited Data_No','Internet Service_No','Internet Type_None','Online Security_No'
                 ,'Online Backup_No'],axis=1)
#there are scale differenece between the column value so we 
#can remove that value from the Dataframe
###################################
# There is a scale difference the values so we normalize it using Normalization
def norm_fun(i):
    x=(i-i.min())/(i.max()-i.min())
    return x
#now we can apply this noramlization function to df2 dataframe for all the rows and column from 1 until end
# since 0 th column has Universcity name hence skipped
df2= norm_fun(v.iloc[:,:])   #here we can use the data make it as noramlize that is in the 0 and 1 form and we can 
# now we can descrine the df2 after we can make it in the normalize form
b=df2.describe()
#####################
# Model Building
# what will be the ideal clusetr 0,1,or 2
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

TWSS=[]
k=list(range(2,8))
for i in k:
    kmeans=KMeans(n_clusters=i)
    kmeans.fit(df2)
    
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

model=KMeans(n_clusters=2)
model.fit(df2)
model.labels_
mb=pd.Series(model.labels_)
type(mb)
df['clust']=mb
df.head()
df=df.iloc[:,[5,0,1,2,3,4]]
df
df.iloc[:,2:8].groupby(df.clust).mean()
df.to_csv('Kmeans_Telco.csv',encoding='utf-8')
import os
os.getcwd()

