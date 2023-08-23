# Day 2: 30 Days of python programming
first_name = "Diego"
last_name = "Anaya"
full_name = "Diego Anaya"
country = "Spain"
city = "Madrid"
age = 33
year = 1989
is_married = "Alicia"
is_true = True
is_light_on = True
first_name, last_name, age, year = "Juan", "García", 23, 2023

print(len(first_name))

# Day 3: 30 Days of python programming
age = 20
height = 1.85
complex_number = 1+1j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h)
base = int(input("Enter base: "))
height = int(input("Enter height: "))
area = base * height * 0.5
print("The area of the triangle is", area)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))
perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is",perimeter)

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r)
area_circulo = 3.15 * base ** 2
print("Area círculo", area_circulo)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
x_intercept = int(input("X = "))
y_intercept = 2 * x_intercept - 2 
print(f"X = {x_intercept}, Y = {y_intercept}")

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))
point_1 = (x1,y1)
point_2 = (x2,y2)
slope = ((y2-y1) / (x2-x1))

euclidean_distance = ((y1-x1) ** 2 + (y2-x2) ** 2) ** 0.5
print("slope: ",slope)
print("Euclidean distance: ",float(euclidean_distance))

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len("Python"))
print(len("Dragon"))

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
x = "Python"
y = "Dragon"
print("on" in ("Dragon" and "Python"))

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print("jargo" in "I hope this course is not full of jargo")

# There is no 'on' in both dragon and python
print(not("on" in ("Dragon" and "Python")))

# Find the length of the text python and convert the value to float and convert it to string
x = len("Python")
print(float(x))
print(str(x))

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
x = int(input("x: "))
if (x % 2) == 0: 
    print(f"{x} es un número par")

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
x = 7 // 3
y = 2.7
print(x==int(y))

# Check if type of '10' is equal to type of 10
print(type("10")==type(10))

# Check if int('9.8') is equal to 10
print(int(9.8)==10)

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours_worked = float(input("Horas trabajadas: "))
rate_hour = float(input("€/hora: "))
print("Tu sueldo es de ", hours_worked * rate_hour,"€")

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
number_years = int(input("Número de años: "))
seconds_year = (60 * 60 * 24 * 365)
print(seconds_year * number_years)

# Write a Python script that displays the following table:
"""
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""
for i in range(1, 6):
    print(i,"1", i, i**2, i**3)

