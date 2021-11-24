given_numbers = input().split()
rounded_numbers = []

for num in given_numbers:
    number = round(float(num))
    rounded_numbers.append(number)
print(rounded_numbers)
