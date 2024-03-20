# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 16:04:18 2024


"""
'''
Johnnie Talkers soft drinks division sales managers has been planning
to launch a new sales incentive program for their sales executives 
The sales executive felt that the adult (>40 yrs) wont buy , children will
And hence requested sales manager not to launch the program.
Analye the data and determine whether there is evidence at 5%
significance level to support the hypothesis
'''

import pandas as pd
import numpy as np
import scipy
from scipy import stats 


# from statmodels.stats import weightstats sa stests
import statsmodels.stats.weightstats

############2- proportion test################################
#h0= poportionA== proportion B
#H1= poportion A!= poportion B
two_prop_test=pd.read_excel("C:/Data Science/15_hypothesis/Hypothesis_Datasets(1)/hypothesis_datasets/JohnyTalkers.xlsx")

from statsmodels.stats.proportion import proportions_ztest

tab1=two_prop_test.Person.value_counts()
tab1
tab2=two_prop_test.Drinks.value_counts()
tab2

#crosstable table
pd.crosstab(two_prop_test.Person, two_prop_test.Drinks)

count=np.array([58,152])
nobs=np.array([480,740])

stats,pval=proportions_ztest(count, nobs, alternative='two-sided')
print(pval)     #Pvalue 0.000

stats,pval=proportions_ztest(count, nobs, alternative='larger')
print(pval)     #Pvalue 0.9999

