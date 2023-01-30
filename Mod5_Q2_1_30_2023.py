#Write a program that takes the radius of a sphere
# (a floating-point number) as input and then outputs the sphere’s surface area

import math 

math.pi = 3.14

radius = float(input("Enter the radius of the sphere: ")) 

surface_area = 4 * math.pi * (radius**2) 

print("The surface area of the sphere is:", surface_area) 