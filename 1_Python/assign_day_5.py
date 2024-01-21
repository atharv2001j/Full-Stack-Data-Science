# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 16:49:05 2023

@author: Atharv
"""
#whether the year is leap year or not
def leap_year(year):
    if((year%400==0) and (year%100==0)):
       return True
    elif((year%4==0) and (year%100!=0)):
        return True
    else:
        return False
year=int(input("Enter the year: "))
leap_year(year)

#Generate and dislay password between 7 and 10 character
from random import randint
SHORTEST=7
LONGEST=10
MIN_ASCII=33
MAX_ASCII=126

#generate random password
def randomPassword():
    #select random length for password
    randomLength=randint(SHORTEST,LONGEST)
    result=' '
    for i in range(randomLength):
        randonChar=chr(randint(MIN_ASCII, MAX_ASCII))
        #CHR() take ascii andrandom character is generated
        result=result+randonChar
    return result

print("The random password is: ",randomPassword())   
    
#homework assignment
#fibbonacci series
def fibbp(n):
    lst=[]
    previous=0
    current=1
    lst.append(current)
    for i in range(n-1):
        previous,current=current,previous+current
        lst.append(current)
    return lst
print(fibbp(10))

##fibbonacci series using recursion

def fibonacciSeries(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return (fibonacciSeries(n - 1) + fibonacciSeries(n - 2))


n = int(input("Enter the range:"))
print("Fibonacci series:", end = ' ')
for n in range(0, n):  
   print(fibonacciSeries(n), end = ' ')
   
   
   
