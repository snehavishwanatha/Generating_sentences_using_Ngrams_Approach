from nltk import CFG
import random
from nltk.parse.generate import generate

grammar = CFG.fromstring('''S -> VP NP   
NP -> Det N   
VP -> V   
Det ->'the '   
N -> 'door' | 'window'   
V -> 'Open' | 'Close' ''')
print(grammar.start())
print(grammar.productions())
for sentence in generate(grammar,n=10):
     print(' '.join(sentence))
     
grammar = CFG.fromstring('''S -> Pro VP | NP VP
  VP -> V NP | V NP PP
  PP -> P NP
  Pro -> "I"
  V -> "saw" | "ate" | "walked"
  NP -> "John" | "Jay" | "Bob" | Det N | Det N PP
  Det -> "a" | "the" | "my"
  N -> "man" | "dog" | "telescope" | "park"
  P -> "in" | "on" | "by" | "with" ''')
print(grammar.start())
print(grammar.productions())
for sentence in generate(grammar,n=19):
     print(' '.join(sentence))

