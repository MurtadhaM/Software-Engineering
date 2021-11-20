# Author: Murtadha Marzouq
# Date: 12/10/2021
# Version: 1.0 Fetching Tweets and saving to file

#!pip3 install twint nest_asyncio
#!pip3 install --user --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint
import twint
import nest_asyncio
import json, codecs
nest_asyncio.apply()



# Instantiate and configure the twint-object
try:
  c = twint.Config()
  c.Store_object = True
  c.Pandas =True
  c.Search = "#okboomer"
  c.Hide_output=True
  c.Pandas_clean=True
  c.Limit = 10
  c.Lang = 'en'
  c.Store_csv = True
  c.Output = "data/Test_Search.csv"

  # Run search
  twint.run.Search(c)

  # Quick check
  twint.storage.panda.Tweets_df.head()


  df = twint.storage.panda.Tweets_df
  print('Columns are')
  print(df.keys())
  print('number of entries:' + str(len(df.values)))
  tweet_text = df['tweet'].to_list()
  print(tweet_text)

  with open('text_data.json', 'wb') as f:
   json.dump(tweet_text, codecs.getwriter('utf-8')(f), ensure_ascii=False)
except Exception as e:
  print(e)
print(tweet_text)

"""# New Section"""

df = twint.storage.panda.Tweets_df
print('Columns are')
print(df.keys())
print('number of entries:' + str(len(df.values)))




from spacy.lang.en import English

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = English()

text = """He determined to drop his litigation with the monastry, and relinguish his claims to the wood-cuting and 
fishery rihgts at once. He was the more ready to do this becuase the rights had become much less valuable, and he had 
indeed the vaguest idea where the wood and river in question were."""

#  "nlp" Object is used to create documents with linguistic annotations.
my_doc = nlp(str(tweet_text))

# Create list of word tokens
token_list = []
for token in my_doc:
    token_list.append(token.text)

from spacy.lang.en.stop_words import STOP_WORDS

# Create list of word tokens after removing stopwords
filtered_sentence =[] 

for word in token_list:
    lexeme = nlp.vocab[word]
    if lexeme.is_stop == False:
        filtered_sentence.append(word) 
print(token_list)
print(filtered_sentence)   