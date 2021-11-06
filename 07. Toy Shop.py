trip_price = float(input())
puzzles_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())
puzzles_profit = puzzles_count * 2.6
dolls_profit = dolls_count * 3
bears_profit = bears_count * 4.1
minions_profit = minions_count * 8.2
trucks_profit = trucks_count * 2
all_toys_profit = puzzles_profit + dolls_profit + bears_profit + minions_profit + trucks_profit
all_toys_count = puzzles_count + bears_count + minions_count + trucks_count + dolls_count
if all_toys_count >= 50:
    all_toys_profit = all_toys_profit * 0.75
profit_after_rent = all_toys_profit * 0.9
if profit_after_rent >= trip_price:
    money_left = profit_after_rent - trip_price
    print(f'Yes! {money_left:.2f} lv left.')
else:
    money_needed = trip_price - profit_after_rent
    print((f'Not enough money! {money_needed:.2f} lv needed.'))
