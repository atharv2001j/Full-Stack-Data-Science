# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 08:50:42 2023

@author: Atharv Joshi
"""
# How to use the TF-IDF

import pandas as pd
from  sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

corpus=['the mouse had a tiny little mouse','The cat saw the mouse','The cat catch the mouse','the end of the mouse story']

# Intialize the count vector
cv=CountVectorizer()

# To count the totalnumber of tf
word_count_vector=cv.fit_transform(corpus)
word_count_vector.shape

# Lets apply the IDF
tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
tfidf_transformer.fit(word_count_vector)

# This matrix is in the raw form lets convert it ino the dataframe
df_idf=pd.DataFrame(tfidf_transformer.idf_,index=cv.get_feature_names_out(),columns=['idf_weights'])

df_idf.sort_values(by=['idf_weights'])
# It will sort the values in ascending order
##################################################################################################
# Try for another example

corpus=["Ther eating pizza, Loel is eating pizza, Tronman ate pizza already",
        "Apple is announcing new phone tomorrow","Tesla is announcing new model 3 tomorrow ","Google is announcing new pixel-6 tomorrow",
        "Microsoft is announcing new surface tomorrow","Amazon is announcing new eco-dot tomorrow",
        "I am eating biryani and you are eating grapes"]

# Let us initialize the vectorizer
v=TfidfVectorizer()
v.fit(corpus)
transfrom_output=v.transform(corpus)

# Print the vocabulary
v.vocabulary_

# Let us print the idf for each word

all_feature_names=v.get_feature_names_out()
for word in all_feature_names:
    # Lets get the index in the feature
    indx=v.vocabulary_.get(word)
    # get the score
    idf_score=v.idf_[indx]
    print(f"{word} : {idf_score}")
###################################################################################
import pandas as pd
df=pd.read_csv('Ecommerce_data.csv')
df.head(5)

df.shape

# Check  the distribution of the labels
df['label'].value_counts()

# Add the new columns by assigning some value tothe distribution

df['label_num']=df['label'].map({
    'Household':0,
    'Books':1,
    'Electronics':2,
    'Clothing & Accessories':3
    })

# Check the result
df.head(5)

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(df.Text,df.label_num,test_size=0.2,random_state=2022,stratify=df.label_num)
# Straisfy equally distribute the data among all classes
# radom state will choose the random data for the testing and training purpose
X_train.shape
X_test.shape

y_train.value_counts()
y_test.value_counts()
###################################################
# Apply to classifier

from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

# 1. Crete a pipeline object
clf=Pipeline(
    [
     ('vectorizer_tfidf',TfidfVectorizer()),
     ('KNN',KNeighborsClassifier())])

# 2. fit the model with X_train and y_train
clf.fit(X_train,y_train)

# 3. Get the prediction for the X_train and stored it in y_pred
y_pred=clf.predict(X_test)

# 4. print the classification report

print(classification_report(y_test, y_pred))
###################################################################################################
