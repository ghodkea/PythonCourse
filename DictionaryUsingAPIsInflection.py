import requests
import json



app_id = '5b6f0752'
app_key = 'fa261a7ff1a3a5852818d35f67f09558'

language = 'en'

word_id=input("Enter the word you want meaning for: ")


inflection_url = 'https://od-api.oxforddictionaries.com/api/v1/inflections/' + language + '/' + word_id.lower()

r = requests.get(inflection_url, headers = {'app_id': app_id, 'app_key': app_key})

#print(r.status_code)
if r.status_code==200:
#when a user enters verbs in different tenses, we will use the inflections api
#below code then finds the original word which will be input to the next API
        response_body = r.json()
        definitions_results_list=response_body["results"]
        for result in definitions_results_list:
            result_lexical_list=result["lexicalEntries"]
            for lexical_category_loop in result_lexical_list:
                lexical_category=lexical_category_loop["lexicalCategory"]

                print(lexical_category)
            if lexical_category.lower()=='verb':

                for lexical_item in result_lexical_list:
                    inflection_word_list=lexical_item["inflectionOf"]
                    print(inflection_word_list)
                    print(len(inflection_word_list))
                    for loop_inflection_word_list in inflection_word_list:
                        word_id_data=loop_inflection_word_list["id"]
                        print(word_id_data)
                        if word_id_data!=word_id.lower():
                            actual_word=word_id_data
            else:
                actual_word=word_id.lower()




        print(actual_word)

        word_url = 'https://od-api.oxforddictionaries.com/api/v1/entries/' + language + '/' + actual_word.lower()

        w = requests.get(word_url, headers = {'app_id': app_id, 'app_key': app_key})
        if w.status_code==200:
            entry_lookup_dictionary = w.json()
            definitions_results=entry_lookup_dictionary["results"]
            definition_dict=definitions_results[0]
            definition_lexicalentries=definition_dict["lexicalEntries"]
            meaning_dict=definition_lexicalentries[0]
            meaning_entries=meaning_dict["entries"]
            definition_objectA=meaning_entries[0]
            definition_objectB=definition_objectA["senses"]

            for item in definition_objectB:
                definition=item["definitions"]
                for subitem in definition:
                    print(subitem)
                    print("---------------------------------------")
        else:
            print("Word not in English Dictionary")
else:
    print("Word not in English Dictionary")
