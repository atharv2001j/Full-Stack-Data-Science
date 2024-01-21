# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 08:07:36 2023

@author: Atharv
"""
#Accessing file using different wayys
import pandas as pd
df=pd.read_csv('C:/Atharv/buzzers.csv')
print(df)
#################################################################
import os
with open("buzzers.csv") as raw_data:
    print(raw_data.read())
#################################################################
#import csv  as list
import csv
with open("buzzers.csv") as raw_data:
    for i in csv.reader(raw_data):
        print(i)


#################################################################
#import csv in the form of dictionary
import csv
with open("buzzers.csv") as raw_data:
    for i in csv.DictReader(raw_data):
        print(i)
#############################################################
#separate the key value by commas
#in output we got \n


with open("buzzers.csv") as data:
    flights={}
    for line in data:
        k,v=line.split(',')
        flights[k]=v
flights
##############################################################
#stripping and then splitting
#It remove the \n fro the output using strip()
with open("buzzers.csv") as data:
    ignore=data.readline()
    flights={}
    for line in data:
        k,v=line.strip().split(',')
        flights[k]=v
flights
##############################################################
########################Decorators###################$$$
#Pre-requisite of decorator
def plus_one(num):
    number1=num + 1
    return number1
plus_one(5)
######################################
#Function inside function
def plus_one(num):#1st
    def add_one(num):#3rd
        number1=num+1 
        return number1
    result=add_one(num)#2nd
    return result#4th
plus_one(5)
######################################
#Passing Function as Arguments
#to other Functions
def plus_one(num):
    result1=num + 1 
    return result1
def function_call(function):
    result=function(5)
    return result
function_call(plus_one)
#plus_one==function as a parameter
#######################################
#Function returning other funtion
def hello_function():
    def say_hi():
        return "Hi"
    return say_hi
hello=hello_function()
#If function returning function then we have to store that
#function in variable then we have to call that function
hello()








