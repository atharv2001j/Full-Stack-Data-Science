# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 08:12:59 2023

@author: atharv
"""
num=int(input("Enter a Number: "))
for i in range(1,10):
    if i==num:
        break
    print(i,'',end='')
print("done")  #done will print after final execution 
    
num=int(input("Enter a Number: "))
for i in range(1,10):
    if i==num:
        break
    print(i,'',end='')
    print("Done")#Done will print after every execution


###############collections################
#create tuple
tup1=(1,2,3,4)
print(f"tup[0]={tup1[0]}")
print(f"tup[1]={tup1[1]}")
print(f"tup[2]={tup1[2]}")
print(f"tup[2]={tup1[3]}")

#accessing tuple values
tupl=('orange','mango','grpes','banana')
for i in tupl:
    print(i)
#accessing using range function
tupl=('orange','mango','grpes','banana')
#
for i in range(4):
    print(tupl[i])
#Tuple related functions
len(tupl)
tup1=('orange','mango','grpes','banana','apple')
tup1.count("apple")
print(tup1.index("apple"))
if 'apple' in tup1:
    print("Apple in tuple")

#Nested tuple
a=(1,2,3,4,5)
b=('apple','orange')
c=(10,a,b,'atharv')
print(c)
#list
lst=['john','reo','nilesh','yash',True]
lst1=[1,2,3,4,4,'Roham']
print(lst1[-1:-3])#it will show blank list
print(lst1[-3:-1])
root_list=[11,12,lst,lst1]
print(root_list)
print(lst[1])
print(lst[-1])
l=lst+lst1
print(l)
#append function
print(lst.append("sanket"))
print(lst)
#extend function
lst.extend(['hi','sorry'])
print(lst)
#remove function
lst.remove('sorry')
print(lst)
#insert function
lst.insert(1,'paresh')
print(lst)
#sorted function
lst=['john','reo','nilesh','yash']#sorted function does not solved the boolean function
sorted(lst)
print(lst)
#sum fiunction
lst2=[1,2,3,4,5,6]
print(sum(lst2))
#max function
print(max(lst2))
#pop()  method
#in this we have to give index
lst2.pop(2)
print(lst2)

#Creating set
basket={'atharv','apple','orange','apple','mango'}
print(basket)
#accessing elements in set
for i in basket:
    print(i,end=' ')
#Adding items in set
basket.add('nilesh') #adding one element
print(basket)
#Adding more than one
basket.update(['yash','Sanket','adi','Paresh'])
print(basket)

#obtening length of set
print(len(basket))
#Obtaining min and max from set
basket={1,2,3,4,5,11,9}
print(max(basket))
print(min(basket))
#remove 
basket.remove(2)
print(basket)
basket.discard(5)
print(basket)
#Set Operations
s1={'atharv','yash','sanket'}
s2={'atharv','adi','paresh'}
#union
print('Union:',s1|s2)
#intersection
print('Intersection:',s1&s2)
#Difference
print('Difference:',s1-s2)
#############Dictionaries###########
capitals={'Maharastra':'Mumbai','Gujrat':'Ahmadabad','UP':'Lakhnow'
          ,'Karnataka':'Bangolore'}
#accessing the data
print('capitals[Maharastra]:',capitals['Maharastra'])
#adding new data
capitals['West_Bengal']='Kolkata'
print(capitals)
#removing
capitals.pop('West_Bengal')
print(capitals)

del capitals['UP']
print(capitals)
#chnging key values
capitals['Gujrat']='Gandhinagar'
print(capitals)
#Iterating over keys
capitals={'Maharastra':'Mumbai','Gujrat':'Ahmadabad','UP':'Lakhnow'
          ,'Karnataka':'Bangolore'}
for states in capitals:
    print(states,end=' ')
for states in capitals:
    print(states,end=' ')
    print(capitals[states])
#value keys and iems
print(capitals.keys())
print(capitals.values())
print(capitals.items())
#checking the members
print('Karnataka' in capitals)
print('Bihar' not in capitals)
#Obtaining length of dict.
print(len(capitals))
#Dictionary can have values in tuple
seasons={'Summer':('feb','march','april','may'),
         'Rainy':('june','july','august','sept'),
         'Winter':('Oct','Nov','dec','jan')}
print(seasons['Rainy'])
#we can also use list insted of tuple if we want to change
#the values in future
season={'Summer':['feb','march','april','may'],
         'Rainy':['june','july','august','sept'],
         'Winter':['Oct','Nov','dec','jan']}
print(season['Rainy'])
#you can access the particular value of the list or tuple
print(season['Rainy'][1])
print(seasons['Rainy'][1])
#Dictionary Methods
capitals={'Maharastra':'Mumbai','Gujrat':'Ahmadabad','UP':'Lakhnow'
          ,'Karnataka':'Bangolore'}
#get() method to access the value of keys in dict.
print(capitals.get('UP'))
#Duplicates are not allow duplicates it will take only one value
dict2={'brand':'Maruti',
       'model':'Brezza',
       'year':2020,
       'year':2021,
       'year':2022}
print(dict2)
#it only take the value which is declare at last
#loop throough dict.
#show only one element
for i in dict2:
    print(i)
#print all values in  dict.
for i in dict2:
    print(dict2[i])
#we can also use value() method to return values
for i in dict2.values():
    print(i)
#we can also use keys() mehod to access keys
for i in dict2.keys():
    print(i)
#loop both through keys and values
for i,j in dict2.items():
    print(i,j)
#copy dict.
my_dict=dict2.copy()
print(my_dict)
