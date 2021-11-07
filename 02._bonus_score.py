number = int(input())
bonus_points = 0
if number <= 100:
    bonus_points = 5
elif 100 < number <= 1000:
    bonus_points = number * 0.2
else:
    bonus_points = number * 0.1
if number % 2 == 0:
    bonus_points += 1
elif number % 10 == 5:
    bonus_points += 2
result = number + bonus_points
print(bonus_points)
print(result)


