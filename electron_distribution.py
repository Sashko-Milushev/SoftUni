number_of_electrons = int(input())
count_of_shell = 1
enough_electrons = True
filled_shells = []
while enough_electrons:
    number_of_electrons -= 2*(count_of_shell**2)
    filled_shells.append(2*(count_of_shell**2))
    count_of_shell += 1
    if 2*(count_of_shell**2) > number_of_electrons:
        filled_shells.append(number_of_electrons)
        enough_electrons = False


print(filled_shells)