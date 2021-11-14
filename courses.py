given_info = input()
courses_dict = {}
while given_info != "end":
    split_data = given_info.split(" : ")
    course = split_data[0]
    student = split_data[1]
    if course not in courses_dict:
        courses_dict[course] = []
    courses_dict[course].append(student)
    given_info = input()
ordered_courses = sorted(courses_dict.items(), key=lambda kvpt: -len(kvpt[1]))
for course, student in ordered_courses:
    print(f"{course}: {len(student)}")
    for name in sorted(student):
        print(f"-- {name}")