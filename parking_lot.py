number_of_commands = int(input())
car_nums = set()
for _ in range(number_of_commands):
    direction, car_number = input().split(", ")
    if direction == "IN":
        car_nums.add(car_number)
    else:
        car_nums.discard(car_number)
if car_nums:
    for car in car_nums:
        print(car)
else:
    print("Parking Lot is Empty")