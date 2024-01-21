# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 16:47:13 2023

@author: atharv
"""
#assignment 1 whether it is duplicate or not
#for consecutive similar
lst1=[1,2,7,3,4,5,1]
def is_duplicate(lst1):
    for i in range(len(lst1)-1):
        if(lst1[i]==lst1[i+1]):
            return True
    return False

print(is_duplicate(lst1))
#for all test cases
def dup(lst1):
    for i in range(0,len(lst1)):
        for j in range(i+1,len(lst1)):
            if(lst1[i]==lst1[j]):
                return True
    return False
print(dup(lst1))

# assignment 2 mario pyramid
for i in range(4):
    for j in range(4):
        print("#",end=" ")
    print()

for i in range(4):
   for j in range(i+1):
      print("#",end=" ")
   print()
        
            
for i in range(4):
   for j in range(4-i):
       print("#",end=" ")
   print()



#asssignment 1 check whwther given text is palindrome or not 
s=input("Enter a text: ")
if s==s[::-1]:
    print("palindrome")
else:
    print("Not Palindrome")

#assignment 2
#calculate min and max from the list
def max_list(lst):
    max_val=lst[0]
    for i in lst:
        if i>max_val:
            max_val=i
    return max_val


def min_list(lst):
    min_val=lst[0]
    for i in lst:
        if i<min_val:
            min_val=i
    return min_val
lst=[1,2,3,4,5,144,7,8]
print("Maximum from the list is:",max_list(lst))
print("Minimum from the list is:",min_list(lst))

#diamond pattern
rows=int(input("Enter the no of rows: "))
#upper part
for i in range(1,rows):
    for j in range(1,rows-i):
        print(' ',end='')
    for j in range(0,2*i-1):
        print('*',end='')
    print()
    
#lower part
for i in range(rows-2,0,-1):
    for j in range(1,rows-i):
        print(' ',end='')
    for j in range(1,2*i):
        print('*',end='')
    print()

        
        
    
