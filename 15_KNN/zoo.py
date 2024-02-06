# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 23:24:26 2024

@author: ASUS
"""
'''
PROBLEM STATEMENT 2 
A National Zoopark in India is dealing with the problem of 
segregation of the animals based on the different attributes
 they have. Build a KNN model to automatically classify the 
 animals. Explain any inferences you draw in the documentation.
'''

import pandas as pd
import numpy as np
zoo = pd.read_csv("Zoo.csv")
zoo
#this dataset has 101 rows & 18 columns
#to understand the distribution of data
zoo.describe()

zoo.info()
#this dataset not contains any null values

zoo['type'].value_counts()
"""
1    41
2    20
4    13
7    10
6     8
3     5
5     4
"""

#animal name is not important so drop that column
zoo = zoo.drop('animal name',axis=1)

#normalization
def norm(i):
    x = (i-i.min())/(i.max()-i.min())
    return x

#let us apply normlization function to the dataset
zoo_norm = norm(zoo.iloc[:,0:16])


#now let us take X as input & Y as output
X = np.array(zoo_norm.iloc[:,:])
Y = np.array(zoo['type'])

#split the dataset into train and test
from sklearn.model_selection import train_test_split
X_train, X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2)
#to avoid the unbalancing of data during splitting the concept of 
#statified sampling is used

#now build the KNN model
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=21)
knn.fit(X_train,Y_train)
pred = knn.predict(X_test)
pred

#now let us evaluate the model
from sklearn.metrics import accuracy_score
print(accuracy_score(pred,Y_test))
pd.crosstab(pred,Y_test)
#so this model is not accepted as there are errors

#let us try to select the correct value of k
acc= []
#running the KNN algorithm for k=3 to 50 in step of 2
#k's value is selected as odd
for i in range(3,50,2):
    #declare model
    n = KNeighborsClassifier(n_neighbors=i)
    n.fit(X_train,Y_train)
    train_acc = np.mean(n.predict(X_train) == Y_train)
    test_acc = np.mean(n.predict(X_test) == Y_test)
    acc.append([train_acc,test_acc])

#lets plot the graph of train_acc and test_acc
import matplotlib.pyplot as plt
plt.plot(np.arange(3,50,2),[i[0] for i in acc],'ro-')
plt.plot(np.arange(3,50,2),[i[1] for i in acc],'bo-')
#there are valiues like 3,5,7,9 where the accuracy is good

#lets try for K=3
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train,Y_train)
pred = knn.predict(X_test)
accuracy_score(pred,Y_test)
#1.0
pd.crosstab(pred,Y_test)
#this is perfect model
"""
col_0  1  2  4  5  6  7
row_0                  
1      6  0  0  0  0  0
2      0  7  0  0  0  0
4      0  0  2  0  0  0
5      0  0  0  2  0  0
6      0  0  0  0  2  0
7      0  0  0  0  0  2
"""