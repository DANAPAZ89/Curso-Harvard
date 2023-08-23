import sys #Importamos el módulo sys para poder salir del programa con el error
try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError: #Código de error que aparece si metemos un valor que no sea un int.
    print("Error: Invalid input.")
    sys.exit(1)
"""Para evitar que al dividir por cero se produzca un error, le decimos que lo intente 
y si no que nos diga que no se puede dividir por 0"""
try:
    result = x / y
except ZeroDivisionError: #Este es el código de error que nos aparecería si ejecutásemos el programa sin la excepción
    print("Error: Cannot divide by 0.")
    sys.exit(1) #Sal del programa con el código de estado 1, que quiere decir error

print(f"{x} / {y} = {result}")