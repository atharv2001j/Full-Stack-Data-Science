# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 14:59:46 2024

@author: Atharv Joshi
"""
import pandas as pd
df=pd.read_csv('movies_classification.csv')

df.head()
df.info()
#

# N-1 dummy variable will be created for a category
df=pd.get_dummies(df,columns=['3D_available','Genre'],drop_first=True)

df.head()

# Input and output split
predictors = df.loc[:,df.columns!='Start_Tech_Oscar']
type(predictors)

target=df['Start_Tech_Oscar']
type(target)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(predictors,target,test_size=0.2,random_state=0)

from sklearn.ensemble import GradientBoostingClassifier
boost_clf=GradientBoostingClassifier()
boost_clf.fit(x_train,y_train)

from sklearn.metrics import accuracy_score,confusion_matrix

confusion_matrix(y_test, boost_clf.predict(x_test))
accuracy_score(y_test, boost_clf.predict(x_test))

# Hyperparameter

boost_clf2 = GradientBoostingClassifier(learning_rate=0.02,n_estimators=1000,max_depth=1)
boost_clf2.fit(x_train,y_train)

from sklearn.metrics import confusion_matrix,accuracy_score
confusion_matrix(y_test,boost_clf2.predict(x_test))
accuracy_score(y_test,boost_clf2.predict(x_test))

# Evaluation on training data
accuracy_score(y_train,boost_clf2.predict(x_train))
