def multiply(a, b):
    return a * b


def divide(a, b):
    return a // b


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def calculate(operator, first_num, second_num):
    res = 0
    if operator == "multiply":
        res = multiply(first_num, second_num)
    elif operator == "divide":
        res = divide(first_num, second_num)
    elif operator == "add":
        res = add(first_num, second_num)
    elif operator == "subtract":
        res = subtract(first_num, second_num)

    return res


operator = input()
number_one = int(input())
number_two = int(input())
result = calculate(operator, number_one, number_two)
print(result)
