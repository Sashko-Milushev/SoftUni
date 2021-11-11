budget = int(input())
season = input()
fishermen_count = int(input())
boat_price = 0
if season == "Spring":
    boat_price = 3000
    if fishermen_count <= 6:
        boat_price = boat_price * 0.90
        if (fishermen_count % 2) == 0:
            boat_price = boat_price * 0.95
    elif 7 < fishermen_count <= 11:
        boat_price = boat_price * 0.85
        if (fishermen_count % 2) == 0:
            boat_price = boat_price * 0.95
    elif fishermen_count >= 12:
        boat_price = boat_price * 0.75
        if (fishermen_count % 2) == 0:
            boat_price = boat_price * 0.95

elif season == "Summer":
    boat_price = 4200
    if fishermen_count <= 6:
        boat_price = boat_price * 0.90
        if (fishermen_count % 2) == 0:
            boat_price = boat_price * 0.95
    elif 7 < fishermen_count <= 11:
        boat_price = boat_price * 0.85
        if (fishermen_count % 2) == 0:
            boat_price = boat_price * 0.95
    elif fishermen_count >= 12:
        boat_price = boat_price * 0.75
        if (fishermen_count % 2) == 0:
            boat_price = boat_price * 0.95
elif season == "Winter":
    boat_price = 2600
    if fishermen_count <= 6:
        boat_price = boat_price * 0.90
        if (fishermen_count % 2) == 0:
            boat_price = boat_price * 0.95
    elif 7 < fishermen_count <= 11:
        boat
        price = boat_price * 0.85
        if (fishermen_count % 2)== 0:
            boat_price = boat_price * 0.95
    elif fishermen_count >= 12:
        boat_price = boat_price * 0.75
        if (fishermen_count % 2) == 0:
            boat_price = boat_price * 0.95
elif season == "Autumn":
    boat_price = 4200
    if fishermen_count <= 6:
        boat_price = boat_price * 0.90
    elif 7 < fishermen_count <= 11:
        boat_price = boat_price * 0.85
    elif fishermen_count >= 12:
        boat_price = boat_price * 0.75

if budget >= boat_price:
    money_left = budget - boat_price
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    money_needed = boat_price - budget
    print(f"Not enough money! You need {money_needed:.2f} leva.")
