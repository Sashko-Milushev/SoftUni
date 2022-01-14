sequence = input()
stack_of_opening = []
balanced = True
for element in sequence:
    if element in "({[":
        stack_of_opening.append(element)
    elif not stack_of_opening:
        balanced = False
        break
    else:
        last_opening_bracket = stack_of_opening.pop()
        if f"{last_opening_bracket}{element}" not in "()[]{}":
            balanced = False
            break


if not balanced:
    print("NO")
else:
    print("YES")