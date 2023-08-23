### closures, decorators, maps, filter, reduce ###

"""
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""

# 1. Explain the difference between map, filter, and reduce.
# 2. Explain the difference between higher order function, closure and decorator
# 3. Define a call function before map, filter or reduce, see examples.
# 4. Use for loop to print each country in the countries list.
# 5. Use for to print each name in the names list.
# 6. Use for to print each number in the numbers list.
# 7. Use map to create a new list by changing each country to uppercase in the countries list
# 8. Use map to create a new list by changing each number to its square in the numbers list
# 9. Use map to change each name to uppercase in the names list
# 10. Use filter to filter out countries containing 'land'.
# 11. Use filter to filter out countries having exactly six characters.
# 12. Use filter to filter out countries containing six letters and more in the country list.
# 13. Use filter to filter out countries starting with an 'E'
# 14. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
# 15. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
# 16. Use reduce to sum all the numbers in the numbers list.
# 17. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
# 18. Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
# 19. Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
# 20. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
# 21. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
# 22. Use the countries_data.py file and follow the tasks below:
    # Sort countries by name, by capital, by population
    # Sort out the ten most spoken languages by location.
    # Sort out the ten most populated countries.


#1.
print("EJERCICIO 1\n")
"""
map(),filter() y reduce() toman como parámetros una función y un iterable (string,list o tuple).
map y filter devuelven otro iterable y reduce devuelve un single value. 
map toma funciones que devuelven datos. y se puede utilizar un lambda en vez de una función como parámetro
filter toma funciones que devuelven un boolean. Sacará por pantalla todos aquellos que den True dentro de la función.
"""

#2.
print("\nEJERCICIO 2\n")

#3.
print("\nEJERCICIO 3\n")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def call(lst):
    return lst
get_function = map(call,countries)
print(list(get_function))

#4.
print("\nEJERCICIO 4\n")
def each_country():
    for country in countries:
        print(country)
each_country()
#5.
print("\nEJERCICIO 5\n")
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
def each_name():
    for name in names:
        print(name)
each_name()
#6.
print("\nEJERCICIO 6\n")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def each_number(lst):
    for number in lst:
        print(number)
each_number(numbers)
#7.
print("\nEJERCICIO 7\n")
def upper_country(country):
   return country.upper()
uppercase = map(upper_country,countries)
print(list(uppercase))

#8.
print("\nEJERCICIO 8\n")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def square_number(number):
    return number ** 2
square = map(square_number,numbers)
print(list(square))

#9.
print("\nEJERCICIO 9\n")
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
def upper_name(name):
    return name.upper()
upper = map(upper_name,names)
print(list(upper))

#10.
print("\nEJERCICIO 10\n")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def search_land(country):
    if "land" in country:
        return True
    return False
country_with_land = filter(search_land,countries)
print(list(country_with_land))

#11.
print("\nEJERCICIO 11\n")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def country_six(country):
    if len(country) == 6:
        return True
    return False   
country_with_six = filter(country_six,countries)
print(list(country_with_six))

#12.
print("\nEJERCICIO 12\n")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def country_more_six(country):
    if len(country) < 6:
        return False
    return True
long_country = filter(country_more_six,countries)
print(list(long_country))

#13.
print("\nEJERCICIO 13\n")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def first_letter_e(country):
    if country[0] == "E":
        return True
    return False
country_with_e = filter(first_letter_e,countries)
print(list(country_with_e))

#14.
print("\nEJERCICIO 14\n")
#(eg. arr.map(callback).filter(callback).reduce(callback)
#country_sixletter_upper = map(call,countries).filter()

#15.
print("\nEJERCICIO 15\n")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def make_string_list1(number):
        return str(number)
string = list(map(make_string_list1,numbers))
print(string)

#16.
print("\nEJERCICIO 16\n")
import functools
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def sum_all_numbers(x,y):
       return x + y
result = functools.reduce(sum_all_numbers,numbers)
print(result)

#17.
print("\nEJERCICIO 17\n")
from functools import reduce
#Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
"""def concat_countries(x,y):
    rango = len(countries) - 1
    chain = x + ", " + y
    if y == y[rango]:
        chain += ", and" + y
        return chain
text = functools.reduce(concat_countries,countries)
print(text)"""

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def concatenate_countries(first_country, country):
    return f"{first_country}, {country}"
sentence = reduce(concatenate_countries, countries)
sentence = f"{sentence[:-7]}and {sentence[-7:-1]} are north European countries"
print(sentence)

#18.
print("\nEJERCICIO 18\n")
from countries import countries

def find_country_with(lst,word):
    filter_countries = []
    for country in lst:
        if word in country:
            filter_countries.append(country)
    return filter_countries

search = input("Países que contienen: ")
print(find_country_with(countries,search))

def find_country_with2(country):
    return True if "land" in country else False
search2 = list(filter(find_country_with2,countries))
print(search2)

from functools import wraps
def list_of_countries(function):
    @wraps(function)
    def countries_with_word(lista, palabra):
        countries_searched = []
        for country in lista:
            if palabra in country:
                countries_searched.append(country)
        print(function(lista,palabra))
        print(countries_searched)
    return countries_with_word

@list_of_countries       
def categorize_countries(list,word):
    return f"Los países que contienen '{word}' son:"

letters = input("Países que contienen: ")

categorize_countries(countries,letters)
print(categorize_countries.__name__)

#19.
print("\nEJERCICIO 19\n")

from string import ascii_uppercase

def dictionary_countries(function):
    @wraps(function)
    def search_countries(lsta):
        dictionary = {}
        for letter in ascii_uppercase:
            number_countries = 0
            for country in lsta:
                if letter == country[0]:
                    number_countries += 1
            dictionary[letter] = number_countries
        print(function(lsta))
        print(dictionary)
    return search_countries
            
@dictionary_countries
def introduction(lst):
    return "El número de páises con cada letra del abecedario"

print(introduction(countries))

#20.
print("\nEJERCICIO 20\n")

def get_first_ten_countries1(lst):
    ten_first_countries = []
    for country in lst[:10]:
        ten_first_countries.append(country)
    return ten_first_countries

print("Opción 1\n",get_first_ten_countries1(countries))

def get_first_ten_countries(country):
    return True if countries.index(country) < 10 else False
    
first_countries = list(filter(get_first_ten_countries,countries))
print("Opción 2\n",first_countries)

#21.
print("\nEJERCICIO 21\n")

def get_last_ten_countries(country):
    return True if country in countries[-10:] else False

last_ten = list(filter(get_last_ten_countries,countries))
print(last_ten)

#22.
print("\nEJERCICIO 22\n")

from countries_data import lst
print(sorted(lst,key = lambda country: country["capital"]),"\n")
print(sorted(lst,key = lambda country: country["population"],reverse = True))