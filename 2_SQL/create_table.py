# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 09:20:43 2023

@author: Lenovo
"""

import psycopg2 as pg2

conn=pg2.connect(database='Test_me',user='postgres',host='localhost',password='root',port=5432)

cur=conn.cursor()

cur.execute('''create table courses(
    course_id serial primary key,
    course_name  varchar(45) unique not null,
    course_instructor varchar(67) not null,
    topic varchar(100) not null);''')

# make changes to database permanan
conn.commit()

# Close cursor and communicate with database
cur.close()