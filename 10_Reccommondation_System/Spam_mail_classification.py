# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 08:46:58 2023

@author: Atharv Joshi
"""

import pandas as pd
import numpy as np

df=pd.read_csv('spam.csv')
df.head()

#######################################
# Total  count of spam and ham
df.Category.value_counts()
'''
ham     4825
spam     747

'''
#######################################
# Create one column that separate the spam and ham in terms of 0 and 1
df['spam']=df['Category'].apply(lambda x: 1 if x=='spam' else 0)
df.shape
#(5572, 3)
#########################################
# Train test split
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(df.Message, df.spam,test_size=0.2)
# It will split the data into 80-20 pattern
# Let us check the shape of X_train and X_Test data

X_train.shape
X_test.shape
#########################################
# Let us check its type
type(X_train)
type(X_test)
#######################################
# Lets create BoW by using the CountVectorizer

from sklearn.feature_extraction.text import CountVectorizer
v=CountVectorizer()
x_train_cv=v.fit_transform(X_train.values)
x_train_cv
####################################
#afer creation of BoW let check its shape
x_train_cv.shape
#(4457, 7744)

####################################
# Train the naive base model
from sklearn.naive_bayes import MultinomialNB
# Initializee thw model
model=MultinomialNB()
#Train the model
model.fit(x_train_cv,y_train)
####################################
# Create BoW reresentation using Countvectorizer of X_test
x_test_cv=v.transform(X_test)
#########################################
# Evaluate Performane
from sklearn.metrics import classification_report
y_pred=model.predict(x_test_cv)
print(classification_report(y_test,y_pred ))
# Our model shwing accuracy of 99% so it is Overfit