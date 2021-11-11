projection = input()
rows = int(input())
columns = int(input())
income = 0
capacity = rows * columns
if projection == "Premiere":
    income = capacity * 12
elif projection == "Normal":
    income = capacity * 7.50
elif projection == "Discount":
    income = capacity * 5
print(f"{income:.2f}")

