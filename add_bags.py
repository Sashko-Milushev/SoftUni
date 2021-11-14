price_for_over_20kg_bags = float(input())
weight_in_kilograms = float(input())
days_before_flight = int(input())
number_of_bags = int(input())
if 10 <= weight_in_kilograms <= 20:
    price = price_for_over_20kg_bags * 0.5

elif weight_in_kilograms < 10:
    price = price_for_over_20kg_bags * 0.2
else:
    price = price_for_over_20kg_bags
if days_before_flight > 30:
    final_price = price * 1.1
elif 7 <= days_before_flight <= 30:
    final_price = price * 1.15
elif days_before_flight < 7:
    final_price = price * 1.4
total_price = final_price * number_of_bags
print(f" The total price of bags is: {total_price:.2f} lv. ")
