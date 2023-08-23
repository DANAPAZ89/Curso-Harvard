# 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
# 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
# 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
# 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
# 5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.            
# 6. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
# 7. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
# 8. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
# 9. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
# 10. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
# 11. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# 12. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
# 13. Declare a function named sum_of_even. It takes a number parameter and it sums all the even numbers in that - range
# 14. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
# 15. Call your function is_empty, it takes a parameter and it checks if it is empty or not
# 16. Write a functions which checks if all items are unique in the list.
# 17. Write a function which checks if all the items of the list are of the same data type.
# 18. Go to the data folder and access the countries-data.py file.
# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.

#1.
print("EJERCICIO 1\n")
def add_two_numbers(x,y):
    sum = x + y
    return sum
print(add_two_numbers(2,3))

# 2.
print("\nEJERCICIO 2\n")
def area_of_circle(r, pi = 3.14):
    area = pi * r * r
    return area
print(area_of_circle(2))

# 3.
print("\nEJERCICIO 3\n")

def add_all_nums(*nums):
    sum = 0
    for num in nums:
        if type(num) == int:
            sum += num
        else:
            print(f"{num} no es un número")
    return sum
print(add_all_nums(1,3,"r",2,4))

# 4.
print("\nEJERCICIO 4\n")
celsius = int(input("Escriba los grados centígrados: "))
def convert_celsius_to_fahrenheit(c):
    farenheit = str((c * 9/5) + 32) + "ºF"
    return farenheit 
print(convert_celsius_to_fahrenheit(celsius))

# 5.
print("\nEJERCICIO 5\n")
estaciones = {"Winter": ["Enero","Febrero","Marzo"], 
              "Spring": ["Abril","Mayo","Junio"],
              "Summer": ["Julio","Agosto","Septiembre"],
              "Autum": ["Octubre","Noviembre","Diciembre"]}
def check_season(month):
    for season in estaciones:
        if month in estaciones.get(season):
            return season
print(check_season("Mayo")) 

# 6.
print("\nEJERCICIO 6\n")
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
def print_list(lst):
    x = 0
    while x < len(lst):
        print(lst[x])
        x += 1
print_list(front_end)

# 7.
print("\nEJERCICIO 7\n")
lst_A = [1, 2, 3, 4, 5]
lst_B = ["A", "B", "C"]
# metodo while
def reverse_list(lista):
    x = 0
    reverse = []
    while x < len(lista):
        element = (len(lista)-1) - x
        reverse.append(lista[element])
        x = x + 1
    else:
        return reverse
print(reverse_list(lst_A))

# metodo for
def reverse_list2(lista):
    range = len(lista) - 1
    reverse = []
    for i in lista:
        num = range - lista.index(i)
        reverse.append(lista[num])
    return reverse
print(reverse_list2(lst_B))

# 8.
print("\nEJERCICIO 8\n")
months = ["Enero","Febrero","Marzo"]
def capitalize_list_items(lst):
        i = 0
        while i < len(lst):
            lst[i] = lst[i].upper()
            i += 1
        else: 
            return lst
print(capitalize_list_items(months))

# 9.
print("\nEJERCICIO 9\n")
        
def add_item(lst,item):
    lst.append(item)
    return lst
print(add_item(months,"Abril"))

# 10.
print("\nEJERCICIO 10\n")
def remove_item(lst,item):
    lst.remove(item)
    return lst
print(remove_item(months,"Abril"))

# 11.
print("\nEJERCICIO 11\n")
def sum_of_numbers(number):
    sum = 0
    for i in range(number + 1):
        sum = sum + i
    return sum
print(sum_of_numbers(10))

# 12.
print("\nEJERCICIO 12\n")
def sum_of_odds(number):
    lst = []
    for num in range(number + 1):
        if num % 2 != 0:
            lst.append(num)
    return lst
print(sum_of_odds(5))

# 13.
print("\nEJERCICIO 13\n")
def sum_of_even(number):
    sum = 0
    for num in range(number + 1):
        if num % 2 == 0:
            sum = sum + num
    return sum
print(sum_of_even(5))

# 14.
print("\nEJERCICIO 14\n")
def evens_and_odds(number):
    count_evens = 0
    count_odds = 0
    for num in range(number + 1):
        if num % 2 == 0:
            count_evens += 1
        else: 
            count_odds += 1
    return f"The number of odds are {count_odds} \nThe number of evens are {count_evens}"

print(evens_and_odds(100))

# 15.
print("\nEJERCICIO 15\n")
item = input("Comprueba si existe el item: ")
def is_empty(data):
    if data:
        return True
    return False
print(is_empty(item))

# 16.
print("\nEJERCICIO 16\n")
def unique(lst):
    for item in lst:
        if lst.count(item) != 1:
            return False
    return True
print("All the items are unique: ",unique(months))

# 17.
print("\nEJERCICIO 17\n")
lista = [1, 4, 6, 5]
def check_type(lst):
    for item in lst:
        if type(lst[0]) != type(item):
            return False
    return True
print("All the items are equal: ",check_type(lista))

            




