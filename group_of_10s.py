numbers = [int(s) for s in input().split(", ")]
group = 10
counter = 0
while counter < len(numbers):
    collected_numbers = []
    for number in numbers:
        if group - 10 < number <= group:
            collected_numbers.append(number)
            counter += 1
    print(f"Group of {group}'s: {collected_numbers}")
    group += 10

    