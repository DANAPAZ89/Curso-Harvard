names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
# Unpack the first five countries and store them in a variable nordic_countries, 
# store Estonia and Russia in es, and ru respectively.

#1.
print("EJERCICIO 1\n")

def first_countries(a,b,c,d,e,f,g):
    nordic_countries = a,b,c,d,e
    es = f
    ru = g
    print(nordic_countries)
    print(ru)
    print(es)

first_countries(*names)

# Práctica de obtención del índice de un item de la lista.
for index, i in enumerate(names):
        print(f"{index}: {i}")

def index_item(lst,item):
    for index, i in enumerate(lst):
         if item == i:
              print(index)

index_item(names,"Iceland")      