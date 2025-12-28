import os
import json
import re

def corpusToJson(word_list) :
    print("Choose your new JSON file name:")
    new_file_name = input("> ")
    while os.path.exists(new_file_name):
        print(f"{new_file_name}.json already exists, please choose a different file name:")
        new_file_name = input("> ")
    if re.search("$[.json]", new_file_name):
        with open(new_file_name, 'w') as json_file:
            json.dump(word_list, json_file)
    else:
        with open(new_file_name + ".json", 'w') as json_file:
            json.dump(word_list, json_file)