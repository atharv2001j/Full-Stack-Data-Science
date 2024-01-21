# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 00:06:32 2023

@author: Atharv
"""

import random
import hashlib
import string

users=[]
passwords=[]
user_dic = {}

current_password = ""
#adding adjectives and noun for creating random password
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
#Checking role of user
def user_role():
    role=input("Enter the role of user: ")
    users_role=[]
    users_role.append(role)
   # print(users_role)
    for i in users_role:
        if i=='Admin':
            print("Hello Admin,Would you like to see status report?")
        elif(i=='Employee'):
            print("Hello employee")
        elif(i=='Manager'):
            print("Hello Manager")
        elif(i=='Worker'):
            print("Hello Worker")
        else:
            print("Hello Staff")
    

#checking a valid password
def check(password):
    
    if len(password) < 8:
        return False
    
    lower=False
    upper=False
    number=False
    special=False
    
    for ch in password:
        
        if ch>='a' and ch<='z':
            lower=True
        
        if ch>='A' and ch<='Z':
            upper=True
            
        if ch>='0' and ch<='9':
            number=True
            
        elif ch in string.punctuation:
            special=True
            
    if lower and upper and number and special:
        return True
    
    return False

#encoding password  in 32 bit
def encode_password(password):
    
    encode = hashlib.sha256(password.encode("utf-8")).hexdigest()
    return encode

#generating password
def generate_password():

    while True:
        
        adjective = random.choice(ad)
        nouns = random.choice(noun)
        special_char = random.choice(string.punctuation)
        number = str(random.randint(1,100))
        
        password = adjective + nouns + special_char + number
        
        if check(password):
            print(f" password: {password}, is strong!\n")
        else:
            print(f" password: {password}, is weak!\n")
            
        choice=input("do you want another password? (y/n): ")
        
        if choice == "n":
            return password
    
#check user and add new user if it not already exist
def add_new_user():
    new_user = input("\nenter a user name: ")
    while new_user in users:
        print()
        if new_user in users:
            print("user already exists, try another")
        new_user = input("enter a user name: ")

    users.append(new_user)
    
    print("\nuser registered successfully!\n")
    print("Please select a passwrod :")
    
    password = generate_password()
    
    encode = encode_password(password)
    
    users.append(new_user)
    passwords.append(encode)
    recent_password=password
    
    user_dic[new_user] = encode
    
    print("\nRegistration Successfull!")
    print("\n\nUser Information:-",new_user,":",recent_password,"\n\n")
    
def User_login():   
    
    count = 0
    
    while True:
        user = input("enter username: ")
        if user not in users:
            print("user not found!.....")
        elif count==3:
            count=0
            print("too many attempts, try after some time.")
        else:
            break
        count+=1
        
    count = 0
    attempt=False
    
    while True:
        password = input("enter password:")
        encode = encode_password(password)
        print(password,encode,"\n")
        if encode in passwords:
            if user_dic[user]==encode:
                attempt=True
                break
            else:
                print("invalid password\n")
        elif count==3:
            print("To many attempts.....Please try again")
            break
        else:
            print("Invalid password\n")
        count+=1
        
    if attempt:
        print("User Login Successfull!")
        user_role()
add_new_user()
User_login()
