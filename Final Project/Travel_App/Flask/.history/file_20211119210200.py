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



import spacy
import pandas as pd
from spacy.lang.en.stop_words import STOP_WORDS

# Load spacy model
nlp = spacy.load('en', parser=False, entity=False)        

# New stop words list 


# Mark them as stop words
for w in customize_stop_words:
    nlp.vocab[w].is_stop = True


# Test data
df = pd.DataFrame( {'Sumcription': ["attach poster on the wall because it is cool",
                                   "eating and sleeping"]})

# Convert each row into spacy document and return the lemma of the tokens in 
# the document if it is not a sotp word. Finally join the lemmas into as a string
df['Sumcription_lema'] = df.Sumcription.apply(lambda text: 
                                          " ".join(token.lemma_ for token in nlp(text) 
                                                   if not token.is_stop))

print (df)