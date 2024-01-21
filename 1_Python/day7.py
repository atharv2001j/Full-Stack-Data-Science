# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 09:13:17 2023

@author: Atharv
"""
#Exception handling
#try and exception block
try:
    print(5/0)
except ZeroDivisionError:
    print("we can't divide it by zero")

#using exception to prevent crashes
print("Give me two number")
print("Enter 'q' to quit")
while True:
    first_num=input("enter first number: ")
    if first_num=='q':
        break
    second_num=input("Enter second number: ")
    if second_num=='q':
        break
    ans=int(first_num)/int(second_num)
    print(ans)
#file not found error
filename='alice.txt'
try:
    with open(filename,encoding='utf-8') as f:
        contents=f.read()
except FileNotFoundError:
    print(f"Sorry,the file {filename} does not exist")
    
        


