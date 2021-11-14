entry = input()
phonebook_dict = {}

while not entry.isnumeric():
    name, number = entry.split("-")
    if name not in phonebook_dict:
        phonebook_dict[name] = number
    phonebook_dict.update({name: number})
    entry = input()

for _ in range(int(entry)):
    name_check = input()
    if name_check in phonebook_dict:
        print(f"{name_check} -> {phonebook_dict[name_check]}")
    else:
        print(f"Contact {name_check} does not exist.")
