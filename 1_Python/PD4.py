
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 17:15:27 2023

@author: Atharv
"""
#Series
#Operation onn one column
import pandas as pd
songs1=pd.Series([145,142,38,13],name='counts')
songs1
songs1.index

#Giving index to series
songs2=pd.Series([145,142,38,13],name='counts',index=['arijit','adnan','ringo','John'])
songs2.index
songs2
#NaN value handling
import numpy as np
songs1=pd.Series([145,142,38,13])
songs1[2]
#calculated in mean
songs1.mean()
#series alloww duplicate index name
george=pd.Series([10,7,1,22],index=['1968','1969','1970','1970'],name='george sp\ongs')
george
#read or select the data from series
george['1968']
#access all the values of series
for i in george:
    print(i)
#updating values in series
george['1968']=68
george['1968']    
#Deletion
s=pd.Series([2,3,4],index=[1,2,3]) 
del(s[1])
s 
#Convert datatype
songs_66=pd.Series([145,None,38,13],name='counts',
                 index=['arijit','raju','ringo','John'])
 
pd.to_numeric(songs_66.apply(str))    
#it will show error
#to ignore error
pd.to_numeric(songs_66.apply(str),errors='coerce')    
#Dealing with NaN value
songs_66.fillna(-1)
#to drop the NULL value
songs_66.dropna()  
#append and join the two series
songs_69=pd.Series([7,6,19,39],index=['ram','shyam','mukul','ani'],name='counts')
songs=songs_66.append(songs_69)    
songs   
#Plot the series
import matplotlib.pyplot as plt 
fig=plt.figure()   
songs_69.plot()
plt.legend()   
##########################
fig=plt.figure()   
songs_69.plot(kind='bar')
songs_66.plot(kind='bar',color='b',alpha=.5)
plt.legend() 
#histogram
data=pd.Series(np.random.randn(500),name='500 random')
fig=plt.figure()
ax=fig.add_subplot(111)
data.hist()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    