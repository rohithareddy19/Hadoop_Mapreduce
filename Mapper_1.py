
#The input is shakespeare file 


#!/usr/bin/env python
import string 
import sys
import os
stopwords = ["a", "able", "about", "across", "after", "all", "almost", "also", "am", "among", "an", "and", "any", "are", "as", "at", "be", "because", "been", "but", "by", "can", "cannot", "could", "dear", "did", "do", "does", "either", "else", "ever", "every", "for", "from", "get", "got", "had", "has", "have", "he", "her", "hers", "him", "his", "how", "however", "i", "if", "in", "into", "is", "it", "its", "just", "least", "let", "like", "likely", "may", "me", "might", "most", "must", "my", "neither", "no", "nor", "not", "of", "off", "often", "on", "only", "or", "other", "our", "own", "rather", "said", "say", "says", "she", "should", "since", "so", "some", "than", "that", "the", "their", "them", "then", "there", "these", "they", "this", "tis", "to", "too", "twas", "us", "wants", "was", "we", "were", "what", "when", "where", "which", "while", "who", "whom", "why", "will", "with", "would", "yet", "you", "your"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]

#Function to remove punctuation and digits
def word_clean(word):
    for c in string.punctuation:
        word = word.replace(c,"")
    for c in numbers:
        word = word.replace(c,"")
    return word

#Function to check for stopwords
def stop_words(word):
    if word in stopwords or word == "":
        return False
    else:
        return True

for line in sys.stdin:
    doc_id = os.getenv('map_input_file') 
    doc_id = doc_id.split("/")[-1] #getting the document name
    l = line.strip().split()
    for word in l:
        word = word_clean(word) #preprocessing each word
        if stop_words(word): # if word is not a stop word
            sys.stdout.write("%s\t%s:1\n" % (word.lower(), doc_id))
