# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 15:13:08 2024
"""

'''
A marketing organization outsourcses there back office operations
to three different supplies . the contracts are up for renewal and
the CMo wants to determine whether they should renew contracts with all
suppliers or any specififc supplier. CMO wants to renew the contract of supplier 
with the least trab=ncsation time.
CmO will renew all contracts if the performance of all suppliers is similar
'''
import pandas as pd
import numpy as np
import scipy
from scipy import stats 


# from statmodels.stats import weightstats sa stests
import statsmodels.stats.weightstats

#########one Way- Anova###########3
# load the dataset
con_renewal=pd.read_excel("C:/Data Science/15_hypothesis/Hypothesis_Datasets(1)/hypothesis_datasets/ContractRenewal_Data(unstacked).xlsx")
con_renewal

#rename the column
con_renewal.columns="SupplierA","SupplierB","SupplierC"

#H0= All the 3 suppliers have equal mean trancation time
#H1= All the 3 suppliers have not equal mean trancation tiime

#normality test
stats.shapiro(con_renewal.SupplierA)    #shapiro test
#pvalue=0.89>0.005 supplierA is normal
stats.shapiro(con_renewal.SupplierB)    #shapiro test
#pvalue
stats.shapiro(con_renewal.SupplierC)    #shapiro test
#pvalue=0.57>0.005 supplierC is normal

#variance test
help(scipy.stats.levene)
#all 3 suppliers sre being checked for variance
scipy.stats.levene(con_renewal.SupplierA,con_renewal.SupplierB,con_renewal.SupplierC)
# the levene test tests the null hypothesis
# that all input samples are from populations with equal variance
#pvalue=0.777>0.005, p is hgh null fly
#H0= All input samples are form population with equla varaince

#one- way Anova
F, p=stats.f_oneway(con_renewal.SupplierA,con_renewal.SupplierB,con_renewal.SupplierC)

#p value
p     # p high null flky
# all the 3 supplier has equal mean trancation  time


