# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 20:05:23 2023

@author: Atharv Joshi
"""
'''
Business Objective:

Maximize: Audience engagement,profit of the movie

Minimize: Production time and production cost

ContraintsL: The business may face constraints related to market competition

'''
'''
DataFrame:
'Sixth Sense'
'Gladiator'
'LOTR1'
'Harry Potter1'
'Patriot'
'LOTR2'
'Harry Potter2'
'LOTR'
'Braveheart'
'Green Mile'

All the columns is of nominal there is no ordinal column in the dataset
'''
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv('my_movies.csv')
df

####################################
df.columns
'''
['Sixth Sense', 'Gladiator', 'LOTR1', 'Harry Potter1', 'Patriot',
       'LOTR2', 'Harry Potter2', 'LOTR', 'Braveheart', 'Green Mile']
'''
###################################
df.shape
# There is total 10 rows and 10 columns 
###################################
df.dtypes
'''
Sixth Sense      int64
Gladiator        int64
LOTR1            int64
Harry Potter1    int64
Patriot          int64
LOTR2            int64
Harry Potter2    int64
LOTR             int64
Braveheart       int64
Green Mile       int64
dtype: object
'''
# All the data in the dataset is of numeric type
####################################
df.info()
'''
#   Column         Non-Null Count  Dtype
---  ------         --------------  -----
 0   Sixth Sense    10 non-null     int64
 1   Gladiator      10 non-null     int64
 2   LOTR1          10 non-null     int64
 3   Harry Potter1  10 non-null     int64
 4   Patriot        10 non-null     int64
 5   LOTR2          10 non-null     int64
 6   Harry Potter2  10 non-null     int64
 7   LOTR           10 non-null     int64
 8   Braveheart     10 non-null     int64
 9   Green Mile     10 non-null     int64
dtypes: int64(10)
'''
# It will show all the information about the columns
#####################################
a=df.describe()
a
# The mean and median are nearly same but shows some variation in the data
# the standard deviation is not equal to zero means the datapoints is in scatter form
#################################
# Check for the null values
v=df.isnull()
v.sum()
'''
Sixth Sense      0
Gladiator        0
LOTR1            0
Harry Potter1    0
Patriot          0
LOTR2            0
Harry Potter2    0
LOTR             0
Braveheart       0
Green Mile       0
dtype: int64
'''
# There is no null value in the dataset
##################################
# Visualization of data
# Plot the boxplot for outlier analysis
sns.boxplot(df,x='Sixth Sense')
# No Outlier
sns.boxplot(df,x='Gladiator')
# No Outlier
sns.boxplot(df,x='LOTR1')
# having one outlier
sns.boxplot(df)
# There is some outlier in the data

# Plot  the pairplot to understand behaviour
sns.pairplot(df)
# The datapoints are in scatter form

corr=df.corr()
sns.heatmap(corr)
# The diagonal colour of the heatmap is same so it follow some patern to understand
# the pattern we will perform some oerations
########################################
#Normalization
#The data is numeric one so we have to perform normalization

def norm_fun(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

df_norm=norm_fun(a)
df_norm

b=df_norm.describe()

sns.boxplot(df_norm)
# No Outlier is remaining
# The all the quantile points are converted in the rande of 0-1
###########################################
# Model Building
# Association Rules
from mlxtend.frequent_patterns import apriori,association_rules

data=pd.read_csv('my_movies.csv')
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

# By using the association rule we will suggest the movies for the customer to 
# increase the viewers of the movies 
# Also by using this rules the revnue and the popularity of the movies
# will increases







