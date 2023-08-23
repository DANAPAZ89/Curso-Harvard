# 1.Create an empty dictionary called dog
# 2.Add name, color, breed, legs, age to the dog dictionary
# 3.Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
# 4.Get the length of the student dictionary
# 5.Get the value of skills and check the data type, it should be a list
# 6.Modify the skills values by adding one or two skills
# 7.Get the dictionary keys as a list
# 8.Get the dictionary values as a list
# 9.Change the dictionary to a list of tuples using items() method
# 10.Delete one of the items in the dictionary
# 11.Delete one of the dictionaries

# 1.
print("\nEJERCICIO 1")
dog = {}

# 2.
print("\nEJERCICIO 2")
dog["Name"] = "Ozak"
dog["Color"] = "gray"
dog["Breed"] = "Malamute"
dog["Legs"] = 4
dog["Age"] = 7
print(dog)

# 3.
print("\nEJERCICIO 3")
student_dictionary = {}
student_dictionary["first_name"] = "Diego"
student_dictionary["last_name"] = "Anaya"
student_dictionary["gender"] = "Male"
student_dictionary["age"] = 33
student_dictionary["marital status"] = "married"
student_dictionary["skills"] = ["strong","tall"]
student_dictionary["country"] = "Spain"
student_dictionary["city"] = "Madrid"
student_dictionary["addresses"] = "López de Hoyos"
print(student_dictionary)

# 4.
print("\nEJERCICIO 4")
print(len(student_dictionary))

# 5.
print("\nEJERCICIO 5")
print(student_dictionary.get("skills"))
lst = student_dictionary.get("skills")
print(type(lst))

# 6.
print("\nEJERCICIO 6")
student_dictionary["skills"].append("handsome")
print(student_dictionary.get("skills"))

# 7.
print("\nEJERCICIO 7")
print(student_dictionary.keys())

# 8.
print("\nEJERCICIO 8")
print(student_dictionary.values())

# 9.
print("\nEJERCICIO 9")
print(student_dictionary.items())

# 10.
print("\nEJERCICIO 10")
del student_dictionary["marital status"]
print(student_dictionary)

# 11.
print("\nEJERCICIO 11")
del student_dictionary
