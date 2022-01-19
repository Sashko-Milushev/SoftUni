number_of_students = int(input())
grades = {}
for data in range(number_of_students):
    name, grade = input().split()
    grade = float(grade)
    if name not in grades:
        grades[name] = []
    grades[name].append(grade)

for data in grades.items():
    print(f"{data[0]} -> {' '.join([f'{el:.2f}' for el in data[1]])} (avg: {sum(data[1])/len(data[1]):.2f})")
