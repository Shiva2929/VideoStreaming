
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




