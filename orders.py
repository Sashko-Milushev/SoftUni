# command_args = input()
# products = {}
# while not command_args == "buy":
#     split_data = command_args.split()
#     name = split_data[0]
#     price = float(split_data[1])
#     quantity = int(split_data[2])
#     if name not in products:
#         products[name] = [price, quantity]
#     else:
#         products[name] = [price, +quantity]
#     command_args = input()
#
# for name, nums in products.items():
#     prod = nums[0]*nums[1]
#     print(f"{name} -> {prod:.2f}")
#
content = input()
products = {}
while not content == "buy":
    content = content.split(" ")
    name = content[0]
    price = float(content[1])
    quantity = int(content[2])
    if name not in products:
        products[name] = {price: quantity}
    else:
        if price in products[name].keys():
            products[name][price] += quantity
        else:
            price_list = list(products[name].keys())
            current_price = price_list[0]
            quantity += products[name].pop(current_price)
            products[name] = {price: quantity}
    content = input()

for product, value in products.items():
    for price, quantity in value.items():
        print(f"{product} -> {price * quantity:.2f}")
