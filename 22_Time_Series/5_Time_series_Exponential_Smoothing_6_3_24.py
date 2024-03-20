# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 08:49:37 2024

@author: Atharv Joshi
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import Holt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# now load tge datasets
cocacola= pd.read_excel("ocaCola_Sales_Rawdata.xlsx")
# lets us plot the datasst and its nature
cocacola.Sales.plot()
# Splitting the data into train and test set data
# since we are working on quartely datasets and in year there are
# test data=4 quarters
# train data= 38
Train=cocacola.head(38)
Test=cocacola.tail(4)
# here are we are considering performab=nce parameter as mean absolute
# rather than mean sqaure error
# custom function is written to calculate MPSE
def MAPE(pred,org):
    temp=np.abs((pred-org)/org)*100
    return np.mean(temp)

# EDA which comparises indentification of level , trends and seasonality
# in order to separate Trend and seasonality moving average can
my_pred=cocacola["Sales"].rolling(4).mean()
my_pred.tail(4)
# now lets us calculate mean absolute percentage of these value

MAPE(my_pred.tail(4), Test.Sales)
# moving average is predictaing complete values , out of which last
# are considered as predictaed value and last four values of test
# basisc purpose of moving average is deseaconality
cocacola.Sales.plot(label='org')
# this is origonal plot
# now let us separate  out trend and seasonality
for i in range(2,9,2):
    # it will take window size 2,4,6,8
    cocacola["Sales"].rolling(i).mean().plot(label=str(i))
    plt.legend(loc=3)
# you can see i=4 and 8 are desesonable plots
# time series decomposition is the another technique of seperating by using the additive seseonality
# sesonality
decompose_ts_add=seasonal_decompose(cocacola.Sales, model="additive", period=4)
print(decompose_ts_add.trend)
print(decompose_ts_add.seasonal)
print(decompose_ts_add.resid)
print(decompose_ts_add.observed)
decompose_ts_add.plot()

# similar plot can be decomposed using multiplicative 
decompose_ts_mul=seasonal_decompose(cocacola.Sales, model="multiplicative", period=4)
print(decompose_ts_mul.trend)
print(decompose_ts_mul.seasonal)
print(decompose_ts_mul.resid)
print(decompose_ts_mul.observed)
decompose_ts_mul.plot()

# you can observere the difference between these plots
# now lets us ACF plots  to check the  auto correlation
import statsmodels.graphics.tsaplots as tsa_plots
tsa_plots.plot_acf(cocacola.Sales, lags=4)
# we can obsereve the output in which r1, r2, r3 and r4 has higher
#  This is all about EDA

# let us apply data to data driven models
##################simple exponential method#############################
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
ses_model=SimpleExpSmoothing(Train['Sales']).fit()
pred_ses=ses_model.predict(start=Test.index[0], end=Test.index[-1])

# now  caclulating MAPE
MAPE(pred_ses, Test.Sales)
# we are getting 8.3698 

################# Holts exponential smoothing#######################  
# here only trend is captured
hw_model=Holt(Train["Sales"]).fit()
pred_hw=hw_model.predict(start=Test.index[0], end=Test.index[-1])
MAPE(pred_hw, Test.Sales)
# 10.48574531487818

###############Holts winter exponential smoothing ######################
#with additive seasonal
hwe_model_add_add=ExponentialSmoothing(Train['Sales'], seasonal="add", trend="add", seasonal_periods=4).fit()
pred_hwe_model_add_add= hwe_model_add_add.predict(start=Test.index[0], end=Test.index[-1])
MAPE(pred_hwe_model_add_add, Test. Sales)
# 3.372576621498227

################## holts winter exponential smoooting ####################
#with multiplicative seasonal
hwe_model_mul_add=ExponentialSmoothing(Train['Sales'], seasonal='mul', trend='add', seasonal_periods=4).fit()
pred_hwe_model_mul_add= hwe_model_mul_add.predict(start=Test.index[0], end=Test.index[-1])
MAPE(pred_hwe_model_mul_add, Test. Sales)
# 1.9367013171775445


#let us apply to complet edata of cocacola 
#we have seen that hwe_model_add_add has lowest MAPE value  hence  it is selected
hwe_model_add_add = ExponentialSmoothing(cocacola['Sales'],seasonal='add',seasonal_periods=4).fit()
#import the new datasets for which prediction has to  
new_data = pd.read_excel("C:/Data Science/19_Time_series/datasets/CocaCola_Sales_New_Pred.xlsx")
newdata_pred = hwe_model_add_add.predict(start=new_data.index[0], end=new_data.index[-1])



