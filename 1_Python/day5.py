# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 08:05:32 2023

@author: Atharv
"""
#get formatted name
def get_formated_name(first_name,last_name):
    full_name=f"{first_name} {last_name}"
    return full_name
musician=get_formated_name('Arijit', 'Singh')
print(musician)


#Returning Dictionary
def get_formated_name(first_name,last_name):
    full_name={'first':first_name,'last':last_name}
    return full_name
musician=get_formated_name('Arijit', 'Singh')
print(musician)


#passing a list

def greet_names(names):
    for i in names:
        msg=f"Hello,{i.title()}!"
        print(msg)
usernames=['Sanket','Yash',"Atharv"]
greet_names(usernames)

#passing an arbitari arguments
#in this we can pass one and more than one argument
def make_pizza(*toppings):
    print(toppings)
make_pizza('pepperoni')
make_pizza('onion','paneer','mushrooms','green papers')
 
#Now we can replace the pint() with loop
def make_pizza(*toppings):
    print("Making pizza with folllowing topppings: ")
    for i in toppings:
        print(f"- {i}")

make_pizza('pepperoni')
make_pizza('onion','paneer','mushrooms','green papers')
   
#Mixing positional and arbitari arguments
def make_pizza(size,*toppings):
    print(f"\nMaking a {size}-inch pizza with following toppings:")
    for i in toppings:
        print(f"-{i}")
make_pizza(12,'pepperoni')
make_pizza(16,'onion','paneer','mushrooms','green papers')
 
#importing module
#don't give the same name for the function if it is 
#already exists
#importing entired module
import pizza
pizza.make_pizza4(12,'pepperoni')
pizza.make_pizza4(16,'onion','paneer','mushrooms','green papers')
#importing speccific function from module
from pizza import make_pizza4
make_pizza4(12,'pepperoni')
make_pizza4(16,'onion','paneer','mushrooms','green papers')
#using as a alias funcction
from pizza import make_pizza4 as mp
mp(12,'pepperoni')
mp(16,'onion','paneer','mushrooms','green papers')

#importing all functions
from pizza import *
make_pizza4(12,'pepperoni')
make_pizza4(16,'onion','paneer','mushrooms','green papers')

