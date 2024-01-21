# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 15:25:34 2023

@author: Atharv Joshi
"""

'''-- Optimization --- from the given set of the point we only calculate the slope and predicet the next step to it'''
#day 25/11/23
#this is the basic optimization 
import numpy as np
def gradient_decent(x,y):
    m_curr=b_curr=0
    iterations=10000
    n=len(x)
    learning_rate=0.08  #0.001  # we are change it it will change the cos function
    
    for i in range(iterations):
        y_predicted=m_curr * x + b_curr # y=mx+c
        cost= (1/n) * sum([val**2 for val in (y-y_predicted)])
        md= -(2/n) *sum(x*(y-y_predicted))
        bd= -(2/n) * sum(y-y_predicted)
        m_curr=m_curr-learning_rate*md
        b_curr=b_curr-learning_rate*bd
        print("m{}),b{},cost{} iteration {}".format(m_curr,b_curr,cost,i))
        
x=np.array([1,2,3,4,5])
y=np.array([5,7,9,11,13])

gradient_decent(x, y)

#

