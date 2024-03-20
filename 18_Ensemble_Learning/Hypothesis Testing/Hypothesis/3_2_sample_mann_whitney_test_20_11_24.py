# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 14:27:54 2024
"""

##################mann-Whitney Test###################
import pandas as pd 
import numpy as np
import scipy
from scipy import stats
from scipy.stats import mannwhitneyu

import statsmodels.stats.descriptivestats as sd
#from statsmodels.stats import Weightstats as stats 
import statsmodels.stats.weightstats as stests
##################mann-Whitney Test###################
#vechical with and without addictive
#H0= fuel additive does not impact the performance
#H1= fuel additive does impact the performance
fuel=pd.read_csv("C:/Data Science/15_hypothesis/Hypothesis_Datasets(1)/hypothesis_datasets/mann_whitney_additive.csv")
fuel

#rename the column
fuel.columns="Without_additive","With_additive"

#normailty -test
#H0=data is normal

print(stats.shapiro(fuel.Without_additive))     #p high null fill
print(stats.shapiro(fuel.With_additive))        #p low null go

#without_additive is normal
# with additive is not normal
# when two sample are not normal then mannwhitney test
#non-parametric test case'
# mann-withney test
scipy.stats.mannwhitneyu(fuel.Without_additive,fuel.With_additive)

#p-value =0.4457>0.05 so p is high null fly 
#H0= fuel additive does not impact the performance
