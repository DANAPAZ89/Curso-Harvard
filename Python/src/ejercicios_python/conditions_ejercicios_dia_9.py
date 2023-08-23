""" 1.Get user input using input(“Enter your age: ”). 
If user is 18 or older, give feedback: You are old enough to drive. 
If below 18 give feedback to wait for the missing amount of years.
"""
""" 2.Compare the values of my_age and your_age using if … else.
Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
You can use a nested condition to print 'year' for 1 year difference in age, 
'years' for bigger differences, and a custom text if my_age = your_age. Output:
"""
""" 3. The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
If the fruit exists print('That fruit already exist in the list')
"""
""" 4. Here we have a person dictionary. Feel free to modify it!
        person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), 
 if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
 if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:
     Asabeneh Yetayeh lives in Finland. He is married.
"""

# 1.
print("EJERCICIO 1")
edad = int(input("Edad: "))
if edad >= 18:
    print("You are old enough to drive")
else:
    print(f"Espera {18-edad} años")

# 2.
print("EJERCICIO 2")
my_age = 33
your_age = int(input("Enter your age: "))
year = my_age - your_age
if year == 1:
    print(f"{year} year difference in age")
elif year > 1:
    print(f"{year} years difference in age")
elif year == 0:
    print("Same ages")
else:
    print("You are older")

# 3. 
print("EJERCICIO 3")
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Compruebe si está la fruta en la lista: ")
if fruits.count(fruit) == 1:
    print("That fruit already exist in the list")
else:
    fruits.append(fruit)
    print(f"Se ha modificado la lista de frutas: {fruits}")

# 4.
print("EJERCICIO 4")
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if "skills" in person:
    lst = person.get("skills")
    print(lst[2])

if "skills" in person:
    lst = person.get("skills")
    if "Python" in lst:
        find = lst.index("Python")
        print(lst[find])

if "skills" in person:
    lst = person.get("skills")
    if "React" and "JavaScript" in lst and len(lst) == 2:
        print("He is a front end developer")
    elif "Node" and "Python" and "MongoDB" in lst:
        print("He is a backend developer")
    else:
        print("unknown title")


m = person.get("is_married")
c = person.get("country")
if m == True and c == "Finland":
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")


