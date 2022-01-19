nums = [float(x) for x in input().split()]
num_dict = {}
for num in nums:
    if num not in num_dict:
        num_dict[num] = 0
    num_dict[num] += 1
for values in num_dict.items():
    print(f"{values[0]} - {values[1]} times")