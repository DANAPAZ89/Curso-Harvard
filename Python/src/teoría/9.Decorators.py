
def announce(f): #La función announce() toma como input la función f() que retornará una función que envuelva (wrap) a la f()
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function")
        return wrapper
#El decorator nos indica que añada la función hello() a la función announce como función f()    
@announce 
def hello():
    print("Hello, World!")

hello()

"""
Coge la función f y crea otra función que anuncie y ejecute la función f() y 
"""

