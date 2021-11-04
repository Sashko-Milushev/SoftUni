given_args = input().split()
products = {}
for item in range(0, len(given_args), 2):
    product = given_args[item]
    value = int(given_args[item + 1])
    products[product] = value
print(products)
