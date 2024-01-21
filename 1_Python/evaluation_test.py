# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 15:11:37 2023

@author: Lenovo
"""

#1 check whether list is empty
lst=[1,2]
c=0
for i in range(len(lst)):
    c+=1
if c==0:
    print('empty')
else:
    print('not empty')
    
    
#2 using list comprehension calculate the square of each element in the list
lst=[1,2,3,4]
lst1=[i*i for i in lst]
lst1

#3.Write a python script to check whether a given key already exist in a  dictionary
dic={
     1:['atharv','joshi'],
     2:['Yash','Halwai'],
     3:['Sanket','Gadekar']
     }
inp=int(input('Enter a key:'))
c= inp in dic.keys()
if c==True:
    print('Present')
else:
    print('NO')

#4.First create a range from 100 to 160 with steps of 10 seconds using dict comprehension
#create a dictionary where each number in the range key and the each item divisible by 100 is values


dic={i for i in range(100,161,10)}
dic
dictionary={i:i for i in dic if i%100==0}
dictionary

#5 create a dataframe which comprises course,fee,duration,and add tutor column
tech={
      'course':['Python','C++','Spark'],
      'fee':[1000,200,2001],
      'duration':['5days','10days','15days']
      }
import pandas as pd
df=pd.DataFrame(tech)
tutor=['atharv','yash','sanket']
df['Tutor']=tutor
df

#6.convert it to csv
df.to_csv('kpg.csv')
#7 Write a python function which returs multile values
def multiple(*arg):
    return arg
multiple(1,2,3)

#8.Write a function which takes two arguments a and b andreturd multiplication 
#of them
multiplication=lambda a,b:a*b
multiplication(3, 4) 

#9.write a numpy program program to test if any of the elememt in given array
#are non_zero

import numpy as np
arr=np.array([1,2,3,0])
any(arr)

#10 write a program to plot two or more lines and set  the line markers
import matplotlib.pyplot as plt
plt.plot([2,4,6,8],marker='*')
plt.plot([3,6,9,12],marker='o')
plt.show()

#11 Write a python programming to display a bar graph of the populrity of 
# programming languages sample data:
#Programming Languages :java,python,c,java,PHP,C#,C++
#Popularity 22.2,23.7,8.8,8,7.7,6.7

plt.bar(['c++','python','c#','java','PHP','C'],[22.2,23.7,8.8,8,7.7,6.7])
plt.xlabel('Languages')
plt.ylabel('Popularity')
plt.show()







