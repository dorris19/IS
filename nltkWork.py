from nltk import *

s = input("Enter text: ")

#print("You typed", len(word_tokenize(s)), "words.")
print(pos_tag(word_tokenize(s)))
