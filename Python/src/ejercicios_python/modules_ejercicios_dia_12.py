# 1. Write a function which generates a six digit/character random_user_id.

# 2. Modify the previous task. Declare a function named user_id_gen_by_user. 
# It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

# 3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).

# 4. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. 
# Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. 

# 5. Write a function generate_colors which can generate any number of hexa or rgb colors.

# 6. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

# 7. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.


#1.
print("EJERCICIO 1\n")
import random
from string import hexdigits

def random_user_id():
    id_number = ""
    for i in range(9):
        number = str(random.randint(0,9))
        id_number = id_number + number 
    return id_number 

print(random_user_id())

#2.
print("\nEJERCICIO 2\n")
number_of_id = int(input("Escribe el número de IDs que desees generar: "))
lenght_of_id = int(input("¿Qué longitud deben tener los IDs?: "))
def user_id_gen_by_user():
    for num_id in range(number_of_id):
        id_number = ""
        for length in range(lenght_of_id):
            number = str(random.randint(0,9))
            id_number = id_number + number 
        print(f"ID {num_id + 1}: {id_number}") 

user_id_gen_by_user()

#3.
print("\nEJERCICIO 3\n")
def rgb_color_gen():
    color_rgb = []
    for num in range(3):
        color = random.randint(0,255)
        color_rgb.append(color)
    return f"rgb{tuple(color_rgb)}"

print(rgb_color_gen())

def rgb_color_gen2():
    color_rgb = []
    num = 0
    while num < 3:
        color = random.randint(0,255)
        color_rgb.append(color)
        num += 1
    return tuple(color_rgb)

print(f"rgb{rgb_color_gen2()}")

#4.
print("\nEJERCICIO 4\n")

def list_of_hexa_colors(length = 6):
    hexadecimal_number = ""
    for num_hex in range(length):
        color = random.choice(hexdigits)
        hexadecimal_number += color
    return f"#{hexadecimal_number}"
print(list_of_hexa_colors())

#5.
print("\nEJERCICIO 5\n")

def generate_colors(function,num):
    lst_rgb = []
    lst_hexa = []
    if function == "hexa":
        for n in range(num):
            hexa = list_of_hexa_colors()
            lst_hexa.append(hexa)
        print(lst_hexa) 
    elif function == "rgb":
        for n in range(num):
            rgb = rgb_color_gen()
            lst_rgb.append(rgb)
        print(lst_rgb) 

generate_colors("hexa", 3)
generate_colors("rgb", 2)

#6.
print("\nEJERCICIO 6\n")
colors_hex = ['#a3e12f','#03ed55','#eb3d2b'] 
def shuffle_list(lst):
    random.shuffle(lst)
    return lst

print(shuffle_list(colors_hex))

#7.
print("\nEJERCICIO 7\n")

def random_numbers(num = 7):
    lst = []
    for n in range(num):
        number = random.randint(0,9)
        while number in lst:
            number = random.randint(0,9)
        else:
            lst.append(number)
    return lst

print(random_numbers())