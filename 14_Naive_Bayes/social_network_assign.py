# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 16:32:50 2024

@author: Atharv Joshi
"""
'''
Problem Statement: -
This dataset contains information of users in a social network.
 This social network has several business clients which can post
 ads on it. One of the clients has a car company which has just launched 
 a luxury SUV for a ridiculous price. Build a Bernoulli Naïve 
 Bayes model using this dataset and classify which of the users 
 of the social network are going to purchase this luxury SUV.
 1 implies that there was a purchase and 0 implies there wasn’t a purchase

'''

'''
Business Objective;

Maximize : The purchase of the Luxury SUV should be increase .So for that 
            the getting such a result we have to increase the social
            media user
            
Minimize : The negative reply to the product and the errors or difficulties
            that faces to increase the sells
            
Business Contraints: The data security and the maintainance of the user
                    requests and the complaints of the user
                    
'''
'''
DataFrame:
The all the columns except the Gender all are numeric and the specially from this
dataframe our target feature is Purchased column and for the accurate value of it
we are going to consider the Estimated Salary and age column
'''

###########################################################################
################ EDA #####################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('NB_Car_Ad.csv')
df.head()
########################################
df.columns
'''
Index(['User ID', 'Gender', 'Age', 'EstimatedSalary', 'Purchased'], dtype='object')
'''
#####################################
df.dtypes
'''
User ID             int64
Gender             object
Age                 int64
EstimatedSalary     int64
Purchased           int64
dtype: object
'''
###################################
df.describe()
'''
           User ID         Age  EstimatedSalary   Purchased
count  4.000000e+02  400.000000       400.000000  400.000000
mean   1.569154e+07   37.655000     69742.500000    0.357500
std    7.165832e+04   10.482877     34096.960282    0.479864
min    1.556669e+07   18.000000     15000.000000    0.000000
25%    1.562676e+07   29.750000     43000.000000    0.000000
50%    1.569434e+07   37.000000     70000.000000    0.000000
75%    1.575036e+07   46.000000     88000.000000    1.000000
max    1.581524e+07   60.000000    150000.000000    1.000000

'''
# There is slight  difference in the median and mean and also the
# the standard deviation is not near to zero so the datapoints aremore 
# scatter from the median and to normalize the datapoints we use the technique 
# of the StandardScalar or the normal function of Normalization

###################################################
df.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 400 entries, 0 to 399
Data columns (total 5 columns):
 #   Column           Non-Null Count  Dtype 
---  ------           --------------  ----- 
 0   User ID          400 non-null    int64 
 1   Gender           400 non-null    object
 2   Age              400 non-null    int64 
 3   EstimatedSalary  400 non-null    int64 
 4   Purchased        400 non-null    int64 
dtypes: int64(4), object(1)
memory usage: 15.8+ KB
''' 
# The above dataframe soes not contain the any Null Value
# So no need of the dataHandling

####################################################
# Now we can apply the NaiveBayes algorithm as our data is nearly good
# for the preprocessing

X=df[['Age','EstimatedSalary']]
y=df['Purchased']

# Now Divide our data nto training and testing data
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y, test_size=0.2)
X_train
X_test
y_train
y_test

##########################################################
# We have the age column and also the estimated salary columns so we have 
# to scale them  so for that we use feature scaling

# Feature Scaling  
from sklearn.preprocessing import StandardScaler  
sc = StandardScaler()  
X_train = sc.fit_transform(X_train)  
X_test = sc.transform(X_test)  
# Now we can apply our train data for model Building 
from sklearn.naive_bayes import GaussianNB  
classifier = GaussianNB()  
classifier.fit(X_train, y_train) 
########################################################
# Now we will predict our result
y_pred = classifier.predict(X_test) 
y_pred
################################################

# For the accuracy purpose we will check whether the predicted result is
# correct or not

from sklearn.metrics import confusion_matrix  
cm = confusion_matrix(y_test, y_pred)  
cm
'''
array([[49,  4],
       [10, 17]], dtype=int64)
'''
# As we can see in the above confusion matrix output, there are 7+3= 10 incorrect predictions, 
# and 65+25=90 correct predictions.

from sklearn.metrics import accuracy_score

# Assuming y_pred is the predicted values and y is the actual values
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy}")
# Accuracy: 0.825
################################

