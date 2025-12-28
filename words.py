import os
import string

# Make a CLI to create corpuses from text file to JSON file. 
# Option to choose what words to remove. One to remove duplicates.
# Maybe add a function that analyses the contents (most used word, longest word, etc.)

# Function definitions
def makeWords(file, word_len) :
    fhandle = open(file, "r")
    inp = fhandle.read()
    del_punct = inp.translate(str.maketrans("", "", string.punctuation))
    words = del_punct.split()
    corpus = [x for x in words if len(x) > word_len]
    return corpus
