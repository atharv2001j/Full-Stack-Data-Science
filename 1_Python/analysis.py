# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 08:16:10 2023

@author:Atharv
"""
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
df=pd.read_excel('ds_attendance_v1.xlsx')
df
df2=df.fillna(0)
df2
#df2=df2.replace('p',0)
#df2

#######################################333
# Replace a particular value with its previous value + 1
column_name = df2[:]
target_value = 'p'  # Specify the value you want to replace
df2.dtypes
df2.astype(int)
# Iterate over each row 
for row in df.iterrows():
    for index, value in enumerate(row[1]):
        if value == target_value:
            previous_value = row[1].iloc[index - 1]
            new_value = previous_value + 1
            df.iloc[row[0], index] = new_value

# Save the updated DataFrame to the Excel sheet
df.to_excel('f.csv', index=False)
###########################################33
df2['Total_attendance']=df2.iloc[:,1:].sum(axis=1)
df2
df2.to_csv('Final_attendance.csv')
df3=df2.drop([0,1])

df3.to_csv('f.csv')
#############################################

df4=pd.read_csv('f.csv')
df4.shape
df4.replace('Ab',0)
df4.drop[33:]
df4=df4.drop(df.columns[0,1],axis=1)
plt.bar(df4['Name'], df4['Total_attendance'])
plt.xlabel('Student')
plt.ylabel('Total Hours Attended')
plt.title('Attendance by Student')

plt.xticks(rotation=90)
plt.show()
###############################################3
df5=pd.read_csv('final_attenadance_ds.csv')
df6=df5.transpose()
df7=df6.to_csv('att.csv')
column_list = df[''].tolist()
plt.bar(df7['datnum'], d7['Total_attendance'])
plt.xlabel('Student')
plt.ylabel('Total Hours Attended')
plt.title('Attendance by Student')

plt.xticks(rotation=90)
plt.show()















