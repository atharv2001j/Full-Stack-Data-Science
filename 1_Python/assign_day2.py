# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 16:49:10 2023

@author: atharv
"""

# calculate BMI
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
# round is used to give the upto deciaml value
BMI = round((weight/(height*height)), 2)
print("BMI is :", BMI)
if BMI < 18.5:
    print(f"You are under weight and your BMI is:{BMI}")
elif BMI > 18.5 and BMI < 25:
    print(f"You are normal weight and your BMI is:{BMI}")
elif BMI > 25 and BMI < 30:
    print(f"You are over weight and your BMI is :{BMI}")
elif BMI > 30 and BMI < 35:
    print(f"You are obese and your BMI is:{BMI}")
elif BMI > 35:
    print(f"You clinically obese and your BMI is:{BMI}")

"""
write python code  for roller coster
@author atharv
"""
print("Welcome to roller coaster")
height = int(input("Please enter your height in cm: "))
if height > 120:
    print("you r eligible for coastel ride ")
    age = int(input("Enter your age in kg: "))
    bill = 0
    if age < 12:
        print("Your ticket is $5")
        bill = 5
    elif age >= 12 and age < 18:
        print("your bill is $7")
        bill = 7
    elif age >= 18 and age < 45:
        print("Your ticket is $12")
        bill = 12
    elif age >= 45 and age < 55:
        print("Your ticket is $50")
        bill = 50
    want_photo = input("Do you want the photos(Y/N): ")
    if want_photo == 'Y':
        bill = bill+3
        print("Your bill is:", bill)
    else:
        print("Your bill is: ", bill)
