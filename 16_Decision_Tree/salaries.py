# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 09:15:59 2024

@author: Atharv Joshi
"""

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

from sklearn import tree
model=tree.DecisionTreeClassifier()
model.fit(input_n,target)

# Is salary of Google,Computer Programmer,Bachleros degree >100k
model.predict([2,1,0])
# Is salary of google,computer programmer,masters_degree>100k
model.predict([2,1,1])
