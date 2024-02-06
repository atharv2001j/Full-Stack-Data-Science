# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 11:00:52 2024

@author: Atharv Joshi
"""

#Random forest_algorithm
import pandas as pd
import numpy as np
from sklearn.datasets import load_digits
digits=load_digits()            # this is the external dataset are load from load_digits
dir(digits)


df= pd.DataFrame(digits.data)
df.head()


df['target']=digits.target
df[0:12]

X=df.drop('target' , axis='columns')
y =df.target

from sklearn.model_selection import train_test_split
X_train,X_test, y_train,y_test= train_test_split(X,y,test_size=0.2)


from sklearn.ensemble import RandomForestClassifier
model= RandomForestClassifier(n_estimators=20)

#n_estimators of trees in the forest
model.fit(X_train,y_train)

model.score(X_test,y_test)
y_predicated=model.predict(X_test)
from sklearn.metrics import confusion_matrix
cm= confusion_matrix(y_test, y_predicated)
cm
 
# % matplotlib inline


import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10,7))
sns.heatmap(cm,annot=True)
plt.xlabel('Predicated')
plt.ylabel('Truth')

###################################################################
#check for the iris data set
from sklearn.datasets import load_iris
iris=load_iris()
dir(iris) 

df=pd.DataFrame(iris.data)
df.head()
df['target']=iris.target
df.head()
X=df.drop('target' , axis='columns')
y =df.target
from sklearn.model_selection import train_test_split
X_train,X_test, y_train,y_test= train_test_split(X,y,test_size=0.2)


from sklearn.ensemble import RandomForestClassifier
model= RandomForestClassifier()

#n_estimators of trees in the forest
model.fit(X_train,y_train)

model.score(X_test,y_test)
y_predicated=model.predict(X_test)
from sklearn.metrics import confusion_matrix
cm= confusion_matrix(y_test, y_predicated)
cm
 
# % matplotlib inline


import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10,7))
sns.heatmap(cm,annot=True)
plt.xlabel('Predicated')
plt.ylabel('Truth')
