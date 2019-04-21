import nltk
from nltk import word_tokenize

text = word_tokenize("And now for something completely different")
tag=nltk.pos_tag(text)
#Here we see that and is CC, a coordinating conjunction; now and completely are RB, or adverbs; for is IN, a preposition; something is NN, a noun; and different is JJ, an adjective.
print(tag)

text = word_tokenize("They refuse to permit us to obtain the refuse permit")
tag=nltk.pos_tag(text)
print(tag)

