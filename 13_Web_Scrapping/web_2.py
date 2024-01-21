# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 09:38:42 2023

@author: Atharv Joshi
"""

# Now we will work on the Online Pages
from bs4 import BeautifulSoup as bs
import requests

link = 'https://sanjivanicoe.org.in/index.php/contact'

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
soup.find_all('p')
#suppose you want extract contents from
#first row
soup.find_all('p')[1].get_text()
#contents from second row
soup.find_all('p')[2].get_text()
#finding text using class
soup.find_all('div',class_='table')
