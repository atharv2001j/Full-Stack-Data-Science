# -*- coding: utf-8 -*-
"""
Created on Sat May 27 11:02:04 2023

@author: HP
"""

################################

import pandas as pd
import numpy as np

###########################################################
att = pd.read_excel('new.xlsx')
att

att.drop('Quiz2',axis=1, inplace=True)

att.to_excel('new.xlsx')
att = pd.read_excel('new.xlsx')
att

att=att.fillna(0)
##########################################

cols = list(att.columns)
cols

cols.remove('Sr.No.')
cols.remove('Name')
cols.remove('class')
cols.remove('Unnamed: 0')

dates = cols
dates
len(dates)
#################################################

per_day = []

for i in dates:
    
    per_day.append(list(att[i]))

per_day

len(per_day)

##############################################
#len(l) == len(dates)

names = att['Name']
names

len(names) == len(per_day[0])

#################################################

#creating set

dates_set = []

for i in dates:
    
    n = int(float(str(i)))
    
    if n not in dates_set:
        dates_set.append(n)

dates_set

#################################################

d = {}

for i in names:
    d[i] = []

d

################################################

for i in range(len(names)):
    
    per_stu_att = []
    
    for x in per_day:
        
         per_stu_att.append(x[i])
        
        #d[names[i]] = list(per_stu_att)
    
    d[names[i]] = list(per_stu_att)

d

####################################################################################################################################

d1 = d['Aditya Dhole']
d1 = {'Aditya Dhole': d1}
d1

d

for i in names:
    
    li = d[i]
    
    for n in dates_set:
        
        count = 0
        var = 0
        
        for date in dates:
            
            if n == int(float(str(date))):
               pass 

dates_set


freq = []

var = 0

for i in dates_set:
    
    count = 0
    
    for date in dates:
        
        if i == int(float(str(date))):
            count+=1
        else:
            break
            
    freq.append(count)
            
     
freq=[]

temp = dates

f = []

for i in dates_set:
    
    count = 0
    
    for date in temp:
        
        if i == int(float(str(date))):
            count+=1
            
        else:
            break
    
    f.append(count)
    
################################################ 
count = 0
for d in range(var, len(dates)):
        print(d)
        
        if i == int(float(str(dates[d]))):
            count+=1
        else:
            #print(d)
            var = d
            break
            
freq.append(count)