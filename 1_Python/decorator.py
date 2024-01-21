
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 08:23:11 2023

@author:Atharv
"""
#############################Decorators#########################
#Prerequisite to decorator
def plus_one(num):
    num1=num+1
    return num1
plus_one(6)
############
#Defining function inside function
def plus_one(num):
    def add_one(num):
        num1=num+1
        return num1
    result=add_one(num)
    return result
plus_one(6)
##############
#Passing function as a argument
def plus_one(num):
    num1=num+1
    return num1

def function_call(plus_one):
    result=plus_one(6)
    return result

function_call(plus_one)
#####################
#Function returning other function
def hello_function():
    def say_hi():
        return "HI"
    return say_hi
hello=hello_function()#You have to assign that function to variable because without assigning variable
#it simply create an object .to access that object we have to assign a vaariable
hello()#call that variable as a function 

#####################
#A python decorator we can call function with some additional functionalities
def say_hi():
    return "hello Atharv"

def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper
decorate=uppercase_decorator(say_hi)
decorate() 
 
#####################
#We simply add @ before the function we had like to decorate a function
@uppercase_decorator
def say_hi():
    return "good morning"
say_hi()
#You have to execute full code not line by line
#######################
#Applying multiple decorator to single function
def split_string(function):
    def wrapper():
        func=function()
        splitted_string=func.split()
        return splitted_string
    return wrapper

@split_string
@uppercase_decorator
def say_hi():
    return "good morning"
say_hi()

#############################

num=[2,6,7,8]
def cal_square(num):
    result=[]
    for i in num:
        result.append(i*i)
    return result

def cal_cube(num):
    result=[]
    for i in num:
        result.append(i*i*i)
    return result

print(cal_cube(num))
print(cal_square(num))

############################3
#To check how much time processor require to execute
#Estimation of execution
import time
def cal_square(num):
    start=time.time()
    result=[]
    for i in num:
        result.append(i*i)
    end=time.time()
    print((end-start)*1000)
    print("took "+str((end-start)*1000)+"mil sec")
    return result
array=range(1,10000)
out_square=cal_square(array)

def cal_cube(num):
    start=time.time()
    result=[]
    for i in num:
        result.append(i*i*i)
    end=time.time()
    print((end-start)*1000)
    print("took "+str((end-start)*1000)+"mil sec")
    return result
array=range(1,10000)
out_cube=cal_cube(array)
##############################3
#Use decorator to above two functions
import time
def time_it(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print("took "+str((end-start)*1000)+"mil sec")
        return result
    return wrapper
@time_it 
def cal_square(numbers):
    result=[]
    for number in numbers:
        result.append(number*number)
    return result
@time_it 
def cal_cube(numbers):
    result=[]
    for number in numbers:
        result.append(number*number*number)
    return result
array = range(1,100000)
out_square = cal_square(array)
out_cube = cal_cube(array)
#########################################





































    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    