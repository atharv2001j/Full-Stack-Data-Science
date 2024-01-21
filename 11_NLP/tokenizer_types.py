# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 09:02:53 2023

@author: Atharv Joshi
"""

import re
sentence='sharat twitted ,wittnessing 70th Republic Day of India from Rajpath,\new Delhi memorizing performance by Indian Army'

re.sub(r'([^\s\w]|_)+', ' ',sentence).split()
# It will remved all the witspace with new line
###################################################
#Use custome designed function
def n_gram_extactor(input_str,n):
    tokens=re.sub(r'([^\s\w]|_)+', ' ',input_str).split()
    for i in range(len(tokens)-n+1):
        print(tokens[i:i+n])

n_gram_extactor('The cute little Yash is playing with Toy', 2)
n_gram_extactor('The cute little Yash is playing with Toy', 3)
#####################################################
# Similarly above we can done by
from nltk import ngrams
list(ngrams('The cute little Yash is playing with Toy'.split(),2))
list(ngrams('The cute little Yash is playing with Toy'.split(),3))
######################################################
from textblob import TextBlob
blob=TextBlob('The cute little Yash is playing with Toy')
blob.ngrams(2)
blob.ngrams(3)
# It will work similar as nltk
######################################################
from keras.preprocessing.text import text_to_word_sequence
sentence='sharat twitted ,wittnessing 70th Republic Day of India from Rajpath,\new Delhi memorizing performance by Indian Army'
text_to_word_sequence(sentence)
# This will also work same as the texblob
########################################################
# Tokenization using Textblob
from textblob import TextBlob
blob=TextBlob(sentence)
blob.words
########################################################
#################Types of Tokenizer#####################
# 1. Tweet Tokenizer

from nltk.tokenize import TweetTokenizer
tweet_tokenizer=TweetTokenizer()
tweet_tokenizer.tokenize(sentence)
# It will tkenize the sentence into list
#######################################################
# 2. multi- word expression
from nltk.tokenize import  MWETokenizer
mwe_tokenize=MWETokenizer([('Republic','Day')])
mwe_tokenize.tokenize(sentence.split())
mwe_tokenize.tokenize(sentence.replace("/",' ').split())

# It will combined the Rebulic Day Word
######################################################
# 3.Regular Expression Tokenizer
from nltk.tokenize import RegexpTokenizer
reg_tokenizer=RegexpTokenizer('\w+|\$[\d\.]+|\S+')
reg_tokenizer.tokenize(sentence)

#########################################################
# 4. White space tokenizer
from nltk.tokenize import WhitespaceTokenizer
wh_tokenizer=WhitespaceTokenizer()
wh_tokenizer.tokenize(sentence)
##########################################################
# 5. Word Punct Tokenizer
from nltk.tokenize import WordPunctTokenizer
wp_tokenizer=WordPunctTokenizer()
wp_tokenizer.tokenize(sentence)
#########################################################
# Regular expression Stemmer
sentence='I love playing cricket .Cricket Player practice hard in training '
from nltk.stem import RegexpStemmer
regex_stemmer=RegexpStemmer('ing$')
' '.join(regex_stemmer.stem(wd) for wd in sentence.split())

#########################################################
# Porter Stemmer
sentence='Before eating i is good to sanitize your hand'
from nltk.stem.porter import PorterStemmer
pr_stemmer=PorterStemmer()
words=sentence.split()
' '.join([pr_stemmer.stem(wd) for wd in words])

###########################################################
# Lemmatization
import nltk
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
nltk.download('wordnet')
lemmatizer=WordNetLemmatizer()
sentence='The codes execute today are better than wjhat is going on'
words=word_tokenize(sentence)
' '.join([lemmatizer.lemmatize(word) for word in words])
##########################################################
# Sigularizatin and Plurlization
from textblob import TextBlob
sentence9=TextBlob("She sells seashells on the seashare")
words=sentence9.words#we want to make word[2] i>e. seashells in singular form
sentence9.words[2].singularize()
#we want word $ i.e. seashare in plural form 
sentence9.words[5].pluralize()
############################################################
# Language Translation
from textblob import TextBlob
en_blob=TextBlob(u'muy bien')
en_blob.translate(from_lang='es',to='en')
############################################################
# Custom stopwors removal
from nltk import word_tokenize
sentence9="She sells seashells on the seashare"
custom_stop_word_list=['she','on','the','am','is']
words=word_tokenize(sentence9)
" ".join([word for word  in words if word.lower() not in custom_stop_word_list])
# It will remove theall the cusom stopwords from sentence
#############################################################