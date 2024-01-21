# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 08:11:04 2023

@author: Lenovo
"""

#complex number
c1=2
c2=2j
print('c1:',c1,',c2:',c2)
print(type(c1))
print(type(c2))
print(c1.real)
print(c2.imag)
print(c1+c2)

#boolean values
#true or false
all_ok=True
print(all_ok)
all_ok=False
print(all_ok)
print(type(all_ok))
#convert sring to bolean
status=bool(input("OK it is confirmed:"))
print(status)
print(type(status))
#Arithemetic  Operator
home=100
away=20
a=print(home+away)
print(type(a))
b=print(home*away)
print(type(b))
c=print(home/away)
print(type(c))
print(home-away)
print(home//away)
print(type(home//away))
print(100%13)
print(type(3%2))
#power operator
a=5
b=3
print(a**b)
#assignment operator
x=0
x+=1  #has same as x=x+1
x-=1 #has same has x=x-1
#None type
#NoneType
winner=None
print(winner is None) #is operator to check whether it is true or false
print(winner is not None)#is not operator it is true or false
print(type(winner))
#comparison Oerator

num=int(input("Enter a number:"))
if num > 66: 
    print(num)
else:
    print("Not greater then 66")

#elif
savings=float(input("enter your savingd:"))
if savings==0:
    print("sorry no savings")
elif savings<500:
    print("well done")
elif savings<1000:
    print("thats a tidy sum")
elif savings<10000:
    print("welcome sir!")
else:
    print("Thank You")
    
#iterating loop
#while loop
count=0
print("Starrting")
while count<10:
    print(count)
    count= count+1
#for loop
#it will print upto n-1
print("Print out values in a range")
num=int(input("Enter a number:"))
for i in range(0,10):
    if(i==num):
        break
    print(i)
print('Done')

#anonymous loop variable
for _ in range(0,10): # _ anonymous variable
    print('.',end='')
   # print() for horizontal result