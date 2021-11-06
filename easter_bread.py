budget = float(input())
price_for_one_kilo_of_floor = float(input())
price_for_one_pack_of_eggs = price_for_one_kilo_of_floor * 0.75
price_for_one_litter_milk = price_for_one_kilo_of_floor * 1.25
price_for_one_bread = (price_for_one_litter_milk / 4) + price_for_one_pack_of_eggs + price_for_one_kilo_of_floor
number_of_breads = 0
colored_eggs_owned = 0
while True:
    if budget < price_for_one_bread:
        break
    number_of_breads += 1
    budget -= price_for_one_bread
    colored_eggs_owned += 3
    if number_of_breads % 3 == 0:
        colored_eggs_owned -= (number_of_breads - 2)


print(
    f"You made {number_of_breads} loaves of Easter bread! Now you have {colored_eggs_owned} eggs and {budget:.2f}BGN left.")
