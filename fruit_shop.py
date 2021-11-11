fruit = input()
day_of_week = input()
quantity = float(input())
cost = 0
if day_of_week not in "Monday Tuesday Wednesday Thursday Friday Saturday Sunday" or fruit not in"banana apple orange grapefruit kiwi pineapple grapes":
    print("error")

elif day_of_week == "Sunday" or day_of_week == "Saturday":
    if fruit == "banana":
        cost = quantity * 2.70
    elif fruit == "apple":
        cost = quantity * 1.25
    elif fruit == "orange":
        cost = quantity * 0.90
    elif fruit == "grapefruit":
        cost = quantity * 1.6
    elif fruit == "kiwi":
        cost = quantity * 3.00
    elif fruit == "pineapple":
        cost = quantity * 5.60
    elif fruit == "grapes":
        cost = quantity * 4.20
    print(f"{cost:.2f}")
elif day_of_week in "Monday Tuesday WednesdayThursday Friday ":
    if fruit == "banana":
        cost = quantity * 2.50
    elif fruit == "apple":
        cost = quantity * 1.20
    elif fruit == "orange":
        cost = quantity * 0.85
    elif fruit == "grapefruit":
        cost = quantity * 1.45
    elif fruit == "kiwi":
        cost = quantity * 2.70
    elif fruit == "pineapple":
        cost = quantity * 5.50
    elif fruit == "grapes":
        cost = quantity * 3.85
    print(f"{cost:.2f}")


