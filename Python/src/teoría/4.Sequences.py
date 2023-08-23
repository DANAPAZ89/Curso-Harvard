#Sequences

#Strings: Ordered Yes, Mutable No.
name = "Diego"
print(name[0])
print(name[1])

#Lists: Ordered Yes, Mutable Yes
names = ["Diego", "juan"]
print(names[0])

print(names) #Imprime toda la lista

names.append("Marta") #añade un nombre a la lista
print(names)

names.sort()#ordena la lista
print(names)

#Tuples: Ordered Yes, Mutable No. Sirve para almacenar dos o tres valores juntos, como por ejemplo coordenadas
coordinates = (2,7)
print(coordinates)
print(coordinates[1])

#Sets: Ordered No, Mutable N/A
s = {"Hola", "mundo", 5}
print(s)

set = set()#creo un set vacío

set.add(1) #Voy añadiendo elementos al set
set.add(4)
set.add(8)
set.add(0)

set.remove(8) #Borra el 8 del set

print(set) 
"""
Set items can appear in a different 
order every time you use them, 
and cannot be referred to by index or key.
"""
print(f"el número de elementos del set es {len(set)}")


#Dictionaries: Ordered No, Mutable Yes
apellidos = {"Diego":"Anaya","Marta":"de Paz"}
print(apellidos["Diego"])
print("El apellido es " + apellidos["Diego"])
