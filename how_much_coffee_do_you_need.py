command = input()
coffee_needed = 0
while command != "END":
    if command in "CAT, DOG, MOVIE,CODING":
        coffee_needed += 2
    elif command in "cat, dog, movie, coding":
        coffee_needed += 1
    command = input()
if coffee_needed <= 5:
    print(coffee_needed)
else:
    print('You need extra sleep')
