#The input for this mapper is set of text files which contains the books written by various authors.

#!/usr/bin/env python
import sys
import string
stopwords = ["a", "able", "about", "across", "after", "all", "almost", "also", "am", "among", "an", "and", "any", "are", "as", "at", "be", "because", "been", "but", "by", "can", "cannot", "could", "dear", "did", "do", "does", "either", "else", "ever", "every", "for", "from", "get", "got", "had", "has", "have", "he", "her", "hers", "him", "his", "how", "however", "i", "if", "in", "into", "is", "it", "its", "just", "least", "let", "like", "likely", "may", "me", "might", "most", "must", "my", "neither", "no", "nor", "not", "of", "off", "often", "on", "only", "or", "other", "our", "own", "rather", "said", "say", "says", "she", "should", "since", "so", "some", "than", "that", "the", "their", "them", "then", "there", "these", "they", "this", "tis", "to", "too", "twas", "us", "wants", "was", "we", "were", "what", "when", "where", "which", "while", "who", "whom", "why", "will", "with", "would", "yet", "you", "your",".","-",":"]

#Function to remove punctuation
def word_clean(word):
    word = word.lower()
    for c in string.punctuation:
        word = word.replace(c,"")
    return word
#Function to check if the word is a stopword
def stop_words(word):
    if word in stopwords or word == "":
        return False
    else:
        return True

#for each line
for text in sys.stdin:
    lines = text.split('\n')
    lines.pop(-1) 
    for line in lines:
        each_line = line.split(':::')
        each_line.pop(0)
        title = each_line[1].split(' ')
        authors = each_line[0]
        each_author = authors.split('::')
        for author_final in each_author:
            for each_word_in_title in title:
                each_word = word_clean(each_word_in_title) #pre-processing 
                if stop_words(each_word): #if it is not a stop word
                    sys.stdout.write("%s\t%s:1\n" %(author_final, each_word))            
            
            
