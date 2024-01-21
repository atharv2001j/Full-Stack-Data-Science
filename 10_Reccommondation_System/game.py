# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 15:15:34 2023

@author: Atharv Joshi
"""

'''
Business Objecive:
    
Minimize: The unusefulness of the DVD's that are not sold on regular basis and also minimize 
the loss in arrangement technique '

Maximize: The retail sales of the DVD's and also the customer satisfaction '

Business Contraints:The regular updates  of the DVD's that are popular in current'

'''

'''
Data Dictionary

UserTd : ordinal data that contain the ID's of the customer

game: Nominal  Dat that contain the information about the game name

rating: Ordinal data that contain the information of the ratings for the gamea
'''

###########################################################################3
####################### EDA ################################################
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv('game.csv')
df

#################################
df.shape
# The dataset contain the 5000 rows and 3  columns
####################################
df.columns
# The Dataset conain the 3 columns i.e userId , game, rating
#################################
df.dtypes
'''
userId      int64
game       object
rating    float64
dtype: object

The dataset contain the two columns with the numeric data type and other with the object datatyoe

'''
###################################
df.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5000 entries, 0 to 4999
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   userId  5000 non-null   int64  
 1   game    5000 non-null   object 
 2   rating  5000 non-null   float64
dtypes: float64(1), int64(1), object(1)
memory usage: 117.3+ KB
'''
# The dataset not contain any Null value and also the dtypes are numeric + Object

######################################
# The Five Number Summary
df.describe()
'''
           userId       rating
count  5000.000000  5000.000000
mean   3432.282200     3.592500
std    1992.000866     0.994933
min       1.000000     0.500000
25%    1742.500000     3.000000
50%    3395.000000     4.000000
75%    5057.750000     4.000000
max    7120.000000     5.000000
'''
# The difference between the mean and median is not same that means the data is not normally distribued
# the standard deviation is also more as compare to the quartie 1 so the data is more deviated from thw
# median

######################################
# Outlier Analysis

# 1. Plot the boxplot to identify whether the dataset contain any oulier or not

sns.boxplot(df['userId'])
# The data is normally distributed as the data not contain the outlier and he central tendancy also it shows

sns.boxplot(df['rating'])
# it contain two outliers we can normalize the data

# 2. Plot the pairplot and heatmap to understand the relationship between the columns

sns.pairplot(df)
# The data is more scatter 

corr=df.corr()
sns.heatmap(corr)
# The heatmap contain the same color so it means the dataset follows some pattern
# to arrange the dataset
######################################
# As the game column is not numeric so we have to convert it into numeric
df_dummies=pd.get_dummies(df)
df_dummies.columns

v=df_dummies.describe()
# So Now we Normalize the data
def norm_fun(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

df2=norm_fun(v)
a=df2.describe()

# The mean and median difference is approx same and the standard deviaion is also near approximate zero so the
# is normally distributed and the all the comonents are converted in the range of
# 0-1
##################################################
################# Model Building #############################
# Now we build the reccommondation engine that suggest the top sellings the DVD's and
# and reccommond the game which the people like most

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load the game dataset
games = pd.read_csv('game.csv', encoding='utf-8')

# Check the structure of the dataset
print(games.shape)
print(games.columns)

# Preprocessing: Handling missing values in the 'game' column
games['game'] = games['game'].fillna('general')
#  It handles the missing data as with general keyword

# TF-IDF Vectorization
tfidf = TfidfVectorizer(stop_words='english')
# It is going to craete TfidfVectorizer to sepaarte all stop words
# it is going toseparate all words from row
tfidf_matrix = tfidf.fit_transform(games.game)
# it has created sparse matrix 


# Cosine Similarity Matrix
cosine_sim_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)
# it willcompared all the elemen of matrix 
# here in cosine similarity matrix there were no index provided 
# we will try tomap game name with the index 
# for that custom functionis written
# Mapping Game Names to Indices
game_index = pd.Series(games.index, index=games['game']).drop_duplicates()

def get_game_recommendations(game_name, topN):
    # Get the index of the given game name
    game_id = game_index[game_name]
    
    # Calculate cosine similarity scores
    cosine_scores = list(enumerate(cosine_sim_matrix[game_id]))
    
    # Sort the scores in descending order
    cosine_scores = sorted(cosine_scores, key=lambda x: x[1], reverse=True)
    
    # Get the top N most similar games
    cosine_scores_N = cosine_scores[0:topN+1]
    
    # Extract indices and scores
    game_idx = [i[0] for i in cosine_scores_N]
    game_scores = [i[1] for i in cosine_scores_N]
    
    # Create a DataFrame to display recommendations
    game_similar_show = pd.DataFrame(columns=['game', 'score'])
    game_similar_show['game'] = games.loc[game_idx, 'game']
    game_similar_show['score'] = game_scores
    game_similar_show.reset_index(inplace=True)
    
    print(game_similar_show)

# Enter the game and the number of games to be recommended
get_game_recommendations('Spider-Man: Web of Shadows', topN=10)

################################################################
#It will helpful for the business to reccommond the game depends on the
# popularity of the game
