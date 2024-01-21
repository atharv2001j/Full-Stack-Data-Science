# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 09:26:34 2023

@author: Atharv
"""
def make_pizza4(size,*toppings):
    print(f"\nMaking a {size}-inch pizza with following toppings:")
    for i in toppings:
        print(f"-{i}")
