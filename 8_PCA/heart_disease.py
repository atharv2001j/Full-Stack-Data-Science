# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 11:25:30 2023

@author: Atharv Joshi
"""

'''

1. Business problem

Business Objective:

Maximize:  Reduce the number of cases where the model 
fails to identify individuals with heart disease.

Minimize:  Accuracy, sensitivity, specificity, or an appropriate 
combination of these metrics depending on the business priorities.

Constraints: Maintaining the result,Data Privacy and Ethics

'''

'''
DataFrame:

 Sure, I'll categorize the columns into nominal and ordinal based on their characteristics. 

### Nominal Columns:

1.'sex': 
   - Description: Nominal variable representing gender.
   - Categories: 0 = Female, 1 = Male

2.'cp' (chest pain type):
   - Description: Nominal variable representing the type of chest pain.
   - Categories: 
      - 0 = Typical angina
      - 1 = Atypical angina
      - 2 = Non-anginal pain
      - 3 = Asymptomatic

3. 'fbs' (fasting blood sugar):
   - *Description:* Nominal variable indicating whether fasting blood sugar is greater than 120 mg/dl.
   - *Categories:* 0 = False, 1 = True

4. **'restecg' (resting electrocardiographic results):**
   - Description: Nominal variable representing resting electrocardiographic results.
   -Categories:
      - 0 = Normal
      - 1 = ST-T wave abnormality
      - 2 = Left ventricular hypertrophy

5. 'exang' (exercise induced angina):
   - Description: Nominal variable indicating whether angina was induced by exercise.
   - Categories: 0 = No, 1 = Yes

6. 'slope':
   - Description: Nominal variable representing the slope of the peak exercise ST segment.
   -Categories:
      - 0 = Upsloping
      - 1 = Flat
      - 2 = Downsloping

7. 'ca' (number of major vessels colored by fluoroscopy):
   - Description: Nominal variable indicating the number of major vessels colored by fluoroscopy.
   - Categories: 0, 1, 2, 3, 4

8. 'thal':
   - Description: Nominal variable representing Thallium stress test result.
   - Categories:
      - 0 = Normal
      - 1 = Fixed defect
      - 2 = Reversible defect

9. 'target':
   - Description: Nominal variable indicating the presence or absence of heart disease.
   - Categories: 0 = No heart disease, 1 = Heart disease

### Ordinal Columns:

1. 'age':
   - Description:*Ordinal variable representing age.
   - Order: Increasing age.

2.'trestbps' (resting blood pressure):
   - Description: Ordinal variable representing resting blood pressure.
   - Order: Increasing resting blood pressure.

3. 'chol' (serum cholesterol):
   - Description: Ordinal variable representing serum cholesterol levels.
   - Order: Increasing cholesterol levels.

4. 'thalach' (maximum heart rate achieved):
   - Description: Ordinal variable representing the maximum heart rate achieved.
   - Order: Increasing maximum heart rate.

5. 'oldpeak' (ST depression induced by exercise relative to rest):
   - Description: Ordinal variable representing ST depression induced by exercise relative to rest.
   - Order: Increasing ST depression.


'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_csv('heart disease.csv')

# EDA 
df.columns
'''
Index(['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
       'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target'],
      dtype='object')
'''
######################

df.head
#######################
df.dtypes
'''
age           int64
sex           int64
cp            int64
trestbps      int64
chol          int64
fbs           int64
restecg       int64
thalach       int64
exang         int64
oldpeak     float64
slope         int64
ca            int64
thal          int64
target        int64
dtype: object

The all the columns of Numeric Type
'''
#########################
df.shape
# The dataset contain the 303 rows and 14 columns
########################
a=df.describe()
a
# Observe that the diffrence between mean and meadian is nearly same but have somewhat
# diffrenece and also the standard deviation is not near to zero its value is more

########################
# Check for the null values

n=df.isnull()
n.sum()
# There is no null value is present in the dataset
#######################
# Check for the outlier
# Plot a boxplot to check whether it contain an outlier or not

import seaborn as sns
sns.boxplot(df)
# the trestbps,chol and thalach column contain the outlier
####################
sns.histplot(df)
#######################
corr=df.corr()
sns.heatmap(corr)
# As there is 2-3 columns showing the darkcolour so they arestrictly co-related 
# to each other
######################
# So there is outlier is present and also the the column shows skewness propery
# and there is scale difference in mean and std so we use standardization technique as we are going to use 
# PCA

# Standardization
# initialize the scalar
from sklearn.preprocessing import StandardScaler
scalar=StandardScaler()
df=scalar.fit_transform(a)
dataset=pd.DataFrame(df)
res=dataset.describe()
# in the resvariable we will see that the mean value is almost value 
#Standard deviation is zero

#########################

# Model Building

##Hierarchical Clusering

#For visualzing the cluster of  the above dataframe we  have to draw
# Dendodron first then we cluster the datapoints

from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch

# linkage function give the hierarchical and Agglomotive clustering
 

z=linkage(dataset,method='complete',metric='euclidean')

plt.figure(figsize=(15,8))
plt.title('Hierarchical Clustering')
plt.xlabel('Index')
plt.ylabel('Disance')
#sch is help to draw 
sch.dendrogram(z,leaf_rotation=0,leaf_font_size=10)
plt.show()

#appying agglomerative clustering choose 1 as a cluster from dendogram

# In dedrogram is not show the clustering it only shows how many clusters are there

from sklearn.cluster import AgglomerativeClustering
h_complete=AgglomerativeClustering(n_clusters=2,linkage='complete',affinity='euclidean').fit(dataset)

#apply labels to the cluster
h_complete.labels_
# so these all are in the form of array we have to convert the Series
cluster_labels=pd.Series(h_complete.labels_)
# so these all are in the form of array we have to convert the Series
cluster_labels=pd.Series(h_complete.labels_)

df['clust']=cluster_labels
df

####### K-Means Clustering ###############
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

TWSS=[]
k=list(range(2,8))
for i in k:
    kmeans=KMeans(n_clusters=i)
    kmeans.fit(dataset)
    
    TWSS.append(kmeans.inertia_)
    
    '''
    kmeans inertia also known as sum odf sqares methos
    .It measures all the datapoints from the centroid of the point.
    it differentiate between observed value and predicted value
    '''
    
TWSS
# Plot a elbow curve
plt.plot(k,TWSS,'ro-')
plt.xlabel('No of clusers')
plt.ylabel('Total within SS')

model=KMeans(n_clusters=3)
model.fit(dataset)
model.labels_
mb=pd.Series(model.labels_)
type(mb)
df['clust']=mb
df.head()
d=df.iloc[:,[0,1,2]]
d


#################### PCA #####################

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale

df=pd.read_csv('heart disease.csv')
df
#Normalize the numeric data
uni_normal=scale(df)
uni_normal

pca=PCA(n_components=3)
pca_values=pca.fit_transform(uni_normal)

#The amount of variance that each PCA explain

var=pca.explained_variance_ratio_
var

#Commulative Variance
var1=np.cumsum(np.round(var,decimals=4)*100)
var1
#Variance plot for PCA component obtained
plt.plot(var1,color='red')
#PCA Scores
pca_values

pca_data=pd.DataFrame(pca_values)
pca_data.columns='comp0','comp1','comp2'

final=pd.concat([df.clust,pca_data],axis=1)

#Visualize the dataframe
ax=final.plot(x='comp0',y='comp1',kind='scatter',figsize=(12,8))
final[['comp0','comp1','clust']].apply(lambda x:ax.text(*x),axis=1)

####################################################################