# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:57:29 2024

@author: Atharv Joshi
"""
import pandas as pd
Walmart=pd.read_csv('Walmart Footfalls Raw.csv')
Walmart.shape
# Pre-processing
import numpy as np
Walmart['t']=np.arange(1,160)
Walmart['t_square']=Walmart['t']*Walmart['t']
Walmart['log_footfalls']=np.log(Walmart['Footfalls'])

Walmart.columns

# Index(['Month', 'Footfalls', 't', 't_square', 'log_footfalls'], dtype='object')
# month=['Jan','Feb','Mar'.......,'Dec']
# In Waaart we have Jan-1991 in 0th column,so we nwwd the only three rows 

p=Walmart['Month'][0]

# Before we will extract ,let us create new column called month to store the extractted value
p[0:3]

Walmart['months']=0

# you can check the dataframe with month name with all values are 0
# Totalrecords in dataframe are 159
for i in range(159):
    p=Walmart['Month'][i]
    Walmart['months'][i]=p[0:3]
    
month_dummies=pd.DataFrame(pd.get_dummies(Walmart['months']))
# now let usoncatenate these dummy values to dataframe
Walmart1=pd.concat([Walmart,month_dummies],axis=1)
# You can check the Walmart1 dataframe


# Visualize the Time plot
Walmart1.Footfalls.plot()

# Data Partition
Train=Walmart1.head(147)
Test=Walmart1.tail(12)

# To change the index values in pandas dataframe
# Test.set_index(np.arange(1,13))


###################### Linear #####################################################
import statsmodels.formula.api as smf

linear_model=smf.ols('Footfalls ~ t',data=Train).fit()
pred_linear=pd.Series(linear_model.predict(pd.DataFrame(Test['t'])))
rmse_linear=np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(pred_linear))**2))
rmse_linear    
# 209.92559265462546

######################## Exponential ######################################
Exp=smf.ols('log_footfalls ~ t',data=Train).fit()
pred_Exp=pd.Series(Exp.predict(pd.DataFrame(Test['t'])))
rmse_Exp=np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(np.exp(pred_Exp)))**2))
rmse_Exp
#  217.05263566813173

################################## Quadratic ##########################################
Quad = smf.ols('Footfalls ~ t + t_square',data=Train).fit()
pred_Quad = pd.Series(Quad.predict(Test[['t','t_square']]))
rmse_Quad=np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(pred_Quad))**2))
rmse_Quad
# Out[42]: 137.15462741356484

############################## Additive Seasonality ######################
add_sea=smf.ols('Footfalls ~ Jan+Feb+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov',data=Train).fit()
pred_add_sea=pd.Series(add_sea.predict(Test[['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov']]))
rmse_add_sea=np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(pred_add_sea))**2))
rmse_add_sea
#  264.6643900568774

########################### Multiplicative Seasonality ########################
Mul_sea=smf.ols('log_footfalls ~ Jan+Feb+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov',data=Train).fit()
pred_Mul_sea=pd.Series(Mul_sea.predict(Test))
rmse_Mul_sea=np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(np.exp(pred_Mul_sea)))**2))
rmse_Mul_sea
# 268.197032530917

###################### Additive Seasonality Quadratic trend ####################
add_sea_Quad=smf.ols('Footfalls ~ t+t_square +Jan+Feb+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov',data=Train).fit()
pred_add_sea_Quad=pd.Series(add_sea_Quad.predict(Test[['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','t','t_square']]))
rmse_add_sea_Quad=np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(pred_add_sea_Quad))**2))
rmse_add_sea_Quad
# 50.60724584048495

#################### Multiplicative Seasonality Quadratic Trend ###################
Mul_sea_Quad=smf.ols('log_footfalls ~ t+t_square+Jan+Feb+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov',data=Train).fit()
pred_Mul_sea_Quad=pd.Series(Mul_sea_Quad.predict(Test))
rmse_Mul_sea_Quad=np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(np.exp(pred_Mul_sea_Quad)))**2))
rmse_Mul_sea_Quad
# 70.94051959578569

################################ Multiplicative Seasonality Linear Trend ####################################################
Mul_sea_Quad1=smf.ols('log_footfalls ~ t+Jan+Feb+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov',data=Train).fit()
pred_Mul_sea_Quad1=pd.Series(Mul_sea_Quad1.predict(Test))
rmse_Mul_sea_Quad1=np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(np.exp(pred_Mul_sea_Quad1)))**2))
rmse_Mul_sea_Quad1
#  172.7672678466982

#########################################
# From above experimentation we observed that the Additive Seasonality Quadratic Trend havinf minimum rmse value

############################## Testing #######################################
predict_data=pd.read_excel('predict_new.xlsx')

model_full=smf.ols('Footfalls ~ t+t_square +Jan+Feb+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov',data=Train).fit()
pred_new=pd.Series(model_full.predict(predict_data))
pred_new
'''
0     2213.628216
1     2252.669534
2     2219.210851
3     2331.668836
4     2384.626820
5     2059.418138
6     2206.876122
7     2204.750773
8     2256.708757
9     2028.471300
10    1999.332467
11    2308.270556
dtype: float64
'''
# it is not fullfilled result because errors are independendant
predict_data['forecasted_Footfalls']=pd.Series(pred_new)
predict_data['forecasted_Footfalls']

#Autoregression Model (AR)
# Calculating residual from best model applied on full stack
# AV-FV

full_res=Walmart1.Footfalls - model_full.predict(Walmart1)


# ACF Plot on residuals
import statsmodels.graphics.tsaplots as tsa_plot
tsa_plot.plot_acf(full_res,lags=12)

# Acf is an (complete ) auto-correlation fiunction gives values
# of auto-correlation of any time serieswith its lagged values
# ACFis applied on the datapoints as well as residuals

# PACF is a partial auto-correlation function
# PACF is only apply on the residuals not datapoints
# It finds correlation of present with lags of the residual of the plot
# It will find that at 0 it will self corelated so ignore that and consider next 4 points which are auto-corelated to eah other

tsa_plot.plot_pacf(full_res,lags=12)

# Alternative approach for the ACF plot 

# AR model
from statsmodels.tsa.ar_model import AutoReg
model_ar=AutoReg(full_res, lags=[1])
# there is someinformation remains in model so we again apply it to the model and consider lag as 1 because it shows higher auto-correlation
model_fit=model_ar.fit()

print('Coefficient:%s'%model_fit.params)
'''
Coefficient:const   -1.505706
y.L1     0.641099
dtype: float64
'''

pred_res = model_fit.predict(start=len(full_res),end=len(full_res)+len(predict_data)-1,dynamic=False)
pred_res.reset_index(drop=True,inplace=True)

# The final prediction using ASQT and AR(1) Model
final_pred=pred_new+pred_res
final_pred
'''
0     2169.823067
1     2223.080383
2     2198.735566
3     2317.036441
4     2373.740298
5     2050.933092
6     2199.930660
7     2198.792337
8     2251.383103
9     2023.551322
10    1994.672566
11    2303.777391
dtype: float64

'''
# Again you calculated full_res and plot the acf plot again apply to the AR model check if their is 
# check if there is a autocorelatiom or not 
# if then again process the same process and if not (zero-autocorelation) then stop it
# pred_res-next_pred_res


