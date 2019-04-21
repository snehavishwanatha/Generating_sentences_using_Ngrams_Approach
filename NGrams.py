import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter

text = "I want to go to London. I also want to go to Norway and Iceland. I want to take my friend to London." 

token = nltk.word_tokenize(text)
bigrams = ngrams(token,2)
trigrams = ngrams(token,3)
fourgrams = ngrams(token,4)

print(Counter(bigrams))
print(Counter(trigrams))

