import spacy
from spacy import displacy

nlp = spacy.load('en')
doc = nlp(u'2 + 2 = 4')
displacy.serve(doc, style='dep')
