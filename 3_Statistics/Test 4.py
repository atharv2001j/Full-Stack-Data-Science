# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 15:12:07 2023

@author: Atharv Joshi


"""

##########################Test 4###################################
#Q1.  Determine if a letter is a vowel or a consonant

letter = input("Enter a letter: ")
letter = letter.lower()

if letter in "aeiou":
    print(f"{letter} is a vowel.")
else:
    print(f"{letter} is a consonant.")
###########################################
#Q2.Convert from a letter grade to a number of grade points
g_points = {
    'A+': 4.0,
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1.0,
    'F': 0.0
}


letter_grade = input("Enter a letter grade: ")  # Convert to uppercase for case-insensitivity


if letter_grade in g_points:
    grade_point = g_points[letter_grade]
    print(f"The grade point for {letter_grade} is {grade_point}.")
else:
    print("Invalid letter grade. Please enter a valid letter grade.")

###########################################################
#Q4. Draw inferences about the following boxplot & histogram.

# The data is not normlly distributed it is right skewed.And as it is right-skewed
# then it contain the outliers and 
#The mean is typically greater than the median and mode because of the presence of the tail on the right side
#Due to the skeness the standard deviation may increased as the the spread of
# data is more towards right

###########################################################
# Q5.  Below are the scores obtained by a student in tests
# 34,36,36,38,38,39,39,40,40,41,41,41,41,42,42,45,49,56
# 1) Find mean, median, variance, standard deviation.
# 2) What can we say about the student marks? [Hint: Looking at the various measures 
# calculated above whether the data is normal/skewed or if outliers are present]. 

import pandas as pd
import numpy as np


data = [34, 36, 36, 38, 38, 39, 39, 40, 40, 41, 41, 41, 41, 42, 42, 45, 49, 56]

df = pd.DataFrame(data, columns=['Scores'])

mean = df['Scores'].mean()
mean
median = df['Scores'].median()
median
variance = df['Scores'].var()
variance
std_deviation = df['Scores'].std()
std_deviation
# Check for skewness
if mean == median:
    print("The data is symmetric.")
elif mean < median:
    print("The data is left skewed.")
else:
    print("The data is right skewed.")

# Check for outliers using the IQR method
Q1 = df['Scores'].quantile(0.25)
Q3 = df['Scores'].quantile(0.75)
IQR = Q3 - Q1
IQR
lower_bound = Q1 - 1.5 * IQR
lower_bound

upper_bound = Q3 + 1.5 * IQR
upper_bound


no_outliers = df[(df['Scores'] < lower_bound) | (df['Scores'] > upper_bound)]
if no_outliers.empty:
    print("No outliers are present.")
else:
    print("Outliers are present.")
    
#########################################################
#Q6.
import pandas as pd

df=pd.read_excel("Assignment_module02.xlsx")
df

df.columns

df.mean()
# Points     3.596563
# Score      3.211562
# Weigh     17.848750
# dtype: float64

df.median()
# Points     3.695
# Score      3.325
# Weigh     17.710
# dtype: float64

# As the mean and median of the columns are not exactly same and somewhat difference
# in there values so it shows some skewness properties

df.std()
# Points    0.534679
# Score     0.965662
# Weigh     1.786943
# dtype: float64

df.var()
# Points    0.285881
# Score     0.932503
# Weigh     3.193166
# dtype: float64

# As the Standard deviation are near the 1 so the spread of the data are near 
# the median value

import seaborn as sns

sns.boxplot(df)
# From boxplot we can see that there is an outlier present in 'Score' and 'Weight'
# column

#######################################################################