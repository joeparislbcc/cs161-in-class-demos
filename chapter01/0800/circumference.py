#! /usr/bin/env python3.7

""" Calculate the area and circumference of a circle from its radius. """

import math

radius = input("Please enter the radius of your circle: ")
radius = int(radius)

circumference = 2 * math.pi * radius
area = math.pi * (radius ** 2)

# print(f"The circumference is: {2 * math.pi * radius}, and the area is: {math.pi * radius ** 2}")
print("The circumference is:", 2 * math.pi * radius, "and the area is:", math.pi * radius ** 2)
