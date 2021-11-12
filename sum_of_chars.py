number_of_chars = int(input())
sum = 0
for char in range(number_of_chars):
    letter = input()
    sum += ord(letter)

print(f"The sum equals: {sum}")

