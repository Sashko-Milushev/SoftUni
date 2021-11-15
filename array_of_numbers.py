def average_value(some_numbers):
    the_sum = sum(some_numbers)
    av_value = the_sum / len(some_numbers)
    return av_value


given_numbers = [int(number) for number in input().split()]

above_average = []
for num in given_numbers:
    if average_value(given_numbers) < num:
        above_average.append(num)

if not above_average:
    print("No")
else:
    above_average.sort(reverse=True)
    print(*above_average[:5])




