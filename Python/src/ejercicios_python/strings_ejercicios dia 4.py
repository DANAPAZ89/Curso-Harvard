# Strings
texto = "hola \nmundo"
print(texto)

texto1 = "hola \tmundo"
print(texto1)

texto2 = "\thola mundo"
print(texto2)

texto3 = "hola \\ mundo"
print(texto3)

texto4 = 'hola \"mundo\"'
print(texto4)

# Old Style String Formatting (% Operator)
name = "Diego"
age = 33
print("Mi nombre es %s y mi edad es %d" %(name, age))
pi = 3.1416
print("El número pi con dos decimales es: %.2f" %(pi))

# Str.format
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)

# String Interpolation / f-Strings (Python 3.6+)
print(f"El número pi con dos decimales es {pi:.2f}") # El porcentaje se sustituye por pi:


language = "Python"
letra = language[0:6:2] # 2 is the number of steps required to reach the next character of your choice
print(letra)

# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
thirty = "Thirty"
days = "Days"
of = "of"
python = "Python"
frase = thirty + " " + days + " " + of + " " + python
print(frase)

# Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
# Print the variable company using print().
print(company)
# Print the length of the company string using len() method and print().
print(len(company))
# Change all the characters to uppercase letters using upper() method.
print(company.upper())
# Change all the characters to lowercase letters using lower() method.
print(company.lower())
# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())
# Cut(slice) out the first word of Coding For All string.
cut = company[0:1]
print(cut)
# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index("Coding"))
# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding","Python"))
# Change Python for Everyone to Python for All using the replace method or other methods.
company2 = "Python For All"
print(company2.replace("Python For All", "Python For Everyone"))
# Split the string 'Coding For All' using space as the separator (split()).
print(company.split())
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(","))
# What is the character at index 0 in the string Coding For All.
print(company[0])
# What is the last index of the string Coding For All.
print(company[-1])
# What character is at index 10 in "Coding For All" string.
print(company[10])
# Create an acronym or an abbreviation for the name 'Python For Everyone'.
course = "Python For Everyone"
print(company.isupper())
# Create an acronym or an abbreviation for the name 'Python For Everyone'.
print(f"{course[0]}{course[7]}{course[11]}")
# Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index("C"))
# Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index("F"))
# Use index or find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.index("because"))
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.replace("because ",""))
# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
phrase = "   Coding For All      "
print(phrase.strip(" "))
# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = " ".join(list)
print(result)
# Use the new line escape sequence to separate the following sentences.
sentences = "I am enjoying this challenge.\nI just wonder what is next."
print(sentences)
# Use the string formatting method to display the following:
"""
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
"""
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

