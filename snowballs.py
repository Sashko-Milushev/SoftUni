n = int(input())
highest_value = 0
highest_time = 0
highest_quality = 0
highest_weight = 0

for _ in range(n):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())
    value = (weight/time_needed) ** quality
    if value > highest_value:
        highest_value = value
        highest_weight = weight
        highest_time = time_needed
        highest_quality = quality
print(f"{highest_weight} : {highest_time} = {highest_value} ({highest_quality})")
