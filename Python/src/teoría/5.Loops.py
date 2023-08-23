for i in[0,1,2,3,4,5]:  
    print(i)

for i in range(6): #range genera una secuencia de números que definamos. Se puede definir el valor inicial: range(2,6)
    print(i)

names = ["Diego", "Marta", "Juan"]
for name in names:
    print(name)

name = "Diego"
for char in name: #En este caso char no es el tipo de variable chr
    print(char)

names = ["Diego", "Marta", "Juan"]
for name in names:
    print(name)
    if name == "Marta":
        break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)