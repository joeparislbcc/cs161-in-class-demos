#! /usr/bin/env python3.7

"""Calculate the area and circumference of a circle from its radius."""


# import math
from math import pi

radius = input("Please enter the radius of your circle: ")
radius = int(radius)

circumference = 2 * pi * radius
area = pi * (radius ** 2)

print(f"The circumference is: {round(circumference, 1)}, and the area is: {area:.2f}.")
# print(f"The circumference is: {2 * math.pi * radius}, and the area is {math.pi * (radius ** 2)}.")
