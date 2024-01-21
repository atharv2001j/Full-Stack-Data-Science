# -*- coding: utf-8 -*-
"""
Created on Wed May  3 08:37:48 2023

@author: Atharv
"""
#Pandas accessing columns using index/poitions
import pandas as pd
import numpy as np
technologies={
    'courses':["spark","pyspark","Hadoop","Python","English","Marathi"],
    'Fee':[20000,25000,26000,50000,23000,np.nan],
    'Duration':['30days','40days','50days','40days','20days','10days'],
    'Discount':[1000,2300,1500,1000,200,100]
    }
row_labels = ['r0','r1','r2','r3','r4','r5']
df = pd.DataFrame(technologies, index = row_labels)
df
#using iloc
df2=df.iloc[ : ,1:3]
df2
df3=df.iloc[0:4 ,1:3]
df3
df4=df.iloc[0:4, : ]
df4
df5=df.iloc[[1,2,3],[1,2]]
df5
#select row by index
df2.iloc[2]             #select 2nd row
df.iloc[1:3]            #select first three rows
df.iloc[-1:]            #select last row
df.iloc[[2,3,4]]        #select particular row
df.iloc[:0]             #empty row
df.iloc[:1]             #slect first row
df.iloc[-3:]            #select last three row
df.iloc[::2]            #select alternate row
#Select index by row label
df
df.loc['r1']
df.loc[['r1','r2','r3']]
df.loc['r1':'r4']
df.loc['r0':'r4':2] #alernatte row
#######################################################
#SELECT multiple column
df2=df[['Fee','Duration']]
df2
#using loc
df2=df.loc[ : ,['Fee','Duration']]
df2
#select columns between two colums
df2=df.loc[ : ,'Fee':'Discount']
df2
#Select columns by range
df2=df.loc[:,'Duration':]
df2
df2=df.loc[:,:'Duration']
df2
###########################################################
#to diaplay f3=df.assign(tutor)
df3
#all the rows containing particular keyword
df2=df.query("courses=='spark'")
df2
#not equals 
df2=df.query("courses!='spark'")
df2
###########################################################
#Add column into DataFrame
technologies={
    'courses':["spark","pyspark","Hadoop","Python","English","Marathi"],
    'Fee':[20000,25000,26000,50000,23000,5000],
    'Discount':[1000,2300,1500,1000,200,100]
    }
df=pd.DataFrame(technologies)
df

#Add new column DataFrame
tutor=['ravi','atharv','avinash','yash','sanket','prachi']
df2=df.assign(TutorAssigne=tutor)
df2 
#Without using assign
tutor=['ravi','atharv','avinash','yash','sanket','prachi']
df2['Tutor']=tutor
df2
#Add multiple columns to the dataframe
MNC=['wipro','TCS','Google','Celeble','Amazon','HCL']
df3=df.assign(MNCCoomp=MNC,TutorAssigned=tutor)
df3
#Derive new column from from existing column
df=pd.DataFrame(technologies)
df2=df.assign(Discount_Percent=lambda x:x.Fee*x.Discount/100)
df2
############
#another way using lambda
df['dp']=df['Fee']*df['Discount']/100
df
#add column into specific position
df=pd.DataFrame(technologies)
df.insert(0,'Tutors',tutor)
df
#########################################################
technologies={
    'courses':["spark","pyspark","Hadoop","Python","English","Marathi"],
    'Fee':[20000,25000,26000,50000,23000,60000],
    'Duration':['30days','40days','50days','40days','20days','10days'],
    'Discount':[1000,2300,1500,1000,200,100]
    }
df=pd.DataFrame(technologies)
df.columns
#Rename the columns
df2=df.rename({'courses':'Courses'},axis=1)
df2.columns
df2=df.rename(columns={'courses':'Corse_list'})
df2=df.rename({'courses':'Corse_list'},axis='columns')
#Quick example  to get the the number of rows
row_count=len(df.index)
row_count
row_count=len(df.axes[0])
row_count
#######################
row_count=df.shape[0]
col_count=df.shape[1]
print(row_count)
print(col_count)
###################################################
data={
      "A":[1,2,3],
      'B':[4,5,6],
      'C':[7,8,9]}
df=pd.DataFrame(data)
df
#apply function on complete dataframe
def add_3(x):
    return x+3
df2=df.apply(add_3)
df2
#apply function to specific column of DataFrame
df['A']=df['A'].apply(add_3)
df['A']    
df
#apply function to multiple columns
df[['A','B']]=df[['A','B']].apply(add_3)
df
#apply lambda function to each column
df2=df.apply(lambda x:x+10)
df2
#apply lambda function to single column
df['A']=df['A'].apply(lambda x:x+10)
df['A'] 
#apply lambda function to multiple column
df[['A','B']]=df[['A','B']].apply(lambda x:x+4)
df
#using transform() function
def add_3(x):
    return x+3
df=df.transform(add_3)
df
#apply function aon single column using map()
df['A']=df['A'].map(add_3)
df
#apply inbuild function on single column
import numpy as np
df['A']=df['A'].apply(np.square)
df
#apply numpy functionn without using he features of pandas
df['A']=np.square(df['A'])
df
#pandas Groupby() with examples
technologies={
    'courses':["spark","spark","Hadoop","Python","Python","Marathi"],
    'Fee':[20000,25000,26000,50000,23000,60000],
    'Duration':['30days','40days','50days','40days','20days','10days'],
    'Discount':[1000,2300,1500,1000,200,100]
    }
df=pd.DataFrame(technologies)
df

df2=df.groupby(['courses']).sum()
df2
#groupby on multiplle columns
df3=df.groupby(['courses','Fee']).sum()
df3
#Reset the index
df3=df.groupby(['courses','Fee']).sum().reset_index()
df3
df2=df.groupby(['courses']).sum()
df2

#######################3
import pandas as pd
import numpy as np
technologies={
    'courses':["spark","spark","Hadoop","Python","Python","Marathi"],
    'Fee':[20000,25000,26000,50000,23000,60000],
    'Duration':['30days','40days','50days',None,np.nan,'10days'],
    'Discount':[1000,2300,1500,1000,200,100]
    }
df=pd.DataFrame(technologies)
df
df.columns
#get the list of columns header as a list
column_header=list(df.columns.values)
print("The column header: ",column_header)
#using list(df) to get the list of all column names
column_header=list(df)
column_header
#Pandas shuffle Dataframe rows
technologies={
    'courses':["spark","spark","Hadoop","Python","Python","Marathi"],
    'Fee':[20000,25000,26000,50000,23000,60000],
    'Duration':['30days','40days','50days','24days','32days','10days'],
    'Discount':[1000,2300,1500,1000,200,100]
    }
df=pd.DataFrame(technologies)
df
#Shuffle the dataframe  rows and return all rows
df1=df.sample(frac=1)
df1
#create a new index starting from zero
df1=df.sample(frac=1).reset_index()
df1
#Drop shuffle index
df1=df.sample(frac=1).reset_index(drop=True)
df1
##############################################
import pandas as pd
technologies={
    'courses':["spark","Hadoop",'Python',"Marathi"],
    'Fee':[20000,25000,26000,50000],
    'Duration':['30days','40days','50days','24days'],
    'Discount':[1000,2300,1500,1000]
    }
df=pd.DataFrame(technologies)
df





































