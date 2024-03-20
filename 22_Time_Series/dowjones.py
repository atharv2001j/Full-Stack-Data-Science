# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:10:07 2024

@author: Lenovo
"""

import numpy as np
import seaborn as sns
import pandas as pd

sns.set_theme()

dowjones=sns.load_dataset('dowjones')
dowjones.head()

sns.lineplot(data=dowjones,x='Date',y='Price')

'''
Simple moving average is calculated the average of selected range of points,
by number of periods in the range

'''
dowjones['sma_30']=dowjones['Price'].rolling(window=30,min_periods=1).mean()
dowjones['sma_50']=dowjones['Price'].rolling(window=50,min_periods=1).mean()
dowjones['sma_100']=dowjones['Price'].rolling(window=100,min_periods=1).mean()
dowjones['sma_365']=dowjones['Price'].rolling(window=365,min_periods=1).mean()

sns.lineplot(x='Date',y='value',legend='auto',hue='variable',data=dowjones.melt('Date'))
'''
As you can see higher the value of the window,the lesser it is afected by theshort-term fluctuations
What if you wanted an average that will give higher weight to more recent points and lesser to points in the past
SMA are often used by the treders in the stock market for technical analysis
'''

# Exponential Moving Average

'''
SMA is nice but they give equal weightage to all datapoints .What if you want 
an average that willgive higher weight to the more recent points than the past.the use EMA
'''
dowjones['ema_50']=dowjones['Price'].ewm(span=50,adjust=False).mean()
dowjones['ema_100']=dowjones['Price'].ewm(span=100,adjust=False).mean()

sns.lineplot(x='Date',y='value',legend='auto',hue='variable',data=dowjones[['Date','Price','ema_50','sma_50']].melt('Date'))

'''
as you see that ema_50 follows the plot chart more closely than the sma_50
'''
