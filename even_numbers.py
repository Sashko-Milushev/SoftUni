def is_even(number):
    if number % 2 == 0:
        return True
    return False


numbers = input().split()
filtered_numbers = []
for number in numbers:
    if is_even(int(number)):
        filtered_numbers.append(int(number))

print(filtered_numbers)


