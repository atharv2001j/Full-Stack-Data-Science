# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 08:29:07 2024

@author: Hp
"""


import pandas as pd
import numpy as np
import scipy
from scipy import stats

import statsmodels.stats.descriptivestats as sd
#from statsmodels.stats import Weightstats as states

import statsmodels.stats.weightstats

#1 sample sign
#for given dataset check whether scores are equal or less than 80
#H0 = scores are either equal or less than 80
#H1 = scores are not eual n greater than 80
#whenever there is single sample and data is not normal

marks=pd.read_csv("D:/12-SUPERVISED ALGORTIHM/Hypothesis/Hypothesis_Datasets(1)/hypothesis_datasets/Signtest.csv")

#normal QQ plot
import pylab
stats.probplot(marks.Scores,dist='norm',plot=pylab)

#Data is not normal
#H0:data is normal
#H1:data is not normal

stats.shapiro(marks.Scores)
#p_value is 0.024 > 0.005, p is high null fly

#Decision: Data is not normal
####################################################

#Let us check the distribution of the data
marks.Scores.describe()
#1 sample sign test

sd.sign_test(marks.Scores,mu0=marks.Scores.mean())
#p_value is 0.82>0.05 so p is high null fly

#Decision:
    #H0=scores are either equal or less than 80