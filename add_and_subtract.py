def sum_numbers(first, second):
    return first + second


def subtract(summ, number):
    return summ - number


def add_and_subtract(first, second, third):
    sum_of_first_two_digits = sum_numbers(first, second)
    result = subtract(sum_of_first_two_digits, third)
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))
