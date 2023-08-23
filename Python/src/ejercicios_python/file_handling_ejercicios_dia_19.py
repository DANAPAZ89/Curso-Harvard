# 1. 
"""
Write a function which count number of lines and number of words in a text. 
All the files are in the data folder: 
    a Read obama_speech.txt file and count number of lines and words 
    b Read michelle_obama_speech.txt file and count number of lines and words 
    c Read donald_speech.txt file and count number of lines and words 
    d) Read melina_trump_speech.txt file and count number of lines and words
"""
# 2. Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
# 3. Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
# 4. Extract all incoming email addresses as a list from the email_exchange_big.txt file


import re
import json
from functools import wraps


# 1.
print("\nEJERCICIO 1")
def count_number_of_lines(file):    
    with open(f"ejercicios_python/{file}", "r") as obama_speech:
        speech_list_of_lines = obama_speech.read().splitlines()
        line_blank = 0
        number_of_words = 0
        for line in speech_list_of_lines:
            regex = r"[a-zA-Z0-9]+"
            match = re.findall(regex,line,re.I)
            number_of_words += len(match)
            if not " " in line: # el item de la lista que se ha generado por cada línea en blanco, como no contiene nada tengo que quitarlo de esta manera. Podría poner cualquier otro caracter en vez de " " 
                line_blank += 1
        number_of_lines = len(speech_list_of_lines) - line_blank
    return f"El número de palabras es de: {number_of_words} \ny el número de líneas es de: {number_of_lines}"

print(count_number_of_lines("donald_speech.txt"))


# 2.
print("\nEJERCICIO 2\n")

def ten_most_spoken_languages(function):
    @wraps(function)
    def ten_most_spoken(lst,num):
        lenguages = function(lst,num)
        ntimes_language = []
        for lang in lenguages:
            number = lenguages.count(lang)
            ntimes_language.append((number,lang))
        ntimes_language.sort(reverse = True)
        result = []
        for item in ntimes_language:
            if item not in result:
                result.append(item)
        return result[:num]
    return ten_most_spoken

@ten_most_spoken_languages
def spoken_languages(lst,num):
    languages = []
    for country in lst:
        languages_in_dct_country = country.get("languages")
        for language in languages_in_dct_country:
            languages.append(language)
    return languages

with open("ejercicios_python/countries_data.json") as countries_data_json:
        countries_data_dct = json.load(countries_data_json)
print(spoken_languages(countries_data_dct,10))

# 3.
print("\nEJERCICIO 3\n")

with open("ejercicios_python/countries_data.json") as countries_json:
    countries_lst = json.load(countries_json)

def ten_countries_most_populated(lst,number):
    sorted_countries_by_population = sorted(lst,key=lambda country: country["population"],reverse = True)
    list_resumed = []
    for country in sorted_countries_by_population[:number]:
        dct_country = {}
        name = country["name"]
        population = country["population"]
        dct_country["country"] = f"{name}"
        dct_country["population"] = f"{population}"
        list_resumed.append(dct_country)
    return list_resumed

print(ten_countries_most_populated(countries_lst,3))

# 4.
print("\nEJERCICIO 4\n")

with open("ejercicios_python/email_exchanges.txt", "r") as email_exchanges:
    list_email_exchanges = email_exchanges.read().splitlines()
    list_with_from_emails = []
    for line in list_email_exchanges:
        if "From" in line:
            list_with_from_emails.append(line)
    list_with_emails = []
    for list_emails in list_with_from_emails:
        regex = r"[A-Za-z0-9]+[.-_]*[A-Za-z0-9]+@[A-Za-z0-9-]+\.[A-Z|a-z]{1,}+"
        email_adress = re.findall(regex,list_emails)
        if email_adress not in list_with_emails:
            list_with_emails.append(email_adress)
        list = [email for email_adress in list_with_emails for email in email_adress]
    print(list)

