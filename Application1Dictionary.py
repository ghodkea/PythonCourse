#accept english word and give its meaning
import json #to handle JSON files
data = json.load(open("data.json"))

def WordDefinition(word):
    try:
        return data[word.lower()] #in case the user enters all caps. JSON has all lower case stored
    except KeyError: #in case the word is not in the JSON. It throws a key error. To avoid giving user a bad message, handling in the exception block
        return "Check the word. If you think the spelling is correct, our aplogies, the word is not yet in the dictionary"

userinput =input("Enter word you want to get the meaning for: ")

print(WordDefinition(userinput))
