# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 09:35:29 2023

@author: Atharv
"""

#### FILPKART PRODUCT  web scrapping
from bs4 import BeautifulSoup as bs
import requests
link="https://www.flipkart.com/motorola-g84-5g-viva-magneta-256-gb/p/itmed938e33ffdf5?pid=MOBGQFX672GDDQAQ&lid=LSTMOBGQFX672GDDQAQSSIAM2&marketplace=FLIPKART&q=mototrola+g84&store=tyy%2F4io&spotlightTagId=FkPickId_tyy%2F4io&srno=s_1_2&otracker=search&otracker1=search&fm=Search&iid=935d5e93-17b2-46d8-83de-be88ce22aa2c.MOBGQFX672GDDQAQ.SEARCH&ppt=sp&ppn=sp&ssid=bx4wjwm2gw0000001699241878165&qH=444db5d770de9392"
'''link:-https://sanjivanicoe.org.in/index.php/contact'''
page=requests.get(link)

page
#<response [200]> it means connection is successfully esatablilshed
#<response[503]> error sevrver not find''https://developer.mozilla.org/en-US/docs/Web/HTTP/Status'''

page.content

soup=bs(page.content,'html.parser')
soup

# now the text is clean but not upto expectation
# now let us apply prettify method
print(soup.prettify())

title =soup.find_all('p',class_="_2-N8zT")
title
review_title=[]
for i in range(0,len(title)):
    review_title.append(title[i].get_text())
review_title
len(review_title)

#We got 10 reviews

#Now let us scrap rating
rating=soup.find_all('div',class_="row _3AjFsn _2c2kV-") 
rating
len(rating)
