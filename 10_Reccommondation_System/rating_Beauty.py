# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 19:32:36 2023

@author: Atharv Joshi
"""
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

beauty=pd.read_csv('ratings_Beauty.csv')
#Identify the shapes of the dataset
beauty.shape
beauty.columns
beauty.dtypes

# preparing for the handling the null values 
beauty['ProductId'] = beauty['ProductId'].fillna(0)

# Tfidfvectrizer
tfidf=TfidfVectorizer()
# TF-IDF Vectorization
tfidf_matrix = tfidf.fit_transform(beauty['ProductId'] + ' ' +str(beauty['Rating']))
# it has created sparse matrix that conatin the information in erms of zeros and ones

# Cosine similarity matrics
cosine_sim_matrix=linear_kernel(tfidf_matrix,tfidf_matrix)
# it will compared all the elemen of matrix 
# here in cosine similarity matrix there were no index provided 
# we will try tomap game name with the index 
# for that custom functionis written
# Mapping Game Names to Indices
# Mapping Title to Indices

beauty_index = pd.Series(beauty.index, index=beauty['ProductId']).drop_duplicates()

def get_entertain_recommendations(ProductId, topN):
    # Get the index of the given title
    beauty_id = beauty_index[ProductId]
    
    # Calculate cosine similarity scores so we will understang the similarity count
    cosine_scores = list(enumerate(cosine_sim_matrix[beauty_id]))
    
    # Sort the scores in descending order so the highest matched movies arranged at the top of 
    # the list to get the actual result
    cosine_scores = sorted(cosine_scores, key=lambda x: x[1], reverse=True)
    
    # Get the top N most similar items
    cosine_scores_N = cosine_scores[0:topN+1]
    
    # Extract indices and scores
    beauty_idx = [i[0] for i in cosine_scores_N]
    beauty_scores = [i[1] for i in cosine_scores_N]
    
    # Create a DataFrame to display recommendations
    beauty_similar_show = pd.DataFrame(columns=['ProductId', 'Rating','score'])
    beauty_similar_show['ProductId'] = beauty.loc[beauty_idx, 'ProductId']
    beauty_similar_show['Rating'] = beauty.loc[beauty_idx, 'Rating']
    beauty_similar_show['score'] = beauty_scores
    beauty_similar_show.reset_index(inplace=True)
    
    print(beauty_similar_show)
    
get_entertain_recommendations('733001998',10)

#############################################################################################
# This will help to reccommend the businesssman to customer which movieshould reccomend theta 
# the customer get satisfied with that and the eventually the revenue of the company
# is also going to increases
