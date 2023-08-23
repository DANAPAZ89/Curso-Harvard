# 1.Create an empty tuple
# 2.Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
# 3.Join brothers and sisters tuples and assign it to siblings
# 4.How many siblings do you have?
# 5.Modify the siblings tuple and add the name of your father and mother and assign it to family_members
# 6.Unpack siblings and parents from family_members
# 
# 1.
tuple()
tpl = ()
# 2.
brothers = ("Hector", "Juan")
sisters = ("Marta", "Maria") # Los tuple deben de tener un mínimo de 2 datos para ser tuple, sino es string
# 3.
siblings = brothers + sisters
print(siblings)
# 4.
print(len(siblings))
# 5.
parents = ("Vicente", "Ana")
family_members = siblings + parents
print(family_members)
# 6.
print(family_members[-2:],family_members[0:4])
parents = family_members[-2:]
siblings = family_members[0:4]
print(siblings,parents)
""" 7. Check if an item exists in tuple:
Check if 'Estonia' is a nordic country
Check if 'Iceland' is a nordic country"""
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(nordic_countries.count("Estonia"))
print(nordic_countries.count("Iceland"))
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)


