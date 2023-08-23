#Conditions
n = int(input("Número: ")) #Necesitamos definir el tipo de variable para luego poder compararla
if n>0:
    print(f"{n} es positivo")
elif n<0:
    print(f"{n} es negativo")
else:
    print("El número es 0")

