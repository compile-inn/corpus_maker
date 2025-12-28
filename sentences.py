import os
import re
import string
import json

# Make a CLI to create corpuses from text file to JSON file. 
# Option to choose what words to remove. One to remove duplicates.
# Maybe add a function that analyses the contents (most used word, longest word, etc.)

# Function definitions
def makeSentences(file) :
    fhandle = open(file, "r")
    inp = fhandle.read()
    corpus = [sentence.strip() for sentence in inp.split(".")]
    return corpus

