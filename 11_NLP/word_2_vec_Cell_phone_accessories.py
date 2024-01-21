# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 08:44:00 2023

@author:Atharv Joshi
"""

#This assignment we done to check the similarity of words

import pandas as pd
import gensim

df = pd.read_json('Cell_Phones_and_Accessories_5.json', lines=True)
df

df.shape

#Simple Preprocessing & Tokenization
review_text = df.reviewText.apply(gensim.utils.simple_preprocess)
review_text

#Let us check first word of each review
review_text.loc[0]
#Let us check first row of dataframe
df.review_text.loc[0]
#Training the Word2Vec Model
model = gensim.models.Word2Vec(
    window=10,
    min_count=2,
    workers=4)

""" 
Where window is how many words you are going to
consider as sliding window you canchoose any count
mind_count-there must min 2 words in each sentence
worker:no.of threads
"""

# Build Vocabulary 
model.build_vocab(review_text,progress_per=1000)
# progress_per: after 1000 words it shows progress


# Train the word2vex\c model
# It will take time,have patience
model.train(review_text,total_examples=model.corpus_count,epochs=model.epochs)

# Save the Model
model.save('word2vec-amazon-cell-accessories-reviews-short.model')

# Now we will find the Similar  words and Similarity between words

model.wv.most_similar('bad')
model.wv.similarity(w1='cheap',w2='inexpensive')
model.wv.similarity(w1='great',w2='good')
