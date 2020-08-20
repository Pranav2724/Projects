#TWITTER sentiment Analysis

import random
import string
import pandas as pd
from nltk import pos_tag
from nltk.classify import accuracy
from nltk import FreqDist
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet,stopwords
from nltk import NaiveBayesClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC

lemmatizer = WordNetLemmatizer()

def simple_pos(pos_tag):         #part of speech
    
    if pos_tag.startswith('J'):
        return wordnet.ADJ
    elif pos_tag.startswith('V'):
        return wordnet.VERB
    elif pos_tag.startswith('N'):
        return wordnet.NOUN
    elif pos_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN


stop = stopwords.words('english')
punc = list(string.punctuation)
stop = stop + punc



df = pd.read_csv('training_twitter_x_y_train.csv')

X_raw = df['text']
Y_raw = df['airline_sentiment']

for i in range(len(X_raw)):
    X_raw[i] = word_tokenize(X_raw[i])
    temp = []
    for j in X_raw[i]:
        if(j not in stop):
            pos = pos_tag([j])
            clean_word = lemmatizer.lemmatize(j,pos=simple_pos(pos[0][1]))       
            temp.append(clean_word.lower())
    X_raw[i] = temp

for i in range(len(X_raw)):
    X_raw[i] = " ".join(X_raw[i])
    
cv = CountVectorizer(max_features=2000,max_df=0.8)#,max_df=0.8,min_df=0.1)
a = cv.fit_transform(X_raw)  #sparse matrix
X_final = a.todense()

df_t = pd.read_csv('Twitter_Test.csv')
X_raw_t = df_t['text']

for i in range(len(X_raw_t)):
    X_raw_t[i] = word_tokenize(X_raw_t[i])
    temp = []
    for j in X_raw_t[i]:
        if(j not in stop):
            pos = pos_tag([j])
            clean_word = lemmatizer.lemmatize(j,pos=simple_pos(pos[0][1]))       
            temp.append(clean_word.lower())
    X_raw_t[i] = temp

for i in range(len(X_raw_t)):
    X_raw_t[i] = " ".join(X_raw_t[i])

b = cv.transform(X_raw_t)
X_t_final = b.todense()


"""___________________________________________________________________________________________"""

clf = SVC()
clf.fit(X_final,Y_raw)

y_pred = clf.predict(X_t_final)
y_pred = pd.DataFrame(y_pred)
y_pred.to_csv('results_TSA.csv',index_label=False,index=False,header=False)

"""__________________________________________________________________________________________"""


from sklearn.naive_bayes import MultinomialNB

clf_nb = MultinomialNB()
clf_nb.fit(X_final,Y_raw)

y_pred2 = clf_nb.predict(X_t_final)
y_pred2 = pd.DataFrame(y_pred2)
y_pred2.to_csv('results_TSA.csv',index_label=False,index=False,header=False)
                    
