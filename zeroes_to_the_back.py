given_string = input().split(", ")
list_as_digits = []
list_as_digits_remake = []
for num in given_string:
    list_as_digits.append(int(num))
index_counter = 0
for number in list_as_digits:

    if number == 0:
        list_as_digits_remake.append(number)
        index_counter -= 1
    else:
        list_as_digits_remake.insert(index_counter, number)
    index_counter += 1

print(list_as_digits_remake)
