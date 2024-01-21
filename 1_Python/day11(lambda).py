# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 08:16:58 2023

@author: Atharv
"""
######################LAMBDA ###########################
def add(a,b,c):
    sum=a+b+c
    return sum
print(add(4,5,6))
#using lmbda function
sum=lambda a,b,c:a+b+c
sum(4,5,6)
#############################################################
def multi(a,b,c):
    mult=a*b*c
    return mult
print(multi(4,5,6))
#using lmbda function
multi=lambda a,b,c:a*b*c
multi(4,5,6)
##############################################################
#using arbitari parameters
val=lambda *args:sum(args)
val(1,2,3,4,5)
###########################################################
myfun=lambda *args:print(args)
myfun("this","is","python")
############################################################
person=lambda size,*args:print(size,args)
person(23,'atharv')
#############################################################
#key value parameter
def person(name,**data):
    print(name)
    print(data)
person(name='atharv',age=28,place='nagar')

person=lambda name,**data:print(name,data)
person(name='atharv',age=28,place='nagar')
#instead of : we write = while calling keyword argument
#############################################################
def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
############################################################
#above program using lambda
val=lambda **data:sum(data.values())
val(a=2,b=3,c=4)
############################################################
#using list comprehenssion
person=lambda **data:[(i,j) for i,j in data.items()]
person(name='atharv',age=28,place='nagar')
##############################################################
#passing  list
lst1=[1,2,3,4]
sqr=lambda lst1:[i**2 for i in lst1]
print(sqr(lst1))
#############################################################










