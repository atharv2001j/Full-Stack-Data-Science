# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 23:50:02 2023

@author: Atharv
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_excel("Cocube.xlsx")
df
df.columns
df['Employability Index']
sns.countplot(x='Employability Index',data=df)
sns.countplot(x='Employability Index',y='Name',data=df)
x=list(df['Name'][:70])
y=list(df['Score'][:70])
plt.bar(x,y)
plt.xticks(rotation=90)
plt.show()

x1=list(df['Name'][70:])
y1=list(df['Score'][70:])
plt.bar(x1,y1)
plt.xticks(rotation=90)
plt.show()
