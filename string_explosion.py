given_string = input()
new_string = ""
strength = 0
for index in range(len(given_string)):
    if given_string[index] != ">" and strength > 0:
        strength -= 1
    elif given_string[index] == ">":
        strength += int(given_string[index + 1])
        new_string += given_string[index]
    else:
        new_string += given_string[index]
print(new_string)
