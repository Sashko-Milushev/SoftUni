import math

figure = input()
if figure == "square":
    square_lenght = float(input())
    area = (square_lenght * square_lenght)

elif figure == "rectangle":
    rectangle_length = float(input())
    rectangle_height = float(input())
    area = (rectangle_height * rectangle_length)

elif figure == "circle":
    radius = float(input())
    area = (math.pi * radius * radius)

else:
    triangle_lenght = float(input())
    triangle_height = float(input())
    area = (triangle_height * triangle_lenght / 2)

print(round(area, 3))
