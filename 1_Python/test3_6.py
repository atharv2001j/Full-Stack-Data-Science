# -*- coding: utf-8 -*-
"""
Created on Wed May 31 09:34:45 2023

@author: Atharv
"""
import numpy as np
print(np.__version__)
print(np.show_config())
#################
#Write a program tget help with add function
print(np.info(np.add))
##################
print(np.info(np.dot))
print(np.info(np.transpose))
##################
#test none of element is zero
x=np.array([1,2,3,4,5])
print("Test the array")
print(np.all(x))
print(np.info())
################
y=np.array([0,1,2,3,4])
print(np.all(y))
###################
#Tesst the non-zero element
print(np.any(y))
########################3
z=np.array([0,0,0])
print(np.any(z))
####################
#for finite list
s=np.array([1,0,np.nan,np.inf])
print(np.isfinite(s))
##################
#check complex,real
a=np.array([1+1j,1+0j,4.5,3,2,1])
print(np.iscomplex(a))
##################
print(np.isreal(a))
####################

print(np.isscalar(a))
print(np.isscalar(3.5))
print(np.isscalar([3.1]))
###################
a=[[1,2,3],[3,5,8.9]]
b=np.array(a)
b.ndim
#2------->vector
#n------->tensar
####################
b.shape
b.size
###############
b[1][2]
b[1][2]
b[1,2]
b[0,0:2]
#access the 1 and 2 row  and 3rd column
b[0:2, 2]
##############
#Basic Operations
x=np.array([[1,2],[3,4]])
x
###################
y=np.array([[2,1],[5,6]])
y
####################
c=np.add(x,y)
c
d=np.multiply(x,y)
d
#or
d=np.dot(x,y)
d
##########
#calculate sine of object
e=np.sin(d)
e
#########
#Calculate traanspose of mattrix
c=np.array([[1,1],[2,3],[3,3]])
np.transpose(c)
#Or
c.T
#######################
#Outer product
result = np.outer(x,y)
print(result)
#####################
#Cross products
"""the dot product results in a scalar quantity, 
which indicates magnitude but not direction, 
while the cross product results in a vector, 
which indicates magnitude and direction."""

re1=np.cross(x, y)
re1
re2=np.cross(y,x)
re2
##########################
#write numpy program to find out determinant of a given matrix
from numpy import linalg as LA
re3=np.linalg.det(x)
re3
########################
#Write a numpy prgram to calculate eigen values and eigen vectors
m=np.mat("3 -2;1 0")
print("Original matrix:")
print("a\n",m)
w , v=np.linalg.eig(m)
print("Eigenvector of the said matrix",w)
print("Eigenvalues of said vector",v)
##################
#write numpy program to calculate inverse of matrix
m=np.array([[1,2],[3,4]])
print(m)
res=np.linalg.inv(m)
res
########################
#Write numpy program to generate random number using normal distribution
"""The normal distribution is extensively used in statistical analysis, 
hypothesis testing, modeling of random variables, and
 estimation of population parameters. It provides a fundamental 
 framework for understanding and analyzing data that follows a 
 symmetric and continuous distribution."""
import random
x=np.random.normal(size=4)
x
########################
x=np.random.randint(low=10,high=30,size=6)
x
############################
#Write numpy program to create 3x3x3 array with random variable
x=np.random.random((3,3,3))
x
###########################
#write numpy program to create 5x5 matrix and calculate minimum and maximum
x=np.random.random((5,5))
x
xmin,xmax=x.min(),x.max()
print(xmin)
print(xmax)
##########################
#Write a numpy program to get the minimum and maximum value of given array with
#second axis
x=np.arange(4).reshape((2,2))
print("\nOriginal value")
x
print("\nMaximum value along with second axis")
print(np.amax(x,1))
print("\nMinimum value along with second axis")
print(np.amin(x,1))
#it will return minimum and maximum value from each row
##################################
#Python program to draw line
import matplotlib.pyplot as plt
x=range(1,50)
y=[value * 3 for value in x]
print('Value of x:')
print(*range(1,50))
print("Value of Y(thrice of x)")
print(y)
plt.xlabel('x-Axis')
plt.ylabel('y-axis')
plt.plot(x,y)
###################################
#
x=[1,2,3]
y=[2,4,1]
plt.plot(x,y)
plt.xlabel("X-Axis")
plt.ylabel('Y-axis')
plt.title("Sample Graph")
plt.show()
####################
import pandas as pd
df=pd.read_csv('fdata.csv')
df.plot()
plt.show()
########################
import seaborn as sns
data=pd.read_csv("Data_Science_Attendance_Sheet2.csv")

sns.countplot(x='Parjane Pranjal',data=df)

#############

df = data.drop('year',axis=1)
df = df.drop('month',axis=1)
df = df.drop('weekday',axis=1)
df = df.drop('datum',axis=1)
df.columns
df=df[:-1]
df.plot()
###########################
x1=[10,20,30]
y1=[20,30,40]
x2=[20,40,10]
y2=[50,60,70]
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sample_Graph')
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.show()
###############################3
# Write python program to plot two or more lines with legends
import matplotlib.pyplot as plt
x1=[10,20,30]
y1=[20,40,10]
# line 2 points
x2=[10,20,30]
y2=[40,10,30]
# labeling to x and y axis
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.title('Two or more lines with diffrence widths and color')
# Display
plt.plot(x1,y1, color='blue',linewidth=3,label='line-width3')
plt.plot(x2,y2, color='red',linewidth=5,label='line-width5')

plt.legend()
##############################################
# Write Python program to plot in diffrent styles

import matplotlib.pyplot as plt
x1=[10,20,30]
y1=[20,40,10]
# line 2 points
x2=[10,20,30]
y2=[40,10,30]
# labeling to x and y axis
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.title('Two or more lines with diffrence widths and color')
# Display
plt.plot(x1,y1, color='blue',linewidth=3,label='line1-dotted',linestyle='dotted')
plt.plot(x2,y2, color='red',linewidth=5,label='line2-dashed',linestyle='dashed')

plt.legend()

plt.show()
############################################
# Write python program to add line markers
# Line markers
import matplotlib.pyplot as plt
x=[1,4,5,6,7]
y=[2,6,3,6,3]

plt.plot(x,y, color='red',linestyle='dashdot',linewidth=3,marker='o',markerfacecolor='blue',markersize=12)

# set y limit of current axis
plt.ylim(1,8)
# set x limit of current axis
plt.xlim(1,8)

plt.xlabel('x-axis')

plt.ylabel('y-axis')

plt.title('Display marker')
plt.show()
#######################################################
# Write a Python program o plot seversl lines with diffrent format styles
import numpy as np
import matplotlib.pyplot as plt

# Sampled time at 200ms intervels
t=np.arange(0.,5.,0.2)

# green dashes , blue squeres and red triangles
plt.plot(t,t,'g--',t,t*2,'bs',t,t*3,'r^')

plt.show()

###########################################################
# Write python program to display a bar chart of the popularity of langauage

import matplotlib.pyplot as plt
x=['Java','Python','PHP','JavaScript','C#','C++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos= [i for i,_ in enumerate(x)]      
#_ is variable means it take one by one letter from the x with its corresponding index
plt.bar(x_pos,popularity,color='blue')
plt.xlabel("langauge")
plt.ylabel("popularity")
plt.title("Populartiy of the proramming langaure\n"+"worldwide ,oct 2017 compared to a year")
plt.xticks(x_pos,x)  
#for rotation of  label
plt.show()

# Graph in horizontal and vertical you can use the yticks
###########################################33
# Write python program to display a bar chart of the popularity of langauage

import matplotlib.pyplot as plt
x=['Java','Python','PHP','JavaScript','C#','C++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos= [i for i,_ in enumerate(x)]      
plt.bar(x_pos,popularity,color='blue')
plt.xlabel("langauge")
plt.ylabel("popularity")
plt.title("Populartiy of the proramming langaure\n"+"worldwide ,oct 2017 compared to a year")
plt.yticks(x_pos,x)  
plt.show()

import matplotlib.pyplot as plt
x=['Java','Python','PHP','JavaScript','C#','C++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos= [i for i,_ in enumerate(x)]      #_ is variable means it take one by one letter from the x with its corresponding index
#enumerate is used to check or access the keys and values from the given list  
plt.barh(x_pos,popularity,color='green')
plt.xlabel("popularity")      #x label
plt.ylabel("language")    #y label
plt.title("Populartiy of the proramming langaure\n"+"worldwide ,oct 2017 compared to a year")
plt.yticks(x_pos,x)     #graph in horizontal and vertical yoou can use the yticks
plt.show()
#############################################
# Write a python program to craete bar plot of scores by groups and gender
import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups=5
men_means=(22,30,33,30,26)
women_means=(25,32,30,35,29)

# create plot
# ax for multiple subplots
fig, ax=plt.subplots()
index=np.arange(n_groups)
bar_width=0.35
opacity=0.8

rects1=plt.bar(index,men_means,bar_width,alpha=opacity,
                  color='g',label='Men')

rects2=plt.bar(index + bar_width ,women_means,bar_width,alpha=opacity,
                  color='r',label='Women')
plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('Scores by Persons')
plt.xticks(index + bar_width,('G1','G2','G3','G4','G5'))
plt.legend()
plt.tight_layout()
plt.show()
##############################











