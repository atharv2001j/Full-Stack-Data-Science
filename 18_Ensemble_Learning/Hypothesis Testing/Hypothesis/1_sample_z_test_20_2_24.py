# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 14:16:51 2024

"""

import pandas as pd
import numpy as np
import scipy
from scipy import stats 


# from statmodels.stats import weightstats sa stests
import statsmodels.stats.weightstats as stests

#################1 sample Z-test######################
#importig the data
fabric=pd.read_csv("C:/Data Science/15_hypothesis/Hypothesis_Datasets(1)/hypothesis_datasets/Fabric_data.csv")
#h0= average lenght of the fabric =<150
#h1= aveergare lenght is >150
#claculating the normality test
print(stats.shapiro(fabric))
#0.1460>0.005 H0 true
#calculating the mean

np.mean(fabric)

#z_test
#parameters in ztest, value is mean of data
import pylab
ztest,pval=stests.ztest(fabric,x2=None,value=150)

print(float(pval))

#p-value=7.156e-06<0.005 so p low null go
#it is greather than 150
