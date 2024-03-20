# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 09:31:51 2024


"""
#shapiro test normality check
import pandas as pd
import numpy as np
import scipy
from scipy import stats 

import statsmodels.stats.descriptivestats as sd
# from statmodels.stats import weightstats sa stests
import statsmodels.stats.weightstats
###########################################
#1 sample sign test

# fro the given dataset check wheather scores are equal or less than 80
#h0=scores are either equal or less than 80
#h1= scores are not equal n greather than 80
#whenever there is single sample and data is not normal

marks=pd.read_csv("C:/Data Science/15_hypothesis/Hypothesis_Datasets(1)\hypothesis_datasets\Signtest.csv")
#Normal QQ plot
import pylab
stats.probplot(marks.Scores,dist='norm',plot=pylab)
#data is not normal
#h0-data is normal
#h1- data is not normal
stats.shapiro(marks.Scores)
#p_value is 0.024<0.005 , p is heigh null fly
#decision : data is not normal
##################################
#let us check the distribution of the data
marks.Scores.describe()
#1-sample sign Test
sd.sign_test(marks.Scores,mu0=marks.Scores.mean())
#p_value os 0.82>0.05 so p is high null fly
#decision:
#h0=scores are either equal or less than 80
