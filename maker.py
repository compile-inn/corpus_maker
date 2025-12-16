import os
import string
import json

# Make a CLI to create corpuses from text file to JSON file. 
# Option to choose what words to remove. One to remove duplicates.
# Maybe add a function that analyses the contents (most used word, longest word, etc.)

# Function definitions
def makeC(file, word_len) :
    fhandle = open(file, "r")
    inp = fhandle.read()
    del_punct = inp.translate(str.maketrans("", "", string.punctuation))
    words = del_punct.split()
    corpus = [x for x in words if len(x) > word_len]
    return corpus

# Maybe the file name could be text name + minimum word length.
def corpusToJson(word_list) :
    if os.path.exists("myCorpus.json"):
        print("myCorpus.json already exists, please choose a different file name:")
        input("> ")
    else:
        with open('myCorpus.json', 'w') as json_file:
            json.dump(word_list, json_file)

# Script start
print("Good day traveler! /n" \
"This little script will list the words of your text file into JSON file.")
print("Input file path:")
file_path = input("> ")
while not os.path.exists(file_path):
    print("Input a correct path or quit with Ctrl+c:")
    file_path = input("> ")
print("Choose the minimal word length to keep. Input 1 to keep every word:")
word_len = input("> ")
while not int(word_len):
    print("Input an integer or quit with Ctrl+c")

corpusToJson(makeC(file_path, int(word_len)))
print("Your corpus in JSON format is ready! Goodbye :)")

