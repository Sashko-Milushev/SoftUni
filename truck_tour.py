from collections import deque
pump_count = int(input())
queue_of_pumps = deque()

for p in range(pump_count):
    pump_data = [int(x) for x in input().split()]
    queue_of_pumps.append(pump_data)
for attempt in range(pump_count):
    tank = 0
    failed = False
    for fuel, distance in queue_of_pumps:
        tank += fuel
        if distance > tank:
            failed = True
            break
        else:
            tank -= distance
    if failed:
        queue_of_pumps.append(queue_of_pumps.popleft())
    else:
        print(attempt)
        break
