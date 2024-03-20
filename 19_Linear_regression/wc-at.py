# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 16:12:03 2024

@author: Atharv Joshi
"""

import pandas as pd
import numpy as np
import seaborn as sns

wcat = pd.read_csv('wc-at.csv')
#Exploratory data analysis
#1. Measure  the central tendancy
#2. Measure of dispersion 
#3. Third moment business decision
#4. Fourth moment business decision
wcat.info()
wcat.describe()

#Graphical Representation
import matplotlib.pyplot as plt
plt.bar(height=wcat.AT,x=np.arange(1,110,1))
#plt.hist(wcat.AT)
sns.displot(wcat.AT)
# data is right skewed
plt.boxplot(wcat.AT)
# scatter plot
plt.scatter(x=wcat['Waist'],y=wcat['AT'],color='green')
# direction:positive, linearity:moderate, strength: poor
# Now let us calculate correlation coeficient
np.corrcoef(wcat.Waist,wcat.AT)
# They are moderately corelated to each  other
#let us check the direction using the cover factor
cov_output=np.cov(wcat.Waist,wcat.AT)[0,1]
cov_output
  
## let us apply to linear regression model
import statsmodels.formula.api as smf
# all machine learning algorithms are implement using sklearn
# but for this statmodel used because it gives you
# backend calculation of bita-0 and bita-1

model=smf.ols('AT~Waist',data=wcat).fit()
model.summary()

# OLS helps to find best fit model, which causes
# least square error.
# first you check R squared value=0.670, if square = 0.8 means that model is best fit
# fit, if R-Square =0.8 to 0.6 moderate correlation
# Next you check P>|t}=0, it means less than alpha,
# alpha is 0.05, Hence the model is accepted

# Regression line
pred1=model.predict(pd.DataFrame(wcat['Waist']))
plt.scatter(wcat.Waist,wcat.AT)
plt.plot(wcat.Waist,pred1,'r')
plt.show()

# Error calculation
res1=wcat.AT-pred1
np.mean(res1)
## it must be zero and here it Out[39]: -9.386986600867379e-14
res_sqrl=res1*res1
mse1=np.mean(res_sqrl)
rmse1=np.sqrt(mse1)
rmse1 # This is for simple linear regression
# Now to improve this model log transformation is used
plt.scatter(x=np.log(wcat['Waist']),y=wcat['AT'],color='brown')
np.corrcoef(wcat.Waist,wcat.AT)
# 0.81855781 this value we got so it is moderately linearity

######################################################
# Model 2

model2=smf.ols('AT~np.log(Waist)',data=wcat).fit()
model2.summary()
# We got an r_squared value is 0.675 which is not as much good.It is moderatly fit
pred2=model2.predict(pd.DataFrame(wcat['Waist']))
# scatter diagram
plt.scatter(np.log(wcat.Waist),wcat.AT)
plt.plot(np.log(wcat.Waist),pred2,'r')
plt.legend('Actual data','Predicted data for model 2')
plt.show()
# Error calculation
res2=wcat.AT-pred1
res_sqr2=res2*res2
mse2=np.mean(res_sqr2)
rmse2=np.sqrt(mse2)
rmse2

# Now lwt change the y value instead of x
plt.scatter(x=wcat['Waist'],y=np.log(wcat['AT']),color='brown')
np.corrcoef(wcat.Waist,np.log(wcat.AT))
# Now it become 0.84090

model3=smf.ols('np.log(AT)~Waist',data=wcat).fit()
model3.summary()
# the R-Squared value is 0.707
pred3=model3.predict(pd.DataFrame(wcat['Waist']))
pred3_at=np.exp(pred3)
pred3_at
# Regression line
plt.scatter(wcat.Waist,np.log(wcat.AT))
plt.plot(wcat.Waist,pred3,'r')
plt.legend('Predicted line','Observed data')
plt.show()
# linearity: Moderate,Direction : Positive ,Srength : Moderate
# error calculation
res3=wcat.AT-pred3_at
res_sqr3=res3*res3
mse3=np.mean(res_sqr3)
rmse3=np.sqrt(mse3)
rmse3
# 38.529001758071416

###############################################################
# We will use the polinomial model so the co-variance we cannot calculate
# i.e r cannot be calculated
model4=smf.ols('np.log(AT)~Waist+I(Waist*Waist)',data=wcat).fit()
model4.summary()
# R-squared value is 0.77
# and p <0.05 so model is acceptable

pred4=model4.predict(pd.DataFrame(wcat.Waist))
pred4
pred4_at=np.exp(pred4)
pred4_at

####################################################################
# Regression line
plt.scatter(wcat.Waist,np.log(wcat.AT))
plt.plot(wcat.Waist,pred4,'r')
plt.legend('Predicted Line','Observed data_model3')
plt.show()
# The data points are more cover and the lined is not linear.
# The line try to cover the more datapoints
# So the from above three models this model will look best 
##############################################################
# Error Calculation
res4=wcat.AT-pred4_at
res_sqr4=res4*res4
mse4=np.mean(res_sqr4)
rmse4=np.sqrt(mse4)
rmse4
# 32.24

################################################
data={'model':pd.Series(['SLR','Log_model','Exp_model','Poly_model'])}
data
table_rmse=pd.DataFrame(data)
table_rmse

###############################################
# We have to generalize the best model
from sklearn.model_selection import train_test_split
train,test=train_test_split(wcat,test_size=0.2)
plt.scatter(train.Waist,np.log(train.AT))
plt.scatter(test.Waist,np.log(test.AT))
final_model=smf.ols('np.log(AT)~Waist+I(Waist*Waist)',data=wcat).fit()
final_model.summary()
# R-squared valoe is 0.779 ,There is scope of improvement
# p<0.05 so it is acceptable
test_pred=final_model.predict(pd.DataFrame(test))

test_pred_at=np.exp(test_pred)
test_pred_at

###########################################################
train_pred=final_model.predict(pd.DataFrame(train))
train_pred_at=np.exp(train_pred)
train_pred_at
#######################################################
#Evalution on test data
test_err=test.AT-test_pred_at
test_sqrt=test_err*test_err
test_mse=np.mean(test_sqrt)
test_rmse=np.sqrt(test_mse)
test_rmse
# 33.18

###################################################
train_err=train.AT-train_pred_at
train_sqrt=train_err*train_err
train_mse=np.mean(train_sqrt)
train_rmse=np.sqrt(train_mse)
train_rmse
# 32.00
#The training error is less than testing error so model is overfit
