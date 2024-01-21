# -*- coding: utf-8 -*-
"""
Created on Fri May 12 15:02:12 2023

@author: Atharv
"""
#single line plot
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.show()
#multiline plot
x=range(1,5)
plt.plot(x,[i*1.5 for i in x])
plt.grid(True)
plt.plot(x,[i*3.0 for i in x])
plt.grid(True)
plt.plot(x,[i/3.0 for i in x])
plt.grid(True)
plt.show()
#############################################
#Grid ,axes and labels
import numpy as np
x=np.arange(1,5)
plt.plot(x,x*1.5,x,x*3.0,x,x*3.5)
plt.grid(True)
plt.show()
#############################################
#Handling axes
x=np.arange(1,5)
plt.plot(x,x*1.5,x,x*3.0,x,x*3.5)
plt.axis()#show current valueslimit
plt.axis([0,5,-1,13])
#[xminn,xmax,yminn,ymax]
plt.show()

##############################################
#adding labels
plt.plot([1,2,3,4])
plt.xlabel("This is X-axis")
plt.ylabel("This is Y-axis")
plt.show()
##############################################
#Adding Title
plt.plot([1,2,3,4])
plt.title("Nummber Graph")
plt.show()
##############################################
#Adding legend
x=np.arange(1,5)
plt.plot(x,x*1.5,label='Normal')
plt.plot(x,x*3.0,label='Fast')
plt.plot(x,x/3,label='Slow')
plt.legend()
plt.show()
##############################################
#Control colors
y=np.arange(1,5)
plt.plot(y,'y')
plt.plot(y+1,'m')
plt.plot(y+2,'c')
plt.show()
#############################################
#Specifying style in multiline plots
y=np.arange(1,3)
plt.plot(y,'y',y+1,'m',y+2,'c')
plt.show()
#control line style
y=np.arange(1,3)
plt.plot(y,'-.',y+1,'--',y+2,':')
plt.show()
#control markers style
y=np.arange(1,3,0.2)
plt.plot(y,'x',y+1,'o',y+2,'D')
plt.show()
#Histogram charts
y=np.random.randn(1000)
plt.hist(y)
plt.show()
#################################################
#bar graph/univariable analysis
plt.bar([1,2,3],[3,2,5])
plt.show()
################################################
#Scatter plots
#Bivariate analysis
x=np.random.randn(1000)
y=np.random.randn(1000)
plt.scatter(x,y)
plt.show()
##############################################
#Giving size AND colour
size=25*np.random.randn(1000)
colors=np.random.randn(1000)
plt.scatter(x,y,s=size,c=colors)
plt.show()
###############################################
#Adding text
x=np.linspace(-4,4,1024)#graph limit(Co-oradinate limit)
y=.25*(x+4.)*(x+1.)*(x-2.)
plt.text(-0.5,-0.25,'Brackmard minimum')
plt.plot(x,y,c='k')
plt.show()
##################################################












































