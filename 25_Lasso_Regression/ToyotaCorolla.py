# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 20:28:52 2024

@author: Atharv Joshi
"""
'''
Problem Statement :
    2.	An online car sales platform would like to improve its customer 
    base and their experience by providing them an easy way to buy and
    sell cars. For this, they would like to have an automated model which
    can predict the price of the car once the user inputs the required 
    factors. Help the business achieve the objective by applying Lasso 
    and Ridge Regression on it.Please use the below columns for the analysis:
    Price, Age_08_04, KM, HP, cc, Doors, Gears, Quarterly_Tax, Weight.

'''

'''
Business Objective :

Maximize : The sales of the cars by improving the overall user experience by
automating the platformand also maximize the sales of the cars

Minimize : The Customer complaints and overall loss of the company

Business Contraints : The data provided by the customer should be safe and overall
maintainace and timely delivery of the car be there.

'''
############################### EDA ####################################
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso, Ridge
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('ToyotaCorolla.csv', encoding='ISO-8859-1')
df.head()

df.columns
# Select relevant columns for analysis
selected_columns = ['Price', 'Age_08_04', 'KM', 'HP', 'cc', 'Doors', 'Gears', 'Quarterly_Tax', 'Weight']
df_selected = df[selected_columns]
# Display basic statistics of the selected columns
print(df_selected.describe())
'''
              Price    Age_08_04  ...  Quarterly_Tax      Weight
count   1436.000000  1436.000000  ...    1436.000000  1436.00000
mean   10730.824513    55.947075  ...      87.122563  1072.45961
std     3626.964585    18.599988  ...      41.128611    52.64112
min     4350.000000     1.000000  ...      19.000000  1000.00000
25%     8450.000000    44.000000  ...      69.000000  1040.00000
50%     9900.000000    61.000000  ...      85.000000  1070.00000
75%    11950.000000    70.000000  ...      85.000000  1085.00000
max    32500.000000    80.000000  ...     283.000000  1615.00000
'''
# There is relatively large difference in mean and median so the datapoints may
# Scatter from the mean position

# Check for missing values
print(df_selected.isnull().sum())
'''
Price            0
Age_08_04        0
KM               0
HP               0
cc               0
Doors            0
Gears            0
Quarterly_Tax    0
Weight           0
dtype: int64
'''
# There is no null value present in the dataset
df.info()
'''
Data columns (total 38 columns):
 #   Column            Non-Null Count  Dtype 
---  ------            --------------  ----- 
 0   Id                1436 non-null   int64 
 1   Model             1436 non-null   object
 2   Price             1436 non-null   int64 
 3   Age_08_04         1436 non-null   int64 
 4   Mfg_Month         1436 non-null   int64 
 5   Mfg_Year          1436 non-null   int64 
 6   KM                1436 non-null   int64 
 7   Fuel_Type         1436 non-null   object
 8   HP                1436 non-null   int64 
 9   Met_Color         1436 non-null   int64 
 10  Color             1436 non-null   object
 11  Automatic         1436 non-null   int64 
 12  cc                1436 non-null   int64 
 13  Doors             1436 non-null   int64 
 14  Cylinders         1436 non-null   int64 
 15  Gears             1436 non-null   int64 
 16  Quarterly_Tax     1436 non-null   int64 
 17  Weight            1436 non-null   int64 
 18  Mfr_Guarantee     1436 non-null   int64 
 19  BOVAG_Guarantee   1436 non-null   int64 
 20  Guarantee_Period  1436 non-null   int64 
 21  ABS               1436 non-null   int64 
 22  Airbag_1          1436 non-null   int64 
 23  Airbag_2          1436 non-null   int64 
 24  Airco             1436 non-null   int64 
 25  Automatic_airco   1436 non-null   int64 
 26  Boardcomputer     1436 non-null   int64 
 27  CD_Player         1436 non-null   int64 
 28  Central_Lock      1436 non-null   int64 
 29  Powered_Windows   1436 non-null   int64 
 30  Power_Steering    1436 non-null   int64 
 31  Radio             1436 non-null   int64 
 32  Mistlamps         1436 non-null   int64 
 33  Sport_Model       1436 non-null   int64 
 34  Backseat_Divider  1436 non-null   int64 
 35  Metallic_Rim      1436 non-null   int64 
 36  Radio_cassette    1436 non-null   int64 
 37  Tow_Bar           1436 non-null   int64 
dtypes: int64(35), object(3)
memory usage: 426.4+ KB
'''
# Almost all the columns are in numeric in nature except the colour
# Fuel_type and Model 

# Check for correlations between variables
correlation_matrix = df_selected.corr()
print(correlation_matrix)
# The datapoints shows co-relation among themselves
# So the result mostly depends on each other
# Check if there is outlier present in that or not

sns.boxplot(df)
# There is outlier present in the age and year column 

sns.distplot(df['Age_08_04'])
# The datais left skewed

sns.distplot(df['Mfg_Year'])
# The data is Bi-modal

# The data shows the mismatched nature means all the columns are not
# Equally contribute to the prediction so we use smf for that
# Now we will build our model


# Data Preprocessing
# Drop any duplicate rows
df = df.drop_duplicates()

# Handle missing values if any
# For example, fill missing values with mean or median
df.fillna(df.mean(), inplace=True)


# Separate categorical and numerical columns
categorical_cols = ['Doors']  # Add other categorical columns if present
numeric_cols = ['Age_08_04', 'KM', 'HP', 'cc', 'Gears', 'Quarterly_Tax', 'Weight']  # Exclude 'Price' column

# One-hot encode categorical columns
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
ct = ColumnTransformer(
    [('encoder', OneHotEncoder(), categorical_cols)],
    remainder='passthrough'
)
data_encoded = ct.fit_transform(df[categorical_cols + numeric_cols])

# Convert the encoded data back to a DataFrame
data_encoded_df = pd.DataFrame(data_encoded, columns=ct.get_feature_names_out())

# Combine the encoded dfFrame with the target variable 'Price'
df_preprocessed = pd.concat([data_encoded_df, df['Price']], axis=1)

# Split the df into features (X) and target variable (y)
X = df_preprocessed.drop('Price', axis=1)
y = df_preprocessed['Price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model Building - Lasso Regression
lasso = Lasso(alpha=0.1)
lasso.fit(X_train_scaled, y_train)

# Model Building - Ridge Regression
ridge = Ridge(alpha=0.1)
ridge.fit(X_train_scaled, y_train)

# Model Evaluation
# Predictions
lasso_preds = lasso.predict(X_test_scaled)
ridge_preds = ridge.predict(X_test_scaled)

# Evaluate Lasso Regression
lasso_rmse = np.sqrt(mean_squared_error(y_test, lasso_preds))
lasso_r2 = r2_score(y_test, lasso_preds)

# Evaluate Ridge Regression
ridge_rmse = np.sqrt(mean_squared_error(y_test, ridge_preds))
ridge_r2 = r2_score(y_test, ridge_preds)

print(f'Lasso Regression RMSE: {lasso_rmse}')
print(f'Lasso Regression R-squared: {lasso_r2}')

print(f'Ridge Regression RMSE: {ridge_rmse}')
print(f'Ridge Regression R-squared: {ridge_r2}')