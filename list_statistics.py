n = int(input())
positives = []
negatives = []

for i in range(n):
    num = int(input())

    if num >= 0:
        positives.append(num)
    else:
        negatives.append(num)

print(positives)
print(negatives)
count_of_positives = len(positives)
sum_of_negatives = sum(negatives)
print(f"Count of positives: {count_of_positives}")
print(f"Sum of negatives: {sum_of_negatives}")