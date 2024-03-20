# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:40:42 2024

@author: Atharv
"""
import pandas as pd
import statsmodels.graphics.tsaplots as tsa_plots
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
from math import sqrt
from matplotlib import pyplot

Walmart=pd.read_csv('Walmart Footfalls Raw.csv')
# data Partition
Train=Walmart.head(147)
Test=Walmart.tail(12)

'''
In order to use this model ,we need first find out the values of p,q and d
p represen tthe number of Autoregressive terms - laggs of dependency
q represent the number of moving average terms- lagges forcasting
d represent the number of non-seasonal difference
to find out the values of p,q, and d we use acf and pacf rps
'''
tsa_plots.plot_acf(Walmart.Footfalls,lags=12)
# the q value is 5 for MA
tsa_plots.plot_pacf(Walmart.Footfalls,lags=12)
# p for AR is 3

# ARIMA with AR=3 and MR=5
# model1=ARIMA(Train.Footfalls,order=(3,1,5))
from statsmodels.tsa.arima.model import ARIMA
import pandas as pd

# Assuming Train is a DataFrame with a 'Footfalls' column
# Replace Train with your actual dataset if needed
model1 = ARIMA(pd.DataFrame(Train['Footfalls']), order=(3, 1, 5))

# Fit the model
res1 = model1.fit()
res1=model1.fit()
print(res1.summary())

# Forcast for next  12 months
start_index=len(Train)
end_index=start_index+11
forcast_test=res1.predict(start=start_index,end=end_index)
print(forcast_test)

# Evaluate forecasts
rmse_test=sqrt(mean_squared_error(Test.Footfalls,forcast_test))
print('Test RMSE :%.3f'%rmse_test)
# Test RMSE :177.348

# Plot forecasts against actual outcomes
pyplot.plot(Test.Footfalls)
pyplot.plot(forcast_test,color='red')
pyplot.show()


# Auto-ARIMA

import pmdarima as pm
ar_model= pm.auto_arima(Train.Footfalls,start_p=0,start_q=0,
                        max_p=12,max_q=12,
                        m=1,
                        d=None,
                        seasonal=False,
                        trace=True,
                        error_action='warn',stepwise=True)

