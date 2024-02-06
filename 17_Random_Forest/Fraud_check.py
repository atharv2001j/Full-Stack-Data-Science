# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 22:49:25 2024

@author: Atharv Joshi
"""

'''
Business Objective:

Maximize: Improve the model's ability to accurately classify individuals into taxable and non-taxable income categories.


Minimize: False Positives and False Negatives:** Reduce the occurrences of incorrectly predicting taxable or non-taxable income, as these errors may have different implications.

Business Contraints : 
1. Interpretability of the Model: Ensure the decision tree model remains interpretable, allowing stakeholders to understand the factors influencing taxability predictions.

2. Resource Constraints: Consider computational resources and time limitations, ensuring the model can be trained and deployed within available constraints.

3. Ethical Considerations: Address potential biases in predictions to avoid discrimination and adhere to ethical standards.

4.Regulatory Compliance: Ensure the model and predictions comply with relevant regulations and standards, especially those related to data protection and privacy in the context of income information.

'''
'''
Data Dictionary:

The ta dictionary of the dataset contain all mix types of the columns i.e. Both the numeric
the numeric and noon-numeric type of the data
    
'''

import pandas as pd
df=pd.read_csv('Fraud_check.csv')
df.columns
##################################################################
df.dtypes
'''
Undergrad          object
Marital.Status     object
Taxable.Income      int64
City.Population     int64
Work.Experience     int64
Urban              object
dtype: object
'''
# The datatype of the dataset are the mix match so we have to convert it into
# the categorical type 
######################################################################
df.info() 
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 600 entries, 0 to 599
Data columns (total 6 columns):
 #   Column           Non-Null Count  Dtype 
---  ------           --------------  ----- 
 0   Undergrad        600 non-null    object
 1   Marital.Status   600 non-null    object
 2   Taxable.Income   600 non-null    int64 
 3   City.Population  600 non-null    int64 
 4   Work.Experience  600 non-null    int64 
 5   Urban            600 non-null    object
dtypes: int64(3), object(3)
memory usage: 28.2+ KB
'''
# There will no any null value in the dataset
# So the no need of data handling
#############################################################################
df.value_counts()
# it will count the each category items and the related elements
#########################################################################
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# Display the first few rows of the dataframe to understand the structure
print(df.head())

# Separate features (X) and target variable (y)
X = df[['Undergrad', 'Marital.Status', 'City.Population', 'Work.Experience', 'Urban']]
y = df['Taxable.Income']

# Convert categorical variables into numerical representations (you might need to handle this based on the nature of your data)
X = pd.get_dummies(X, columns=['Undergrad', 'Marital.Status', 'Urban'], drop_first=True)

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

########################################################################################
