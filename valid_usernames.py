usernames = input().split(", ")

valid_usernames = []
for name in usernames:
    isvalid = False
    if 3 <= len(name) <= 16:
        for element in name:
            if element.isalpha() or element.isdigit() or element == "-" or element == "_":
                isvalid = True
            else:
                isvalid = False
                break
    if isvalid:
        valid_usernames.append(name)

print(*valid_usernames, sep="\n")
