# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 08:45:36 2024

@author: Atharv Joshi
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import roc_curve,auc
from sklearn.metrics import classification_report

claimants=pd.read_csv('claimants.csv')
# The Casenum do not contributr in a prediction so we will drop it
c1=claimants.drop('CASENUM',axis=1)
c1.head()
c1.describe()
# let us check the null value
c1.isna().sum()
'''
ATTORNEY      0
CLMSEX       12
CLMINSUR     41
SEATBELT     48
CLMAGE      189
LOSS          0
dtype: int64
'''
# It contain several null values so process on it
# We will use an inputation for that because droping those rows will affecton accuracy

c1.dtypes
mean_value=c1.CLMAGE.mean()
mean_value

# Now lw us impute the same
c1.CLMAGE=c1.CLMAGE.fillna(mean_value)
c1.CLMAGE.isna().sum()
# hENCE HERE ALL the null values are replaced with the mean_value for the CLMAGE column
# for the columns who having the discrete value we will apply the Mode for them
mode_CLMSEX=c1.CLMSEX.mode()
mode_CLMSEX
c1.CLMSEX=c1.CLMSEX.fillna((mode_CLMSEX)[0])
c1.CLMSEX.isna().sum()
# CLAMINSUR in also a categorical soapply mode 
mode_ClMINSUR=c1.CLMINSUR.mode()
mode_ClMINSUR
c1.CLMINSUR=c1.CLMINSUR.fillna((mode_ClMINSUR)[0])
c1.CLMINSUR.isna().sum()

# SEATBELT is also categorical
mode_SEATBELT=c1.SEATBELT.mode()
mode_SEATBELT
c1.SEATBELT=c1.SEATBELT.fillna((mode_SEATBELT)[0])
c1.SEATBELT.isna().sum()

#Now THR PERSON WE MET AN ACCCIDENT WILL HIRE the atternev or no
# let us buils the model
logit_model=sm.logit('ATTORNEY~CLMAGE+LOSS+CLMINSUR+CLMSEX+SEATBELT',data=c1).fit()
logit_model.summary()
# In Logistic regression we do nothave an R squared value ,only check the p value
# SEATBELT is statistically insignificant ignore and proceed

logit_model.summary2()
# here we going to check the summary2 because AIC value,its stands for the Akaike Information criterion
# It mention how well model fits the data
# Lower the AIC value better model

# Now lets us go for the prediction
pred=logit_model.predict(c1.iloc[:,1:])
# Here we are applying the all rows for training and except one column which is our
# target column (ATTORNEY)

# let us check the performnace of the model
fpr,tpr,thresholds=roc_curve(c1.ATTORNEY,pred)
# We are applying the actual values and predicted values so we will get the fpr,
# tpr,and the threshold
# Theoptimal cutoff value is the point where there is a high true positive rate
optimal_idx=np.argmax(tpr-fpr)
optimal_threshold=thresholds[optimal_idx]
optimal_threshold

#ROC : recieber oprerating characteritics
# determine best cutoff/threshhold value
i = np.arange(len(tpr))

roc=pd.DataFrame({'fpr':pd.Series(fpr,index=i),
                  'tpr':pd.Series(tpr,index=i),
                  '1-fpr':pd.Series((1-fpr),index=i,),
                  'tf' : pd.Series(tpr-(1-fpr),index=i),
                  'thresholds' : pd.Series(thresholds,index=i)})

plt.plot(fpr,tpr)
plt.xlabel('False positive rate');plt.ylabel('True positive rate')
roc.iloc[(roc.tf-0).abs().argsort()[:1]]
roc_auc=auc(fpr,tpr)
print('area under the curve:%f'% roc_auc)

# tpr Vs 1-fpr
fig,ax=plt.subplot()
plt.plot(roc['tpr'],color='red')
plt.plot(roc['1-fpr'],colr='blue')
plt.xlabel('1-false positive rate')
plt.ylabel('True positive rate')
plt.title('ROC')
ax.set_xticklabels([])
# The optimal cutoff point is the point where tpr is high and fpr is low
# The optimal cutoff point is 0.3176
# So anything above this can be label as 0 else 1
# crossing 1-FPR the IPR is 63%

# filling the cells with zeros
c1['pred']=np.zeros(1340)
c1.loc[pred>optimal_threshold,'pred']=1
# let us check the classification report
classification=classification_report(c1['pred'],c1['ATTORNEY'])
classification

# Splitting the data into train and test
train_data,test_data=train_test_split(c1,test_size=0.3)
# Model Building
model=sm.logit('ATTORNEY~CLMAGE+LOSS+CLMINSUR+CLMSEX+SEATBELT',data=train_data).fit()
model.summary()
# P value is below condition of 0.05
# but the SEATBELT has got statistically insignificant

model.summary2()

# Let us go for the prediction
test_pred=logit_model.predict(test_data)
# creating a new column
test_data['test_pred']=np.zeros(402)
test_data.ioc[test_pred>optimal_threshold,'test_pred']=1
# Confusion matrix
confusion_matrix=pd.crosstab(test_data.test_pred,test_data.ATTORNEY)
confusion_matrix
accracy_test=(143+151)/(402)
accracy_test
# It is 0.6940298

#Clasification repirt
classification_test=classification_report(test_data['test_pred'],test_data.ATTORNEY)
classification_test
# Accuracy os 0.73

# ROC curve and AUC
fpr,tpr,thresholds=metrics.roc_curve(test_data['ATTORNEY'],test_pred)

# Plot the ROC Curve
plt.plot(fpr,tpr);plt.xlabel('False Positive Rate');plt.ylabel('True Positive Rate')

# Area under the curve
roc_auc_test=metrics.auc(fpr,tpr)
roc_auc_test

# Prediction on train Data
train_pred=logit_model.predict(train_data)
train_data['train_pred']=np.zeros(938)
train_data.loc[train_pred>optimal_threshold,'train_pred']=1
# Confusion matrix
confusion_matrix=pd.crosstab(train_data.train_pred,train_data.ATTORNEY)
confusion_matrix

accuracy_train=(315+347)/(938)
accuracy_train
# It is 0.7217484000

# Classification Report
classification_train=classification_report(train_data['train_pred'],train_data['ATTORNEY'])
classification_train
# ccuracy is 0.69

#ROC Curve and AUC
fpr,tpr,thresholds=metrics.roc_curve(train_data['ATTORNEY'],train_pred)

# Plot the ROC Curve
plt.plot(fpr,tpr);plt.xlabel('False Positiove Rate');plt.ylabel('True Positive Rate')
# Area under the curve
roc_auc_train=metrics.auc(fpr,tpr)

roc_auc_test