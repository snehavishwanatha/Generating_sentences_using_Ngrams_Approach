"""
Created on Mon Apr  1 16:11:02 2019

@author: sneha
"""

import nltk

'''defining the pattern for identifying Noun Phrase'''
patterns = """
    NBAR:
        {<NN.+|JJ>*<NN.*>}
    NP:
        {<NBAR>}
        {<NBAR><IN><NBAR>} 
    """

'''Calling the RegexpParser method'''
NPChunker = nltk.RegexpParser(patterns)

'''Tokenizing the sentence and Pos-tagging the tokenized sentence'''
statement=input("Enter the statement  ")
sentences = [nltk.word_tokenize(statement)]
print("Tokenized sentence",sentences)
sentences = [nltk.pos_tag(sent) for sent in sentences]
print("POS-Tagged sentence",sentences)

'''Identifying the NP chunks'''
nps = []
tree = NPChunker.parse(sentences[0])
print("Tree",tree)
for subtree in tree.subtrees():
    print("POS",subtree.label())
    if subtree.label() == 'NP' or subtree.label() == 'NBAR':
            t = subtree
            t = ' '.join(word for word, tag in t.leaves())
            print(t)
            nps.append(t)
print("Noun phrases",set(nps))