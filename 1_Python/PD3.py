
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 08:53:58 2023

@author: Atharv
"""
import pandas as pd
technologies={
    'courses':["spark","pyspark","Python","Hadoop"],
    'Fee':[20000,25000,26000,50000],
    'Duration':['30days','40days','50days','40days']

    }
index_label=['r1','r2','r3','r9']
df1=pd.DataFrame(technologies,index=index_label)
#df1=pd.DataFrame(technologies)
df1
technologies1={
    'courses':["spark","Java","Python","Go"],
    'Discount':[2000,2300,1200,2000]
    }
index_label2=['r1','r6','r3','r4']
df2=pd.DataFrame(technologies1,index=index_label2)
#df2=pd.DataFrame(technologies1)
df2
#left join
df3=df1.join(df2,lsuffix='_left',rsuffix='_right',how='left')

df3
#inner join
df4=df1.join(df2,lsuffix='_left',rsuffix='_right',how='inner')
df4
#right join
df4=df1.join(df2,lsuffix='_left',rsuffix='_right',how='right')
df4
#pandas using columns
df3=df1.set_index('courses').join(df2.set_index('courses'),how='inner')
df3
df3=df1.set_index('courses').join(df2.set_index('courses'),how='left')
df3
df3=df1.set_index('courses').join(df2.set_index('courses'),how='right')
df3
df3=df1.set_index('courses').join(df2.set_index('courses'),how='outer')
df3
#Merging two dataframes
import pandas as pd
technologies={
    'courses':["spark","pyspark","Python","pandas"],
    'Fee':[20000,25000,22000,30000],
    'Duration':['30days','40days','35days','50days']

    }
index_label=['r1','r2','r3','r4']
df1=pd.DataFrame(technologies,index=index_label)
df1
technologies1={
    'courses':["spark","Java","Python","Go"],
    'Discount':[2000,2300,1200,2000]
    }
index_label2=['r1','r6','r3','r5']
df2=pd.DataFrame(technologies1,index=index_label2)
df2

df3=pd.merge(df1,df2)
df3
#using dataframe.merge()
df3=df1.merge(df2)
df3
df3=df1.merge(df2,how='right')
df3
#using pandas.concat() to concat two dataframes
data=[df1,df2]
df3=pd.concat(data)
df3
technologies3={
    'courses':["C","Java","Python","C++"],
    'Discount':[2000,2300,100,20000]
    }
df3=pd.DataFrame(technologies3)
df4=pd.concat([df1,df2,df3])
df4
#write dataframe to csv file with default parameter
df4.to_csv('c:/Atharv/courses.csv')
#read csv file into DataFrame
df=pd.read_csv('courses.csv')
#Write dataframe to excel
df.to_excel('c:/Atharv/courses.xlsx')
#########################################################################
#Read excel  file
df=pd.read_excel('courses.xlsx')
df


















