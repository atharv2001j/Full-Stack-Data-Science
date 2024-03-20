# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 16:20:25 2024

@author: Atharv Joshi
"""
'''
Business Objective :

Maximize : The Strength of the password we have to maximize as possible as so
the hacker cannot crack or identify the pattern of the password

Minimize : The weak password count 

Business Contraints : The password security should be maintain so the userrs 
or client should trust on us.

'''
'''
Data Dictionary:

The dataset contain the two columns one is nominal columns that contain the 
values of the password and and another column contain the categorical column 
which categories whether the pasword is strong or not.
'''

################################ EDA ######################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from scipy.stats import skew

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report

data=pd.read_excel("Ensemble_Password_Strength.xlsx")

#Data information
data.head()
data.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1999 entries, 0 to 1998
Data columns (total 2 columns):
 #   Column               Non-Null Count  Dtype  
---  ------               --------------  -----  
 0   characters           1999 non-null   object 
 1   characters_strength  1999 non-null   float64
dtypes: float64(1), object(1)
memory usage: 31.4+ KB
'''

data.isna().sum()
'''
Out[35]: 
characters             0
characters_strength    0
dtype: int64
'''
# There will be no any null value inside the dataset so we canprocess further
###############################################

target=data["characters_strength"]
sns.countplot(x=target,palette='winter')
plt.xlabel("Password Strength")
#our data is oddly distributed. Atleast 250 are there in both choise
plt.figure(figsize=(16,8))
sns.heatmap(data.corr(),annot=True, cmap='YlGnBu',fmt='.2f')

#####################################################################
# Encode the data which is not a numeric

from sklearn.preprocessing import LabelEncoder
le_characters=LabelEncoder()

data['characters'] = data['characters'].astype(str)
data['characters']= le_characters.fit_transform(data['characters'])
data

sns.set_context('notebook', font_scale=1.2)
fig,ax=plt.subplots(1,figsize=(20,13))

plt.suptitle('Distribution of characters based on characters_strength',fontsize=20)

ax1=sns.histplot(x='characters',data=data,hue='characters_strength',kde=True,ax=ax[0],palette='winter')
ax1.set(xlabel='Twitter_hastags',title='Distribution of characters based on characters_strength')


plt.show()

data.hist(bins=30,figsize=(20,15),color='#005b96');
#####################################################################################
#  Check the skewness of in dataset for the better understand

skew_df=pd.DataFrame(data.select_dtypes(np.number).columns,columns=['Feature'])
skew_df['Skew']=skew_df['Feature'].apply(lambda feature:skew(data[feature]))
skew_df['Absolute Skew']=skew_df['Skew'].apply(abs)
skew_df['Skewed']=skew_df['Absolute Skew'].apply(lambda x: True if x>0.5 else False)
skew_df
############################################################################

#Total Charges column is clearly skewed as we also saw in the histogram

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
data2.drop(['characters_strength'],axis=1,inplace=True)
data2.head()
############################################################################
#Splitting
data_f=data2.copy()
target=data['characters_strength']
target=target.astype(int)
target

X_train,X_test,y_train,y_test=train_test_split(data_f,target,test_size=0.2,stratify=target,random_state=42)

#############################################################################
#Modeling
from sklearn.ensemble import  AdaBoostClassifier

ad_clf=AdaBoostClassifier(learning_rate=0.02,n_estimators=5000)
ad_clf.fit(X_train,y_train)

from sklearn.metrics import confusion_matrix

#Evaluation on testing data
confusion_matrix(y_test, ad_clf.predict(X_test))
accuracy_score(y_test, ad_clf.predict(X_test))

#Evalution on Training data
accuracy_score(y_train,ad_clf.predict(X_train))


