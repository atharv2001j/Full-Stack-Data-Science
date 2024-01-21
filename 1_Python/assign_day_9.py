# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 19:41:54 2023

@author: Lenovo
"""
ad=[]
for i in range(0,4):
    adj=input("Enter the adjective:")
    ad.append(adj)  
print(ad)
noun=[]
for i in range(0,4):
    nou=input("Enter the noun:")
    noun.append(nou)
   
print(noun)

import random
import string
#select adjective
adject=random.choice(ad)
#select noun
nouns=random.choice(noun)
#select number
number=random.randint(0,100)#we can use randrange()
#special character
spc_char=random.choice(string.punctuation)
#Creating a password
password=adject + nouns + str(number) + spc_char
print("The new password is:%s" % password)  
def checkPassword(n):
    has_lower=False
    has_upper=False
    has_number=False
    has_spc=False
    for i in n:
        if(i>='A' and i<='Z'):
            has_upper=True
        elif(i>='a' and i<='z'):
            has_lower=True
        elif(i>='0' and i<='9'):
            has_number=True
        else:
            has_spc=True
    if(len(n)>=8 and (has_lower and has_upper and has_number and has_spc )==True):
        return True
    return False

if(checkPassword(password)):
    print("Good Password")
else:
    print("Bad Password")
        
       
    