command = input()
products = {}
while command != "statistics":
    given_args = command.split(": ")
    product = given_args[0]
    quantity = int(given_args[1])
    if product not in products:
        products[product] = quantity
    else:
        products[product] += quantity
    command = input()
total_quantity = sum(products.values())
print("Products in stock:")
for key, value in products.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {total_quantity}")
