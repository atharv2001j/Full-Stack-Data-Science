# -*- coding: utf-8 -*-
"""
Created on Mon May 15 19:37:40 2023

@author: Atharv
"""
#NLP for Python

import seaborn as sns
import pandas
import matplotlib.pyplot as plt
#Tokenization
txt='Hello good morning'
x=txt.split()
print(x)
#####################################################
#Removing special chaacters
import re
def remove_spec_char(text):
    pat=r'[^a-zA-Z0-9.,!?/:;\"\'\s]'#s should be small
    return re.sub(pat, '',text)
remove_spec_char('hello @ good morning! %$#@?')
#####################################################
#Remove numbers
def remove_num(text):
    pat=r'[^a-zA-Z.,!?/:;\"\'\s]'#s should be small
    return re.sub(pat, '',text)
remove_num('hello 22200937')
####################################################3


txt='Welcome :to the ,new year :2023!'
x=re.split(r'(?:,|;|\s)\s*',txt)
print(x)
#Removing punctuations
import string
def remove_punctuation(text):
    text= ''.join([c for c in text if c not in string.punctuation])
    return text
remove_punctuation('what?')
############################################################
#stemming 
#stemming is the process of reducing inflected/derived words
#to their stem word. base or root form 
#these mainly rely on chopping off 's' 'es' 'ing' , 'ly' etc from
#the end of the words and sometimes the conversation is not desirable.
#but nonthless ,  stemming helps us in standard 
import nltk # function for stemming
def get_stem(text):
    stemmer = nltk.porter.PorterStemmer()
    text = ' '.join([stemmer.stem(word)for word in text.split()])
    return text

print(get_stem("we are eating and swimming ; we have running and sleeping"))

#lemmatization
#it is the advanced form of stemming , it does conversion proerty with the 
#help of vocubualary

line = 'asdf fjdk afed, fjek,asdf, foo'
re.split(r'(?:,|;|\s)\s*' , line)

#matching text at the start or at end of the string
filename = 'spam.txt'
filename.endswith('.txt')

area_name = '6th lane west Andheri'
area_name.endswith('west Andheri')

#-------------------------------------------------------------------
#startswith() method and endswith() method are provided by nltk
choices = ('http:' , "ftp:")
url = 'http://www.python.org'
url.startswith(choices)

#--------------------------------------------------------------------
#slicing a string
#string_name[start : end :step]
S = "ABCDEFGHI"
print(S[2:7]) #CDEFG
#note the item at the index 7 i.e 'H' is not included
#slicing with negative values
print(S[-7:-2:]) #CDEFG

#slicing with postive and negative indexing
S = "ABCDEFGHI"
print(S[2:-5]) #CD

#specifing the step-value for slicing
print(S[2:7:2]) #CEG

#negative slice value
print(S[6:1:-2]) #GEC

#slice at the beginning and end
print(S[:6]) #beg--->ABCDEF
print(S[6:]) #end-->GHI

#reverse a string
S = "ABCDEFGHI"
print(S[::-1])

#similar operations can be done with slicing
filename = 'spam.txt'
filename[-4 : ] =='.txt'

#------------------------------------------------------------------------
url = 'https://www.python.org'
url[:6] == 'https:' 
url[:7] == 'https:' 
url[:4] == 'ftps'
#or

url[:6] =='https:'
############################################################
#Matching string using shell wide card pattern
#if yiou  match the wide card patttern then you can use fnmatch package
#it provides two functions fnmatch and fnmatchcase .
from fnmatch import fnmatch,fnmatchcase
names=['Dat1.csv','Dat2.csv','config.csv','foo.csv']
[name for name in names if fnmatch(name,'Dat*.csv')]
############################################################
from fnmatch import fnmatch,fnmatchcase
names=['Andheri east','Parle east','dadar west']
[name for name in names if fnmatch(name,'*east')]    
########################################################
addresses=['5412 N CLARK ST','1060 W ADISION ST','1039 W GRANVILLE AVE'
           '2122 N CLARK ST','4802 N BROAWAY']
[name for name in addresses if fnmatch(name,'*ST')]     
#########################################################
#Matching and searching for text pattern 
#if a test  that youu are trying to match is simple literal you can use basic
#string method like string.find() or string.endswith() or string.startswith() or 
#similar
text='yeah,but no,but yeah,but no,bu yeah'
#Exact match
text=='yeah'
#--->False
#Match at start or end
text.startswith('yeah')    
text.endswith('no')    
#Search for the locatin of first occurence off text
text.find('no')    
##########################################################
#Matching dates
txt1='11/27/2023'
txt2='Nov 27,2012'
import re
if re.match(r'\d+/\d+/\d+',txt1):
    print('Yes')
else:
    print('No')
    
if re.match(r'\d+/\d+/\d+',txt2):
    print('Yes')
else:
    print('No')    
########################################################
if re.match(r'\d{2}/\d{2}/\d{4}',txt1):
    print('Yes')
else:
    print('No') 
    
if re.match(r'\d\d/\d\d/\d\d\d\d',txt1):
    print('Yes')
else:
    print('No')   
#########################################################
#####################Assignment1########################
#split the text
txt='This is AI era'
s=txt.split()
print(s)
################
txt='India : has great history , in 2023 india is leading to its gorious future!'
x=re.split(r'(?:,|;|\s)\s*',txt)
print(x)
################
#matching text at the start and end with
txt='Rama went to Haridwar to get Gangajal'
txt.startswith('Gangajal')
txt.endswith('Gangajal')
######################
choices=('Rama','to')
txt.startswith(choices)
txt.endswith(choices)
#####################
txt='I like mango'
txt[7:]=='mango'
txt[-5:]=='mango'
###################
#extract only date
txt='I had been visited pune on 11/5/2023'
txt[27:]
txt[-9:]
x=re.findall(r'\d\d/\d/\d\d\d\d',txt)
print(x)  
#####################
#replace the value
txt='yeah,but no,but yeah,but no,bu yeah'
txt.replace('yeah', 'yup')
####################
#Obtain date in required pattern
txt='Today is 17/5/2023 and our exam will starts from 2/7/2023'
re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2',txt)
####################
datepan=re.compile(r'(\d+)/(\d+)/(\d+)')
datepan.sub(r'\3-\1-\2',txt)
####################
#To count the number of substitutions
newteaxt,n=datepan.subn(r'\3-\1-\2', txt)
print(n)    
print(newteaxt)    
####################
#Searching and replacing case sensitive text
txt='UPPER PYTHON,lower python,mixed python'    
re.findall('python',txt,flags=re.IGNORECASE)
#substitute value
re.sub('python','snake',txt,flags=re.IGNORECASE)    
####################
#to remove  thhe drawback of previous method
import re
text='UPPER PYTHON,lower python,Mixed Python' 
def matchcase(word):
    def replace(m):
        text=m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace
re.sub('python',matchcase('snake'),text,flags=re.IGNORECASE)  
#####################
#To access the text written in " "/' '
#it is also called starting and ending delimeters
str_pat=re.compile(r'\"(.*)\"')
text1='Computer says "no"'
str_pat.findall(text1)
########################
str_pat=re.compile(r'\"(.*)\"')
text1='Computer says"no" phone says "yes"'
str_pat.findall(text1)
##########remove  drawbak############
#Put question mark
str_pat=re.compile(r'\"(.*?)\"')
text1='Computer says"no" phone says "yes"'
str_pat.findall(text1)
##################
#To write comment
comment=re.compile(r'/\*(.*?)\*/')
text1='/*this is comment */'
comment.findall(text1)
####################
#if their is multiline comment we have to change pattern
comment=re.compile(r'/\*((?:.|\n)*?)\*/')
text2='''/*this is
comment/'''
comment.findall(text2)
################################
#Remove numbers from thw  text
def remove_num(text):
    result=re.sub(r'\d+', '',text)
    return result
text='there are 3 balls in a bag'
remove_num(text)
#################################
#to convert number to word
import inflect
p=inflect.engine()
def convert_number(text):
    temp_str=text.split()
    new_str=[]
    for word in temp_str:
        if word.isdigit():
            temp=p.number_to_words(word)
            new_str.append(temp)
        else:
            new_str.append(word)
    temp_str=' '.join(new_str)
    return temp_str
text='there are 3 balls in bag'
convert_number(text)
#########################
#Exersise1
#reverse a each word of string
def reverse_word(input):
    if input==" ":
        return "You entered wrong input"
    else:
        words=input.split()
        reverse_sentence=" ".join(reversed(words))
        
    return reverse_sentence
print(reverse_word("My name is atharv"))
################
def rev_str(text):
    words=text.split()
    reverse_sentence=" ".join(reversed(words))
    
    return reverse_sentence
text='India is my Country'
rev_str(text)
#######################
#Exersise 2
#make a single line in file
def convert_to_single_line(file_path):
    with open("sampel.txt",'r') as file:
        content=file.read() # Read the file content
    single_line=content.replace('\n',' ')# Replace newlines with a space
    return single_line
convert_to_single_line("sampel.txt")
##############################################3
























