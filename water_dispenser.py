from collections import deque
water_quantity = int(input())
queue = deque()
name = input()
while not name == "Start":
    queue.append(name)
    name = input()
command = input().split()
while not command[0] == "End":
    if command[0] == "refill":
        water_quantity += int(command[1])
    else:
        quantity_to_get = int(command[0])
        if water_quantity >= quantity_to_get:
            water_quantity -= quantity_to_get
            print(f"{queue.popleft()} got water")
        else:
            print(f"{queue.popleft()} must wait")
    command = input().split()
print(f"{water_quantity} liters left")