# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 14:51:38 2024

"""
'''A financial analyst at a Financial Institte want to aevaluate a 
recent credit card promrtion . After this prormrotion , 500 cardholder
were randomly selected . Half received an ad 
promroting a full waivver of interest rate on purhases 
made over the next three months and half received a standarsdds christmas
adverstiment . did  the ad promoting full iintereset rate waiver
increase purchases'''

import pandas as pd
import numpy as np
import scipy
from scipy import stats 


# from statmodels.stats import weightstats sa stests
import statsmodels.stats.weightstats

#################2-sample T test for equal_variance##################
# load the dataset
prom=pd.read_excel("C:/Data Science/15_hypothesis/Hypothesis_Datasets(1)/hypothesis_datasets/Promotion.xlsx")
prom
#H0:InterstRateWaiver< StandardPromotion
#H1:InterstRateWaiver> StandardPromotion

prom.columns="InterestRateWaiver","StandardPromotion"


#normality test
stats.shapiro(prom.InterestRateWaiver)  #shapiro test
print(stats.shapiro(prom.StandardPromotion))

#data are normal

#variance test
help(scipy.stats.levene)
#H0=both column have equal variance
#H1= both the column has not equal variance
scipy.stats.levene(prom.InterestRateWaiver,prom.StandardPromotion)

#p-value=0.287>0.05 so p high null fly=> Equal variance

#2 sample T test
scipy.stats.ttest_ind(prom.InterestRateWaiver,prom.StandardPromotion)
help(scipy.stats.ttest_ind)

#Ho= equal mean
#Ha :unequal mean
#p-value =0.024<0.05 so p low null go


