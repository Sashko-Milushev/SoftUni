import math
number_of_people = int(input())
capacity = int(input())
# if number_of_people <= capacity:
#     print("1")
# else:
#     number_of_courses = number_of_people // capacity
#     if (number_of_courses * capacity) < number_of_people:
#         number_of_courses += 1
#     print(f'{number_of_courses}')

number_of_courses = math.ceil(number_of_people/capacity)
print(number_of_courses)

