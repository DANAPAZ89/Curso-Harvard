"""
FIZZBUZZ
 Escribe un programa que muestre por consola (con un print) los
 números de 1 a 100 (ambos incluidos y con un salto de línea entre
 cada impresión), sustituyendo los siguientes:
 - Múltiplos de 3 por la palabra "fizz".
 - Múltiplos de 5 por la palabra "buzz".
 - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizzbuzz(number_range):
    for i in range(1,number_range):
        if i % 3 == 0 and i % 5 == 0:
            i = "fizzbuzz"
        elif i % 5 == 0:
            i = "buzz"
        elif i % 3 == 0:
            i = "fizz"
        print(f"{i}\n")

print("\nFIZZBUZZ\n")
fizzbuzz(101)

"""
¿ES UN ANAGRAMA?
 Escribe una función que reciba dos palabras (String) y retorne
 verdadero o falso (Bool) según sean o no anagramas.
  - Un Anagrama consiste en formar una palabra reordenando TODAS
    las letras de otra palabra inicial.
  - NO hace falta comprobar que ambas palabras existan.
  - Dos palabras exactamente iguales no son anagrama.
"""  
# Opción 1      
def is_an_anagram(word1,word2):
    word1_l = word1.lower()
    word2_l = word2.lower()
    if word1_l == word2_l:
        return False
    for letter in word1_l:
        if word1_l.count(letter) != word2_l.count(letter):
            return False
    return True

# Opción 2
def is_an_anagram_short(word1,word2):
    if word1.lower() == word2.lower():
        return False
    return sorted(word1.lower()) == sorted(word2.lower())

#print("\n¿ES UN ANAGRAMA?\n")
#first_word = input("Primera palabra: ")
#econd_word = input("Segunda palabra: ")
#print(f"{second_word} is an anagram of {first_word}?: ",is_an_anagram_short(first_word,second_word))

"""
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
  - La serie Fibonacci se compone por una sucesión de números en
    la que el siguiente siempre es la suma de los dos anteriores.
    0, 1, 1, 2, 3, 5, 8, 13...
"""
# Opción 1
def fibonacci():
    lst_fibo = [0,1]
    while len(lst_fibo) < 50:
        x2 = lst_fibo[len(lst_fibo)-2]
        x1 = lst_fibo[len(lst_fibo)-1]
        num_sucession = x1 + x2
        lst_fibo.append(num_sucession)
    return lst_fibo
    #for index,i in enumerate(lst_fibo):
    #    print(f"{index+1}: {i}")

print("\nFIBONACCI\n")
print(fibonacci())

# Opción 2
def fibonacci2():
    prev = 0
    next = 1
    for index in range(50):
        print(prev)
        fibo = prev + next
        prev = next
        next = fibo

fibonacci2()

"""
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""
def numeros_primos(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True 

def first_100_prime():
    for i in range(1,101):
        if numeros_primos(i):
            print(i)
                

print("\n¿ES UN NÚMERO PRIMO?\n")
numero = int(input("Comprueba si es número primo: "))
print(numeros_primos(numero))
first_100_prime()

"""
 Crea una única función (importante que sólo sea una) que sea capaz
 de calcular y retornar el área de un polígono.
 - La función recibirá por parámetro sólo UN polígono a la vez.
 - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 - Imprime el cálculo del área de un polígono de cada tipo.
 """

def area_polygon(polygon):   
    pol = polygon.lower()
    if pol == "triángulo":
        base = float(input("Introduzca la base: "))
        height = float(input("Introduzca la altura: "))
        area = (base * height)/2
        print(area)
    elif pol == "cuadrado":
        side = float(input("Introduzca el lado: "))
        area = side * side 
        print(area)
    elif pol == "rectángulo":
        base = float(input("Introduzca la base: "))
        height = float(input("Introduzca la altura: "))
        area = base * height
        print(area)
    else:
        print("Escriba bien el polígono según los ejemplos")
    
choose_polygon = input("¿Qué área desea calcular?  Opciones Cuadrado/Triángulo/Rectángulo\n")
print(area_polygon(choose_polygon))

"""
 Crea un programa que invierta el orden de una cadena de texto
 sin usar funciones propias del lenguaje que lo hagan de forma automática.
 - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def invert_str(string):
    inverse_word = ""
    for i in range(1,(len(string)+1)):
        inverse_word += string[-i]
    return inverse_word

word = input("Escribe el texto/palabra que desee invertir: ")
print(invert_str(word))

"""
"EL LENGUAJE HACKER"
Escribe un programa que reciba un texto y transforme lenguaje natural a
 "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 se caracteriza por sustituir caracteres alfanuméricos.
 - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
   con el alfabeto y los números en "leet".
   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")

"""

import random 

def hacker_language(text):
        
    leet = {"A": "4", "B": "I3", "C": "[", "D": ")", "E": "3", "F": "|=", "G": "&", "H": "#", "I": "1",
        "J": ",_|", "K": ">|", "L": "1", "M": "/\/\ ", "N": "^/", "O": "0", "P": "|*", "Q": "(_,)",
        "R": "I2", "S": "5", "T": "7", "U": "(_)", "V": "\/", "W": "\/\/", "X": "><", "Y": "j", "Z": "2",
        "1": "L", "2": "R", "3": "E", "4": "A", "5": "S", "6": "b", "7": "T", "8": "B", "9": "g", "0": "o"}
    
    leet_text = ""
    
    for letter in text:
        if letter.upper() in leet.keys():
            leet_text += leet[letter.upper()]
        else:
            leet_text += letter
    
    return leet_text

print(hacker_language(input("Introduzca el texto a cifrar: ")))