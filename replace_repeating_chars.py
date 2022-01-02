given_string = input()
new_string = ''
for letter in given_string:
    new_string += letter
    for ch in new_string:
        if (ch * 2) in new_string:
            new_string = new_string.replace(ch*2, ch)
print(new_string)