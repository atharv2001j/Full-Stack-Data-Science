# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 17:11:13 2023

@author: Atharv Joshi
"""
"""
Business Objective:
    
Minimize : wastage of the items in the store

Maximaze : Sales  of the product items

Business constraints  : Resource availability for the customer
"""
'''
The Dataframe is of fully unstructured data
'''

from mlxtend.frequent_patterns import apriori,association_rules
# in this we are oing use transaction data where size of each row is not same
# we canot use the pandas to load the data because it is in string form

groceries=[]
with open('groceries.csv') as f:groceries=f.read()

# it will split data in the comma separater form

groceries=groceries.split('\n')
#Earlier it was in the format of sring it will convert it into the form of
# list
groceries_list=[]
for i in groceries:
    groceries_list.append(i.split(','))

# it will separate items from each list so further we can separe it for support caculation

all_groceries_list=[i for item in groceries_list for i in item]
# we will get all the transactions 
# we will get 43368 items in various transaction


#Now let us count the frequency of each item 

from collections import Counter
item_frequencies=Counter(all_groceries_list)

# item_frequencies will be contain key and dictionary 
# we want to sort it into count frequencies 
# means it will show he count of item purchased
# let us sort the frequencies in ascending order

item_frequencies=sorted(item_frequencies.items(),key=lambda x:x[1])
#when we execute this,items frequencies will be in sorted form 
# item name with count
#Support values will be sorted in descending order 
#Even EDA was also have the same trend, in EDA there was count 
#and here it is support value 
#we will generate  association rules, This association rule will calculate all the matrix of each and every combination 

items=list(reversed([i[0] for i in item_frequencies]))
# This is the list comprehenssion it will give the items from dictionaries 

frequencies=list(reversed([i[1] for i in item_frequencies]))

#This will  give he frequencies of each items

# we will plot the frequencies
import matplotlib.pyplot as plt
plt.bar(height=frequencies[0:11],x=list(range(0,11)))
plt.xticks(list(range(0,11),items[0:11]))
plt.xlabel('items')
plt.ylabel('count')
plt.show()

# Now we will convert it into dataframe
import pandas as pd
groceries_series=pd.DataFrame(pd.Series(groceries_list))
# Now we will get the the  dataframe of size 9836x1
# the last row of the dataframe is empty so we will remove it
groceries_series=groceries_series.iloc[:9836,:]

# So it will remove the last row
# groceries_series having column name 0 so rename as Transaction
groceries_series.columns=['Transactions']

# So there is various elements which is separeted by , = we will seperate using
# *
x=groceries_series['Transactions'].str.join(sep='*')

# Now we will apply one-hot encoding to convert it into numeric form

x=x.str.get_dummies(sep='*')

# This is the data which we are going to apply for the Apriori algorithm

frequency_items=apriori(x,min_support=0.0075,max_len=4,use_colnames=True)

# You will get support value for 1,2,3,4 max items
# let us sort the support values

frequency_items.sort_values('support',ascending=False,inplace=True)

# This will sort the support the value in descending order 
# in EDA also there was same trend there it was a count
# and here it was support value

rules=association_rules(frequency_items,metric='lift',min_threshold=1)
# This generate association rule of size 1198x9 columns
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

#########################################################3
# The objective behind forming this association rule is that using this rule
# the shopkeeper can arrange the items in the store in such a way that the
# the customer should purchase more items or associated items
# which will directly affect on the revenue of the shop
