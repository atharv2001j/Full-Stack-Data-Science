# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 16:52:56 2023

@author: Atharv
"""
users=['Admin','Employee','Manager','Worker','Staff']
for i in users:
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
##############################################################
current_users=['avi','yash','atharv','sanket','aniket']
new_users=['avi','kumar','krishna','atharv','yash']
for i in new_users:
    if i in current_users:
        print("User has to enter new user name")
    else:
        print("You got your Username")
#############################################################
import hashlib
hashlib.sha256("Atharv@321".encode('utf-8')).hexdigest()
len(hashlib.sha256("Atharv@321".encode('utf-8')).digest())




