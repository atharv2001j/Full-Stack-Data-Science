# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 14:42:08 2024

"""

import pandas as pd
import numpy as np
import scipy
from scipy import stats 


# from statmodels.stats import weightstats sa stests
import statsmodels.stats.weightstats
############paired T-test##############
#When 2 features are normal then paired T test
# A universal test that tests for a siginiicant differencs=e between 2 relation A and B

sup= pd.read_csv("C:/Data Science/15_hypothesis/Hypothesis_Datasets(1)/hypothesis_datasets/paired2.csv")
sup.describe()

#H0: there is no siginificant difference between means of supplies of A and B
#Ha: There is siginifact difference betwwen means of suppliers of A and B
# Normailty test-#shapiro test
stats.shapiro(sup.SupplierA)
stats.shapiro(sup.SupplierB)

#data is Normal

import seaborn as sns
sns.boxplot(data=sup)

#assuing the external conditions are same for both the samples
#paired T test
ttest, pval=stats.ttest_rel(sup["SupplierA"],sup["SupplierB"])
print(pval)

#p-value=0<0.05 so p low null go





