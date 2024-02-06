# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 11:07:51 2024

@author: Atharv Joshi
"""
'''
Business Objective :

maximize : Business wants to maximize the number of employees earning more than 100k.

Minimize : If there are costs associated with hiring or degree requirements, the business may want to minimize these costs.

Business Contraints : Ensure diversity in job positions and degrees to create a balanced and inclusive workforce.

'''
'''
Data Dictionary :
The dataset contain mix type of data so there is numeric as well as categorical data 
and our target variable will be the salary_more_than_100k .
'''


import pandas as pd
df=pd.read_csv('salaries.csv')
df.head()
df.columns
inputs=df.drop('salary_more_then_100k',axis='columns')
target=df['salary_more_then_100k']

from sklearn.preprocessing import LabelEncoder
le_company=LabelEncoder()
le_job=LabelEncoder()
le_degree=LabelEncoder()

inputs['company_n']=le_company.fit_transform(inputs['company'])
inputs['job_n']=le_job.fit_transform(inputs['job'])
inputs['degree_n']=le_degree.fit_transform(inputs['degree'])

input_n=inputs.drop(['company','job','degree'],axis='columns')
target

from sklearn.ensemble import RandomForestClassifier
model= RandomForestClassifier()
model.fit(input_n,target)

# Is salary of Google,Computer Programmer,Bachleros degree >100k
model.predict([[2,1,0]])
# Is salary of google,computer programmer,masters_degree>100k
model.predict([[2,1,1]])
