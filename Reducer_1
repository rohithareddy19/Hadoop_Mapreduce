#! /usr/bin/python
import sys
new_dict = {}
for line in sys.stdin:
    word, doc_count = line.split('\t')
    new_dict.setdefault(word,{})    
    for document_count in doc_count.split():
        document, count = document_count.split(':')
        count = int(count)
        new_dict[word].setdefault(document, 0)
        new_dict[word][document] += count 

for each_key in new_dict:    
    sys.stdout.write('%s\t%s\n' % (each_key, new_dict[each_key]))
