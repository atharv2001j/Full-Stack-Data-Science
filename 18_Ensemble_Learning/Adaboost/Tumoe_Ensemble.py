# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 16:37:00 2024

@author: Atharv Joshi
"""
'''
Business Objective:

Maximize : The Correct classification of the dataset information wheher
the person having tumor or not by classifying and checking the parameters
values

Minimize : The false prediction of the data i.e the tumor prediction
so the correct prescription should be taken from the patient side

Business Contraints : The information regarding the tumor should be secure 
so the mishandling of the data will be less.
'''
'''
Data Dictionary:
    
all the columns except the Diagonis all are the numeric columns 

'''

################################################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from scipy.stats import skew

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report

data=pd.read_csv("Tumor_Ensemble.csv")

#Data information
data.head()
data.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 569 entries, 0 to 568
Data columns (total 32 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   id                 569 non-null    int64  
 1   diagnosis          569 non-null    object 
 2   radius_mean        569 non-null    float64
 3   texture_mean       569 non-null    float64
 4   perimeter_mean     569 non-null    float64
 5   area_mean          569 non-null    float64
 6   smoothness_mean    569 non-null    float64
 7   compactness_mean   569 non-null    float64
 8   concavity_mean     569 non-null    float64
 9   points_mean        569 non-null    float64
 10  symmetry_mean      569 non-null    float64
 11  dimension_mean     569 non-null    float64
 12  radius_se          569 non-null    float64
 13  texture_se         569 non-null    float64
 14  perimeter_se       569 non-null    float64
 15  area_se            569 non-null    float64
 16  smoothness_se      569 non-null    float64
 17  compactness_se     569 non-null    float64
 18  concavity_se       569 non-null    float64
 19  points_se          569 non-null    float64
 20  symmetry_se        569 non-null    float64
 21  dimension_se       569 non-null    float64
 22  radius_worst       569 non-null    float64
 23  texture_worst      569 non-null    float64
 24  perimeter_worst    569 non-null    float64
 25  area_worst         569 non-null    float64
 26  smoothness_worst   569 non-null    float64
 27  compactness_worst  569 non-null    float64
 28  concavity_worst    569 non-null    float64
 29  points_worst       569 non-null    float64
 30  symmetry_worst     569 non-null    float64
 31  dimension_worst    569 non-null    float64
dtypes: float64(30), int64(1), object(1)
memory usage: 142.4+ KB
'''

data.isna().sum()
'''
Out[40]: 
id                   0
diagnosis            0
radius_mean          0
texture_mean         0
perimeter_mean       0
area_mean            0
smoothness_mean      0
compactness_mean     0
concavity_mean       0
points_mean          0
symmetry_mean        0
dimension_mean       0
radius_se            0
texture_se           0
perimeter_se         0
area_se              0
smoothness_se        0
compactness_se       0
concavity_se         0
points_se            0
symmetry_se          0
dimension_se         0
radius_worst         0
texture_worst        0
perimeter_worst      0
area_worst           0
smoothness_worst     0
compactness_worst    0
concavity_worst      0
points_worst         0
symmetry_worst       0
dimension_worst      0
dtype: int64
'''
# The dataset does not contain any null value
############################################################
data.dtypes
'''
id                     int64
diagnosis             object
radius_mean          float64
texture_mean         float64
perimeter_mean       float64
area_mean            float64
smoothness_mean      float64
compactness_mean     float64
concavity_mean       float64
points_mean          float64
symmetry_mean        float64
dimension_mean       float64
radius_se            float64
texture_se           float64
perimeter_se         float64
area_se              float64
smoothness_se        float64
compactness_se       float64
concavity_se         float64
points_se            float64
symmetry_se          float64
dimension_se         float64
radius_worst         float64
texture_worst        float64
perimeter_worst      float64
area_worst           float64
smoothness_worst     float64
compactness_worst    float64
concavity_worst      float64
points_worst         float64
symmetry_worst       float64
dimension_worst      float64
dtype: object
'''
# All the columns are numeric except the Diagnosis
#######################################################################

target=data["diagnosis"]
sns.countplot(x=target,palette='winter')
plt.xlabel("diagnosis")
#our data is evenly distributed. Atleast 200 are there in both choise
plt.figure(figsize=(16,8))
sns.heatmap(data.corr(),annot=True, cmap='YlGnBu',fmt='.2f')

#observations

#1) radius_mean ,texture_mean ,perimeter_mean  and area_mean,points_mean,radius_se are highly correlated to each other

sns.set_context('notebook', font_scale=1.2)
fig,ax=plt.subplots(2,figsize=(20,13))

plt.suptitle('Distribution of tumor patient based on area_mean and area_worst',fontsize=20)

ax1=sns.histplot(x='area_mean',data=data,hue='diagnosis',kde=True,ax=ax[0],palette='winter')
ax1.set(xlabel='area_mean',title='Distribution of Dtumor patient based on diagnosis')

ax2=sns.histplot(x='area_worst',data=data,hue='diagnosis',kde=True,ax=ax[1],palette='coolwarm')
ax2.set(xlabel='area_worst',title='Distribution of tumor patient based on diagnosis')

plt.show()

data.hist(bins=30,figsize=(20,15),color='#005b96');

#As we cans ee there are outliers in radius_mean, _texture_mean,concavity_mean,dimension_mean,texture_se

sns.boxplot(x=data["radius_mean"])
sns.boxplot(x=data["texture_mean"])
sns.boxplot(x=data["concavity_mean"])
sns.boxplot(x=data["dimension_mean"])
sns.boxplot(x=data["texture_se"])

#checking skewness

skew_df=pd.DataFrame(data.select_dtypes(np.number).columns,columns=['Feature'])
skew_df['Skew']=skew_df['Feature'].apply(lambda feature:skew(data[feature]))
skew_df['Absolute Skew']=skew_df['Skew'].apply(abs)
skew_df['Skewed']=skew_df['Absolute Skew'].apply(lambda x: True if x>0.5 else False)
skew_df

#area_se column is clearly skewed as we also saw in the histogram

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
data2.drop(['diagnosis_B'],axis=1,inplace=True)
data2.head()

from sklearn.preprocessing import LabelEncoder
le__Class_variable=LabelEncoder()

data['diagnosis']= le__Class_variable.fit_transform(data['diagnosis'])
data

#Splitting
data_f=data2.copy()
target=data['diagnosis']
target=target.astype(int)
target

X_train,X_test,y_train,y_test=train_test_split(data_f,target,test_size=0.2,stratify=target,random_state=42)

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
