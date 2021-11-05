list_of_gifts = input().split()
commands = input().split()
index_counter = len(list_of_gifts)
while "No Money" not in commands:
    if "OutOfStock" in commands:
        for item in list_of_gifts:
            if item == commands[1]:
                list_of_gifts[int(item)] = "None"
    elif "Required" in commands:
        if 0 <= int(commands[2]) <= index_counter:
            list_of_gifts[int(commands[2])] = commands[1]
    elif "JustInCase" in commands:
        list_of_gifts[-1] = commands[1]

    commands = input().split()

for gift in list_of_gifts:
    if gift == "None":
        list_of_gifts.remove(gift)
print(*list_of_gifts, sep=" ")