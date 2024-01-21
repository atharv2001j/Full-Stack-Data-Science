# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 08:24:20 2023

@author: Atharv
"""
import psycopg2 as pg2


conn=pg2.connect(database='Test_me',user='postgres',host='localhost',password='root',port=5432)

cur=conn.cursor()

cur.execute('''
            insert into courses(course_id,course_name,course_instructor,topic)
            values(2,'Introduction of Pyhon','prof khirsagwr','Pyhon')''');


cur.execute('''
            insert into courses(course_id,course_name,course_instructor,topic)
            values(3,'Introduction of DS','prof NAIK sir','DS')''');

cur.execute('''
            insert into courses(course_id,course_name,course_instructor,topic)
            values(4,'Introduction of CN','prof kalavadekar','CN')''');

cur.execute('''
            insert into courses(course_id,course_name,course_instructor,topic)
            values(5,'Introduction of c++','prof A.D.Sangle','C++')''');

conn.commit()
cur.close()
conn.close()
