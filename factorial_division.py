def calculation(first, second):
    for factorial in range(1, first):
        first *= factorial
    for factorial in range(1, second):
        second *= factorial
    result = first / second
    return f"{result:.2f}"


first_number = int(input())
second_number = int(input())
print(calculation(first_number, second_number))