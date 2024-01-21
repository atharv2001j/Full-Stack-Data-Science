# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 23:42:57 2023

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
########################################################################

#EDA 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_excel("Telco_customer_churn.xlsx")
df
#######################
#1.column
df.columns
#######################
#2.shape
df.shape  
#There are total 7043 rows and 30 columns in the dataframe


df.dtypes 
# The dataframe is of mixed datatype so we have to find the relationship
# between the columns so we draw the heatmap and pairplot for the understanding

df.isna()
# It does not contain any null value

corr=df.corr()
sns.heatmap(corr)
# The column noof refferrals,tenue of Months,Long distance charges
# ,Monthly gb dowmload,Total Refund ,Total extra data charges,long distance
# charges these columns are corelated

# plot the pairplot tounderstand more about the data
sns.pairplot(df)
#description of the dataframe 
df.describe()
# we can store the above description in the one varible
a=df.describe()
# there is slight difference in the mean and mesian of some columns and
# and standard deviation is also higher so it contain some outlier 
# plot the boxplot so we understand the outlier conaining coluumns
sns.boxplot(df)
# Total Extra Data Charges and Total Long Distance Charges columns contain 
# the outliers so we will remove or normalize it

df.columns
# we are checking which column is not necserray or
# the column which is  numerical data  that can be place in the datframe
df1=df.drop(['Customer ID','Count', 'Quarter', 'Referred a Friend', 'Offer', 'Phone Service',
       'Multiple Lines', 'Contract','Paperless Billing','Payment Method'],axis=1) 
df1.columns
df1.shape()

df_dummies=pd.get_dummies(df1)
df_dummies.columns

v=df_dummies.drop(['Device Protection Plan_No','Premium Tech Support_No','Online Security_No',
                 'Streaming TV_Yes','Streaming Movies_No','Streaming Music_Yes',
                 'Unlimited Data_No','Internet Service_No','Internet Type_None','Online Security_No'
                 ,'Online Backup_No'],axis=1)
#there are scale differenece between the column value so we 
#can remove that value from the Dataframe
# by using the normalization or standardization
#so we can use the normalization
def norm_fun(i):
    x=(i-i.min())/(i.max()-i.min())
    return x
#now we can apply this noramlization function to df2 dataframe for all the rows and column from 1 until end
# since 0 th column has Universcity name hence skipped
df2= norm_fun(v.iloc[:,:])   #here we can use the data make it as noramlize that is in the 0 and 1 form and we can 
# now we can descrine the df2 after we can make it in the normalize form
b=df2.describe()
#####################
#before you can applying the clustering you need to plot dendrogram first
# now to create the dendrogram , we need to measure distance
#we have import the linkage
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch
#linkage function gives us hierarchical or aglomerative clustering
#ref the help for linkage
p=linkage(df2,method="complete",metric="euclidean")
plt.figure(figsize=(16,8));
plt.title("Hierarchical Clustering Dendrogram");
plt.xlabel("phone");
plt.ylabel("internet_servise")
#ref help of dendogram
#sch.dendrogram
sch.dendrogram(p,leaf_rotation=0,leaf_font_size=10)
plt.show()

#######################
#dendrogram()
# now we can draw the dendgram
#applying  agglomertive clustering choosing 3 a clusters from dendrogram
#whatever has been dispalyed in dendrogram is not clustering
#it is just showing number of possible clusters
from sklearn.cluster import AgglomerativeClustering
dendo=AgglomerativeClustering(n_clusters=5,linkage='complete',affinity='euclidean').fit(df2)
#apply labels to the cluster
dendo.labels_
cluster_labels=pd.Series(dendo.labels_)
#assign this series to df2 dataframe as column and name the column as 'cluster'
df['clust1']=cluster_labels

########################################
df.shape
#we want to realocate th ecolumnn 7 to 0 th postion
df=df.iloc[:,[10,1,2,3,4,5,6,7,8,9]]
#now check the Univ1 Dataframe
df.iloc[:,2:].groupby(df.clust1).mean()
#from the output cluster 2 has got highest top10
#lowest accept ratio , best faculty ratio and highest expenses
#highest graduates ratio
#######################
df.to_csv("telco_customer.csv",encoding="utf-8")
import os
os.getcwd()

######################################################################



