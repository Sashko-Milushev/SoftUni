given_string = input()
resources = []
dict_of_resources = {}
index_counter = 0
while "stop" not in given_string:
    resources.append(given_string)
    given_string = input()
for item in resources:
    if index_counter % 2 == 0:
        if item not in dict_of_resources:
            dict_of_resources[item] = int(resources[index_counter + 1])
        else:
            dict_of_resources[item] += int(resources[index_counter + 1])
    index_counter += 1
for key, value in dict_of_resources.items():
    print(f"{key} -> {value}")