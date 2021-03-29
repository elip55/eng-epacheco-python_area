
# Square calculations for area and surface area for box


def rectangle_area():
    l = float(input("Input the length of the rectangle: "))
    w = float(input("Input the width of the rectangle: "))

    area = l*w
    print(f"The area of the rectangle is {area}")

    ansr =  input("Would you like to turn the rectangle into a box and find the surface area?")
    if ansr == 'y' or ansr == ' y':
        h = float(input("Input the height of the box."))
        surface_area = (2*w*l)*(2*l*h)+(2*w*h)
        print(f"The surface area of the box is: {surface_area}")
    else:
        print("Okay!")