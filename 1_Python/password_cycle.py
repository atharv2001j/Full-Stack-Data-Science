# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 19:58:59 2023

@author: atharv
"""
lst=[]
def random_password():
    new_users=['Avi','kumar','Krishna','Atharv','Yash']
    adjectives=['yellow','orange','green','yellow','pink','blue',
                'slow','fast']
    import random
    import string
    #select adjective
    adject=random.choice(adjectives)
    #select noun
    nouns=random.choice(new_users)
    #select number
    number=random.randint(0,100)#we can use randrange()
    #special character
    spc_char=random.choice(string.punctuation)
    #Creating a password
    password=adject + nouns + str(number) + spc_char
    print(password)
    #checking of password whey=ther it is good or bad
    chosen_password=""
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
    import hashlib
    chosen_password = password
    lst_hash=hashlib.sha256(password.encode('utf-8')).hexdigest()
    lst.append(lst_hash)
    #print(lst)        
        
    #print("The new password is:%s" % password)
    #choice=input("If you want to generaate more password(Y/N): ")
#random_password() 
#lst=[] 
n=int(input("Enter the number of password do you want:"))
for i in range(n):
    rand=random_password()
#print(lst)
#Taking input from user as username and password
count=0
password_user=""
user=""

user=input("Enter the username: ")

while True:
    
    if count==3:
        print("Too many attempts, try after some time.")
        break
        
    password_user=input("Enter the password:")
    #for storing password in the form of hash code
    
    if password_user == chosen_password:
        print("login successfull!")
    
    count+=1
    print(count)


#lists for username and password
#print(lst2)
lst1=[]
#for storing the username
lst2=[]
lst2.append(user)


import hashlib
lst_hash=hashlib.sha256(password_user.encode('utf-8')).hexdigest()
lst1.append(lst_hash)
#print(lst1)
#check whether the password and username enter by the user are
#acceptable or not
new_users=['Avi','kumar','Krishna','Atharv','Yash']
for i in lst2:
    c=False
    if i in new_users:
        print("Username is correct you can proceed further..")
        c= True
    else:
        print("Invalid username.....")
for i in lst1:
    m=False
    if i in lst:
        print("Password is correct you can proceed further..")
        m=True
    else:
        print("Invalid password.....")
        m=False
if(c==True and m==True):
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

    
