# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 11:41:57 2024

@author: Atharv Joshi
"""

'''
Business Objective : 

Maximize : Improve the model's ability to accurately predict monthly income, 
enhancing its effectiveness in identifying accurate salary claims.

Minimize :  Reduce discrepancies between claimed and predicted incomes to minimize 
the risk of candidates providing inaccurate salary information.

Business Contraints : Adhere to relevant regulations, especially those related to data
protection and privacy in the recruitment domain.
 
'''
'''
Data Dictionary:
    
The dataset contain a mixed type of data where it contain both the categorical and 
numerical data where the monthly income of the employee become the target variable
and all other ecome the features that affect the overall result of the program.
'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder
df=pd.read_csv('HR_DT.csv')
df.head()
###########################################################################
df.columns
'''
Index(['Position of the employee', 'no of Years of Experience of employee',
       ' monthly income of employee'],
      dtype='object')
'''
###########################################################################
df.dtypes
'''
Position of the employee                  object
no of Years of Experience of employee    float64
 monthly income of employee                int64
dtype: object
'''
# The datatype of the all columns are integer except Position of the employee
##########################################################################
df.describe()
'''
       no of Years of Experience of employee   monthly income of employee
count                             196.000000                   196.000000
mean                                5.112245                 74194.923469
std                                 2.783993                 26731.578387
min                                 1.000000                 37731.000000
25%                                 3.000000                 56430.000000
50%                                 4.100000                 63831.500000
75%                                 7.100000                 98273.000000
max                                10.500000                122391.000000
'''
# The difference between mean and median is comapritevly more so result
# the spread of data is more .Also the standard deviation is more so the
# the points are deviated from the median
#############################################################################
df.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 196 entries, 0 to 195
Data columns (total 3 columns):
 #   Column                                 Non-Null Count  Dtype  
---  ------                                 --------------  -----  
 0   Position of the employee               196 non-null    object 
 1   no of Years of Experience of employee  196 non-null    float64
 2    monthly income of employee            196 non-null    int64  
dtypes: float64(1), int64(1), object(1)
memory usage: 4.7+ KB
'''
# The dataset does not contain any null value so no need of the data handling
###############################################################################33
df.value_counts()
# The value counts shows that the dataset is not balanced so we have to treat
# The algorithm according to that.
##############################################################################
# Separate features (X) and target variable (y)
X = df[['Position of the employee', 'no of Years of Experience of employee']]
y = df[' monthly income of employee']

# Convert categorical variables into numerical representations
label_encoder = LabelEncoder()
X['Position of the employee'] = label_encoder.fit_transform(X['Position of the employee'])

# Divide the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Decision Tree model
from sklearn.ensemble import RandomForestClassifier
model= RandomForestClassifier(n_estimators=20)

# Train the model on the training se
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)
y_pred
# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print the evaluation metrics
print(f"Mean Squared Error: {mse}")
print(f"R-squared Score: {r2}")
##################################################################################

