budget = float(input())
extras_count = int(input())
price_for_clothes_for_one_extra = float(input())
decor = budget * 0.1
price_for_all_clothes = extras_count * price_for_clothes_for_one_extra
if extras_count > 150:
    price_for_all_clothes -= price_for_all_clothes * 0.1
total_cost = decor + price_for_all_clothes
if total_cost <= budget:
    money_left = budget - total_cost
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
if total_cost > budget:
    money_needed = total_cost - budget
    print("Not enough money!")
    print(f"Wingard needs {money_needed:.2f} leva more.")
