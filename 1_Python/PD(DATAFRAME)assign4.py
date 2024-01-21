# -*- coding: utf-8 -*-
"""
Created on Mon May  8 19:08:14 2023

@author: atharv
"""
import pandas as pd
df=pd.read_csv("company_data.csv")
df

df.shape
df.size
df.columns
df.describe()
#Accessing one column
df1=df['Sales']
df1
#Acessing multiplle columns
df2=df[['Sales','Income']]
df2
#Accessing particular cell
df3=df['Sales'][2]
df3
#rename column names
df4=df.rename({'Sales':'SALES','Income':'INOME'},axis=1)
df4
#covert all the columns to possible datatypes
df5=df.convert_dtypes()
df5.dtypes
#Convert allcolumns into particular datatype
df5=df.astype(str)
df5.dtypes
#Convert the datatype of particular column
df6=df.astype({'Sales':str,'Income':str})
df6.dtypes
#convert the datatype of all elements present in list
lst=['Sales','CompPrice','Income']
df[lst]=df[lst].astype(str)
df[lst].dtypes
#ignore error
df7=df.astype({"Sales":str},errors='ignore')
df7
#Raised error
df8=df.astype({"Sales":str},errors='raised')
df8
#convert feed column to numeric
df['Sales']=pd.to_numeric(df['Sales'])
df
#Giving label to the rows
df9=df[:6]
df9
row_label=['r0','r1','r2','r3','r4','r5']
df10=pd.DataFrame(df9,index=row_label)
df10
#Delete row  by label
df11=df10.drop(['r0','r1'])
df11
#Delete row by index
df12=df.drop(df.index[1])
df12
df13=df.drop(df.index[[1,3]])
df13
#Delete index by index range
df14=df.drop(df.index[2:9])
df14
#Default index are availabe
df15=df.drop(0)
df15
#Delete multiple row
df16=df.drop([1,3])
df16
#drop column by colname
df17=df.drop(['Sales'],axis=1)
df17
#Drop miuliple column
df18=df.drop(['Sales','Income'],axis=1)
df18
#Drop column by index
df19=df.drop(df.columns[0],axis=1)
df19
#drop multiple columns by index name
df20=df.drop(df.columns[[0,1]],axis=1)
df20
#drop the columns in the list
lst=['Sales','Income']
df21=df.drop(lst,axis=1)
df21
#iloc
df22=df.iloc[1:3,2:5]
df22
df23=df.iloc[[1,2],[2,3]]
df23
#Select row by index
df2.iloc[2]             #select 2nd row
df.iloc[1:3]            #select first three rows
df.iloc[-1:]            #select last row
df.iloc[[2,3,4]]        #select particular row
df.iloc[:0]             #empty row
df.iloc[:1]             #slect first row
df.iloc[-3:]            #select last three row
df.iloc[::2]            #select alternate row
#Select rows by labels
df10
df10.loc['r1']
df10.loc[['r1','r2','r3']]
df10.loc['r1':'r4']
df10.loc['r0':'r4':2] #alernatte row
#Select random column
df23=df.iloc[:,[1]]
df23
#Select column between two columns
df24=df.loc[:,'Income':]
df24
df25=df.loc[:,:'Income']
df25
df26=df.loc[:,'Sales':'Income']
df26
#Add new column in DataFrame
lst=[12,12,13,14,13,19]
df27=df10.assign(Cost=lst)
df27.columns
#Derive new columns from exising columns
df28=df.assign(Discount=lambda x:x.Income * x.Population)
df28
#Add column to specfic position
df29=df10.insert(0,'Cost',lst)
print(df29)
#To get the number of rows
rows_count=len(df.index)
rows_count
rows_count=len(df.axes[0])
rows_count

#Calculate number of rows and number of columns
row_count=df.shape[0]
rows_count
row_count=df.shape[1]
row_count
#Apply function to specific column
def add_1000(x):
    return x+'1000'
df['Income']=df['Income'].apply(add_1000)
df['Income']

#apply lambdafunction to specific column
df['Sales']=df['Sales'].apply(lambda x:x+100.0)
df['Sales']
#using Transform
df30=df.transform(add_1000)
df30
#apply function aon single column using map()
def add_1000(x):
    return x+1000
df['Sales']=df['Sales'].map(add_1000)
df
#apply numpy inbuild functiion
import numpy as np
df['Sales']=df['Sales'].apply(np.square)
df['Sales']
#apply  numpy inbuild functions without using pandas feature
df['Sales']=np.square(df['Sales'])
df['Sales']    
#Use group by
df33=df.groupby(['Sales','Income']).sum()
df33
#Reset the index
df34=df.groupby(['Sales','Income']).sum().reset_index()
df34
#Shuffle the rows
df35=df.sample(frac=1)
df35
df36=df.sample(frac=1).reset_index()
df36
df37=df.sample(frac=1).reset_index(drop=True)
df37
