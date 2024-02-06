# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 15:39:46 2024

@author: Atharv Joshi
"""
"""
Problem Statement: Prepare a classification model using the Naive Bayes algorithm 
for the salary dataset. Train and test datasets are given separately. 
Use both for model building. 
"""

"""
Business Objectives:
    
maximize : The overall salary of the employee based on its education and number of hours
            he/she is working and the capitalgain 
            
Minimize : The capitalloss of the company should be minimize as it will affect on the salary
            of the employee as well as the its performance
            
Business Contraints: The overall data of employee and maintaining all the information 
                    which will directly affect on the salary should be maintain
                    
"""

"""
DataFrame:

age: Numeric 

workclass: Categorical

educationno = Numeric

education : Non-numeric , Categorical

maritalstatus = Non-numeric , Categorical

occupation = Non-numeric ,Categorical

relationship = Non-numeric ,categorical

race = Categorical

sex = Categorical

capitalgain = Numeric

capitalloss = Numeric

hoursperweek = Numeric

native = Categorical

Salary = Categorical

"""

##########################################33

########################## EDA #########################################3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

df=pd.read_csv('SalaryData_Train.csv')
df.head()
df.shape
# The dataset contain the total  30161 rows and 14 columns

df.dtypes
'''
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
############################3
df.columns
'''
Index(['age', 'workclass', 'education', 'educationno', 'maritalstatus',
       'occupation', 'relationship', 'race', 'sex', 'capitalgain',
       'capitalloss', 'hoursperweek', 'native', 'Salary'],
      dtype='object')
'''
###############################
df.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 30161 entries, 0 to 30160
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
# The dataset does not contain any null value so that there will be not need for any 
# replacement
##############################
a=df.describe()
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
# The mean and meadian of the the capitalgain and capitaloss showing measure diffrence 
# so to minimize it we have to normalize it
########################################
# Visualize the data

# For understanding the nature of yhe data that is the presence of the outlier

# For Detecting the outlier we will plot the boxplot

sns.boxplot(df)
#########################################

# Normalization of the data

def norm_fun(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

df_norm=norm_fun(a)
df_norm

'''
           age  educationno  capitalgain  capitalloss  hoursperweek
count  1.000000     1.000000     0.301613     1.000000      1.000000
mean   0.000839     0.000302     0.010921     0.002928      0.001324
std    0.000000     0.000051     0.074065     0.013399      0.000364
min    0.000128     0.000000     0.000000     0.000000      0.000000
25%    0.000493     0.000265     0.000000     0.000000      0.001293
50%    0.000792     0.000298     0.000000     0.000000      0.001293
75%    0.001123     0.000398     0.000000     0.000000      0.001459
max    0.002550     0.000497     1.000000     0.144425      0.003249
'''
# From above normalization we can see that the mean and median value difference become less and the
# standard deviation tends to zero

################################################
# Read the train Data and Test data 
Test_data=pd.read_csv('SalaryData_Test.csv')
Test_data.head()

######################################
X=Test_data[['educationno','hoursperweek']]
y=Test_data[['Salary']]
###########################################
Train_data=pd.read_csv('SalaryData_Train.csv')
Train_data
############################################
X1=Train_data[['educationno','hoursperweek']]
y1=Train_data[['Salary']]

from sklearn.naive_bayes import MultinomialNB as MB
classifier_mb=MB()

# The fit the model
classifier_mb.fit(X1,y1)
####################################
# Check the accuracy of the model

y_pred = classifier_mb.predict(X)  
y_pred

from sklearn.metrics import accuracy_score

# Assuming y_pred is the predicted values and y is the actual values
accuracy = accuracy_score(y, y_pred)

print(f"Accuracy: {accuracy}")
################################
