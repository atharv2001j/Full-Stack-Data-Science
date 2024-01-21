
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 08:03:59 2023


@author: Atharv
"""
# file handling

with open('file.txt') as file_object:
    content = file_object.read()
print(content)

# to remove extra line at the end of output we use rstrip() method
with open('file.txt') as file_object:
    content = file_object.read()                
    print(content.rstrip())

# absolute path
file_path = 'C:/Atharv/file.txt'
with open(file_path) as file_object:
    content = file_object.read()
    print(content.rstrip())

# reading line by line
filename = 'file.txt'
with open(filename) as fo:
    for i in fo:
        print(i)

filename = 'file.txt'
with open(filename) as fo:
    for i in fo:
        print(i.rstrip())

# making list of line for file
# readline() is used to store  each line in the list
# readline does not support rstrip()
file_path = 'C:/Atharv/file.txt'
with open(file_path) as file_object:
    content = file_object.readlines()
    print(content)


file_path = 'C:/Atharv/file.txt'
with open(file_path) as file_object:
    content = file_object.readlines()
for i in content:
    print(i.rstrip())

# working with a file data
# after reading the file in main memory we can do whatever we have to do

filename = "file.txt"
with open(filename) as fo:
    lines = fo.readlines()
    pi_string = " "
    for line in lines:
        pi_string += line.rstrip()
        print(pi_string)
        print(len(pi_string))

# write the content in the file
# w remove old content and replace it with new content
# to write content along with the old one we use 'a' instead of
# 'w'
filename = "file.txt"
with open(filename, 'w') as fo:
    fo.write("I love Programming")
# to write multiple lines
filename = "file.txt"
with open(filename, 'w') as fo:
    fo.write("I love Programming")
    fo.write("hello")
# to add new liness
filename = "file.txt"
with open(filename, 'w') as fo:
    fo.write("I love Programming\n")
    fo.write("hello\n")

# Appending a file
filename = "file.txt"
with open(filename, 'a') as fo:
    fo.write("I love Programming")
    fo.write("I love Sanjivani")
with open(filename, 'r') as fo:
    print(fo.read())
