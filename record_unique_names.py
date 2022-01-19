number_of_names = int(input())
unique_names = set()
for name in range(number_of_names):
    unique_names.add(input())
for _ in unique_names:
    print(_)