# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 08:43:26 2023

@author: Atharv
"""
####################Generator##################################

#generator without function
gen=(x for x in range(3))
print(gen)
#here gen is behave as a object
for i in gen:
    print(i)
    
#########################
gen=(x for x in range(3))
next(gen)
#next(gen)
#next(gen)
#next(gen)
#########################
#Generator using function
def range_even(end):
    for num in range(0,end,2):
        yield num
        #returning value and object of funcion
for num in range_even(6):
    print(num)
#########################
#instead of for loop we can write next()
gen=range_even(6)
next(gen)
#########################
#Chaining Generator
def lengths(itr):
    for ele in itr:
        yield len(ele)

def hide(itr):
    for ele in itr:
        yield ele*'*'

passwords=['not-good','give m-pass']
for password in hide(lengths(passwords)):
    print(password)
    
##############################################################
#priting list with index
lst=['milk','Bread','Dahi']
for i in range(len(lst)):
    print(f"{i+1} {lst[i]}")
##############################################################
#another methode is using enumerator
for i,j in enumerate(lst,start=1):
    print(i,j)
############################################################
#zip function()
#it is used to access more than one list
lst1=['dada','mama','kaka','kaku']
lst2=[1234,1456,5634,8765]
for i,j in zip(lst1,lst2):
    print(i,j)
###########################################################
#drawback of zip()
lst1=['dada','mama','kaka','kaku','mami']
lst2=[1234,1456,5634,8765]
for i,j in zip(lst1,lst2):
    print(i,j)
##############################################################
#it will print None for mismatched value
from itertools import zip_longest
lst1=['dada','mama','kaka','kaku','mami']
lst2=[1234,1456,5634,8765]
for i,j in zip_longest(lst1,lst2):
    print(i,j)
############################################################
#It will print zero for mismatched value
from itertools import zip_longest
lst1=['dada','mama','kaka','kaku','mami']
lst2=[1234,1456,5634,8765]
for i,j in zip_longest(lst1,lst2,fillvalue=0):
    print(i,j)
#############################################################
lst=[1,2,3,4,5]
if all(lst):
    print("All values are True")
else:
    print("Useless")
###########################################################
#any() to check NOT NULL value
lst=[1,0,0,0]
if any(lst):
    print("it having some value")
else:
    print("Useless")
##########################################################
lst=[0,0,0,0]
if any(lst):
    print("It havingsome value")
else:
    print("Useless")
#############################################################
# count()
from itertools import count
counter=count()
print(counter)
print(next(counter))
###########################################################
from itertools import count
counter=count(start=1)
print(next(counter))
print(next(counter))
############################################################
#It will check whether list cotain NULL/0 value
lst=[1,2,3,4,5,0]
if all(lst):
    print("All values are True")
else:
    print("Useless")
##########################################################
#cycle() function to execute the task periodically
import itertools
instructions=['eat','code','sleep']
for i in itertools.cycle(instructions):
    print(i)
############################################################
#repeat() is used to repeat somehing
from itertools import repeat
for i in repeat('keep patience',times=3):
    print(i)
#############################################################
#group()
from itertools import combinations
players=['joy','jony','janardhan']
for i in combinations(players, 2):
    print(i)


##############################################################
#password ticker
import string
adjectives=['yellow','orange','green','yellow','pink','blue',
            'slow','fast']
nouns=['amit','atharv','yash','sanket','adi','paresh',
       'nilesh','om']
#pick the word
import random
import string
#select adjective
adjective=random.choice(adjectives)
#select noun
noun=random.choice(nouns)
#select number
number=random.randint(0,100)#we can use randrange()
#special character
spc_char=random.choice(string.punctuation)
#Creating a password
password=adjective + noun + str(number) + spc_char
print("The new password is:%s" % password)

#######################################################
#generate more than one password
while True:
    adjective=random.choice(adjectives)
    noun=random.choice(nouns)
    number=random.randrange(0,100)
    spc_char=random.choice(string.punctuation)
    password=adjective + noun + str(number) + spc_char
    print("The new password is:%s" % password)
    res=input("Would yu like more password?")
    if res=='n':
        break
#####################################################

for i in range(0,4):
    adj=input("Enter the adjective:")
    adjectives.append(adj)
   
print(adjectives)
for i in range(0,4):
    nou=input("Enter the noun:")
    nouns.append(nou)
   
print(nouns)

import random
import string
#select adjective
adjective=random.choice(adjectives)
#select noun
noun=random.choice(nouns)
#select number
number=random.randint(0,100)#we can use randrange()
#special character
spc_char=random.choice(string.punctuation)
#Creating a password
password=adjective + noun + str(number) + spc_char
print("The new password is:%s" % password)  
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

if(checkPassword(password)):
    print("Good Password")
else:
    print("Bad Password")
        
       
    

    
    
    
    
    