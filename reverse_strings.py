text = [x for x in input()]
stack = []
for word in range(len(text)):
    stack.append(text.pop())
print("".join(stack))