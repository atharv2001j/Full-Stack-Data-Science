# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 21:25:42 2023

@author: Atharv Joshi
"""
'''Text- minimng'''

###############
# fiinding the index of the letter
senctence="we are learning textmining from Sanjivani AI"
# if we want to know position of learning
senctence.index("learning")
# it will show learning is at the 7 position
# this is going to show thw charater position from 0  inculding

###################################
# finding the position of the words
# we want to know postion textminig word
senctence.split().index('textmining')
#it will split the words  in list  and count the position
# if you want to see the list select senectence.split() and
# it will show at 3

############################################################
#suppose we want print any word in the reverse order
senctence.split()[2][: :-1]
# [start:end end:-1 (start)]  will start from -1,-2,-3 till the end
#learnig will be printed in the reverse order

################################################
# suppose we want to print first and last word of the sentence
words=senctence.split()
first_words=words[0]
first_words
last_words=words[-1]
last_words

##########################################
# now we want to concate the first and last words
concate_word=first_words+" "+last_words
concate_word
###########################################
# we want the to print  even words from the sentence
[words[x] for x in range(len(words)) if x%2==0]
# the words having the odd length are not print
##############################################
senctence
# now we want to display only ai
senctence[-3:]
# balaji  publication
############################################
# suppose we want to display the entire sentence in the revrese order
senctence[::-1]
# now the all the sentence are print in the reverse order

##########################################
# suppose we want to select each word and print in the reverse order
words
print(" ".join(word[::-1] for word in words))
# 


#############################################################
''' ********************tokenization*******************************'''
import nltk
nltk.download('punkt')          # it is install here only
from nltk import word_tokenize
words=word_tokenize("I am reading NLP Fundamentals")
print(words)
# it is split the hole sentance into each words
##########################################################
# Parts of speech tagging
nltk.download('averaged_perceptron_tagger')
nltk.pos_tag(words)
############################################################
# Parts of speecg
'''
CC => Coordinating Conjunction
CD => Cardinal Number
DT => Determiner
EX => Existential There
FW => Foreign Word
IN => Preposition or Subordinating Conjunction
JJ => Adjective
JJR => Adjective, Comparative
JJS => Adjective, Superlative
LS => List Item Marker
MD => Modal
NN => Noun, Singular or Mass
NNS => Noun, Plural
NNP => Proper Noun, Singular
NNPS => Proper Noun, Plural
PDT => Predeterminer
POS => Possessive Ending
PRP => Personal Pronoun
PRP$ => Possessive Pronoun
RB => Adverb
RBR => Adverb, Comparative
RBS => Adverb, Superlative
RP => Particle
SYM => Symbol
TO => to
UH => Interjection
VB => Verb, Base Form
VBD => Verb, Past Tense
VBG => Verb, Gerund or Present Participle
VBN => Verb, Past Participle
VBP => Verb, Non-3rd Person Singular Present
VBZ => Verb, 3rd Person Singular Present
WDT => Wh-determiner
WP => Wh-pronoun
WP$ => Possessive Wh-pronoun
WRB => Wh-adverb

'''
###############################################
from nltk.corpus import stopwords
stop_words=stopwords.words('English')
# you can verify that 179 sopwords in library
print(stop_words)

sentence1='I am Learning NLP: It is one of the most popular Language'

#First we will tokenize it
sentence_words=word_tokenize(sentence1)

sentence_no_stops=' '.join([words for words in sentence_words if words not in stop_words])
sentence_no_stops
sentence1

##############################################
# suppose we want to  replace the  words
sentence2='I visited MY from IND on 14-02-19'
normalized_sentence=sentence2.replace('MY','Malesia').replace('IND','India')
normalized_sentence=normalized_sentence.replace('-19','-2020')
print(normalized_sentence)

###############################################
# if we want autocorrection in sentence
from autocorrect import Speller
# Declare the function Speller for English
spell=Speller(lang='en')
spell('English')
###################################################
# Suppose we want to correct whole sentence
sentence3='Natural Language processi deals withinnnn the aaart of extracin sentiiments'
sentence3=word_tokenize(sentence3)
corrected_sentence=" ".join([spell(word) for word in sentence3])
print(corrected_sentence)
#####################################################
#Stemming
stemer=nltk.stem.PorterStemmer()
stemer.stem('Programming')
stemer.stem('Programed')
stemer.stem('Jumping')
stemer.stem('Jumped')
#######################################################
#Lematization
nltk.download('wordnet')
from nltk.stem.wordnet import WordNetLemmatizer
lematizer=WordNetLemmatizer()
lematizer.lemmatize("Programed")
lematizer.lemmatize("Program")
lematizer.lemmatize('batting')
lematizer.lemmatize('amazing')
####################################################
# Name entity recognition
# It is usually not present in dictionary so we haave t treet
# themseparately
#################################################
#Chunking
import nltk
nltk.download('maxent_ne_chunker')
nltk.download('words')
senetence='We are leaarning NLP in python by sanjivaniAI '
##First we will tokenize
word=word_tokenize(senetence)
words=nltk.pos_tag(word)
i=nltk.ne_chunk(words,binary=True)
[a for a in i if len(a)==1]
#####################################################
# Sentence Tokenization
from nltk.tokenize import sent_tokenize
sent=sent_tokenize('we are lerning NLP in Python .Deliver by SanjivaniAI. ')
sent
########################################################
# if we have to find the context of particular word
from nltk.wsd import lesk
sentence1='keep your savings in the bank'
print(lesk(word_tokenize(sentence1),'bank'))
#Try for same word
sentence2='It is risk to drive over bank of river'
print(lesk(word_tokenize(sentence2),'bank'))

'''
the first bank and the second bank having diffrent meaning as per
the sentence so to identify it we use the lesk methos which will
categorized the the two sentence according to its type
'''
########################################################
# Bank has different meaning if we have to find the exact meaning
# of the bank execute following code