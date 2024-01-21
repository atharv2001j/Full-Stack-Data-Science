# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 09:02:55 2023

@author: Lenovo
"""

import psycopg2 as pg2

conn=pg2.connect(database='Test_me',user='postgres',host='localhost',password='root',port=5432)

cur=conn.cursor()

cur.execute('select course_instructor,count(*) from courses group by course_instructor;')

conn.commit()

rows=cur.fetchall()

for i in rows:
    print(i)
    
cur.close()
conn.close()
