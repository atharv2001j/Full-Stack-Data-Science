# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 11:37:07 2024

@author: Atharv Joshi
"""
'''
Business objective :

Maximize : he primary business objective is likely to maximize the accuracy 
of the predictive model. Achieving a high accuracy means that the model can 
effectively classify individuals as having or not having diabetes based on 
the given features.

Minimize : While maximizing accuracy is crucial, there might be business
 constraints related to minimizing false positives (predicting diabetes whe
 it's not present) and false negatives (not predicting diabetes when it is 
 present). Depending on the business context, these errors might have 
 different costs or implications.
 
 Business Contraints :  Compliance with relevant regulations and standards, 
 especially in healthcare, is a critical constraint.
 
'''

'''
DataFrame:

All the Columns except the Class variable are numeric datatype so the target 
varible are class_variable and other are the training purpose variables
'''

import pandas as pd
df=pd.read_csv('Diabetes.csv')
df.head()

df.columns
'''
Index([' Number of times pregnant', ' Plasma glucose concentration',
       ' Diastolic blood pressure', ' Triceps skin fold thickness',
       ' 2-Hour serum insulin', ' Body mass index',
       ' Diabetes pedigree function', ' Age (years)', ' Class variable'],
      dtype='object')
'''

########################################
df.dtypes
'''
Number of times pregnant          int64
 Plasma glucose concentration      int64
 Diastolic blood pressure          int64
 Triceps skin fold thickness       int64
 2-Hour serum insulin              int64
 Body mass index                 float64
 Diabetes pedigree function      float64
 Age (years)                       int64
 Class variable                   object
dtype: object
'''

###########################################
df.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 768 entries, 0 to 767
Data columns (total 9 columns):
 #   Column                         Non-Null Count  Dtype  
---  ------                         --------------  -----  
 0    Number of times pregnant      768 non-null    int64  
 1    Plasma glucose concentration  768 non-null    int64  
 2    Diastolic blood pressure      768 non-null    int64  
 3    Triceps skin fold thickness   768 non-null    int64  
 4    2-Hour serum insulin          768 non-null    int64  
 5    Body mass index               768 non-null    float64
 6    Diabetes pedigree function    768 non-null    float64
 7    Age (years)                   768 non-null    int64  
 8    Class variable                768 non-null    object 
dtypes: float64(2), int64(6), object(1)
memory usage: 54.1+ KB
'''
# The Dataset does not contain any null value nd except class variable 
# all the datatype of variable are of numeric type
# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Assuming your data is stored in a DataFrame named 'diabetes_data'
# You may load your data using pd.read_csv() or any other appropriate method

# Display the first few rows of the dataframe to understand the structure
print(df.head())

# Separate features (X) and target variable (y)
X = df[[' Number of times pregnant', ' Plasma glucose concentration',
       ' Diastolic blood pressure', ' Triceps skin fold thickness',
       ' 2-Hour serum insulin', ' Body mass index',
       ' Diabetes pedigree function', ' Age (years)']]
y = df[' Class variable']

# Divide the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


from sklearn.ensemble import RandomForestClassifier
model= RandomForestClassifier(n_estimators=20)

# Train the model on the training set
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# Print the evaluation metrics
print(f"Accuracy: {accuracy}")
print(f"Confusion Matrix:\n{conf_matrix}")
print(f"Classification Report:\n{class_report}")

