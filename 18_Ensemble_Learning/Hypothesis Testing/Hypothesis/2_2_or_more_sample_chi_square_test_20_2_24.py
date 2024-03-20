# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 16:18:26 2024
"""

import pandas as pd
import numpy as np
import scipy
from scipy import stats 


# from statmodels.stats import weightstats sa stests
import statsmodels.stats.weightstats

#########################Chi- square -test#######################3
Bahaman=pd.read_excel("C:/Data Science/15_hypothesis/Hypothesis_Datasets(1)/hypothesis_datasets/Bahaman.xlsx")
Bahaman

count=pd.crosstab(Bahaman["Defective"], Bahaman["Country"])
count
Chisquares_results= scipy.stats.chi2_contingency(count)

Chi_square=[['Test Statistic','p-value'],[Chisquares_results[0],Chisquares_results[1]]]

Chi_square

'''
you use chi2_contingency when you want to test
whether two  (or more) gruops have the same distribution
'''
#H0=Null Hypothesis: the 3 group have no significant differance
#since p=0.63>0.05 hence H0 is true 
