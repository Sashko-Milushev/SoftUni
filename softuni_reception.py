first_employee_per_hour = int(input())
second_employee_per_hour = int(input())
third_employee_per_hour = int(input())
students_count = int(input())
hour_counter = 0
all_employees_efficiency = first_employee_per_hour + second_employee_per_hour + third_employee_per_hour
while students_count > 0:
    hour_counter += 1
    students_count -= all_employees_efficiency
    if hour_counter % 4 == 0:
        hour_counter += 1

print(f"Time needed: {hour_counter}h.")
