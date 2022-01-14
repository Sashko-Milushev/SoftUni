stack_of_numbers = [x for x in input().split()]
reversed_stack = []

for num in range(len(stack_of_numbers)):
    reversed_stack.append(stack_of_numbers.pop())
print(" ".join(reversed_stack))