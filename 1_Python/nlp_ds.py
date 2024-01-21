# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 09:02:19 2023

@author: Atharv
"""

import re
text1="My mobile number is 9850603297"
text2="My alternate mobile is 850234567"
text3="My international mobile no is (124)-456-75432"
pat1='\d{10}'#It will return the 10 digit from text1
pat2=r"\(\d{3}\)-\d{3}-\d{5}"#\ is given to access the braces type
mob_no=re.findall(pat1,text1)
mo_no=re.findall(pat2,text3)
mo_no
mob_no
#########################
#matching an email id
text1="My-email-id  is joshiatharv7@gmail.com"
text2="My alternate emailid is prince02@gmail.com"
text3="My alternate emailid is atharvjoshicomp@sanjivani.com"
patt=r"[a-zA-z0-9]*@[a-z].*com"
a=re.findall(patt,text3)
a
##################
import re
text1="Hi my order #496724 is not received yet"
text2="Hi I have problem with my order number 496724"
text3="Hi my order 496724 is having an issue"
pat4='order[^\d]*(\d*)'
b=re.findall(pat4,text1)
b
#######################
chat1="Hi my order #59326 is not received yet"
chat2="Hi I have problem with my order number 59326, which is not received"
chat3="Hi my order 59326 is having an issue"
patt='order[^\d]*(\d*)'
b=re.findall(patt,chat1)
b
c=re.findall(patt,chat2)
c
##########################
text1="My-email-id  is joshiatharv67@gmail.com"
text2="My alternate emailid is joshiath564@gmail.com"
patt="[a-zA-z0-9]@[a-z]\.*com"
a=re.findall(patt,text1)
a
text3="My college mail id is atharv.joshi@sanjivani.org.in"
patt="[a-zA-Z]\.[a-z]@[a-z]\.*org\.*in"
a=re.findall(patt,text3)
a
##########################
import re
def get_pattern_match(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        return matches
    
get_pattern_match('order[^\d]*(\d*)', chat1)
################################
#Getting both mailid and number
text='''Born	Elon Reeve Musk
June 28, 1971 (age 51)
Pretoria, Transvaal, South Africa
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner, CTO and chairman of Twitter
President of the Musk Foundation
Founder of the Boring Company, X Corp. and X.AI
Co-founder of Neuralink, OpenAI, Zip2 and X.com (part of PayPal)
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)​
Partner	Grimes (2018–2021)[1]
Children	10[a][3]
Parents	
Errol Musk (father)
Maye Musk (mother)
Family	Musk family
'''
age=get_pattern_match(r'age (\d*)', text) #or we can give 'age (\d+)'
age
name=get_pattern_match(r'Born(.*)', text)
name
name[0].strip()
matches=get_pattern_match(r'Born.*\n(.*)', text)
matches
birth_date=get_pattern_match(r'Born.*\n(.*)\(age', text)#It will give only the date
matches
birth_place=get_pattern_match(r'\(age.*\n(.*)', text)#It will give birthplace
###########################3
def extract_data(text):
    age=get_pattern_match(r'age (\d*)', text)
    name=get_pattern_match(r'Born(.*)', text)
    birth_date=get_pattern_match(r'Born.*\n(.*)\(age', text)#It will give only the date
    birth_place=get_pattern_match(r'\(age.*\n(.*)', text)#It will give birthplace
    return{
        'age':age,
        'name':name,
        'birth_date':birth_date,
        'birth_place':birth_place
        }
extract_data(text)
###########################################
text='''
Born	Mukesh Dhirubhai Ambani
19 April 1957 (age 66)
Aden, Colony of Aden
(present-day Yemen)[1][2]
Nationality	Indian
Alma mater	
St. Xavier's College, Mumbai
Institute of Chemical Technology (B.E.)
Occupation(s)	Chairman and MD, Reliance Industries
Spouse	Nita Ambani ​(m. 1985)​[3]
Children	3
Parent	
Dhirubhai Ambani (father)
Relatives	Anil Ambani (brother)
Tina Ambani (sister-in-law)
'''
age=get_pattern_match('age (\d*)', text)
age
name=get_pattern_match('Born(.*)', text)
name[0].strip()
birth_date=get_pattern_match(r'Born.*\n(.*)\(age', text)
birth_date
birth_place=get_pattern_match(r'\(age.*\n(.*)', text)
birth_place
extract_data(text)
get_pattern_match(r'Parent.*\n(.*)', text)

##################################################
#Extract all twitter handler from text
text='''
Follow our leader Elon musk on twitter here: https://twitter.com/elonmusk, more information 
on Tesla's products can be found at https://www.tesla.com/. Also here are leading influencers 
for tesla related news,
https://twitter.com/teslarati
https://twitter.com/dummy_tesla
https://twitter.com/dummy_2_tesla
'''
pattern='https://twitter\.com/([a-zA-Z0-9_]+)'
re.findall(pattern,text)
##################################################
#Extract text after Conentration of risk
text='''
Concentration of Risk: Credit Risk
Financial instruments that potentially subject us to a concentration of credit risk consist of cash, cash equivalents, marketable securities,
restricted cash, accounts receivable, convertible note hedges, and interest rate swaps. Our cash balances are primarily invested in money market funds
or on deposit at high credit quality financial institutions in the U.S. These deposits are typically in excess of insured limits. As of September 30, 2021
and December 31,
'''
pattern='Concentration of Risk: ([^\n]*)'
re.findall(pattern,text)
################################
text='''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
BMW's gross cost of operating vehicles in FY2021 S1 was $8 billion.
'''
pattern='FY(\d{4} (?:Q[1-4]|S[1-4]))'#? matches any character
re.findall(pattern,text)
#######################################
#Extract phone number
text='''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777
'''
pattern='\(\d{3}\)-\d{3}-\d{4}|\d{10}'
re.findall(pattern,text)
##############################
text='''
Note 1 - Overview
Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”) was incorporated in the State of Delaware on July 1, 2003. We design, develop, manufacture and sell high-performance fully electric vehicles and design, manufacture, install and sell solar energy generation and energy storage
products. Our Chief Executive Officer, as the chief operating decision maker (“CODM”), organizes our company, manages resource allocations and measures performance among two operating and reportable segments: (i) automotive and (ii) energy generation and storage.
Beginning in the first quarter of 2021, there has been a trend in many parts of the world of increasing availability and administration of vaccines
against COVID-19, as well as an easing of restrictions on social, business, travel and government activities and functions. On the other hand, infection
rates and regulations continue to fluctuate in various regions and there are ongoing global impacts resulting from the pandemic, including challenges
and increases in costs for logistics and supply chains, such as increased port congestion, intermittent supplier delays and a shortfall of semiconductor
supply. We have also previously been affected by temporary manufacturing closures, employment and compensation adjustments and impediments to
administrative activities supporting our product deliveries and deployments.
Note 2 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated balance sheet as of September 30, 2021, the consolidated statements of operations, the consolidated statements of
comprehensive income, the consolidated statements of redeemable noncontrolling interests and equity for the three and nine months ended September
30, 2021 and 2020 and the consolidated statements of cash flows for the nine months ended September 30, 2021 and 2020, as well as other information
disclosed in the accompanying notes, are unaudited. The consolidated balance sheet as of December 31, 2020 was derived from the audited
consolidated financial statements as of that date. The interim consolidated financial statements and the accompanying notes should be read in
conjunction with the annual consolidated financial statements and the accompanying notes contained in our Annual Report on Form 10-K for the year
ended December 31, 2020.
'''
pattern='Note \d - ([^\n]*)'
re.findall(pattern,text)
############################################
#Extract financial period from company's finantial report
text='''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. 
'''
pattern='FY\d{4} Q[1-4]'
re.findall(pattern,text)
####################################
#Case sensitive pattern match using flags
text='''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion. 
'''
pattern='FY\d{4} Q[1-4]'
re.findall(pattern,text,flags=re.IGNORECASE)
#####################################
text='''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. 
'''
pattern='\$([0-9\.]+)'#. show extract all the content after that
re.findall(pattern,text)
##########################3



































































#for reading the pdf files
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfReader
#Creating pdf reader object 
reader= PdfReader('daa.pdf')
#printing number of pages in pdf file
print(len(reader.pages))
#Getting specific page from  pdf file
#Indexing will start from zero
page=reader.pages[0]
#Extract the content of page
text=page.extract_text()
print(text)
#################################
import re
char2='Hi:I have problem with my order number 412889912'
pattern='order[^\d]*(\d*)'
matches=re.findall(pattern,char2)
print(matches)
#####################################
