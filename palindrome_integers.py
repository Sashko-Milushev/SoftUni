def is_palindrome(*args):
    for num in args:
        reversed_num = num[::-1]
        if reversed_num == num:
            return True
        return False


numbers = input().split(", ")
for number in numbers:
    if is_palindrome(number):
        print("True")
    else:
        print("False")

