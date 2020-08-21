#text classification
import numpy as np
import pandas as pd
from sklearn import model_selection
from sklearn import datasets
import re
import operator

data = datasets.load_files(r'C:\\python_20\\20_newsgroups')


X = data.data
Y = data.target
Y_t = data.target_names

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

x_train,x_test,y_train,y_test=model_selection.train_test_split(X,Y)

dic={}
for i in range(len(x_train)):
    word=str(x_train[i].lower())
    word = word.replace('\\n','')
    #splitting the text into words
    stripped=re.split(r'\W+',word)   #\W+ indicates splitting where a word DOES NOT occur
    #Iterating over each text
    for s in stripped:
        #we will not include stop_words, alpha-numerics, punctuations or irrelevant word of length less than 2 in our dictionary
        if not(s.isalpha()) or s in stop_words or len(s)<=2:
            continue
        if s in dic:
            dic[s]+=1
        else:
            dic[s]=1

sorted_dic = sorted(dic.items(), key=operator.itemgetter(1),reverse=True)

bag_of_words = [i[0] for i in sorted_dic[:2001]]

x_train_dataset=np.zeros([len(x_train),len(bag_of_words)],int)
for i in range(len(x_train)):
    words = str(x_train[i].lower())
    words = words.replace('\\n','')
    word=re.split(r'\W+',words)
    #Iterating over each word
    for j in word:
        #We will add the frequency corresponding to that word only which is in our answer1(feature list)
        if j in bag_of_words:
            x_train_dataset[i][bag_of_words.index(j)]+=1
            
x_test_dataset=np.zeros([len(x_test),len(bag_of_words)],int)
for i in range(len(x_test)):
    words = str(x_test[i].lower())
    words = words.replace('\\n','')
    word=re.split(r'\W+',words)
    #Iterating over each word
    for j in word:
        #We will add the frequency corresponding to that word only which is in our answer1(feature list)
        if j in bag_of_words:
            x_test_dataset[i][bag_of_words.index(j)]+=1
            
"""__________________________________________________________________________________________________________________"""

#Multinomial Naive Bayes


from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score

clf=MultinomialNB()
clf.fit(x_train_dataset,y_train)         

y_pred=clf.predict(x_test_dataset)   

print("Score on training data:",clf.score(x_train_dataset,y_train))
print("Score on testing data:",clf.score(x_test_dataset,y_test))

#Score on training data: 0.9011802360472094
#Score on testing data: 0.871

"""___________________________________________________________________________________________________________________"""
            
# Self Implementation

def fit(x_train_dataset,y_train,bag_of_words):
    count={}
    total_word=0
    y_train=np.array(y_train)
    #Total no. of document is calculated
    count["total_doc"]=len(y_train)
    classes=set(y_train)
    for i in classes:
        temp=0
        #selecting x_train corresponding to class present in y_train
        x_train_with_i=x_train_dataset[y_train==i]
        #finding length of data with category corresponding to i 
        temp2=x_train_with_i.shape[0]
        count[i]={}
        #Iterating over answer1(actual feature list)
        for feature in bag_of_words:
            #Calculating total word in feature
            l=(x_train_with_i[:,bag_of_words.index(feature)]).sum()
            count[i][feature]=l
            temp+=l
        #Total word in that class
        count[i]["word_in_class"]=temp
        #Length of data with y_train belonging to specific class
        count[i]["length"]=temp2
        
    return count

def probability(x_test,dic,classes):
    prob=np.log(dic[classes]["length"])-np.log(dic["total_doc"])
    feature=list(dic[classes].keys())
    #-2 is done becuase there will be "length" and "word in class" present in feature. 
    for j in range (len(feature)-2):
        xj=x_test[j]
        #If frequency is 0, we will not consider it
        if xj==0:
            current_prob=0
        else:
            #Extra addition part is Laplace correction
            num=dic[classes][feature[j]]+1
            den=dic[classes]["word_in_class"]+len(dic[classes].keys())-2
            current_prob=np.log(num)-np.log(den)
        prob+=current_prob
    return prob

def predict_for_single(x_test,dic):
    best_prob = -1000
    best_class = -10
    first_run=True
    classes=dic.keys()
    for i in classes:
        if i=="total_doc":
            continue
        prob=probability(x_test,dic,i)
        if first_run or prob>best_prob:
            best_prob=prob
            first_run=False
            best_class=i
    return best_class

def predict_(x_test,dic):
    y_pred=[]
    for x in x_test:
        y_pred.append(predict_for_single(x,dic))
    return y_pred

def score(y_test,y_pred):
        count = 0
        for i in range(len(y_pred)):
            if y_pred[i] == y_test[i]:
                count+=1
        return count/len(y_pred)
    
dictionary=fit(x_train_dataset,y_train,bag_of_words)
y_pred=predict_(x_test_dataset,dictionary)   

print("Score on training data:",score(y_train,y_pred))
print("Score on testing data:",score(y_test,y_pred))


#Score on testing data is 90.48%
 

            
