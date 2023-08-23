class Person: 
    def __init__(self, firstname, surname, age, country, city):
        self.firstname = firstname
        self.surname = surname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []
    def name(self):
        return f"Mis datos son: {self.firstname} {self.surname}, edad {self.age}. Nacido en {self.city} "
    def add_skill(self,skill):
        self.skills.append(skill)

p = Person("Diego", "Anaya", "33", "España", "Madrid")
p.add_skill("Python")
p.add_skill("Git")
print(p.name())
print(p.skills)

class Student(Person):
    def __init__ (self, firstname='Asabeneh', surname='Yetayeh',age=250, country='Finland', city='Helsinki', gender='male'):
        self.gender = gender
        super().__init__(firstname, surname, age, country, city)
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.firstname} {self.surname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki','male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)

from math import fsum

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

class Statistics:
    def __init__(self,list):
        self.list = list
    def count(self):
        return len(self.list)
    def sum(self):
        return int(fsum(self.list))
    def min(self):
        ordered_list = sorted(self.list)
        return f"Min: {ordered_list[0]}"
    def max(self):
        ordered_list = sorted(self.list, reverse = True)
        return f"Max: {ordered_list[0]}"
    
data = Statistics(ages)
print(data.count())
print(data.sum())
print(data.min())
print(data.max())

"""
Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties 
and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods.
Incomes is a set of incomes and its description. 
The same goes for expenses.
"""

class PersonAccount:
    def __init__(self,firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}
        self.expenses_properties = {}

    def total_income(self):
        total = sum(self.incomes.values())
        return total
    
    def total_expense(self):
        total = sum(self.expenses_properties.values())
        return total
    
    def add_income(self,description, income):
        self.incomes[description] = income

    def add_expense(self,expense, value):
        self.expenses_properties[expense] = value

    def account_info(self):
        return f"Cliente: {self.firstname} {self.lastname}"
    
    def account_balance(self,total_income,total_expense):
        return total_income - total_expense

description_income = input("Concepto de ingreso: ")
income_value = float(input("Introduzca la cantidad: "))
description_expense = input("Concepto de gasto: ")
expense_value = float(input("Introduzca el valor: "))

perfil = PersonAccount(firstname = "Diego",lastname = "Anaya")
perfil.add_income(description_income,income_value)
perfil.add_expense(description_expense,expense_value)
print(perfil.incomes)
print(perfil.expenses_properties)
print(f"Gastos totales: {perfil.total_expense()}€")
print(f"Ingresos totales: {perfil.total_income()}€")
print(f"Balance: {perfil.account_balance(perfil.total_income(),perfil.total_expense())}€")

class ApartamentoAlquiler:
    def __init__(self,apartamento, descripcion, bedrooms, bathrooms):
        self.apartamento = apartamento
        self.descripcion =descripcion
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.caracteristicas = []

    def caracteristics(self,caracteristic):
        list_caracteristics = self.caracteristicas.append(caracteristic)
        return list_caracteristics

    