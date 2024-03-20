# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 09:23:13 2024

@author: Atharv Joshi
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn import metrics
import warnings
warnings.filterwarnings('ignore')

load_data=pd.read_csv('income.csv')
load_data.columns
load_data.head()

# Split the data in to input and output
X=load_data.iloc[:,0:6]
y=load_data.iloc[:,6]

# Split the dataset
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

# Create Adaboost Clssifier
ada_model=AdaBoostClassifier(n_estimators=100,learning_rate=1)
# N_estimator is no of weak learners

# Train the model
model=ada_model.fit(x_train,y_train)
# Predict the result
y_pred=model.predict(x_test)
print('accuracy',metrics.accuracy_score(y_test, y_pred))


# let us try this for another model
from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()

Ada_model=AdaBoostClassifier(n_estimators=50,base_estimator=lr,learning_rate=1)
model=ada_model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print('accuracy',metrics.accuracy_score(y_test, y_pred))
