# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 08:09:05 2023

@author: Atharv
"""
#function
def prime_no(num):
    for i in range(2,num):
        if(num%i==0):
            return "The number is not Prime"
            break
    return "The number is prime"
print(prime_no(15))

#without pssing argument
def greed_user():
    print("Hello")
greed_user()
#passing argument
def greed_user(username):
    print(f'hello {username}')
greed_user('atharv')

#positonal argument and arbitari argument
#orders matter in positonal argument
def describe_pet(animal_type,name):
    print(f"{animal_type}")
    print(f"{name}")
describe_pet('dog','Moti')
#default value parameter
def describ_pet(animal_type,name='Moti'):
    print(f"{animal_type}")
    print(f"{name}")
describ_pet('dog')
#Anagram or not
#if both string contain same characters
def are_anagram(str1,str2):
    a=list(str1.replace("","").lower())
    b=list(str2.replace("","").lower())
    if (len(a)!=len(b)):
        return False
    else:
        return (sorted(a)==sorted(b))

str1=input("Enter the str1: ")
str2=input("Enter the str2:  ")
are_anagram(str1, str2)

#asssignment 2
#calculate sum which is divisible by 5&7
def cal_sum(lst):
    sum=0
    for i in range(len(lst)):
        if(lst[i]%5==0 or lst[i]%7==0):
            sum=sum+lst[i]
    return sum
lst=[1,2,5,10,7,49]
cal_sum(lst)
#using and function
def cal_sum(lst):
    sum=0
    for i in range(len(lst)):
        if(lst[i]%5==0 and lst[i]%7==0):
            sum=sum+lst[i]
    return sum
lst=[1,2,5,10,7,49,70]
cal_sum(lst)
#Homework Assignment
#write a function to reverse the sentence
def reverse_word(input):
    if input==" ":
        return "You entered wrong input"
    else:
        words=input.split()
        reverse_sentence=" ".join(reversed(words))
        
    return reverse_sentence
print(reverse_word("My name is atharv"))












