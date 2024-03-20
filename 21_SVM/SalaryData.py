# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 18:18:36 2024

@author: Atharv Joshi
"""
'''
Problem Statement :
    A construction firm wants to develop a suburban locality with new 
    infrastructure but they might incur losses if they cannot sell the
    properties. To overcome this, they consult an analytics firm to get 
    insights on how densely the area is populated and the income levels 
    of residents. Use the Support Vector Machines algorithm on the given 
    dataset and draw out insights and also comment on the viability of 
    investing in that area.

'''
'''
Business Contraints:

Maximize : The profit gain from the selling the plot 

MInimize : Risk in Investing in the Suburban Locality and reduce the loss of
the property.

Business Contraints : Limited Budget: The construction firm may have a limited budget for developing infrastructure.
Market Demand: The demand for properties in the suburban locality may vary based on population density and income levels.
Competition: There may be existing competitors or potential future competitors in the real estate market.

'''

#################### EDA ###################################################
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


Salary = pd.read_csv('SalaryData_Train.csv')
Salary.head()

# The columns of the dataset
Salary.columns
'''
Limited Budget: The construction firm may have a limited budget for developing infrastructure.
Market Demand: The demand for properties in the suburban locality may vary based on population density and income levels.
Competition: There may be existing competitors or potential future competitors in the real estate market.
'''
# Check the datatypes of eah column
Salary.dtypes
'''
age               int64
workclass        object
education        object
educationno       int64
maritalstatus    object
occupation       object
relationship     object
race             object
sex              object
capitalgain       int64
capitalloss       int64
hoursperweek      int64
native           object
Salary           object
dtype: object
'''
# The mixed kind of data is available

# Five Number summary
Salary.describe()
'''
                age   educationno   capitalgain   capitalloss  hoursperweek
count  30161.000000  30161.000000  30161.000000  30161.000000  30161.000000
mean      38.438115     10.121316   1092.044064     88.302311     40.931269
std       13.134830      2.550037   7406.466611    404.121321     11.980182
min       17.000000      1.000000      0.000000      0.000000      1.000000
25%       28.000000      9.000000      0.000000      0.000000     40.000000
50%       37.000000     10.000000      0.000000      0.000000     40.000000
75%       47.000000     13.000000      0.000000      0.000000     45.000000
max       90.000000     16.000000  99999.000000   4356.000000     99.000000
'''
# There is difference in mean and median so the central tendancy is somewhat 
# Missing in this dataset .And there is chances of outlier present in the dataset

# Check information of the datset whether it contain the null value or not 
Salary.info()
'''
Data columns (total 14 columns):
 #   Column         Non-Null Count  Dtype 
---  ------         --------------  ----- 
 0   age            30161 non-null  int64 
 1   workclass      30161 non-null  object
 2   education      30161 non-null  object
 3   educationno    30161 non-null  int64 
 4   maritalstatus  30161 non-null  object
 5   occupation     30161 non-null  object
 6   relationship   30161 non-null  object
 7   race           30161 non-null  object
 8   sex            30161 non-null  object
 9   capitalgain    30161 non-null  int64 
 10  capitalloss    30161 non-null  int64 
 11  hoursperweek   30161 non-null  int64 
 12  native         30161 non-null  object
 13  Salary         30161 non-null  object
dtypes: int64(5), object(9)
memory usage: 3.2+ MB
'''
# As we see there is no null value is present inside the dataset so no need of missing
# Value handling

# Check for the outliers
sns.boxplot(Salary['age'])
# Outlier is present

sns.boxplot(Salary['educationno'])
# Outlier is present

sns.boxplot(Salary['capitalgain'])
# Outlier is present

sns.boxplot(Salary['capitalloss'])
# Outlier is present

sns.boxplot(Salary['hoursperweek'])
# Outlier is present 

# Encode categorical variables
label_encoder = LabelEncoder()
Salary['workclass'] = label_encoder.fit_transform(Salary['workclass'])
Salary['education'] = label_encoder.fit_transform(Salary['education'])
Salary['maritalstatus'] = label_encoder.fit_transform(Salary['maritalstatus'])
Salary['occupation'] = label_encoder.fit_transform(Salary['occupation'])
Salary['relationship'] = label_encoder.fit_transform(Salary['relationship'])
Salary['race'] = label_encoder.fit_transform(Salary['race'])
Salary['sex'] = label_encoder.fit_transform(Salary['sex'])
Salary['native'] = label_encoder.fit_transform(Salary['native'])
Salary['Salary'] = label_encoder.fit_transform(Salary['Salary'])

# Use Winsorization technique to remove the outlier
from feature_engine.outliers import Winsorizer
winsorizer = Winsorizer(capping_method='iqr', tail='both', fold=1.5, variables=['age'])
df_t = winsorizer.fit_transform(Salary[['age']])
sns.boxplot(df_t.age)

from feature_engine.outliers import Winsorizer
winsorizer = Winsorizer(capping_method='iqr', tail='both', fold=1.5, variables=['educationno'])
df_t = winsorizer.fit_transform(Salary[['educationno']])
sns.boxplot(df_t.educationno)

from feature_engine.outliers import Winsorizer
winsorizer = Winsorizer(capping_method='iqr', tail='both', fold=1.5, variables=['capitalgain'])
df_t = winsorizer.fit_transform(Salary[['capitalgain']])
sns.boxplot(df_t.capitalgain)

from feature_engine.outliers import Winsorizer
winsorizer = Winsorizer(capping_method='iqr', tail='both', fold=1.5, variables=['capitalloss'])
df_t = winsorizer.fit_transform(Salary[['capitalloss']])
sns.boxplot(df_t.capitalloss)

from feature_engine.outliers import Winsorizer
winsorizer = Winsorizer(capping_method='iqr', tail='both', fold=1.5, variables=['hoursperweek'])
df_t = winsorizer.fit_transform(Salary[['hoursperweek']])
sns.boxplot(df_t.hoursperweek)

# Split the data into features and target variable
X = Salary.drop('Salary', axis=1)
y = Salary['Salary']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model Training
svm_model = SVC(kernel='linear')  # Using linear kernel for interpretability
svm_model.fit(X_train_scaled, y_train)

# Model Evaluation
y_pred_train = svm_model.predict(X_train_scaled)
y_pred_test = svm_model.predict(X_test_scaled)

train_accuracy = accuracy_score(y_train, y_pred_train)
test_accuracy = accuracy_score(y_test, y_pred_test)

print("Train Accuracy:", train_accuracy)
# Train Accuracy: 0.8114638594164456
print("Test Accuracy:", test_accuracy)
# Test Accuracy: 0.8054036134593071

print("\nClassification Report on Test Data:")
print(classification_report(y_test, y_pred_test))

print("\nConfusion Matrix on Test Data:")
print(confusion_matrix(y_test, y_pred_test))
'''
[[4365  125]
 [1049  494]]
'''
