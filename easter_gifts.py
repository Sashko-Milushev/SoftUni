list_of_gifts = input().split()
command = input().split()
while command[0] != "No" and command[1] != " Money":
    if command[0] == "OutOfStock":
        for index, item in enumerate(list_of_gifts):
            if item == command[1]:
                list_of_gifts[index] = "None"
    elif command[0] == "Required":
        if 0 <= int(command[2]) <= len(list_of_gifts):
            for item in range(len(list_of_gifts)):
                if item == int(command[2]):
                    list_of_gifts[item] = command[1]
    elif command[0] == "JustInCase":
        list_of_gifts[-1] = command[1]
    command = input().split()
for index, item in enumerate(list_of_gifts):
    if item == "None":
        list_of_gifts.remove(item)
print(*list_of_gifts, sep= " ")
