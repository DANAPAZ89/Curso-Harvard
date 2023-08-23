# 1. Filter only negative and zero in the list using list comprehension
# 2. Flatten the following list of lists of lists to a one dimensional list:
# 3. Using list comprehension to create the following list of tuples:
"""
[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
"""

# 4. Flatten the following list to a new list:
"""
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
"""

# 5. Change the following list to a list of dictionaries:
"""
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}]
"""

# 6. Change the following list of lists to a list of concatenated strings:
"""
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output
['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
"""

#1.
print("EJERCICIO 1\n")
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
zero_negatives = [i for i in numbers if i <= 0]
print(zero_negatives)

#2.
print("\nEJERCICIO 2\n")
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
one_dim_lst = [number for row in list_of_lists for set in row for number in set]
print(one_dim_lst)

#3.
print("\nEJERCICIO 3\n")
mega_lst = [(i,1,i,i**2,i**3,i**4,i**5) for i in range(11)]
print(mega_lst)

#4.
print("\nEJERCICIO 4\n")
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_list = [[country.upper(), country[:3].upper(), city.upper()] for lst in countries for country, city in lst]
print(flattened_list)

#5.
print("\nEJERCICIO 5\n")
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
lst = [{"country":country.upper(),"city":city.upper()} for pair in countries for country, city in pair]
print(lst)

#6.
print("\nEJERCICIO 6\n")
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
lst1 = [(name + " " + surname) for full_name in names for name,surname in full_name ]
print(lst1)

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
zero_negative_numbers = [number for number in numbers if number >= 0]
print(zero_negative_numbers)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
name = [first_name + " " + surname for lst in names for first_name, surname in lst]
print(name)