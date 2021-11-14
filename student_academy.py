
count = int(input())
grades = {}
for _ in range(count):
    name = input()
    grade = float(input())
    if name not in grades:
        grades[name] = []
    grades[name].append(grade)

filtered_grades = {}
for name, grade in grades.items():
    avg_grade = sum(grade)/ len(grade)
    if avg_grade >= 4.50:
        filtered_grades[name] = avg_grade
sorted_grades = sorted(filtered_grades.items(), key=lambda kvpt: -kvpt[1])
for name, grade in sorted_grades:
    print(f"{name} -> {grade:.2f}")


