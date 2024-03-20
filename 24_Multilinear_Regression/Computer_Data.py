# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 14:17:47 2024

@author: Atharv Joshi
"""
'''
Problem Statement:
    	Perform multilinear regression with price as the output variable and 
    document the different RMSE values.

'''
'''
Business Objective :
    
Maximize : The production as well as the quality of the computer

Minimize : The price of the computer as well the production cost of the 
Computer.

Business Cotraints : The overll budget of the company and the data required
for the computer should be secuure.The maintainance of the computer.

'''

################################ EDA ################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('Computer_Data.csv')

df.info()
'''
#   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   Unnamed: 0  6259 non-null   int64
 1   price       6259 non-null   int64
 2   speed       6259 non-null   int64
 3   hd          6259 non-null   int64
 4   ram         6259 non-null   int64
 5   screen      6259 non-null   int64
 6   cd          6259 non-null   int32
 7   multi       6259 non-null   int32
 8   premium     6259 non-null   int32
 9   ads         6259 non-null   int64
 10  trend       6259 non-null   int64
dtypes: int32(3), int64(8)
'''
# All the datapoints are numeric in nature as well as there is no null value
# Is present in the dataset
#Label Encoder for cd, multi,premium
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
select_column=['cd','multi','premium']
le.fit(df[select_column].values.flatten())
df[select_column]= df[select_column].apply(le.fit_transform)

#corelation matrix
df.corr() 
corelation_values=df.corr() 
 
# Visualize the data
import seaborn as sns
sns.pairplot(df)
#here colinearity is high between hd & ram but scatter plot shows no any linearity.

# Check for the Outliers 
sns.boxplot(df)
# There is outlier in hd and price column

#Split the data into train and test .
from sklearn.model_selection import train_test_split
train_data,test_data=train_test_split(df)

train_data=train_data.reset_index()
test_data=test_data.reset_index()
# drop the column no. 1
train_data1=df.drop(["Unnamed: 0"], axis=1)
test_data1=df.drop(["Unnamed: 0"], axis=1)

import statsmodels.formula.api as sf
#Building the regression model w.r.t. t training data.

m1=sf.ols("price~speed+hd+ram+screen+cd+multi+premium+ads+trend",data=train_data1).fit()
m1.summary()   #R-SQUARE=0.776
#Here r-square is less than 0.8 ,we need some transformations for r-square value more than 0.8.

#check with the vif value.
rsq=sf.ols("price~speed+hd+ram+screen+cd+multi+premium+ads+trend",data=train_data1).fit().rsquared

rsq_final=1/(1-rsq)
#vif value is less than 10.i.e 4.53

import statsmodels.api as sm
sm.graphics.influence_plot(m1)
sm.graphics.plot_partregress_grid(m1)

#Transformations for better value of r-squared.
#Take the sqrt for all input variables.
trans_m1=sf.ols("price~np.sqrt(speed)+np.sqrt(hd)+np.sqrt(ram)+np.sqrt(screen)+cd+multi+premium+np.sqrt(ads)+trend",data=train_data1).fit()
trans_m1.summary()  #r-squared=0.793
#providing the sqrt to output variable w.r.t. to output 
trans_m2=sf.ols("np.sqrt(price)~np.sqrt(speed)+np.sqrt(hd)+np.sqrt(ram)+np.sqrt(screen)+cd+multi+premium+np.sqrt(ads)+trend",data=train_data1).fit()
trans_m2.summary()    #r-squared=0.807

#taking log 
trans_m3=trans_m1=sf.ols("np.log(price)~np.log(speed)+np.log(hd)+np.log(ram)+np.log(screen)+cd+multi+premium+np.log(ads)+trend",data=train_data1).fit()
trans_m3.summary()     #r-squared=0.791

#taking log for price & sqrt for speed and hd
trans_m4=sf.ols("np.log(price)~np.sqrt(speed)+np.sqrt(hd)+ram+screen+cd+multi+premium+ads+trend",data=train_data1).fit()
trans_m4.summary()    #0.805

#Taking log to price,sqrt to speed,hd & qudratic to speed & hd
trans_m5=trans_m1=sf.ols("np.log(price)~np.sqrt(speed)+(speed*speed)+np.sqrt(hd)+(hd*hd)+(ram)+(screen)+cd+multi+premium+ads+trend",data=train_data1).fit()
trans_m5.summary()        #0.814
             
#taking th model5 because r squared is high i.e 0.815 with rmse value of train=244.3 & test rmse =249.3
trans_m5=sf.ols("np.log(price)~np.sqrt(speed)+(speed*speed)+np.sqrt(hd)+(hd*hd)+(ram)+(screen)+cd+multi+premium+ads+trend",data=train_data1).fit()
trans_m5.summary()                   #0.814
#train data
final_train_pred=trans_m5.predict(train_data1)
final_train_pred1=np.exp(final_train_pred)
#train residual
train_res=train_data1['price']-final_train_pred1
train_res
#train rmse
train_rsme=np.sqrt(np.mean(train_res*train_res))
train_rsme                    #244.60
#test pred
final_test_pred=trans_m5.predict(test_data1)
final_test_pred1=np.exp(final_test_pred)
#test residuals
final_test_res=test_data1['price']-final_test_pred1
#test rmse
final_test_rmse=np.sqrt(np.mean(final_test_res*final_test_res))

#testing the finalised model with original dataset
df1=df.drop(["Unnamed: 0"],axis=1)
final=sf.ols("np.log(price)~np.sqrt(speed)+(speed*speed)+np.sqrt(hd)+(hd*hd)+(ram)+(screen)+cd+multi+premium+ads+trend",data=df1).fit()
final.summary()                     #0.814

#prediction model
final_pred_log=final.predict(df1)
final_pred=np.exp(final_pred_log)
#checking the linearity with plotting the scatter plot
plt.scatter(df1['price'],final_pred);plt.xlabel("Actual Values");plt.ylabel("fitted values")
plt.scatter(final_pred,final.resid_pearson, c='r');plt.axhline(y=0,color='blue');plt.xlabel("Fitted values");plt.ylabel("Residuals")
#somehow homoscadasticity is present
#check for normality
plt.hist(final.resid_pearson)
#Data is normally distributed

