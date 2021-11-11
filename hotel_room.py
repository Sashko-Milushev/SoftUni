month = input()
days = int(input())
studio_price = 0
apartment_price = 0

if month in " May October":
    studio_price = 50
    apartment_price = 65
    if 7 < days <= 14:
        studio_price = studio_price * 0.95
    elif 14 < days:
        studio_price = studio_price * 0.70
        apartment_price = apartment_price * 0.90
elif month in "June September":
    studio_price = 75.20
    apartment_price = 68.70
    if days > 14:
        studio_price = studio_price * 0.80
        apartment_price = apartment_price * 0.90
elif month in "July August":
    apartment_price = 77
    studio_price = 76
    if days > 14:
        apartment_price = apartment_price * 0.90

apartment_cost = days * apartment_price
studio_cost = days * studio_price
print(f"Apartment: {apartment_cost:.2f} lv.")
print(f"Studio: {studio_cost:.2f} lv.")
