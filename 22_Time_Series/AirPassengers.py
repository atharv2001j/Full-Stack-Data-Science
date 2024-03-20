# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 15:33:49 2024

@author: Atharv Joshi
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
plt.style.use('dark_background')

df=pd.read_csv('AirPassengers.csv')
df.columns
# # is used for the comment purpose so we have to rename it
df = df.rename({'#Passengers': 'Passengers'}, axis=1)

print(df.dtypes)
#Month is text and passengers is int
#NOw let us convert into date and time
df['Month']=pd.to_datetime(df['Month'])
print(df.dtypes)

df.set_index('Month', inplace=True)


plt.plot(df.Passengers)
#There is increasing trend and it has got seasonality


#is the data stationary?
#Dickey Fuller test
from statsmodels.tsa.stattools import adfuller
adf,pvalue,usedlag_,nobs_,critical_values_,icbest_=adfuller(df)
print('pvalue: ',pvalue,' if above 0.05 ,data is not stationary')
# since data is not stationary ,we may need SARIMA and not just ARIMA
# now let us extract the year and month from the data 

df['year']=[d.year for d in df.index]
df['month']=[d.strftime('%b') for d in df.index]
years = df['year'].unique()

# Plot yearly and monthly vaues as boxplot
sns.boxplot(x='year',y='Passengers',data=df)

# No. of passengers are going year by year
sns.boxplot(x='month',y='Passengers',data=df)

# Over all there is higher trend in July and August compared to rest of the month
# Extract and plot the trend ,seasonal and residual

from statsmodels.tsa.seasonal import seasonal_decompose
decomposed=seasonal_decompose(df['Passengers'],model='additive')

trend=decomposed.trend
seasonal=decomposed.seasonal
residual=decomposed.resid

plt.figure(figsize=(12,8))
plt.subplot(411)
plt.plot(df['Passengers'],label='Original',color='yellow')
plt.legend(loc='upper left')
plt.subplot(412)
plt.plot(trend,label='Trend',color='yellow')
plt.legend(loc='upper left')
plt.subplot(413)
plt.plot(seasonal,label='Seasonal',color='yellow')
plt.legend(loc='upper left')
plt.subplot(414)
plt.plot(residual,label='Residual',color='yellow')
plt.legend(loc='upper left')

plt.show()

# trend is going from 1950 to 60s 
# It is highly seasonal showing peaks at particular interval
# This helps to select specific prediction models

'''
Autocorrelation

values are nor co-related with its x-axis but with its lag
means yeastterday value is depends on the day before yesterday
autocorelation is simply series corelation with its lag
'''
from statsmodels.tsa.stattools import acf

acf_144=acf(df.Passengers,nlags=144)
plt.plot(acf_144)

# Auto corelation above zero means positive corelation and below zerpo means negative corelation
# Obtain same but in single line and more info

from pandas.plotting import autocorrelation_plot
autocorrelation_plot(df.Passengers)

# any lag before 40 has positive autocorelation 
# Horizontal bands indicate that 95% andd 99% confidence bands