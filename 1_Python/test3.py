# -*- coding: utf-8 -*-
"""
Created on Thu May 25 15:34:53 2023

@author: Hp
"""

'''
Name:- Atharv Avinash Joshi
TY Comp 
'''
from fnmatch import fnmatch
import pandas as pd
import pandas as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
df=pd.read_csv('Data_Science_Attendance_Sheet2.csv')
df
#Q1. Rename Your name Column
df1=df.rename(columns={'joshi':'JOSHI'})
df1['JOSHI']
##############################################################

#Q2. Convert your column into list
df2=df1['JOSHI'].tolist()
df2

#Q.3 From the derived list,find out how for how many days,you appeared 0,1,2,3,4,5,7 sessions
df2.count(4)
df2.count(0)
df2.count(1)
df2.count(2)
df2.count(3)
df2.count(5)
df2.count(7)
#Q.4 Generate a bar graph of your attendance
sns.countplot(x='JOSHI',data=df1)

#Q.5 Generate 5 number summary using describe() and illustrate the minimum number of sessions ,max
#number of sessions and mean number of sessions you did during the training
df3=df[:6]
df3.describe()
#Q.6 Generate box plot using seaborn for your column and write the inference
sns.boxplot(df1.JOSHI)
#Q.7 Generate joint plot using seaborn for your column and write the inference
sns.jointplot(x='joshi',y='joshi',data=df)
#Q. 8 From complete dataframe, find out how many are regular students, how many are moderate and 
#how many are poor in attendance.
df
df.describe()
n = len(df.columns) - 3
n
regular=0
moderate=0
poor=0
for i in range(n):
    name = df.columns[i]
    d = df[name].describe()
    d
    if d[1] >= 4.7:
        regular+=1
    elif d[1] >= 2 and d[1]<4.7:
        moderate+=1
    else:
        poor+=1

print(f'regualar students are = {regular}, moderate students are = {moderate}, poor students are = {poor}')

#Q.9 Out of functions, list and dictionary ,in which area you are strong and weak?
df=pd.read_csv('Marksheet.csv')
df
df2=df.index[df['Name']=='Joshi_Athrva']
df[29:30].max()
#Q.10 How many students have shown very good performance and how many have shown poor
#performance?
n = len(df)

good=0
bad=0

for i in range(n):
    f=df.iloc[i].Function
    l=df.iloc[i].List
    d=df.iloc[i].Dictionary
    
    tot = f+l+d
    
    if tot>=6:
        good+=1
    else:
        bad+=1
    
print(f'Students with good performance are {good} and with bad performance are {bad}')

#Q.11 Open the given file in read mode
filename='AI_jobs_in_2024.txt'
with open(filename) as file_object:
    data = file_object.read()
print(data)
        

#Q.12 Remove the numbers from the text    

filename='AI_jobs_in_2024.txt'
with open(filename) as file_object:
    data = file_object.read()
    pat=r'[^a-zA-Z.,!?/:;\"\'\s]'
    print(re.sub(pat, '',data))
    
 
#Q.13 How many companies were surveyed ,extract using text processing  
with open(filename) as file_object:
    data = file_object.read()
    num=re.findall(r'\d+(?:\.\d+)?',data)
    print(num)
    num[0]

#Q.14 How many companies are willing to shift in AI domain,extract using text processing  
with open(filename) as file_object:
    data = file_object.read()
    num=re.findall(r'\d+(?:\.\d+)?',data)
    print(num)  
    print("Percentage of companies:",num[-8])
 
#Q.15 How many millions jobs are expected to create in 2024 in field of AI
with open(filename) as file_object:
    data = file_object.read()
    num=re.findall(r'\d+(?:\.\d+)?',data)
    print(num)
    num[-1]
#Q.16 Convert numbers into words
import inflect 
p= inflect.engine()
with open(filename) as file_object:
    data = file_object.read()
    temp_str=data.split()
    new_string=[]
    for word in temp_str:
        if word.isdigit():
            temp=p.number_to_words(word)
            new_string.append(temp)
        else:
            new_string.append(word)
    temp_str=' '.join(new_string)
    print(temp_str)

