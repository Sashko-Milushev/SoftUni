given_args = input().split()
searched_products = input().split()
products = {}
for item in range(0, len(given_args), 2):
    product = given_args[item]
    value = int(given_args[item + 1])
    products[product] = value
for item in searched_products:
    if item in products:
        print(f"We have {products[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")