people_count = int(input())
days_of_trip = int(input())
money = 0
for day in range(1, days_of_trip+1):
    if day % 10 == 0:
        people_count -= 2
    if day % 15 == 0:
        people_count += 5
    if day % 3 == 0:
        money -= people_count * 3
    if day % 5 == 0:
        money += people_count * 20
        if day % 3 == 0:
            money -= people_count * 2
    money += 50
    money -= people_count * 2
coins_per_person = money // people_count

print(f"{people_count} companions received {coins_per_person} coins each.")