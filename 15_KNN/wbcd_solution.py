# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 15:42:27 2024

@author: Atharv Joshi 
"""
'''
Business Objective:

Maximize : The count of the  cancer patents that are predicted correct should me maximize

Minimize : The false prediction of the cancer should be minimize so it would be easy to 
            improve the accuracy
            
Business Contraints: The parameters that are cosider for the prediction purpose

'''
import pandas as pd
import numpy as np

wbcd=pd.read_csv('wbcd.csv')
wbcd['diagnosis'].value_counts()
'''

B    357
M    212
Name: diagnosis, dtype: int64
'''

wbcd.shape
# there are 569 rows and 12 columns
wbcd.describe()
# The output column only contain B for Beniegn and M for Malignant

# let us first we will convert it into there proper form
wbcd['diagnosis']=np.where(wbcd['diagnosis']=='B','Beniegn',wbcd['diagnosis'])
wbcd['diagnosis']=np.where(wbcd['diagnosis']=='M','Malignant',wbcd['diagnosis'])
############################################################
# Te dataset contain the id column which wwill not contribute on the
# on the overall contribution of the prediction

wbcd=wbcd.iloc[:,1:32]

#################################################
# Normalize the data
def norm_fun(i):
    x=(i+i.min())/(i.max()-i.min())
    return x

# now let us apply this function to datset
wbcd_n=norm_fun(wbcd.iloc[:,1:32])
############################################
# Now let us apply X as a input and y as a output
X=np.array(wbcd_n.iloc[:,:])
# In wbcd_n we already include the output column ,hence alll rows
# and lastcolumn

y=np.array(wbcd['diagnosis'])
###############################################
# Lets split the data into train and test
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

# while handlind X and y instead of the whole dataframe there may be 
# chance of the data imbalance problem where it would be some mismatch in
# dividing the columns

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=21)
knn.fit(x_train,y_train)
pred=knn.predict(x_test)
pred 

########################################################
# After predicting a model let us evaluate the model

from sklearn.metrics import accuracy_score
print(accuracy_score(pred, y_test))
pd.crosstab(pred,y_test)
'''
col_0      Beniegn  Malignant
row_0                        
Beniegn         70          3
Malignant        1         40
'''
###################################################
acc=[]
# For the better accuracy purpose we have chosse the values are odd
for i in range(3,50,2):
    neigh=KNeighborsClassifier(n_neighbors=i)
    neigh.fit(x_train,y_train)
    train_acc=np.mean(neigh.predict(x_train)==y_train)
    test_acc=np.mean(neigh.predict(x_test)==y_test)
    acc.append([train_acc,test_acc])

# From dictionary it will see that we got two accuracy that is train accuracy and test accuracy
# lets plot the graph of that

import matplotlib.pyplot as plt
plt.plot(np.arange(3,50,2),[i[0] for i in acc],'ro-')
plt.plot(np.arange(3,50,2),[i[1] for i in acc],'bo-')

# fromthe above graph 3,5,7 are possible best values
# Let us check for k=7
knn=KNeighborsClassifier(n_neighbors=7)
knn.fit(x_train,y_train)
pred=knn.predict(x_test)
pred
# Lets check the accuracy   
from sklearn.metrics import accuracy_score
print(accuracy_score(pred, y_test))
pd.crosstab(pred,y_test)

'''
col_0      Beniegn  Malignant
row_0                        
Beniegn         68          3
Malignant        3         40
'''