animals = input()
list_of_animals = animals.split()
sheep_counter = 0
for _ in range(len(list_of_animals)):
    if list_of_animals[-1] == "wolf":
        print("Please go away and stop eating my sheep")
        break
    elif list_of_animals[-1] == "sheep," or list_of_animals[-1] == "sheep":
        sheep_counter += 1
        list_of_animals.pop()
if list_of_animals[-1] != "wolf":
    print(f"Oi! Sheep number {sheep_counter}! You are about to be eaten by a wolf!")






