from os.path import expanduser
home = expanduser("~")
import nltk
from nltk.tag.senna import SennaTagger
st = SennaTagger(home+'/senna')


text="The race is tough."
tag = nltk.word_tokenize(text)
print("POS tag ",nltk.pos_tag(tag))
print("Senna tagger ",st.tag(text.split()))


text="The candidate has finally decided to race."
tag = nltk.word_tokenize(text)
print("POS tag ",nltk.pos_tag(tag))
print("Senna tagger ",st.tag(text.split()))


