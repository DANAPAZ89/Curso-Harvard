### Classes ###
# las clases nos sirven para agrupar funciones o código que guarden una relación.
class MyPerson: # Las clases las nombramos utilizando CamelCase
    pass        # pass lo utlilizamos para que una función o clase que nos va a dar error no lo de.

# Lo suyo es que tengamos un fichero con la clase Person y no lo mezclemos con otras funciones o clases al que luego llamaremos desde fuera
class Person1:
    def __init__(self, name, surname): # init es el constructor de la clase
        self.name = name
        self.surname = surname
        self.full_name = f"{name} {surname}"

my_first_person = Person1("Diego","Anaya") # Creo una variable para acceder a la clase
print(my_first_person.name)

class Person:
    def __init__(self, name, surname, alias = "Sin alias"): 
        self.full_name = f"{name} {surname} {alias}"
        self.__name = name # Porpiedad privada, solo puedo acceder a ella, no puedo modificarla
    
    def get_name(self):
        return self.__name
        
    def walk(self): 
        print(f"{self.full_name} está camninando")

my_person = Person("Diego", "Anaya")
print(my_person.full_name)
my_person.walk()
print(my_person.get_name())
my_person.full_name = "324"
print(my_person.full_name)