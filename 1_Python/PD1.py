# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 09:15:46 2023

@author: Atharv
"""
import pandas as pd
pd.__version__

##################creating dataframes######################
#1.List
import pandas as pd
tech=[["Spark",2000000,"30days"],
      ["pandas",300000,"40days"]]
df=pd.DataFrame(tech)
df
##################################
#giving name to columns and rows
column_name=['courses','fee','duration']
row_label=['a','b']
df=pd.DataFrame(tech,columns=column_name,index=row_label)
print(df)
##################################
#checking datatype of columns
df.dtypes
#assign datatype to columns
types={'courses':str,'fee':float,'duration':str}
df.dtypes

#2.Dictionary
tech={'Courses':['spark','hadoop','pyspark'],
      'Fee':[2999999,2999888,300000],
      'duration':['30days','40days','50days'],
      'Discount':[3099,3900,4000]     
 }
df=pd.DataFrame(tech)
df
###################################
#Convert dataframe to csv
df.to_csv('data_file.csv')
###################################
#convert all ype to best possible tyoe
tech={'Courses':['spark','hadoop','pyspark','C','C++','Python','R'],
      'Fee':[2999999,2999888,300000,4000,98877,3425,7654],
      'duration':['30days','40days','50days','34days','54days','53days','65days'],
      'Discount':[3099,3900,4000,6785,5463,876,546]     
 }
df=pd.DataFrame(tech)
print(df.dtypes)

df2=df.convert_dtypes()
print(df2.dtypes)
########################################
#change all columns to same type
df=df.astype(str)
print(df.dtypes)
########################################
#Change type for one or multiple columns
df=df.astype({"Courses":str,"Fee":int,"Discount":float})
print(df.dtypes)
#########################################
#convert data type for all columns in a list
df=pd.DataFrame(tech)
df.dtypes
cols=['Fee','Discount']
df[cols]=df[cols].astype(float)
df[cols].dtypes
df.dtypes

df=pd.DataFrame(tech)
df.dtypes
cols=['Courses','duration']
df[cols]=df[cols].astype(str)
df[cols].dtypes
df.dtypes
###################################################
#Ignoreerror
df=df.astype({"Courses":int},errors='ignore')
df.dtypes
###################################################
#Raise/generate  eror
df=df.astype({"Courses":int},errors='raise')
df.dtypes
#####################################################
#Convert feed column to numeric type
df=df.astype(str)
print(df.dtypes)
df['Fee']=pd.to_numeric(df['Fee'])
df.dtypes
####################################################
technologies={
    'courses':["spark","pyspark","Hadoop","Python","English","Marathi"],
    'Fee':[20000,25000,26000,50000,23000,60000],
    'Duration':['30days','40days','50days','40days','20days','10days'],
    'Discount':[1000,2300,1500,1000,200,100]
    }
row_labels = ['r0','r1','r2','r3','r4','r5']
df = pd.DataFrame(technologies, index = row_labels)
df
df=pd.DataFrame(technologies,index=row_labels)
#assign new header by setting new column names
df.columns=['A','B','C','D']
df
#delete rows by label
df1=df.drop(['r1','r2'])
df1
#Delete row by position/index
df2=df.drop(df.index[[1,3]])
df2
#delete rows by index  range
df3=df.drop(df.index[2:])
df3
#when you have default index for rows
df=pd.DataFrame(technologies)
df1=df.drop(0)
df1
df=pd.DataFrame(technologies)
df1=df.drop([0,3])#it will delete row 0 and row 3
df1
df2=df.drop(range(0,2))#it will delete row 0 and 1
df2
#################################################
technologies={
    'courses':["spark","pyspark","Hadoop","Python","English","Marathi"],
    'Fee':[20000,25000,26000,50000,23000,60000],
    'Duration':['30days','40days','50days','40days','20days','10days'],
    'Discount':[1000,2300,1500,1000,200,100]
    }
df=pd.DataFrame(technologies)
df
#########################################################
#drop column
#drop  column by name
df1=df.drop(['Fee'],axis=1)
df1
#xplicitely using parameter name 'label'
df2=df.drop(labels=['Fee'],axis=1)
df2 
#insrtead of label use columns
df2=df.drop(columns=['Fee'],axis=1)
df2 
#drop column by index
df3=df.drop(df.columns[1],axis=1)
df3
#using inplace=True
df
df.drop(df.columns[2],axis=1,inplace=True)
df
#########################################################
#multiple  column deletion  using label
df=pd.DataFrame(technologies)
df2=df.drop(['Fee','Duration'],axis=1)
df2
#by index
df2=df.drop(df.columns[[1,2]],axis=1)
df2
#delete using list
df=pd.DataFrame(technologies)
lisCol=['Fee','Discount']
df2=df.drop(lisCol,axis=1)
df2
#inplace=True
df.drop(df.columns[2],axis=1,inplace=True)
df
