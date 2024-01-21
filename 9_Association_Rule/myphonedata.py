# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 12:13:50 2023

@author: Atharv joshi
"""
'''
Business Objective:

Maximize: The customer Satisfaction

Minimize: The product return means the failure of the productt

Cobnstrains: Resources and availability of the devices 
'''

'''
Dataframe:

['red', 'white', 'green', 'yellow', 'orange', 'blue'] all the columns is of
nominal there is no ordinal data is present in the dataset
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('myphonedata.csv')
df

#################################
df.columns
'''
['red', 'white', 'green', 'yellow', 'orange', 'blue']
'''
##################################
df.head()
# It will show thw first five rows of the data
####################################
df.shape
# The dataset contain 11 rows and 6 columns
###################################
a=df.describe()
# The mean is near to zero and the mean and median diffrence is also not very
# big . The standard deviation is also near to zero
# so  we can say that the datapoints are scatter near the mradian
###################################
df.info()
'''
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   red     11 non-null     int64
 1   white   11 non-null     int64
 2   green   11 non-null     int64
 3   yellow  11 non-null     int64
 4   orange  11 non-null     int64
 5   blue    11 non-null     int64
dtypes: int64(6)
'''
###################################
df.dtypes
'''
red       int64
white     int64
green     int64
yellow    int64
orange    int64
blue      int64
dtype: object
'''
# The datatype of all columns is of numeric type so no need of encoding technique

######################################
# Find the missing values
df.isnull().sum()
'''
red       0
white     0
green     0
yellow    0
orange    0
blue      0
dtype: int64
'''
# There is no null  value in the daaset
######################################
# Visualize the dataset

#Plot the boxplot for the outlier analysis
sns.boxplot(df,x='red')
# No outlier 
sns.boxplot(df,x='white')
# No outlier
sns.boxplot(df,x='green')
# One outlier is present
sns.boxplot(df,x='yellow')
# One outlier present
sns.boxplot(df)
# There is three columns which contain the outliers 

# Plot a pairplot to understand the relationship between columns
sns.pairplot(df)
# The graphs does not show any relation as the datapoints are in scatter form

# To know more plot the heatmap
corr=df.corr()
sns.heatmap(corr)
# The heatmap showing some pattern of  the datapoins

############################################
#  As there is outliers present in the dataset so we normalize it using normalization technque


def norm_fun(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

df_norm=norm_fun(a)
df_norm
# The mean and median diffrence is in the range of 0-1 and the standard deviation
# is also near to zero


b=df_norm.describe()

sns.boxplot(df_norm)
# No Outlier is remaining
# The all the quantile points are converted in the rande of 0-1
###########################################

# Model Building
# Association Rules
from mlxtend.frequent_patterns import apriori,association_rules

data=pd.read_csv('myphonedata.csv')
data

# All the data is in properly separated form so no need to apply the encoding techique
# as it is already is in the form of numeric one

from collections import Counter
item_frequencies=Counter(data)

# Apriori algorithm
frequent_itemsets = apriori(data, min_support=0.05, use_colnames=True)

# Generate association rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)

# This generate association rule for columns
# comprises of antescends,consequences

rules.head(20)
rules.sort_values('lift',ascending=False).head(10)

# Visualize the rules
import networkx as nx
import matplotlib.pyplot as plt

# Create directed graph from the rules
G = nx.from_pandas_edgelist(rules, 'antecedents', 'consequents')

# Draw the graph
fig, ax = plt.subplots(figsize=(14, 8))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=2500, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", edge_color="gray", linewidths=1, alpha=0.7)
plt.title("Association Rules Network", fontsize=15)
plt.show()

###################################################
# By using this data we can suggest to the customer which colour he/she
# should select for the mobile 
