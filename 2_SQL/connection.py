# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 08:28:13 2023

@author:Atharv
"""

import psycopg2 as pg2

# to connect the database wit python
conn=pg2.connect(database='dvd_rental',user='postgres',host='localhost',password='root',port=5432)

#establish connection and start cursor to be ready to query
cur=conn.cursor()

# pass the postgre query as a string
cur.execute('select * from payment')

#return a tuple of first row as python object
cur.fetchone()

# return mutiple rows as a python object
cur.fetchmany(10)

# return all data from the table
cur.fetchall()

# Don't forget to close the connection
#killing the kernel or shutting down the jupyter also work
conn.close()

