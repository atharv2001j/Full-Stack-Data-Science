# -*- coding: utf-8 -*-
"""
Created on Sat May 27 09:38:57 2023

@author: Atharv
"""
import pandas as pd

df = pd.read_csv('Data_Science_Attendance_Sheet2.csv')
df

df1 = df.rename(columns = {'Parjane Pranjal' : 'Pranjal', 'Game Saburi': 'Game'})
df1

##############################################################

import numpy as np

transpose_df = df1.transpose()
print(transpose_df)

transpose_df.head()

transpose_df['datum':'Pranjal']
transpose_df.dropna()
transpose_df['datum':'Pranjal'].to_csv('att.csv')


##########################################
df=pd.read_excel('Coca_Rating_Ensemble.xlsx')
df
df.dtypes
df2=df.convert_dtypes()
df2.dtypes
######
df3=df.astype(str)
df3.dtypes
############
df4=df.astype({'REF':str})
df4.dtypes
############
cols=['Company','Name','Company_Location','Bean_Type','Origin']
df5=df[cols].astype(str)
df5.dtypes
#################
df6=df.astype({'Company':float},errors='ignore')
df6.dtypes
#################
df6=df.astype({'Company':float},errors='raised')
df6.dtypes
###################
df.columns
df.columns.values
df.index
df.dtypes
#######################
df['Company']
##################
df[['Company','Origin']]
################
df[:6]
############
df['Company'][3]
#################
df5=df['Rating']-1
df5
###########3
df.describe()
#mean=1035.904735
#std=553.8863665
####################
df6=df.rename({'Company':'COMPANY'},axis=1)
df6
####################
df.rename({'Company':'Co'},inplace=True)
df
###########
df3=df.drop([1,3])
df3
##############
df3=df.drop(df.index[[2,4]])
df3
##############
df4=df.drop(df.index[2:])
df4
#################
df5=df.drop(['Company'],axis=1)
df5
##############
df.drop(df.columns[[2]],axis=1,inplace=True)
df
##############3
lisCol=['Name','Rating']
df6=df.drop(lisCol,axis=1)
df6
################
import pandas as pd
import numpy as np
df.columns
df.loc[:,'Rating':]
###############
import random
row_label=['r0','r1','r2','r3','r4','r5']
df8=pd.DataFrame(df,[random.choice(row_label) for i in range(405)])
df8
#####################
#different ways to access row by index
df.iloc[2]             #select 2nd row
df.iloc[1:3]            #select first three rows
df.iloc[-1:]            #select last row
df.iloc[[2,3,4]]        #select particular row
df.iloc[:0]             #empty row
df.iloc[:1]             #slect first row
df.iloc[-3:]            #select last three row
df.iloc[::2]    
######################
df8.loc['r1']
df8.loc[['r1','r2','r3']]
#######################
df.dtypes
df9=df.query('Rating==3.75')
df9
#################
df.query('Rating!=3.75')
##################
#using numpy function on single column
#using dataframe.apply() and [] operator
import numpy as np
df10=df['Rating'].apply(np.square)
df10
#######################################
#using Numpy.square() method
#using numpy.square() and [] operator
df11=np.square(df['Rating'])
df11

#groupby() function
#for single column
df=pd.read_excel('Coca_Rating_Ensemble.xlsx')
df12=df.groupby(['Rating']).sum()
df12
##########################################3

#group by multiple columns
df13=df.groupby(['REF','Review']).sum()
df13
######################################
#add index to the groupby data
#add row index to the group by result
df14=df.groupby(['REF','Review']).sum().reset_index()
df14
################################

df=pd.read_excel('Coca_Rating_Ensemble.xlsx')
df.columns

#get the list of all column names from header
columns_header=list(df.columns.values)
print("The column Header:",columns_header)

#####################################
#using list(df) to get the column headers as a list
column_headers=list(df.columns)
column_headers

#using list(df) to get the list of all column names
column_headers=list(df)
column_headers
###################################

#pandas shuffle Dataframe rows
#shuffle the DataFrame rows and return all rows

df15= df.sample(frac=1)
df15
#######################################

#create a new index starting from zero
df16=df.sample(frac=1).reset_index()
df16
#########################

#Drof shuffle index
df17=df.sample(frac=1).reset_index(drop=True)
df17

