from collections import deque

chocolates_stack = [int(x) for x in input().split(", ")]
milk_cups = deque(int(x) for x in input().split(", "))
milkshakes = 0
while milkshakes < 5 and chocolates_stack and milk_cups:
    current_cup = milk_cups[0]
    current_chocolate = chocolates_stack[-1]
    if current_chocolate <= 0 or current_cup <= 0:
        if current_chocolate <= 0:
            chocolates_stack.pop()
        if current_cup <= 0:
            milk_cups.popleft()
        continue
    if current_chocolate == current_cup:
        milkshakes += 1
        milk_cups.popleft()
        chocolates_stack.pop()
    else:
        milk_cups.append(milk_cups.popleft())
        new_chocolate = chocolates_stack.pop() - 5
        chocolates_stack.append(new_chocolate)
if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates_stack:
    print(f"Chocolate: {', '.join(str(x) for x in chocolates_stack)}")
else:
    print("Chocolate: empty")
if milk_cups:
    print(f"Milk: {', '.join(str(x) for x in milk_cups)}")
else:
    print("Milk: empty")
