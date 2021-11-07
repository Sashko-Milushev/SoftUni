import math

record = float(input())
distance = float(input())
time_in_seconds_for_swimming_one_meter = float(input())
time_to_take_distance = distance * time_in_seconds_for_swimming_one_meter
additional_time = math.floor(distance / 15) * 12.5
total_time = time_to_take_distance + additional_time
if total_time < record:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    over_time = total_time - record
    print(f"No, he failed! He was {over_time:.2f} seconds slower.")