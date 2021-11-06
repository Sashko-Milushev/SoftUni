divisor = int(input())
boundary = int(input())
# number must be % divisor == 0
# number must be <= boundary
# number must be > 0
for number in range (boundary, 0, -1):
    if number % divisor == 0:
        print(number)
        break

