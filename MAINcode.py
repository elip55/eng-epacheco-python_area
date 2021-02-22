# area with functions

import math

def explain ():     # Explain what the program is going to do 
    print("Hello.")
    print("This program will tell you the area of various objects")


def calculate(c):   # Function will calculate the area of circle 
    area = round(3.14159*pow(c,2), 3)
    print(f"The are of the circle is: {area}")

def calculate_t(b,h):  # Function will calculate the are of triangle 
    area = round(0.5*b*h, 3)
    print(f"The area of the triangle is: {area}")

def calculate_s(s): # This function will calculate the area and volume of the sphere 
    area = round(3.14159*4*pow(s,2), 3)
    volume = round(3.14159*1.3333333*pow(s,3), 3)
    print(f"The surface area of the sphere is: {area}")
    print(f"The volume of the sphere is: {volume} ")


explain()
print("First, we'll gather the information we need!")

c = float(input("Input the radius of the circle: "))
s = float(input("Input the radius of the sphere: "))
b = float(input("Input the base of the triangle: "))
h = float(input("Input the height of the triangle: "))
calculate(c)
calculate_s(s)
calculate_t(b,h)
