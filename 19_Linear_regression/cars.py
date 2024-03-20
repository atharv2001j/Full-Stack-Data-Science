# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 15:00:33 2024

@author: Atharv Joshi
"""
# Multiple regression collinearity

import pandas as pd
import numpy as np
import seaborn as sns

cars=pd.read_csv('cars.csv')
# 1. Measures the central tendancy
# 2. Measure the dispersion
# 3. Third moment business decision
# 4. fourth moment decision
# 5. probability distribution

cars.describe()

#Graphial Representation
import matplotlib.pyplot as plt
plt.bar(height=cars.HP,x=np.arange(1,82,1))
sns.distplot(cars.HP)
# data is right skewed
plt.boxplot(cars.HP)
# There are several outliers in HP
sns.distplot(cars.MPG)
# data is slightly left distributed
plt.boxplot(cars.MPG)
# There are no outlier
sns.displot(cars.VOL)
# Data is slightly left distributed
plt.boxplot(cars.VOL)
sns.distplot(cars.SP)
# Data is slightly right distributed
plt.boxplot(cars.SP)
# There are several outliers
sns.distplot(cars.WT)
plt.boxplot(cars.WT)
#There are several outliers
# Now joint plot : It will plot the scatter plot
#  histogram
sns.jointplot(x=cars['HP'],y=cars['MPG'])

# Now lwt us plot the countplot
plt.figure(1,figsize=(16,10))
sns.countplot(cars['HP'])
# count plot shows how many times the value occure
# 92 HP value occurs 72 times

# QQ Plot
from scipy import stats
import pylab
stats.probplot(cars.MPG,dist='norm',plot=pylab)
plt.show()
#MPG data is normally distributed
# there are 10 scatter plot we have to plotted so plot a pairplot plot insted of separate
sns.pairplot(cars.iloc[:,:])
# MPG vs Sp Linearity: Moderate, Strength : Poor, Direction : negative
# Similarly we can see it in pairplot

# Now let us check r value
cars.corr()
# The SP and HP valye is 0.97 so it is very high
# Similarly WT and VOl also have 0.99 which is very hogh
# So this feature are not contributing on prediction

# Linear Regression
import statsmodels.formula.api as smf
ml1=smf.ols('MPG ~WT+VOL+SP+HP',data=cars).fit()
ml1.summary()
# R-squared is 0.771 which is good
# p value of WT and VOL is 0.814 and 0.554 which is very high
# It means it is greater than 0.05 
# So we need to ignore it
# Or delete . Instead deleting 81 entries ,
# Lets us check row wise outliers
# Identifying there is any influencing value
# To check you can use an influencing index

import statsmodels.api as sm
sm.graphics.influence_plot(ml1)

# 76 is the value which got an outliers
# go to data check the entry and delete it

cars_new=cars.drop(cars.index[[76]])

# again apply regression to the cars_new
ml_new=smf.ols('MPG~WT+VOL+HP+SP',data=cars_new).fit()
ml_new.summary()

# R-squared value is 0.819 nut p value are same ,hence not so conform
# Now next option is detlete the column not
# WT is less hence can be deleted

rsq_hp=smf.ols('HP~WT+VOL+SP',data=cars).fit().rsquared
vif_hp=1/(1-rsq_hp)
vif_hp
# 639.92658897499852

rsq_vol=smf.ols('VOL~WT+HP+SP',data=cars).fit().rsquared
vif_vol=1/(1-rsq_vol)
vif_vol
# 638.8060836592878

rsq_sp=smf.ols('SP~WT+HP+VOL',data=cars).fit().rsquared
vif_sp=1/(1-rsq_sp)
vif_sp
# 20.00763878305008

# Lets us drop WT and apply co-relation to remaning three columns
final_ml=smf.ols('MPG~VOL+HP+SP',data=cars).fit()
final_ml.summary()

final_ml=smf.ols('MPG~VOL+HP+SP',data=cars_new).fit()
final_ml.summary()
# R-squared is 0.819 and p values are less than 0.05
# So take cars_new

pred=final_ml.predict(cars_new)

# QQ Plot
res=final_ml.resid
sm.qqplot(res)
plt.show()

# It will normally distributed
stats.probplot(res,dist='norm',plot=pylab)
plt.show()

# Let us plot residual plot
sns.residplot(x=pred,y=cars.MPG,lowess=True)
plt.xlabel('Fitted')
plt.ylabel('Residual')
plt.title('Fited vs Residual')
plt.show()

# Resisual plot is to draw for the error
from sklearn.model_selection import train_test_split
cars_train,cars_test=train_test_split(cars,test_size=0.2)

model_train=smf.ols('MPG~VOL+SP+HP',data=cars_train)
model_train.summary()
test_pred=model_train.predict(cars_test)
#test error
test_error=test_pred.cars_test.MPG
test_rmse=np.sqrt(np.mean(test_error*test_error))
test_rmse