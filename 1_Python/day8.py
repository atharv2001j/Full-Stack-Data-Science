
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 08:35:10 2023

@author: Atharv
"""
###################Storing data#####################3
#working with JSON file
import json
num=[2,3,4,5,7,11,13]
filename='num.json'
with open(filename,'w') as f:
    json.dump(num,f)

#Saving data with json file is useful
import json
username=input("Enter your name: ")
filename='username.json'
with open(filename,'w') as f:
    json.dump(username,f)
print(f"we'll remember you when you back ,{username}!")

# greet a user which is already stored
import json
filename='username.json'
with open(filename) as f:
    username=json.load(f)
print(f"Welcome back,{username}")


###try and except
import json
filename='username.json'
try:
    with open(filename) as f:
        username=json.load(f)
except:
    username=input("Enter your name: ")
    filename='username.json'
    with open(filename,'w') as f:
        json.dump(username,f)
    print(f"we'll remember you when you back ,{username}!")
else:#it will executed when there is no error
    print(f"Welcome back,{username}!")
finally:#it will executed each time
    print("completed")

###List comprehension
lst=[]
for i in range(0,20):
    lst.append(i)
print(lst)

#using list comprehenssion
lst=[i for i in range(0,20)]
print(lst)

names=['dada','mama','kaka']
lst=[name.capitalize() for name in names]
print(lst)
    
names=['dada','mama','kaka']
lst=[name.upper() for name in names]
print(lst)

#list comprehension with if else
def is_even(num):
    return num%2==0
lst=[num for num in range(10) if is_even(num)]
print(lst)    
###############################################################
lst=[f"{x}{y}"
    for x in range(3)
    for y in range(3)]
print(lst)

lst=[f"{x}{y}{z}"
    for x in range(3)
    for y in range(3)
    for z in range(3)]
print(lst)

###################set comprehension##########################
lst={x for x in range(3)}
print(lst)

######################3Dictionary comprehension##############
dict={x:x*x
      for x in range(3)}
print(dict)
#############################################################














