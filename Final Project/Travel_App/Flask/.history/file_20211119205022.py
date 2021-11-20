import spacy
from spacy.lang.en.stop_words import STOP_WORDS
nlp = spacy.load('en')

# Build a list of stopwords to use to filter
stopwords = list(STOP_WORDS)

stopwords

"""##### Getting Lemma and Stop words"""

print(stopwords)
