import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
import pandas as pd

df = pd.read_csv("test_data1_and_name.csv", usecols=['nameSupplier', 'nameAmazon'])

for element in df['nameAmazon']:


    nlp = en_core_web_sm.load()
    doc = nlp(element)
    print([(X.text, X.label_) for X in doc.ents])
