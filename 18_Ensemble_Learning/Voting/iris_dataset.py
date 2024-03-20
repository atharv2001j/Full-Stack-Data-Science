# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 08:53:27 2024

@author: Atharv Joshi
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn import model_selection
from sklearn.ensemble import VotingClassifier

from mlxtend.classifier import StackingClassifier
import warnings
warnings.filterwarning('Ignore')

from sklearn import datasets

iris=datasets.load_iris()
X, y=iris.data[:,1:3], iris.target #Taking entire dataset

clf1=LogisticRegression()
clf2=RandomForestClassifier(random_state=1)
clf3=GaussianNB()
#########################################################

print("After five fold cross validation")
labels=['Logistic Regression','Random forest algorithm','Naive Bayes Algorithm']
for clf,labels in zip([clf1,clf2,clf3],labels):
    score = model_selection.cross_val_score(clf,X,y,cv=5,scoring='accuracy')
    print('accuracy:',score.mean(),"for ",labels)

voting_clf_hard = VotingClassifier(estimators=[(labels[0],clf1),
                                               (labels[1],clf2),
                                               (labels[2],clf3)],

                                               voting='hard')



voting_clf_soft = VotingClassifier(estimators=[(labels[0],clf1),
                                               (labels[1],clf2),
                                               (labels[2],clf3)],
                                               voting='soft')

labels_new=['Logistic regression','Random Forest Model','Naive Bayes Model','hard voting','soft voting']
for clf,labels in zip([clf1,clf2,clf3,voting_clf_hard,voting_clf_soft],labels_new):
    score = model_selection.cross_val_score(clf,X,y,cv=5,scoring='accuracy')
    print('accuracy:',score.mean(),"for ",labels)