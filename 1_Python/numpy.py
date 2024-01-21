# -*- coding: utf-8 -*-
"""
Created on Wed May 10 15:30:21 2023

@author: Atharv
"""
import numpy as np
arr1=np.array([7,20,30])
arr1=np.array([7,20,30])

arr1
arr1.dtype
#multidimentional array
arr3=np.array([[1,2,3],[4,5,6]])
arr3
#or
arr3=np.array([1,2,3,4,5,6],ndmin=2)
arr3
arr3=np.array([1,2,3,4,5,6],ndmin=3)
arr3
#change the datatttype of array
arr1=np.array([7,20,30],dtype=complex)
arr1
#findout dimensions of array
arr3=np.array([[1,2,3],[4,5,6]])
print(arr3.ndim)
arr3
#finding the size of each item in the array
arr=np.array([10,20,30])
print("Each item contains in byte: ",arr.itemsize)
print("Each size contains in byte: ",arr.dtype)
#get the shape and size  of an array
arr3=np.array([[1,2,3],[4,5,6]])
print("Array size:",arr3.size)
print("Array shape:",arr3.shape)
#array with specific datatype
arr3=np.array([[1,2,3],[4,5,6]],dtype='float')
arr3
#Create sequence of number
arr1=np.arange(0,20,2)
arr1
#Acess single element
arr1=np.arange(10)
arr1
#Accessing array elemens
arr1[2]
arr1[-2]

arr3=np.array([[1,2,3],[4,5,6]])
arr3.shape
arr3[0,1]
arr3[1,-1]
#access array element using slicing
arr=np.array([0,1,2,3,4,5,6,7,8,9])
x=arr[1:8:2]
x
arr[-2:3:-1] #start last but one(-2) upto 3 but not 3 in step 
arr[-2:10]#start last but one -2 upto 10 but not 10
############################
arr=np.array([[10,20,30],
              [1,2,3],
              [4,5,6]])
arr
arr[1,2]
arr[:,1]
arr[1,:]
arr[:3,::2]
#Integer array indexing
arrr=np.arange(35).reshape(5,7)
arrr
##############################################################################
arr=np.arange(12).reshape(3,4)
arr
rows=np.array([False,True,True])
wanted_rows=arr[rows,:]
wanted_rows
#convert numpy array to list
arr=np.array([10,20,30,40])
arr
print(type(arr))
#convert it to list
list=arr.tolist()
list
print(type(list))

#multidimensional tolist
arr3=np.array([[1,2,3],[4,5,6]])
lst=arr3.tolist()
print('list:',lst)
#############################################
#convert  python list  to array
lst=[20,40,60,80]
arr=np.array(lst)
arr
#anoter method
arr=np.asarray(lst)
arr
###########################################
#numpy proprties
#Shape
arr=np.array([10,20,30,40])
arr.shape


#Resize array
arr3=np.array([[1,2,3],[4,5,6]])
arr3.shape=(3,2)
arr3
#Rshape
arr3=np.array([[1,2,3],[4,5,6]])
arr4=arr3.reshape(3,2)
arr4
#ndim
arr3=np.array([[1,2,3],[4,5,6]])
print(arr3.ndim)
#######################################################################
#Arithemetic operations with array
arr1=np.arange(16).reshape(4,4)
arr2=np.array([10,29,30,40])
new_array=np.add(arr1,arr2)
new_array
new_array=np.subtract(arr1,arr2)
new_array
new_array=np.multiply(arr1,arr2)
new_array
new_array=np.divide(arr1,arr2)
new_array
############################3


#Reciprocal 
arr1=np.array([10,2,34,5,6])
rep_array=np.reciprocal(arr1)
rep_array

#numpy power
arr1=np.array([1,2,3])
arr2=np.power(arr1,3)
arr2
#power of matrix
arr1=np.array([10,2,34,5,6])
arr2=np.array([1,2,3,4,5])
pow_arr2=np.power(arr1,arr2)
pow_arr2
arr1=np.array([10,2,34,5,6])
arr2=np.array([1,2,3,4,5])
mod_arr2=np.mod(arr1,arr2)
mod_arr2
#create an empty array
from numpy import empty
a=empty([3,3])
a
#create  zeros array
from numpy import zeros
a=zeros([3,4])
a
#create one array
from numpy import ones
a=ones([2,3])
a
#create array with vstack
from numpy import array
from numpy import vstack
from numpy import hstack
a1=array([1,2,3])
a1
a2=array([4,5,6])
a2
#vertical array
a3=vstack((a1,a2))
a3
print(a3.shape)
#horinzontal array
a3=hstack((a1,a2))
a3
##############################################
#index array  out of bound
from numpy import array
data=array([11,22,33,44,55])
print(data[5])
#negative array indexing
data=array([11,22,33,44,55])
data[-1]
data[-2]
#index row of two dimentional array
from numpy import array
data=array([[11,22],[33,44],[55,66],[77,88]])
data[0,]#0th row an all column
##################################################################
#split input and output data
from numpy import array
data=array([[11,22,33],[44,35,66],[77,88,99]])
X,y=data[:,:-1],data[:,-1]
X
y
######################################
#Broadcast scalar to one-dimensional array
#To add pixel in image during ML
a=array([2,6,8,9])
print(a)

b=2
print(a)

c=a+b
print(c)
##############################3##
#Vector addtion
#addition two matrix
#c=a+b
#Vector subtraction c=a-b
#################################
#Vector L1 norm/manhatten distance
from numpy import array
from numpy.linalg import norm
a=array([1,2,3])
l1=norm(a,1)
print(l1)
#vector L2 norm/Euclidean norm
l2=norm(a)
l2
##########################
#Triangular matrices
from numpy import tril
from numpy import triu
n=array([[1,2,3],[1,2,3],[1,2,3]])
lower=tril(n)
lower
upper=triu(n)
upper
#########################
#Diagonal matrix
from numpy  import diag
n=array([[1,2,3],[1,2,3],[1,2,3]])
#extract diagonal vactor
d=diag(n)
d
#create diagonal matrix fromvector
D=diag(d)
D
##############################################################
#identity matrix
from numpy import identity
I=identity(3)
I
###################33###
#orthogonal matrix
from numpy.linalg import inv
Q=array([[1,0],
        [0,-1]])
print(Q)
#inverse equivalence
V=inv(Q)
print(Q.T)
print(V)
#identity equivalence
I=Q.dot(Q.T)
print(I)

















