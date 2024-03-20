# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 14:38:49 2024

@author: Atharv Joshi
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from scipy.stats import skew

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split,cross_val_predict,KFold
from sklearn.metrics import accuracy_score,classification_report,roc_auc_score,roc_curve


data=pd.read_csv("movies_classification.csv")

#data information
data.head()
data.info()
data.isna().sum()
data.columns
#EDA
target=data['Start_Tech_Oscar']
sns.countplot(x=target,palette='winter')
plt.xlabel("Oscar Rate")
#our data is evenly distributed atleast 200 are there is both choice
plt.figure(figsize=(16,8))
sns.heatmap(data.corr(),annot=True,cmap='YlGnBu',fmt='.2f')

#observation
#1. lead_actor_Rating, Lead_Acctress_rating , Director_rating and predictoion

sns.countplot(x='Genre', data=data,hue='Start_Tech_Oscar',palette='pastel')
plt.title('O chance based on Ticket Class',fontsize=10);

#observation
#here are more chance of getting Oscar in Drama , comedey  and action genre
sns.countplot(x='3D_available',data=data,hue='Start_Tech_Oscar',palette='pastel')
plt.title('O chance based on Ticket Class', fontsize=10);
#observation
#It is clear that
sns.set_context('notebook',font_scale=1.2).fig, ax=plt.subplot(2,figsize=(20,13))


plt.suptitle('Distraction of Twitter_Hostage and collection based on target variable',fontsize=20)
ax1=sns.histplot(x='Twitter_hastags',data=data,hue='Start_Tech_Oscar',kde=True,ax=ax[0],palette='winter')
ax1.set(xlable='Twitter_hostage',title='Distribution of Twitter_hostags based on target variable')

ax2=sns.histplot(x='Collection',data=data,hue='Start_Tech_Oscar',kde=True,ax=ax[1],palette='viridis')
ax2.set(xlabel='Collection',title='Distribution of Fare based on target variable')

plt.show()

data.hist(bins=30,figsize=(20,15),color='#005b96')

#as we can see there are outlier in Twitter_hastags , marketting and so on
sns.boxplot(x=data['Twitter_hostags'])
sns.boxplot(x=data["Marketing_expense"])
sns.boxplot(x=data["Time_taken"])
sns.boxplot(x=data["Avg_age_actors"])

#Write code for winsorizor
from feature_engine.outliers import Winsorizer

winsor=Winsorizer(capping_method='iqr',
                  tail='both',
                  fold=1.5,
                  variables=['Twitter_hastags'])

data_t1=winsor.fit_transform(data[['Twitter_hastags']])
sns.boxplot(data['Twitter_hastags'])

sns.boxplot(data_t1['Twitter_hastags'])
# for Marketting_expenses

winsor=Winsorizer(capping_method='iqr',
                  tail='both',
                  fold=1.5,
                  variables=['Time_taken'])

data_t2=winsor.fit_transform(data[['Time_taken']])
sns.boxplot(data['Time_taken'])

sns.boxplot(data_t2['Time_taken'])

# For the Time_taken


winsor=Winsorizer(capping_method='iqr',
                  tail='both',
                  fold=1.5,
                  variables=['Marketing expense'])

data_t=winsor.fit_transform(data[['Marketing expense']])
sns.boxplot(data['Marketing expense'])

sns.boxplot(data_t['Marketing expense'])

# for the Avg_age_actors

winsor=Winsorizer(capping_method='iqr',
                  tail='both',
                  fold=1.5,
                  variables=['Avg_age_actors'])

data_t=winsor.fit_transform(data[['Avg_age_actors']])
sns.boxplot(data['Avg_age_actors'])

sns.boxplot(data_t['Avg_age_actors'])


#checking skeweness

skew_df=pd.DataFrame(data.select_dtypes(np.number).columns,columns=['Feature'])
skew_df['Skew']=skew_df['Feature'].apply(lambda feature: skew(data[feature]))
skew_df['Absolute Skew']=skew_df['Skew'].apply(abs)
skew_df['Skewed']=skew_df['Absolute Skew'].apply(lambda x:True if x>=0.5 else False)
skew_df


# Total charges columns is clearly skewed as we also saw in the histogram
# Encoding

data1=data.copy()
data1=pd.get_dummies(data1)
data1.head()

# Scaling 
data2 = data1.copy()
sc = StandardScaler()
data2[data1.select_dtypes(np.number).columns] = sc.fit_transform(data2[data1.select_dtypes(np.number).columns])
data2.drop(['Start_Tech_Oscar'],axis=1,inplace=True)
data2.head()

#splitting
data_f = data2.copy()
target = data['Start_Tech_Oscar']
target = target.astype(int)
target
x_train,x_test,y_train,y_test=train_test_split(data_f,target,test_size=0.2,stratify=target,random_state=42)

# Modelling
from sklearn.ensemble import AdaBoostClassifier

ada_clf=AdaBoostClassifier(learning_rate=0.02,n_estimators=5000)
ada_clf.fit(x_train,y_train)

from sklearn.metrics import accuracy_score,confusion_matrix

confusion_matrix(y_test,ada_clf.predict(x_test))
accuracy_score(y_test,ada_clf.predict(x_test))
