my_list = input().split()
n = int(input())
numbers = []
for i in range(len(my_list)):
    numbers.append(int(my_list[i]))

for number in range(n):
    smallest = min(numbers)
    numbers.remove(smallest)


print(f"{', '.join([str(i) for i in numbers])}")


