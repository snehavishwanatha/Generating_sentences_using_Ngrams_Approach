import nltk

#Word Tokenizing
text="Arthur is not feeling well."
tokens=nltk.word_tokenize(text)
print(tokens)

#Sentence Tokenizing
text ="Arthur is not feeling well. He will not come to the office. We must inform the boss."
stokens=nltk.sent_tokenize(text)
print(stokens)

#Regular Expression Tokenizing
#--->
text = "I can't do this. I won't do this."
tokens=nltk.word_tokenize(text)
print(tokens)
tokens=nltk.regexp_tokenize(text,"[\w']+")
print(tokens)

#--->
text="Good muffins cost $3.88 in New York."
tokens=nltk.word_tokenize(text)
print(tokens)
tokens=nltk.regexp_tokenize(text,"[\s]+",gaps=True)
print(tokens)

#--->
tokens=nltk.regexp_tokenize(text,"[A-Z]\w+")
print(tokens)

#--->
text = "Alas, it has not rained today. When, do you think, will it rain again?"
tokens=nltk.regexp_tokenize(text,"[,\.\?!]\s*")
print(tokens)

