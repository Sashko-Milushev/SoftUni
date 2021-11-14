company_name = input()
adults_tickets_count = int(input())
child_tickets_count = int(input())
net_price_for_adults = float(input())
service_price = float(input())
net_price_for_children = net_price_for_adults * 0.3
final_price_for_adult_tickets = net_price_for_adults + service_price
final_price_for_child_tickets = net_price_for_children + service_price
total_money_from_adult_tickets = adults_tickets_count * final_price_for_adult_tickets
total_money_from_child_tickets = child_tickets_count * final_price_for_child_tickets
total_money_from_all_tickets = total_money_from_child_tickets + total_money_from_adult_tickets
total_profit = total_money_from_all_tickets * 0.2
print(f"The profit of your agency from {company_name} tickets is {total_profit:.2f} lv.")