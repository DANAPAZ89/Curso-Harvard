# 1. What is the most frequent word in the following paragraph?
#  paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.
# 2. The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
# 3. Write a pattern which identifies if a string is a valid python variable
# 4. Clean the following text. After cleaning, count three most frequent words in the string.
"""
%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. 
There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. 
;I found tea@ching m%o@re interesting tha@n any other %jo@bs. 
%Do@es thi%s mo@tivate yo@u to be a tea@cher!?
"""

import re

# 1.
print("\nEJERCICIO 1")
paragraph = "I love teaching. If you do$ not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."

regex_pattern = r"[a-z]+"
match = re.findall(regex_pattern,paragraph,re.I)

def count_words1(lst):
    num = 0
    lst_words = []
    for word in lst:
        num = lst.count(word)
        if  (num,word) not in lst_words:
            lst_words.append((num,word))
    return lst_words

print(*count_words1(match),sep = "\n")
# [print(item) for item in count_words(match)] # Otro ejemplo de cómo imprimir en vertical:

# 2.
print("\nEJERCICIO 2")

text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles."
    
regex_pattern = r"[-]\d+|\d+"
match = re.findall(regex_pattern,text)
print(match)
def diference_list_of_points(lst):
    list_numbers = [int(num) for num in lst]
    ordered_list = sorted(list_numbers)
    distance = ordered_list[len(ordered_list)-1]-ordered_list[0]
    return distance
print(diference_list_of_points(match))

# 3.
print("\nEJERCICIO 3")
phrase = input("Comprueba si es una variable tipo str válida: ")
def is_valid_variable(str):
    regex_pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*"
    return re.match(regex_pattern,str) is not None and "-" not in str
print(is_valid_variable(phrase))

# 4.
print("\nEJERCICIO 4")

from functools import wraps

phrase = "%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?"

def count_words(function):
    @wraps(function)
    def most_frequent_words(phrase1):
        num = 0
        lst_words = []
        lst = function(phrase1)
        for word in lst:
            num = lst.count(word)
            if num > 1 and (num,word) not in lst_words:
                lst_words.append((num,word))
        print(lst_words)
    return most_frequent_words

@count_words
def list_all_words(new_phrase):
    regex_pattern = r"[a-z]+"
    list_of_words = re.findall(regex_pattern,new_phrase,re.I)
    return list_of_words

def clean_text(string):
    return re.sub("[#%@$&;]","",string)

print(clean_text(phrase))
print(list_all_words(clean_text(phrase)))

