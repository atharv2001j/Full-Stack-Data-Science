# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 12:33:20 2024

@author: Atharv Joshi
"""
'''
Problem ststement :
    3.	An online car sales platform would like to improve its 
    customer base and their experience by providing them an 
    easy way to buy and sell cars. For this, they would like 
    an automated model which can predict the price of the car 
    once the user inputs the required factors. Help the business 
    achieve their objective by applying multilinear regression 
    on the given dataset. Please use the below columns for the 
    analysis purpose: price, age_08_04, KM, HP, cc, Doors, Gears, 
    Quarterly_Tax, and Weight.

'''
'''
Business Objective :

Maximize : The sales of the cars by improving the overall user experience by
automating the platformand also maximize the sales of the cars

Minimize : The Customer complaints and overall loss of the company

Business Contraints : The data provided by the customer should be safe and overall
maintainace and timely delivery of the car be there.

'''

####################################### EDA ##########################
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

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

# Define the formula for multilinear regression
model_formula = 'Price ~ Age_08_04 + KM + HP + cc + Doors + Gears + Quarterly_Tax + Weight'

# Create and fit the multilinear regression model
model = smf.ols(formula=model_formula, data=df_selected)
model_fit = model.fit()

# Print the summary of the model
print(model_fit.summary())
# The R-Squared value is 0.864 which is greater than 0.85 and quite significant
# towards prediction
# And the Durbin-Watson value is 1.545 and it is greater than 1 so our model
# Fit for the testing