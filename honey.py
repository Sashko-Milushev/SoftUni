from collections import deque
bees = deque(int(x) for x in input().split())
nectar_stack = [int(x) for x in input().split()]
symbols = deque(input().split())
total_honey_made = 0
while bees and nectar_stack:
    current_bee = bees.popleft()
    current_nectar = nectar_stack.pop()
    if current_nectar >= current_bee:
        current_symbol = symbols.popleft()
        if current_symbol == "+":
            honey_made = abs(current_bee + current_nectar)
            total_honey_made += honey_made
        elif current_symbol == "-":
            honey_made = abs(current_bee - current_nectar)
            total_honey_made += honey_made
        elif current_symbol == "*":
            honey_made = abs(current_bee * current_nectar)
            total_honey_made += honey_made
        elif current_symbol == "/" and current_nectar > 0:
            honey_made = abs(current_bee/current_nectar)
            total_honey_made += honey_made
    else:
        bees.appendleft(current_bee)
        continue
print(f"Total honey made: {total_honey_made}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectar_stack:
    print(f"Nectar left: {', '.join(str(x) for x in nectar_stack)}")