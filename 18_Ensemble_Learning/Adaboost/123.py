# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 03:45:03 2024

@author: Atharv Joshi


#DATA DICTIONARY

Company: Name of the chocolate company.
Name: Name of the chocolate product.
REF: Reference number or identifier for each chocolate product.
Review: Review metric or score for each chocolate product.
Cocoa_Percent: Percentage of cocoa in each chocolate product.
Company_Location: Location of the chocolate company.
Rating: Numerical rating for each chocolate product.
Bean_Type: Type of cocoa bean used in each chocolate product.
Origin: Origin of the cocoa beans used in each chocolate product.
Rating_catogorical: Categorical ratings for each chocolate product.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from scipy.stats import skew

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report

data=pd.read_excel("Coca_Rating_Ensemble.xlsx")

data['Rating_catogorical'] = pd.qcut(data['Rating'], q=2, labels=['Good', 'bad'])

data


#Data information
data.head()
data.info()
data.isna().sum()
#There is  null value present in column Bean_Type, Origin in given dataset

#EDA
target=data["Rating_catogorical"]
sns.countplot(x=target,palette='winter')
plt.xlabel("Coca_rating")
#our data is evenly distributed. Atleast 600 are there in both choise
plt.figure(figsize=(16,8))
sns.heatmap(data.corr(),annot=True, cmap='YlGnBu',fmt='.2f')

#observations

#1) REF ,Review are highly correlated to each other


sns.set_context('notebook', font_scale=1.2)
fig,ax=plt.subplots(2,figsize=(20,13))

plt.suptitle('Distribution of cocoa bean production based on Rating_catogorical',fontsize=20)

ax1=sns.histplot(x='REF',data=data,hue='Rating_catogorical',kde=True,ax=ax[0],palette='winter')
ax1.set(xlabel='REF',title='Distribution of cocoa bean production based on Rating_catogorical')

ax2=sns.histplot(x='Cocoa_Percent',data=data,hue='Rating_catogorical',kde=True,ax=ax[1],palette='coolwarm')
ax2.set(xlabel='Cocoa_Percent',title='Distribution of cocoa bean production based on Rating_catogorical')

plt.show()

data.hist(bins=30,figsize=(20,15),color='#005b96');

#As we cans ee there are outliers in Cocoa_Percent

sns.boxplot(x=data["Cocoa_Percent"])



#checking skewness

skew_df=pd.DataFrame(data.select_dtypes(np.number).columns,columns=['Feature'])
skew_df['Skew']=skew_df['Feature'].apply(lambda feature:skew(data[feature]))
skew_df['Absolute Skew']=skew_df['Skew'].apply(abs)
skew_df['Skewed']=skew_df['Absolute Skew'].apply(lambda x: True if x>0.5 else False)
skew_df

#Cocoa_Percent column is clearly skewed as we also saw in the histogram

for column in skew_df.query("Skewed==True")['Feature'].values:data[column]=np.log1p(data[column])

data.head()
#Encoding
data1=data.copy()
data1=pd.get_dummies(data1)
data1.head()
#Scaling
data2 = data1.copy()
sc=StandardScaler()
data2[data1.select_dtypes(np.number).columns]=sc.fit_transform(data2[data1.select_dtypes(np.number).columns])
data2.drop(['Rating_catogorical_Good'],axis=1,inplace=True)
data2.head()

from sklearn.preprocessing import LabelEncoder
le__Class_variable=LabelEncoder()

data['Rating_catogorical']= le__Class_variable.fit_transform(data['Rating_catogorical'])
data

#Splitting
data_f=data2.copy()
target=data['Rating_catogorical']
target=target.astype(int)
target

X_train,X_test,y_train,y_test=train_test_split(data_f,target,test_size=0.2,stratify=target,random_state=42)

#Modeling
from sklearn.ensemble import  AdaBoostClassifier

ad_clf=AdaBoostClassifier(learning_rate=0.02,n_estimators=5000)
ad_clf.fit(X_train,y_train)

from sklearn.metrics import accuracy_score,confusion_matrix

#Evaluation on testing data
confusion_matrix(y_test, ad_clf.predict(X_test))
accuracy_score(y_test, ad_clf.predict(X_test))

#Evalution on Training data
accuracy_score(y_train,ad_clf.predict(X_train))

from sklearn.metrics import accuracy_score, confusion_matrix

##Evaluation on testing data
