# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 16:42:44 2023

@author: Atharv
"""
#assignment 1
#generating random number for lottery number
from random import randrange
MIN_NUM=1
MAX_NUM=49
NUM_NUMS=6
ticket_nums=[]
for i in range(NUM_NUMS):
    #generate the number which is not in list
    rand=randrange(MIN_NUM,MAX_NUM+1)
    #to check whether the number is unique or not
    while rand in ticket_nums:
        rand=randrange(MIN_NUM,MAX_NUM+1)
        #add distinct number to the lisst
    ticket_nums.append(rand)
ticket_nums.sort()
for i in ticket_nums:
    print(i,end=" ")

#write a python code to remove outliers(remove extream numbers)
values=[89,105,1,2,5,6,7]
retval=sorted(values)
def removeOutliers(data,num_outliers):
    retval=sorted(data)
    for i in range(num_outliers):
        retval.pop(-1)
    return retval
removeOutliers(values, 3)



#homework assignment
#Write python code that determines whether the password is good or bad
#1.It must have 8 characters
#2.It  must haveat least one upper case
#3.one lower case 
def checkPassword(n):
    has_lower=False
    has_upper=False
    has_number=False
    for i in n:
        if(i>='A' and i<='Z'):
            has_upper=True
        elif(i>='a' and i<='z'):
            has_lower=True
        else:
            has_number=True
    if(len(n)>=8 and (has_lower and has_upper and has_number)==True):
        return True
    return False
p=input("Enter a password: ")
if(checkPassword(p)):
    print("Good Password")
else:
    print("Bad Password")
        
    


