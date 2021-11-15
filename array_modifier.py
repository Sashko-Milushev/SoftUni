values = [int(number) for number in input().split()]

commands = input().split()
while commands[0] != "end":
    if commands[0] == "swap":
        values[int(commands[1])], values[int(commands[2])] = values[int(commands[2])], values[int(commands[1])]
    elif commands[0] == "multiply":
        values[int(commands[1])] = values[int(commands[1])] * values[int(commands[2])]
    elif commands[0] == "decrease":
        values = [num - 1 for num in values]

    commands = input().split()
print(", ".join(str(n) for n in values))

