import os
import words as w 
import sentences as s 
import verses as v
import toJson as tj


print("Good day traveler! \n"
"This little script will list the words of your text file into JSON file.")
print("First, input your corpus file path:")
file_path = input("> ")
while not os.path.exists(file_path):
    print("Input a correct path or quit with Ctrl+c:")
    file_path = input("> ")

print("Tell me how you want to split your corpus: \ntype w for words, s for sentences and v for verses.")
choice = input("> ")
while True: 
    match choice:
        case "v":
            tj.corpusToJson(v.makeVerses(file_path))
            print("Creating JSON...")
            print("Your corpus in JSON format is ready! Goodbye :)")
            quit()
        case "s":
            tj.corpusToJson(s.makeSentences(file_path))
            print("Creating JSON...")
            print("Your corpus in JSON format is ready! Goodbye :)")
            quit()
        case "w":
            print("Choose the minimal word length to match. Input 1 to keep every word:")
            wordLen = input("> ")
            while not int(wordLen):
                print("Input an integer or quit with Ctrl+c")
                word_len = input("> ")
            tj.corpusToJson(w.makeWords(file_path, int(wordLen)))
            print("Creating JSON...")
            print("Your corpus in JSON format is ready! Goodbye :)")
            quit()
        case _:
            print("Incorrect imput. Type v, s or w.")
    choice = input("> ")

