# Hadoop_Mapreduce
Hadoop Map Reduce program on text files
This program creates an inverted list of words, files that contain them and the number of times the word occurs in each file.
The outcome of first mapper program i.e mapper_1 would be each word in the file followed by the name of that file follwed by a count of one.
The output from the reducer would be in the below format
‘anger’		{‘histories’: 3, ‘tragedies’: 8}
‘laugh’		{‘comedies’: 7, ‘poems’: 2, ‘histories’: 15}
………

The second set of map reduce program computes how many times every term occurs across titles, for each author.
Here is an example of the outcome:

For example, the author Alberto Pettorossi has the following terms occur in titles with the indicated cumulative frequencies (across all his papers): program:3, transformation:2, transforming:2, using:2, programs:2, and logic:2. 
