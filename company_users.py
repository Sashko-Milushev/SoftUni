data = input()
information = {}
while not data == "End":
    split_data = data.split(" -> ")
    company = split_data[0]
    employee_id = split_data[1]
    if company not in information:
        information[company] = []
    if employee_id not in information[company]:
        information[company].append(employee_id)
    data = input()
ordered_info = sorted(information.items())
for company, users in ordered_info:
    print(f"{company}")
    for id in users:
        print(f"-- {id}")