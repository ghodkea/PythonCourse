import requests
import json
import difflib
from difflib import get_close_matches

#amitbghodke
#Zxcv1234$

app_id = '5b6f0752'
app_key = 'fa261a7ff1a3a5852818d35f67f09558'

language = 'en'

word_id=input("Enter the word you want meaning for: ")


url = 'https://od-api.oxforddictionaries.com/api/v1/entries/' + language + '/' + word_id.lower()

r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

print(r.status_code)
if r.status_code==200:
        #print("code {}\n".format(r.status_code))
        #print("text \n" + r.text)
        #print("json \n" + json.dumps(r.json()))

        entry_lookup_dictionary = r.json()
        definitions_results=entry_lookup_dictionary["results"]
        definition_dict=definitions_results[0]
        definition_lexicalentries=definition_dict["lexicalEntries"]
        meaning_dict=definition_lexicalentries[0]
        meaning_entries=meaning_dict["entries"]
        definition_objectA=meaning_entries[0]
        definition_objectB=definition_objectA["senses"]

        for item in definition_objectB:
            #print(item)
            #print(type(item["definition"]))
            #print(item.keys())
            #print(type(item))
            definition=item["definitions"]
            for subitem in definition:
                print(subitem)
else:

        print("Word not in English Dictionary")
