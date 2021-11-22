import sys

n = int(input())

max_number = -sys.maxsize
sum_numbers = 0

for _ in range(n):
    current_number = int(input())
    sum_numbers += current_number
    if current_number > max_number:
        max_number = current_number

sum_numbers -= max_number
if max_number == sum_numbers:
    print("Yes")
    print(f"Sum = {sum_numbers}")
else:
    print("No")
    diff = max_number - sum_numbers
    print(f"Diff = {abs(diff)}")
