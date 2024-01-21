# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 08:45:25 2023

@author: Atharv
"""
import psycopg2 as pg2

conn=pg2.connect(database='Test_me',user='postgres',host='localhost',password='root',port=5432)

cur=conn.cursor()

cur.execute('select * from courses;')

rows=cur.fetchall()

print(rows)

conn.commit()
cur.close()
conn.close()

for i in rows:
    print(i)
    
