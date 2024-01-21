# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 08:39:59 2023

@author: Atharv Joshi
"""

# Now we will work on the Online Pages
from bs4 import BeautifulSoup as bs
import requests

link = 'https://www.flipkart.com/zebronics-pixaplay-22-3200-lm-portable-electronic-focus-multi-connectivity-supported-formats-in-built-speaker-dual-band-connectivity-cotton-swab-pack-stunning-720p-hd-smart-projector/p/itm6a77d543b5e99?pid=PROGPEHBQETTRE6G&lid=LSTPROGPEHBQETTRE6GPUW0LP&marketplace=FLIPKART&q=zebronic+pixaplay&store=search.flipkart.com&srno=s_1_17&otracker=search&otracker1=search&fm=organic&iid=b684e42c-1134-4b54-9eb1-63df399f3c64.PROGPEHBQETTRE6G.SEARCH&ppt=hp&ppn=homepage&ssid=0k2lhi9ljk0000001701745772754&qH=25332aa4c3f33ca2'

page = requests.get(link)
page

#<Response[200]> it means connection is successfully establish
page.content
#you will get all html source code but very crowdy text
#let us apply html parser
soup = bs(page.content, 'html.parser')
soup 
#Now the text is clean but not upto the expectations
#Now let us apply prettify method
print(soup.prettify())
#The text is neat and clean
list(soup.children)
#Finding all contents using tab
title=soup.find_all('p',class_="_2-N8zT")
print(title)

review_title=[]

for i in range(len(title)):
    review_title.append(title[i].get_text())
    
review_title

len(review_title)
# Here we got 10 review titles
####################################################
#Let us scrap ratings
rating=soup.find_all('div',class_='_3LWZlK _1BLPMq')
rating

rate=[]
for i in range(len(rating)):
    rate.append(rating[i].get_text())
    
rate

len(rate)
# We have to make the dataframe siz equal so we have to add thrree rows
# As our length of the review_title list is 10 and and rating is
# is 7 we make it equal so we add three blank spaces in rate list

rate.append(" ")
rate.append(" ")
rate.append(" ")
len(rate)
####################################
# Now let us scrap revoew body

review=soup.find_all('div',class_='t-ZTKy')
review
review_body=[]

for i in range(len(review)):
    review_body.append(review[i].get_text())
review_body
len(review_body)


import pandas as pd
df=pd.DataFrame()
df['Review_title']=review_title
df['rating']=rate
df['Review']=review_body
df

######################################3
#To create csv file
df.to_csv('Flipkart_sentiment.csv',index=True)

##########################################
#Sentiment Analysis

from textblob import TextBlob

sent='this is very excellent garden'
pol=TextBlob(sent).sentiment.polarity
pol

df=pd.read_csv('Flipkart_sentiment.csv')
df.head()

df['Polarity']=df['Review'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['Polarity']
