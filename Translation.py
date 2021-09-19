import requests 

auth_key = "KEY"

target_language = 'FR'


def traduction(text):



    result = requests.get( 
       "https://api-free.deepl.com/v2/translate", 
       params={ 
         "auth_key": auth_key, 
         "target_lang": target_language, 
         "text": text, 
       }, 
    ) 
    return result.json()["translations"][0]["text"]


