# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 17:26:47 2023

@author: Atharv Joshi
"""
'''
Q1. Using tokenization , Extract all money transaction from below sentence along with currency. 
transactions = "Tony gave two $ to Peter, Bruce gave 500 € to Steve"

'''
transactions = "Tony gave two $ to Peter, Bruce gave 500 € to Steve"

from nltk import word_tokenize

word=word_tokenize(transactions)
word
print(word[2],word[3])
print(word[-4],word[-3])
##################################################################################

# Q.2 Use stemming for following docs
docs = [
    "Mando talked for 3 hours although talking isn't his thing",
    "eating eats eat ate adjustable rafting ability meeting better"
    ]
import nltk
# first initialize the Porterstemmer for stemming
Stemmer=nltk.stem.PorterStemmer()
# We have given and docs which contain the two sentences as two exract thatt senetence we have to
# execute the loop so the both the statements get executed properly and the tokenization and steeming
# can be done.
for i in docs:
    words=word_tokenize(i)
    word=[Stemmer.stem(j) for j in words]
    senetence=' '.join(word)
    print(senetence)
# In this loop first we tokenize the sentence and then we will tokenize each word and then 
# join the words

#######################################################################################

# Q3.Convert these list of words into base form using Stemming and Lemmatization and observe the transformations 

lst_words = ['running', 'painting', 'walking', 'dressing', 'likely', 'children', 'whom', 'good', 'ate', 'fishing']
Stemmer=nltk.stem.PorterStemmer()

for i in lst_words:
    words=Stemmer.stem(i)
    print(words)

# After Execution of the code the each word in lst_words are convered into its base forn
# The suffix and preffix of the word get removed

from nltk.stem.wordnet import WordNetLemmatizer
lematizer=WordNetLemmatizer()
doc = "running painting walking dressing likely children who good ate fishing"
words=word_tokenize(doc)
words

for i in range(len(words)):
    word=lematizer.lemmatize(words[i])
    print(word)
    
# There will be doesn't change in any value of tthe text

#####################################################################################
#3.convert the given text into it's base form using both stemming and lemmatization
text ='''Latha is very multi talented girl.She is good at many skills like dancing, running, singing, playing.She also likes eating Pav Bhagi. she has a 
habit of fishing and swimming too.Besides all this, she is a wonderful at cooking too.
'''

# 1. Stemming
words=word_tokenize(text)
Stemmer=nltk.stem.PorterStemmer()
for i in words:
    word=Stemmer.stem(i)
    print(word)
    
# 2. Lemtization
lematizer=WordNetLemmatizer()
# Lemmatization using WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
for i in lemmatized_words:
    print(i)
    
##########################################################################################
'''
Q4. You are parsing a news story from cnbc.com. News story is stores in news_story.txt which is on whatsapp. You need to, 
1.	Extract all NOUN tokens from this story. You will have to read the file in python first to collect all the text and then extract NOUNs in a python list
2.	Extract all numbers (NUM POS type) in a python list
3.	Print a count of all POS tags in this story
'''

with open('news_story.txt') as tf:
    sen=tf.read()
sen

# 1. Extracting Noun
words=word_tokenize(sen)
words
tags=nltk.pos_tag(words)
nouns = [word for word, pos in tags if pos.startswith('N')]
nouns

# 2. Extract all numbers
num=[word for word, pos in tags if pos.startswith('CD')]
num

# 3. print Count of all PoS tags
from collections import Counter
count=Counter([pos[1 ]for pos in tags])
count
########################################################################################
# Name Entity Recognition Exercise

# 1.Extract all the Geographical (cities, Countries, states) names from a given text
text = """Kiran want to know the famous foods in each state of India. So, he opened Google and search for this question. Google showed that
in Delhi it is Chaat, in Gujarat it is Dal Dhokli, in Tamilnadu it is Pongal, in Andhrapradesh it is Biryani, in Assam it is Papaya Khar,
in Bihar it is Litti Chowkha and so on for all other states"""

import spacy

# Load the spaCy English language model
nlp = spacy.load('en_core_web_sm')

# Process the text using spaCy
doc = nlp(text)

# Extract geographical entities
geo = [ent.text for ent in doc.ents if ent.label_ in ['GPE', 'LOC']]

# Print the extracted geographical entities
print(geo)
################################
# 2. Extract all the birth dates of cricketers in the given Text
text = """Sachin Tendulkar was born on 24 April 1973, Virat Kholi was born on 5 November 1988, Dhoni was born on 7 July 1981
        and finally Ricky ponting was born on 19 December 1974."""

# Process the text using spaCy
doc = nlp(text)

# Extract entities with DATE label
dates = [ent.text for ent in doc.ents if ent.label_ == 'DATE']

# Print the extracted birth dates
for i in dates:
    print(i)

#Another Method for this is using nltk
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import ne_chunk

# Given text
text = """Sachin Tendulkar was born on 24 April 1973, Virat Kohli was born on 5 November 1988, Dhoni was born on 7 July 1981
        and finally Ricky Ponting was born on 19 December 1974."""

# Tokenize the text
tokens = word_tokenize(text)

# Perform part-of-speech tagging
tagged_tokens = pos_tag(tokens)

# Use named entity recognition (NE) to extract entities
named_entities = ne_chunk(tagged_tokens)

# Extract birth dates
birth_dates = []
for entity in named_entities:
    if isinstance(entity, tuple) and entity[1] == 'CD':
        birth_dates.append(entity[0])

# Print the extracted birth dates
for date in birth_dates:
    print(date)


###################################
