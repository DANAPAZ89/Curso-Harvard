# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1.Find the length of the set it_companies
# 2.Add 'Twitter' to it_companies
# 3.Insert multiple IT companies at once to the set it_companies
# 4.Remove one of the companies from the set it_companies
# 5.What is the difference between remove and discard
# 6.Join A and B
# 7.Find A intersection B
# 8.Is A subset of B
# 9.Are A and B disjoint sets
# 10.Join A with B and B with A
# 11.What is the symmetric difference between A and B
# 12.Delete the sets completely
# 13.Convert the ages to a set and compare the length of the list and the set, which one is bigger?
# 14.I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

# 1.
print(len(it_companies))
# 2.
it_companies.add("Twitter")
print(it_companies)
# 3.
it_companies.update(["Xiaomi","Samsung"])
print(it_companies)
# 4.
it_companies.remove("Twitter")
print(it_companies)
# 5. las dos borran un elemento del set, pero con remove si no existe el elemento devuelve error.
# 6.
print(A.union(B))
# 7.
print(A.intersection(B))
# 8.
print(A.issubset(B))
# 9.
print(A.isdisjoint(B))
# 10.
st1 = A.union(B)
st2 = B.union(A)
print(st1)
print(st2)
# 11.
print(A.symmetric_difference(B))
# 12.
del A,B
# print(B)
# 13.
lst = set(age)
print(type(lst))
print(len(age)==len(lst))
# 14.
phrase = "I am a teacher and I love to inspire and teach people"
st = set(phrase.split(" "))
print(len(st))
print(st)