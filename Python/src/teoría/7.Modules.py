"""As our projects get larger and larger, 
it will become useful to be able to write 
functions in one file and run them in another"""
from Functions import square

for i in range(6):
    print(f"The square of {i} is {square(i)}")

"""Alternatively, we can choose to import the entire 
functions module and then use dot notation to access 
the square function:"""
import Functions

for i in range(3):
    print(f"The square of {i} is {Functions.square(i)}")