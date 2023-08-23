class MyClass: #Creo la clase Myclass
    x = 5      #Tiene una propiedad llamada x
p1 = MyClass() #Creamos un objeto llamado p1

print(p1.x)    #Imprimimos el valor de x que está almacenado dentro de p1
"""Todas las clases tienen una función __init__() que se ejecuta siempre
que la clase es iniciada. Se usa para asignar valores a las propiedades del objeto u otras 
operaciones que son necesarias cuando se crea el objeto
"""
class Person:
    def __init__(self,name,age): #self representa el objeto en cuestión, en este caso necesitamos el nombre y la edad
        self.name = name #name será almacenada en Person dentro de la propiedad name
        self.age = age #age será almacenada en Person dentro de la propiedad age
    def __str__(self): 
        return f"{self.name} ({self.age})"
    
P = Person("Diego", 33)
print(P)
print(P.name)
print(P.age)


class Flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = [] #Creo una lista vacía que se va a almacenar en la propiedad passengers
    def add_passengers(self,name):
        if not self.open_seats(): # Es lo mismo que decir if self.opne_seats() == 0:
            return False
        self.passengers.append(name) #añadimos el nombre del pasajero a la lista passengers
        return True
    def open_seats(self):
        return self.capacity - len(self.passengers)
    
flight = Flight(3)
people = ["Harry", "Ron", "Hermione", "Ginny"]

for person in people:
    if flight.add_passengers(person): #Dentro de flight utilizamos la función add_passengers()
        print(f"Added {person} to flight successfully")
    else:
        print(f"No available seats for {person}")


"""Práctica del ejemplo 
anterior
"""

class Flight():
    def __init__(self,number):
        self.number = number
        self.passenger = []
    def add_passenger(self,name):
        if not self.seats_available():
            return False
        self.passenger.append(name)
        return True
    def seats_available(abc): #En vez de self se puede llamar como sea, y dentro de la función llamamos a la propiedad que queramos
        return abc.number - len(abc.passenger)

flight = Flight(3)
people = ["Diego","Marta","Juan","Pedro"]
print(f"La capacidad del vuelo es de {flight.number}")
for pax in people:
    if flight.add_passenger(pax):
        print(f"Se ha añadido a {pax}")
    else:
        print(f"No hay hueco en el vuelo para {pax}")