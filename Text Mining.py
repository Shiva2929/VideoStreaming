
# coding: utf-8

# In[83]:


import os
import nltk
import nltk.corpus
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.stem import PorterStemmer


# In[54]:


corp = PlaintextCorpusReader("C:\\My Data/", ".txt")


# In[44]:


text = nltk.Text(corp.words())


# In[55]:


#match = text.concordance('hadoop')
def lemmatize_stemming(text):
    return PorterStemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))


# In[82]:


def preprocess(text):
    result=[]
    for token in gensim.utils.simple_preprocess(text) :
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))
    return result
   
        


# In[79]:




from sklearn.datasets import fetch_20newsgroups
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import nltk
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
import nltk
from nltk.corpus.reader.plaintext import PlaintextCorpusReader


data = pd.read_csv("C:\\Users/shiva/Desktop/VideoData.txt", sep=":", header=None, names = ["Videoid", "Text"],
                   dtype={"Videoid": np.str, "Text": np.str})


data['word_count'] = data['Text'].apply(lambda x: len(str(x).split(" ")))
data['char_count'] = data['Text'].str.len() ## this also includes spaces


data['Text'] = data['Text'].apply(lambda x: " ".join(x.lower() for x in x.split()))

data['Text'] = data['Text'].str.replace('^\w\s"}{','')
data['Text'] = data['Text'].str.replace('[music]','')
data['Text'] = data['Text'].str.replace('[applause]','')
data['Text'] = data['Text'].str.replace('[','')
data['Text'] = data['Text'].str.replace(']','')
data['Text'] = data['Text'].str.replace('"','')

#stop = stopwords.words('english')
#data['Text'] = data['Text'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))




#print(data['Text'].head())
#file = open("C:\\Users/shiva/Downloads/news_summary.csv")
#read_file = file.read()
#data['Videoid'] = data['Videoid'].str.replace('{','')

sentence = data['Text'].astype('str')

from nltk.tokenize import sent_tokenize
import nltk.data
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

print('\n-----\n'.join(tokenizer.tokenize(sentence)))

#print(data['Text'])

#corp = PlaintextCorpusReader('',sentence)
#print(sentence)
#text1 = nltk.Text(sentence.words())
#tokens = nltk.word_tokenize(sentence, 'english')
#print(text1)

#st = PorterStemmer()
#data['Text'][:5].apply(lambda x: " ".join([st.stem(word) for word in x.split()]))















#newsgroups_train = "I am doing very good"
#newsgroups_test = fetch_20newsgroups(subset="test", shuffle = True)


#print(list(newsgroups_train))

#text = nltk.Text(nltk.word_tokenize(read_file))

#print(text)

#match = text.concordance('india')
#print(match)



#def lemmatize_stemming(text):
 #   return PorterStemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))
  #  print(PorterStemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v')))






