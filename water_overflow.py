n = int(input())
water_in_tank = 0
for line in range(n):
    current_flow = int(input())
    water_in_tank += current_flow
    if water_in_tank > 255:
        water_in_tank -= current_flow
        print("Insufficient capacity!")

print(water_in_tank)
