# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 09:31:03 2023

@author: Atharv
"""
import pandas as pd

df=pd.read_csv('ethnic diversity.csv')

df


#check shape
df.shape

#check columns
df.columns

# check  datatype
df.dtypes

# pairplot
import seaborn as sns

sns.pairplot(df)

# Five nummber summary
df.describe()

# finding null value
df.isna()

#Convert salaries column datatype into int
salaries=df.Salaries.astype(int)
salaries.dtype

# the age columns in also  in int if we want data in continuous form
# so will convert it into float

age=df.age.astype(float)
age.dtype

age

########################################################################
#2. finding duplicates

df_new=pd.read_csv('education.csv')
df_new


duplicate=df_new.duplicated()
duplicate

sum(duplicate)
#Try on another dataset
df_new1=pd.read_csv('mtcars_dup.csv')
df_new1

duplicate1=df_new1.duplicated()
duplicate1
sum(duplicate1)

#There are 3 duplicates on the dataset
#So to remove the duplicates we will use drop_duplicate function
df_new2=df_new1.drop_duplicates()
df_new2

####################################################################3
#3. outlier Analysis 

import seaborn as sns
#Finding an outlier 
sns.boxplot(df['Salaries'])
#threre is an outliers
sns.boxplot(df['age'])
#threre is no ouliers


#lets us calculate IQR
IQR=df.Salaries.quantile(0.75)-df.Salaries.quantile(0.25)
IQR


#Calculate lower and upper limit
lower_limit=df.Salaries.quantile(0.25)-1.5*IQR
lower_limit

upper_limit=df.Salaries.quantile(0.75) + 1.5 * IQR
upper_limit
#######################################################################3

#4. Trimming

import numpy as np

outlier_df=np.where(df.Salaries>upper_limit,True,np.where(df.Salaries < lower_limit,True,False))
outlier_df

#remove the outlier
df_trimmed=df.loc[~outlier_df]
df_trimmed.shape

########################################################################
#5. Replacement techniue

df_replaced=pd.DataFrame(np.where(df.Salaries>upper_limit,upper_limit,np.where(df.Salaries < lower_limit,lower_limit,df.Salaries)))

df_replaced

sns.boxplot(df_replaced[0])

#########################################################################
# 6. Winsorizor
from feature_engine.outliers import Winsorizer

winsor=Winsorizer(capping_method='iqr',
                  tail='both',
                  fold=1.5,
                  variables=['Salaries'])

df_t=winsor.fit_transform(df[['Salaries']])
sns.boxplot(df['Salaries'])

sns.boxplot(df_t['Salaries'])

########################################################################3

# 7. zero variance and near zero variannca
import pandas as pd
df=pd.read_csv('ethnic diversity.csv')
df.var()
#Here zip and EmpID are nominal data
#here all the variance are not havinng zero variance or near zero variance


df.var()==0

#There is no column having zero varriance 

df.var(axis=0)==0

df.var(axis=1)==0

##################################################################

#8. Discritzation or Binning

import pandas as pd
import numpy as np

data=pd.read_csv('ethnic diversity.csv')
data

data.head()

data.info()
#it gives size,null values,data types,rows,columns,and column dat

data.describe()
#applicable only for numerical columns

#Uniform Stratergy
data['Salaries_new']=pd.cut(data['Salaries'],bins=[min(data.Salaries),data.Salaries.mean(),max(data.Salaries)],labels=['low','high'])
data.Salaries_new.value_counts()

# Quantile Stratergy
data['Salaries_new']=pd.cut(data['Salaries'],bins=[min(data.Salaries),data.Salaries.quantile(0.25),data.Salaries.mean(),data.Salaries.quantile(0.75),max(data.Salaries)],labels=['grp1','grp2','grp3','grp4'])
data.Salaries_new.value_counts()

#It will categorize the data present in columns with the labels by 
# matching the labels then we will visulaize the data

#########################################################################################################################################

# 9.  Dummy variable Creation
# we can convert nominal data and  ordinal data into dummy variable

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('animal_category.csv')
df.shape

df.drop(['Index'],axis=1,inplace=True)

df

df_new=pd.get_dummies(df)
#It will create dummy columns and convert it into numerical value

df_new.shape

# we are geting two columns for homely and gender ,so we can delete one 
# column from both

df_new.drop(['Gender_Male','Homly_Yes'],axis=1,inplace=True)
df_new.shape


df_new.rename(columns={'Gender_Female':'Gender','Homly_No':'Homly'})

#############################
#Use of ethnic dataset 

df=pd.read_csv('ethnic diversity.csv')
df.shape

df.head()
df.columns
df.dtypes

df.drop(['EmpID','Salaries','age'],axis=1,inplace=True)
 # we have to drop the three columns because they already in numeric form
 
df_new=pd.get_dummies(df)
df_new.columns
df_new.shape

###############################################################################

# 10. One hot encoding

import pandas as pd

from sklearn.preprocessing import OneHotEncoder
enc=OneHotEncoder()
df=pd.read_csv('ethnic diversity.csv')
df.columns

#We have salaries and age column in numeric form thenrearrange it 
# so we can preprocess further

df=df[['Salaries','age','Position','State','Sex','MaritalDesc','CitizenDesc','EmploymentStatus','Race','Employee_Name','EmpID','Zip','Department']]

# we want only nominal and ordinal data for preprocessing so we exclude the 
#  alredy nummeric form column 
enc_df=pd.DataFrame(enc.fit_transform(df.iloc[:,2:]).toarray())
enc_df.columns

######################################################################################

# 11. label Encoder 
# in this we have to convert the nominal and ordinal columns 
# into the numerical one by one 

from sklearn.preprocessing import LabelEncoder

labelencoder=LabelEncoder()

#split the data into imput and output variables
X=df.iloc[:,0:9]
y=df['Race']

df.columns

# we have sex ,maritaDesc,CitizenDesc column we want to convert to label encoder
X['Sex']=labelencoder.fit_transform(X['Sex'])
X['MaritalDesc']=labelencoder.fit_transform(X['MaritalDesc'])
X['CitizenDesc']=labelencoder.fit_transform(X['CitizenDesc'])

# label encodery
y=labelencoder.fit_transform(y)

# this is going to create an array we have to convert back
# into dataFrame

y=pd.DataFrame(y)

# conca the input and output variables

new_df=pd.concat([X,y],axis=1)

#if ypu explorer , y do not have column name
# hence rename the column

new_df= new_df.rename(columns={0:'Race'})

new_df

##################################################################################





