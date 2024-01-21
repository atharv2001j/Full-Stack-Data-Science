# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 08:17:57 2023

@author: Atharv
"""
#shallow and deep copy
#Assignment operation
list_a=[1,2,3,4,5]
list_b=list_a
list_a[0]=-10
list_b[1]=99
print(list_a)
print(list_b)
#############################################################################
#Shallow copy
import copy
lst_a=[1,2,3,4]
lst_b=copy.copy(lst_a)
#it will not affect the other
lst_b[0]=-10
print(lst_a)
print(lst_b)
########################3
#For nested list
import copy
lst_a=[[1,2,3,4,5],[6,7,8,9,81]]
lst_b=copy.copy(lst_a)
#Affect the other
lst_a[0][0]=-10
print(lst_a)
print(lst_b)
######################################################################
#Deep copy
lst_a=[[1,2,3,4,5],[6,7,8,9,81]]
lst_b=copy.deepcopy(lst_a)
#not affect the other
lst_a[0][0]=-10
print(lst_a)
print(lst_b)
#######################


















