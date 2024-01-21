# -- coding: utf-8 --
"""
Created on Fri Oct 17 20:14:24 2023

@author: Atharv Joshi
"""

''' problem statement 1.	
Perform K-Means clustering for the airlines data to obtain 
optimum number of clusters. 
Draw the inferences from the clusters obtained. 
Refer to EastWestAirlines.xlsx dataset.

'''
'''
Business Objective:

Maximize: The overall travelling distance should increases

Minimize: he cost  of travel

Contraints: The data privacy and Resources
'''
# Data Dictionary
'''

  Name_of_feature          Discription          Type    Relevance
0                  ID       ID of customer  Quantitative  Irrelevance
1             Balance  Balance of customer  Quantitative    Relevance
2          Qual_miles           Qual_miles  Quantitative    Relevance
3           cc1_miles            cc1_miles       ordinal    Relevance
4           cc2_miles            cc2_miles       ordinal    Relevance
5           cc3_miles            cc3_miles       ordinal    Relevance
6         Bonus_miles          Bonus_miles   Quantitaive    Relevance
7         Bonus_trans          Bonus_trans  Quantitative    Relevance
8   Flight_miles_12mo    Flight_miles_12mo  Quantitative    Relevance
9     Flight_trans_12      Flight_trans_12  Quantitative    Relevance
10  Days_since_enroll    Days_since_enroll     continous    Relevance
11              Award               Award?       ordinal    Relevance

'''
#######################################################################
'''********EDA / Expolatry data analysis*********'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# we import the dataset excel file
df=pd.read_excel("EastWestAirlines.xlsx") 
df
#######################
#1.column
df.columns

#In this dataset there are 12 column and 
#in there are ID# column has ordinal data and  other all  column has the nominal data'''
#######################
#2.shape
df.shape    
# in the EastWestAirline has there are 3999 records and 12 column
#######################
#3.1 Now we count the number of the datapoint in the Balance clomun
df["Balance"].value_counts()
'''
# in this dataset there are 1000 value are 10 inthis dataset 
and 500,2000 are 5 in this dataset
1500 has  4 value in this dataset 
5000 has 3 entry in this dataset
and other has the value has the 1  time come in this dataset
'''
#######################
#3.data types 
df.dtypes
'''ID#                  int64
Balance              int64
Qual_miles           int64
cc1_miles            int64
cc2_miles            int64
cc3_miles            int64
Bonus_miles          int64
Bonus_trans          int64
Flight_miles_12mo    int64
Flight_trans_12      int64
Days_since_enroll    int64
Award?               int64
dtype: object'''
######################
#4. missing value
a=df.isnull()
a.sum()
##########################
#5.scatter

df.plot(kind='scatter', x='Balance', y='Bonus_miles') ;
plt.show()
#Here we can observes that around 0-0.5 miles mostly award for travel
#with bonus miles of maximum 150000
###########################
#6 2-D Scatter plot with color-coding for each type/class.
#we are making the code with the Balance and Bonus_miles  with respect to the Awards? 
sns.set_style("whitegrid");
sns.FacetGrid(df, hue="Award?", height=4) \
   .map(plt.scatter, "Balance", "Bonus_miles") \
   .add_legend();
plt.show();
#Here we can observes that around 0-0.5 miles mostly award for travel
#with bonus miles of maximum 150000
###########################
#6 2-D Scatter plot with color-coding for each  type/class.

#we are making the code with the Balance and Bonus_miles  with respect to the Awards? 
sns.set_style("whitegrid");
sns.FacetGrid(df, hue="Award?", height=4) \
   .map(plt.scatter, "Balance", "Days_since_enroll") \
   .add_legend();
plt.show();
############################
# pairwise scatter plot: Pair-Plot
# Dis-advantages: 
##Can be used when number of features are high.
##Cannot visualize higher dimensional patterns in 3-D and 4-D. 
#Only possible to view 2D patterns.
#pair plot 
plt.close();
sns.set_style("whitegrid");
sns.pairplot(df, hue="Award?", height=3);
plt.show()
############################################
#Box-plot can be visualized as a PDF on the side-ways.

sns.boxplot(x='Award?',y='Balance', data=df)
plt.show()
#It will clearly indicate that the outliers are occur in Balance and Award Column

##################################
#outlier are occuurs
#box plot
sns.boxplot(df["Balance"])
##########################
#five number summary
v=df.describe()
# here we observed that there is scae difference in mean and 
# standard deviation for some columns which clearly shows that
# there is an presence of an outlier
# Next we will perform Outlier performance
##########################################################################
#2 outlier treatement
import pandas as pd
import seaborn as sns

#let us import the dataset
df=pd.read_excel("EastWestAirlines.xlsx") 
df

#now let us find the outlier in the Balance column
sns.boxplot(df.Balance)
#there are outlier
#let us check there are outlier in the Bouns_miles column
sns.boxplot(df.Bonus_miles)
#there are no outlier
#we can calclaute the IQR

IQR=df.Balance.quantile(0.75)-df.Balance.quantile(0.25)

#have observation that the IQR in the variable explore
#no becaue the IQR are in the capaitalluze letter
#treated as constant
IQR

lower_limit=df.Balance.quantile(0.25)-1.5*IQR    #make the lower limit value as 0 not the negative
lower_limit         
upper_limit=df.Balance.quantile(0.75)+1.5*IQR 
upper_limit         

#negative vaule are not the lowre limit so make it as 0
# for change go to the varible explore and make it as 0 directly
###############################################
#trimming
import numpy as np
outliers_df=np.where(df.Balance>upper_limit,True,np.where(df.Balance<lower_limit,True,False))
#you can check outlier_df column in the varible explore
#floting the point number,if possible in varible explore
#now trimm that
df_trimmed=df.loc[~outliers_df]
df_trimmed      #it can show the trimmed element
df.shape        #without the trimed shape is
#Out[60]: (310, 13)
df_trimmed.shape        #we trimmed this elemnt
#Out[61]: (34, 13)

################################################################
##repalcemet technique
#masking technique
#drawback of trimming is we can loosing the data
import pandas as pd
import seaborn as sns
import numpy as np
#let us import the dataset
df=pd.read_excel("EastWestAirlines.xlsx") 
df
df.describe()

#recored number 23 has got the outliers
# map all the outlier to the upper limit
df_replace=pd.DataFrame(np.where(df.Balance>upper_limit,upper_limit,np.where(df.Balance<lower_limit,lower_limit,df.Balance)))
df_replace

# if the value is lower than the lower limit ie is it has oulier
#so make it as the lower limit value  to that entry 
#if the value is greater than the upper limit ie is it has outlier
#so make it upper limit value to it 
#other wise make it as the same  for that columns
###################

sns.boxplot(df_replace[0])
#all the outiler are remove
###########################################################
#Winsorizer
from feature_engine.outliers import Winsorizer
winsor = Winsorizer(capping_method='iqr',
                    tail='both',
                    fold=1.5,
                    variables=['Balance']
                    )


df_t=winsor.fit_transform(df[['Balance']])
sns.boxplot(df['Balance'])
sns.boxplot(df_t['Balance'])
##############################
#variance
#zero and naer zero variance features
#if there are no variance in the feature , then ml model
#will not get any intellgence , so it is betttre  to ignore that feature

import pandas as pd
#let us import the dataset
df=pd.read_excel("EastWestAirlines.xlsx") 
df
df.var()

#######################
df.var()==0
###############################
#axis =0 then it is gonig to give the sam e results 
# if there are varienace then it give true 
df.var(axis=0)==0

#############################################
#4.missing value
# missing value
a= df.isnull()
#we can store the null value  in 'a' varible and we take the null value count from the 'a' varible
a.sum()
#there are no any missing value 
#############################################
#discretization
import pandas as pd
import numpy as np
data=pd.read_excel("EastWestAirlines.xlsx") 
data.head()     #show the first five record of the dataset/smaple data
data.head(10)  # 0 to 9 record are display
data.info()         #size of the data
#it gives size , null values,rows ,columns and datatype of the columns

data.describe()     #appllicabe fro numerical value  only
data['Balance_new']=pd.cut(data['Balance'],bins=[min(data.Balance),data.Balance.mean(),max(data.Balance)],labels=['low','High'])
data.Balance_new.value_counts()

#in the above code we can descriteze the data from the variou ppoint and mark them
#with the high value and low value  
# we can divide that data from the mena and label with them with the high value
# and more value from the mean are mark with the high value


data['Balance_new']=pd.cut(data['Balance'], bins=[min(data.Balance),data.Balance.quantile(0.25),data.Balance.mean(), data.Balance.quantile(0.75),max(data.Balance)], labels=['group1','group2','group3','group4'])
data.Balance_new.value_counts()
###########################################################################
#Standardization

import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
d=pd.read_excel("EastWestAirlines.xlsx")
d.describe()
a=d.describe()

#intialize the scalar
scalar=StandardScaler()
df=scalar.fit_transform(d)
dataset=pd.DataFrame(df)
res=dataset.describe()
#here if you will check res, in varaible explorer or in the vraible environment then
# mean is zero and standard deviation is zero
##########################################


#Normalization
import pandas as pd
df=pd.read_excel("EastWestAirlines.xlsx")
df
#now read the columns
df.columns
#there are some column which are not useful , we need to drop
df.drop(['ID#'],axis=1, inplace=True)
#now read minimum value and maximum value of salarie s and age
a1=df.describe()
#check a1 data frame in the varible explorer
#you find minimum saralies is 0 and max is 108304
#same way you check for age, there is huge difference
#in min and max .value . Hence we are going for normalization
#first we will have to convert non-numerical data to label encoding'
df =pd.get_dummies(df, drop_first=True)
#Normalization function written where ethnic argument is passed
def norm_fun(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

df_norm=norm_fun(df)
b=df_norm.describe()

##################Model Building############################
# what will be the ideal clusetr 0,1,or 2
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

TWSS=[]
k=list(range(2,8))
for i in k:
    kmeans=KMeans(n_clusters=i)
    kmeans.fit(df_norm)
    
    TWSS.append(kmeans.inertia_)
    
    '''
    kmeans inertia also known as sum odf sqares methos
    .It measures all the datapoints from the centroid of the point.
    it differentiate between observed value and predicted value
    '''
    
TWSS
# Plot a elbow curve
plt.plot(k,TWSS,'ro-')
plt.xlabel('No of clusers')
plt.ylabel('Total within SS')

model=KMeans(n_clusters=3)
model.fit(df_norm)
model.labels_
mb=pd.Series(model.labels_)
df['clust']=mb
df.head()
df=df.iloc[:,[7,0,1,2,3,4,5,6]]
df
df.iloc[:,2:8].groupby(df.clust).mean()
df.to_csv('Kmeans_airlines.csv',encoding='utf-8')
import os
os.getcwd()
