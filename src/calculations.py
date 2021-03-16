

from .variables import c,b,h,s

def calculate_c():   # Function will calculate the area of circle 
    area = round(3.14159*pow(c,2), 3)
    print(f"The area of the circle is: {area}")

def calculate_t():  # Function will calculate the are of triangle 
    area = round(0.5*b*h, 3)
    print(f"The area of the triangle is: {area}")

def calculate_s(): # This function will calculate the surface area and volume of the sphere 
    area = round(3.14159*4*pow(s,2), 3)
    volume = round(3.14159*(4/3)*pow(s,3), 3)
    print(f"The surface area of the sphere is: {area}")
    print(f"The volume of the sphere is: {volume} ")