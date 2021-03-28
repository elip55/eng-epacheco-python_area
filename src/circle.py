
# Calculations for the are of a circle 
from src.pi import pi
import math

def circle_area():
    radius = float(input("Input the radius of the circle: "))
    area_circle = pi*pow(radius,2)

    print(f"The area of the circle is: {area_circle}")
    answr = input("Would you like to turn this circle into a sphere and calculate the area/volume? y/n")
    
    if answr == 'y' or answr == ' y':
        area_sphere = 4*pi*pow(radius, 2)
        volume_sphere = 1.3333*pi*pow(radius,3)

        print(f"The surface area of the sphere is: {area_sphere}")
        print(f"The volume of the sphere is: {volume_sphere}")
    else:
        print("Okay!")

