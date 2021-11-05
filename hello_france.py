ticket_price = 150
list_of_items_and_prices = input().split("|")
budget = float(input())
bought_items_prices = []
profit = 0
for item in list_of_items_and_prices:
    args = item.split("->")
    type_of_item = args[0]
    price_of_item = float(args[1])
    if type_of_item == "Clothes" and price_of_item <= 50 and budget >= price_of_item:
        budget -= price_of_item
        profit += price_of_item * 0.40
        bought_items_prices.append(price_of_item * 1.40)
    elif type_of_item == "Shoes" and price_of_item <= 35.00 and budget >= price_of_item:
        budget -= price_of_item
        profit += price_of_item * 0.40
        bought_items_prices.append(price_of_item * 1.40)
    elif type_of_item == "Accessories" and price_of_item <= 20.50 and budget >= price_of_item:
        budget -= price_of_item
        profit += price_of_item * 0.40
        bought_items_prices.append(price_of_item * 1.40)
for item in bought_items_prices:
    sum_of_new_prices = sum(bought_items_prices)
budget += sum_of_new_prices

for item in bought_items_prices:
    print(f"{item:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")
if budget >= ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")


