string_to_remove = input()
string_to_remove_from = input()
while string_to_remove in string_to_remove_from:
    string_to_remove_from = string_to_remove_from.replace(string_to_remove, "")

print(string_to_remove_from)