# # until "end of contest" get input and save the data in dict
# # until "end of submissions" get input: "{contest}=>{password}=>{username}=>{points}"
# # check if contest is valid, it must be received in the dict
# # check the password for the given contest
# # if both are valid save the user with the contest and the points in that contest
# # if user and contest exist - update the points if new points are higher
# # print user with most points(sum of all points for the user)
# # print all students, by name. and all contest for this user, by points
# official_contests = {}
# contests_info = input()
# while not contests_info == "end of contests":
#     contest_and_pass = contests_info.split(":")
#     name_of_contest, pass_for_contest = contest_and_pass[0], contest_and_pass[1]
#     official_contests[name_of_contest] = pass_for_contest
#     contests_info = input()
# user_info = input()
# contest_dict = {}
# while not user_info == "end of submissions":
#     information = user_info.split("=>")
#     contest, password, username, points = information[0], information[1], information[2], int(information[3])
#     if contest in official_contests and password == official_contests[contest]:
#         if username not in contest_dict:
#             contest_dict[username] = {contest: points}
#         else:
#             if contest not in contest_dict[username]:
#                 contest_dict[username][contest] = points
#             else:
#                 if contest_dict[username][contest] < points:
#                     contest_dict[username][contest] = points
#     user_info = input()
# ranking = {}
# for user, contents in contest_dict.items():
#     sum_of_points = 0
#     max_sum = 0
#     for course, points in contents.items():
#         sum_of_points += points
#         ranking[user] = sum_of_points
# best_candidate = max(ranking, key=ranking.get)
# print(f"Best candidate is {best_candidate} with total {ranking[best_candidate]} points.")
# print("Ranking:")
#
# sorted_users = sorted(contest_dict.items(), key=lambda x: x[0], reverse=False)
#
# for student, courses in sorted_users:
#     print(student)
#     sorted_courses = sorted(courses, key=lambda i: -i['points'])
#     for course in sorted_courses:
#         print(f"# {course['name']} -> {course['points']}")
#
#
content = input()
contests = {}

while not content == "end of contests":
    contest, password = content.split(":")
    contests.update({contest: password})
    content = input()

users = {}
content = input()

is_item = False
while not content == "end of submissions":
    contest, password, username, points = content.split("=>")
    points = int(points)
    if contest in contests:
        if contests[contest] == password:
            if username in users:
                is_item = False
                for item in users[username]:

                    if contest == item['name']:
                        is_item = True
                        if item["points"] < points:
                            item["points"] = points
                if not is_item:
                    users[username].append({"name": contest, "points": points})
            else:
                users[username] = [{"name": contest, "points": points}]
    content = input()

order_contests = sorted(users.items(), key=lambda x: x[0], reverse=False)

best_points = {}
for student, courses in order_contests:
    sorted_courses = sorted(courses, key=lambda i: -i['points'])
    total_points = 0
    for course in courses:
        total_points += course['points']

    best_points[student] = total_points

best_student = sorted(best_points.items(), key=lambda p: -p[1])

name, best_points = best_student[0]
print(f"Best candidate is {name} with total {best_points} points.")
print("Ranking:")

for student, courses in order_contests:
    print(student)

    sorted_courses = sorted(courses, key=lambda i: -i['points'])
    for course in sorted_courses:
        print(f"#  {course['name']} -> {course['points']}")
