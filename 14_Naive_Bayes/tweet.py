# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 16:36:27 2024

@author: Atharv Joshi
"""
'''
Problem Statement :
    
In this case study, you have been given Twitter data collected from 
an anonymous twitter handle. With the help of a Naïve Bayes model, 
predict if a given tweet about a real disaster is real or fake.
1 = real tweet and 0 = fake tweet
'''

'''
Business Objective:
    
Maximize : The selection of positive tweets should be more

Minimize : The negative tweets be less

Business Contraints : The size and the tweeets pattern should be minimize

'''

'''
DataFrame:
    
All the columns except the target and id are non-numeric 

'''

############# EDA ###############################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('Disaster_tweets_NB.csv')
df.head

df.columns
'''
Index(['id', 'keyword', 'location', 'text', 'target'], dtype='object')
'''

##############################
df.dtypes
'''
id           int64
keyword     object
location    object
text        object
target       int64
dtype: object
'''
##############################
df.describe()
'''
                 id      target
count   7613.000000  7613.00000
mean    5441.934848     0.42966
std     3137.116090     0.49506
min        1.000000     0.00000
25%     2734.000000     0.00000
50%     5408.000000     0.00000
75%     8146.000000     1.00000
max    10873.000000     1.00000
'''
# the difference between mean and meadian is somewhat different so normalize it

# Also the standard deviation is also not appropriate means near to zero
# so the data are more scattered than the other

####################################
df.info()

'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 7613 entries, 0 to 7612
Data columns (total 5 columns):
 #   Column    Non-Null Count  Dtype 
---  ------    --------------  ----- 
 0   id        7613 non-null   int64 
 1   keyword   7552 non-null   object
 2   location  5080 non-null   object
 3   text      7613 non-null   object
 4   target    7613 non-null   int64 
dtypes: int64(2), object(3)
memory usage: 297.5+ KB
'''
# the dataframe does not contain any null value and there is no need to
# fill the dataframe

####################################
# Actual Implementation of the data 
# Before that we have to perform the the countvectorizor and the other
# method to convert the text data into the matrix and numeric form

import re

def cleaning_text(i):
    w=[]
    i=re.sub('[^A-Za-z'']+',' ',i).lower()
    for word in i.split(' '):
        if len(word)>3:
            w.append(word)
    return (' '.join(w))

########################################3
# apply above function to the DataFrame

df.text=df.text.apply(cleaning_text)
df=df.loc[df.text!='',:]

# Then split the training and testing data 
from sklearn.model_selection import train_test_split
X_train,X_test=train_test_split(df, test_size=0.2)
X_train
X_test
#####################################
# Creating matrix of token count for the entire dataset
def split_into_words(i):
    return[word for word in i.split(" ")]

from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer

tweet_bow=CountVectorizer(analyzer=split_into_words).fit(df.text)
all_tweet_matrix=tweet_bow.transform(df.text)
####################################
# Training Messages

train_tweet_matrix=tweet_bow.transform(X_train.text)
###########################
# Testing Messages
test_tweet_matrix=tweet_bow.transform(X_test.text)

tfidf_transformer=TfidfTransformer().fit(all_tweet_matrix)
# preparing for train emails
train_tfidf=tfidf_transformer.transform(train_tweet_matrix)

# preparing for the test emails
test_tfidf=tfidf_transformer.transform(test_tweet_matrix)
#Learning term weightaging and normalizing on entire emails

########################################
from sklearn.naive_bayes import MultinomialNB as MB
# Assuming 'target' is the column representing the binary labels (0 or 1)
y_train = X_train['target']

# Create a new Naive Bayes classifier
classifier_mb = MB()

# Fit the model using the transformed TF-IDF data and the 1-dimensional target variable
classifier_mb.fit(train_tfidf, y_train)

# Evaluate the model on the test data
test_pred_m = classifier_mb.predict(test_tfidf)
accuracy_test_m = np.mean(test_pred_m == X_test['target'])
print("Accuracy on the test data:", accuracy_test_m)
