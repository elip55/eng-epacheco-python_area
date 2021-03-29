

from src.circle import circle_area
from src.triangle import triangle_area
from src.rectangle import rectangle_area

# Introduction to the app and ask shape needed.
def intro():
    print("This is a simple program to find the area of certain shapes.")
    print("What shape would you like to find the area for?")
    shape = input("Type 'c' for circle, 't' for triangle, and 'r' for rectangle.\n Type 'a' for all three:")
    
    if shape == 'c' or shape == ' c':
        circle_area()
    elif shape == 't' or shape == ' t':
        triangle_area()
    elif shape == 'r' or shape == ' r':
        rectangle_area()
    elif shape == 'a' or shape == ' a':
        circle_area()
        triangle_area()
        rectangle_area()
    else:
        print("Input not valid")