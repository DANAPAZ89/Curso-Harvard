#Podemos crear listas con diccionarios dentro, o listas con listas, etc
people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]
"""Necesitamos definir una función que le diga a la función sort() cómo ordenar people por el name.
Toma person como input y devuelve el name de ese person, busca el campo name dentro de ese diccionario"""
def f(person):
    return person["name"]

"""Ahora le decimos que ordene a toda esa people, 
y la manera en la que lo tiene que hacer es ejecutando la función f(), key=f"""
people.sort(key=f)

print(people)

print("Usando Lambda:")
#Podemos hacer lo mismo con la función lambda:
people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]
#Utilizamos la fucnión Lambda, como inut person: y como output person["name"]
people.sort(key=lambda person: person["name"])

print(people)