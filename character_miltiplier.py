given_strings = input().split()
total_sum = 0
first, second = given_strings[0], given_strings[1]
if len(first) == len(second):
    for num in range(len(first)):
        total_sum += ord(first[num]) * ord(second[num])
if len(first) > len(second):
    for num in range(len(second)):
        total_sum += ord(first[num]) * ord(second[num])
    to_add = first[len(second):]
    for el in to_add:
        total_sum += ord(el)
if len(first) < len(second):
    for num in range(len(first)):
        total_sum += ord(first[num]) * ord(second[num])
    to_add = second[len(first):]
    for el in to_add:
        total_sum += ord(el)

print(total_sum)
