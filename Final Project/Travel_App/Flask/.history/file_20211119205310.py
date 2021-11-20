import spacy
from spacy.lang.en.stop_words import STOP_WORDS

# Build a list of stopwords to use to filter
stopwords = list(STOP_WORDS)

stopwords

"""##### Getting Lemma and Stop words"""
clean_words = []
for word in stopwords:
    if word.is_stop == False and not word.is_punct:
        print(word)
        clean_words.append(word)
        
        print(len(clean_words))
        

