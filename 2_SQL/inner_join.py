# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 09:13:02 2023

@author: Lenovo
"""

import psycopg2 as pg2

conn=pg2.connect(database='Test_me',user='postgres',host='localhost',password='root',port=5432)

cur=conn.cursor()

cur.execute('''
            create table courses_admin(
                course_id int ,
                course_duration varchar(16) not null,
                course_fees int not null)''');
            
conn.commit()

cur.execute('''insert into courses_admin(course_id,course_duration,course_fees)
            values(2,'10_days',200)''');
            
cur.execute('''insert into courses_admin(course_id,course_duration,course_fees)
            values(3,'11_days',210)''');
            
cur.execute('''insert into courses_admin(course_id,course_duration,course_fees)
            values(4,'13_days',2100)''');
            
cur.execute('''insert into courses_admin(course_id,course_duration,course_fees)
            values(5,'11_days',2100)''');
            
conn.commit()


cur.execute('''select Course_name ,course_instructor from courses
            inner join courses_admin on
            courses.course_id=courses_admin.course_id''');
            
rows=cur.fetchall()
for i in rows:
    print(i)