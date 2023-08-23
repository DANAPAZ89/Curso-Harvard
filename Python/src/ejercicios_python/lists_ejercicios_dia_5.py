# Declare an empty list
lst = list()
lista = []
# Declare a list with more than 5 items
lista = [4,5,6,4,8,9]
# Find the length of your list
print(len(lista))
# Get the first item, the middle item and the last item of the list
first_item = lista[0]
middle_item = lista[2]
last_item = lista[5]
print(first_item,middle_item,last_item)
# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Diego", 33, 1.85, "married", "madrid"]
# Print the list after modifying one of the companies
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies[2] = "Xiaomi"
print(it_companies)
# Add an IT company to it_companies
it_companies.append("Samsung")
print(it_companies)
# Insert an IT company in the middle of the companies list
it_companies.insert(4,"Microsoft")
print(it_companies)
# Change one of the it_companies names to uppercase (IBM excluded!)
# 1st method within the list
x = it_companies[0]
it_companies[0] = x.upper()
# it_companies[0].upper()
print(it_companies)
# 2nd method out of the list
first_company, second_company, *rest = it_companies
print(second_company.upper())
# Join the it_companies with a string '#;  '
listado = "#; ".join(it_companies)
print(listado)
# Check if a certain company exists in the it_companies list.
print("Apple" in it_companies)
# Sort the list using sort() method
it_companies.sort()
print(it_companies)
# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)
# Slice out the first 3 companies from the list
print(it_companies[3:])
# Slice out the last 3 companies from the list
print(it_companies)
print(it_companies[:-3])
# Slice out the middle IT company or companies from the list
print(it_companies[4:5])
print(it_companies[4])
# Remove the last IT company from the list
print(it_companies)
it_companies.pop()
print(it_companies)
# Remove all IT companies from the list
it_companies.clear()
print(it_companies)
# Destroy the IT companies list
del it_companies
#print(it_companies)
# Join the following lists:
"""
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
"""
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
web = front_end + back_end
print(web)
front_end.extend(back_end)
print(front_end)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
print(web)
full_stack = web.copy()
full_stack.insert(5,"Python")
full_stack.insert(6,"SQL")
print(full_stack)

"""
The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
Sort the list and find the min and max age
Add the min age and the max age again to the list
Find the median age (one middle item or two middle items divided by two)
Find the average age (sum of all items divided by their number )
Find the range of the ages (max minus min)
Compare the value of (min - average) and (max - average), use abs() method
Find the middle country(ies) in the countries list
Divide the countries list into two equal lists if it is even if not one more country for the first half.
['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
"""
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = ages[0]
max_age = ages[len(ages)-1]
print(min_age, max_age)
ages.append(min_age)
ages.append(max_age)
ages.sort()
mid_age = ages[len(ages) // 2]
mediana = mid_age / 2
print(ages)
print(mid_age)
print(mediana)
suma = sum(ages)
media = suma / len(ages)
print(media)
rango_edades = ages[len(ages)-1] - ages[0]
print(rango_edades)
value1 = abs(ages[0] - media)
value2 = abs(ages[len(ages)-1] - media)
print(value1)
print(value2)
print(value1 == value2)
print(value1 < value2)
print(value1 > value2)
paises = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
mid_contry = paises[len(paises) // 2]
print(mid_contry)
n = len(paises)
punto_medio = n // 2
print(paises)
if n % 2 == 0:
    print(paises[:punto_medio])
    print(paises[punto_medio:])
else:
    print(paises[:punto_medio+1])
    print(paises[punto_medio+1:])






