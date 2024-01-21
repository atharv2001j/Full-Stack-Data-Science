# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 09:15:53 2023

@author: Atharv Joshi
"""
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

corpus=['At least seven pharma companies are working to develop vaccine against the corona',' virus that are already infected to the 14 billions people in the world','So india made a vaacine to fight against him']
bag_of_word_model=CountVectorizer()
print(bag_of_word_model.fit_transform(corpus).todense())
bag_of_word_df=pd.DataFrame(bag_of_word_model.fit_transform(corpus).todense())
bag_of_word_df.columns=sorted(bag_of_word_model.vocabulary_)
bag_of_word_df.head()
######################################################################
#  Create small bag of model 
bag_of_word_model=CountVectorizer(max_features=5)
bag_of_word_df=pd.DataFrame(bag_of_word_model.fit_transform(corpus).todense())
bag_of_word_df.columns=sorted(bag_of_word_model.vocabulary_)
bag_of_word_df.head()
'''
Out[16]: 
   14  against  are  the  to
0   0        1    1    1   1
1   1        0    1    2   1
2   0        1    0    0   1

it will consist only the first 5 features
'''
###########################################################
