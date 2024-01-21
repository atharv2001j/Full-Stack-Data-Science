# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 10:25:09 2023

@author: Atharv Joshi
"""
'''
Business Objective:

Maximize: The watching time of the movie and alsoo the ovaerall ratings of the movie

Minimize:The cost of the movie that are require for making and also the flopness of the movies

Contraints: The flow of the current trends and the comtent similarity with the other movies

'''
'''
Data Dictonary:

Id: This is ordinal data as the data arange in order

Titles: This is nominal data as the titles are not in order

Category: This contain the categorical data as the columns are divide into
various category i.e into the action,drama etc

Reviews: This column contain the ordinal data as the data are order according to the revews

'''

##########################################################################################
############################## EDA ##############################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv('entertainment.csv')
df

##########################
df.head

#########################
df.columns
'''
Index(['Id', 'Titles', 'Category', 'Reviews'], dtype='object')
'''
#########################
# Check the datatype of each column
df.dtypes
'''
Id            int64
Titles       object
Category     object
Reviews     float64
'''
# The dataset contain the column which of mixed datatype as the two colummns is o
# numeric type and other two is of the string type
##################################
df.info()
'''
#   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   Id        51 non-null     int64  
 1   Titles    51 non-null     object 
 2   Category  51 non-null     object 
 3   Reviews   51 non-null     float64
'''
# The info() function from this we will shown  the it is not contain any null value
# the datatypes are also shown 

#####################################
# Five number summary
df.describe()
'''
                Id    Reviews
count    51.000000  51.000000
mean   6351.196078  36.289608
std    2619.679263  49.035042
min    1110.000000  -9.420000
25%    5295.500000  -4.295000
50%    6778.000000   5.920000
75%    8223.500000  99.000000
max    9979.000000  99.000000
'''
# the diffrenece between mean and median is not same as they are show some variations tthat means the datais
# is not normalize and the standard deviation is also not small so the data points
# are more scatter from the mean and median
#########################################
# Outlier Analysis

#1.Plot the boxplot to check the outlier
sns.boxplot(df.Id)
# It does not contain any outlier as the data is normalize
sns.boxplot(df.Reviews)
# It does not contain any outlier and somewhat the skewness propery it will show

# For understanding the relation between the columns

sns.pairplot(df)
# The datapoints are more scatter that we have to normalize the data

corr=df.corr()
sns.heatmap(corr)
# The datapoints are co-related because the heatmap shows some dark colors andthe diagonal
# color is also light so the datapoints are arranges in particular pattern
##################################################################
# As the column is not numeric so we have to convert it into numeric
df_dummies=pd.get_dummies(df[['Category','Titles']])
df_dummies.columns

v=df_dummies.describe()
# So Now we Normalize the data
def norm_fun(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

df2=norm_fun(v)
a=df2.describe()

# The dataframe that summary are converted in the range 0-1

#################################################################

################# Model Building #############################
# Now we build the reccommondation engine that suggest the top sellings the DVD's and
# and reccommond the game which the people like most


import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

entertain = pd.read_csv('entertainment.csv', encoding='utf-8')

# Check the structure of the dataset
print(entertain.shape)
print(entertain.columns)

# Preprocessing: Handling missing values in the 'Category' column
#entertain['Category'] = entertain['Category'].fillna('general')

# TF-IDF Vectorization
tfidf = TfidfVectorizer(stop_words='english')
# It is going to craete TfidfVectorizer to sepaarte all stop words
# it is going toseparate all words from row
# Fill NaN values in 'Category' and 'Reviews' columns with empty strings
entertain['Category'] = entertain['Category'].fillna('')
entertain['Reviews'] = entertain['Reviews'].fillna('')

# TF-IDF Vectorization
tfidf_matrix = tfidf.fit_transform(entertain['Category'] + ' ' +str( entertain['Reviews']))
tfidf_matrix = tfidf.fit_transform(entertain['Category'] + ' ' + str(entertain['Reviews']))
# it has created sparse matrix 

# Cosine Similarity Matrix
cosine_sim_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)
# it will compared all the elemen of matrix 
# here in cosine similarity matrix there were no index provided 
# we will try tomap game name with the index 
# for that custom functionis written
# Mapping Game Names to Indices
# Mapping Title to Indices
entertain_index = pd.Series(entertain.index, index=entertain['Titles']).drop_duplicates()

def get_entertain_recommendations(title, topN):
    # Get the index of the given title
    entertain_id = entertain_index[title]
    
    # Calculate cosine similarity scores so we will understang the similarity count
    cosine_scores = list(enumerate(cosine_sim_matrix[entertain_id]))
    
    # Sort the scores in descending order so the highest matched movies arranged at the top of 
    # the list to get the actual result
    cosine_scores = sorted(cosine_scores, key=lambda x: x[1], reverse=True)
    
    # Get the top N most similar items
    cosine_scores_N = cosine_scores[0:topN+1]
    
    # Extract indices and scores
    entertain_idx = [i[0] for i in cosine_scores_N]
    entertain_scores = [i[1] for i in cosine_scores_N]
    
    # Create a DataFrame to display recommendations
    entertain_similar_show = pd.DataFrame(columns=['Titles', 'Category', 'Reviews', 'score'])
    entertain_similar_show['Titles'] = entertain.loc[entertain_idx, 'Titles']
    entertain_similar_show['Category'] = entertain.loc[entertain_idx, 'Category']
    entertain_similar_show['Reviews'] = entertain.loc[entertain_idx, 'Reviews']
    entertain_similar_show['score'] = entertain_scores
    entertain_similar_show.reset_index(inplace=True)
    
    print(entertain_similar_show)

# Enter the title and the number of items to be recommended
get_entertain_recommendations('Toy Story (1995)', topN=10)

################################################################################################
# This will helpful for the the customer or veiewer to findout the movies that are related to selected category
# and also for the producer to understand the pattern of the movie that the user like and which kind of the movie
# should we make so it will give more profit and overall revenue of the comapany get increases

