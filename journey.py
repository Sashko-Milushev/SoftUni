budget = float(input())
season = input()
destination = " "
type_of_accommodation = " "
price = 0
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        type_of_accommodation = "Camp"
        price = budget * 0.3
    elif season == "winter":
        type_of_accommodation = "Hotel"
        price = budget * 0.70
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        type_of_accommodation = "Camp"
        price = budget * 0.4
    elif season == "winter":
        type_of_accommodation = "Hotel"
        price = budget * 0.80
elif budget > 1000:
    destination = "Europe"
    type_of_accommodation = "Hotel"
    price = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{type_of_accommodation} - {price:.2f}")