#accept english word and give its meaning
import json #to handle JSON files
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def WordDefinition(word):
        word = word.lower()
        if word in data:
            return data[word]
        elif len(get_close_matches(word,data.keys(),cutoff=0.8))>0:
            top_match = get_close_matches("rainn",data.keys())[0]
            print("Did you mean %s instead?" % (top_match))
            choice = input("Enter Y or N: ")
            if choice.upper() == 'Y':
                return data[top_match]
            else:
                return "Word does not exist"
        else:
            return "Word does not exist"




userinput =input("Enter word you want to get the meaning for: ")

output = WordDefinition(userinput)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
