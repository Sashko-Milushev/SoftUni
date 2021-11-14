collected = {'shards': 0, 'motes': 0, 'fragments': 0}
obtained = False
counter = 0
input_args = input().lower()
while True:

    materials = input_args.split()
    list_of_materials = []
    list_of_quantities = []
    for items in materials:
        if items.isalpha():
            list_of_materials.append(items)
        elif items.isnumeric():
            list_of_quantities.append(int(items))
    for material in list_of_materials:
        if material not in collected:
            collected[material] = 0
        collected[material] += list_of_quantities[counter]
        counter += 1
        if material in " shards fragments motes" and collected[material] >= 250:
            break
    for material, quantity in collected.items():
        if material == "shards" and quantity >= 250:
            print(f"Shadowmourne obtained!")
            collected[material] -= 250
            obtained = True
        elif material == "fragments" and quantity >= 250:
            print(f"Valanyr obtained!")
            collected[material] -= 250
            obtained = True
        elif material == "motes" and quantity >= 250:
            print(f"Dragonwrath obtained!")
            collected[material] -= 250
            obtained = True
    if not obtained:
        counter = 0
        input_args = input().lower()
        continue
    break
key_materials = {}
junk = {}
for items, values in collected.items():
    if items in "shards fragments motes":
        key_materials[items] = values
    if items not in "shards fragments motes":
        junk[items] = values

ordered_materials = sorted(key_materials.items(), key=lambda kvp: (-kvp[1], kvp[0]))
ordered_junk = sorted(junk.items(), key=lambda kvp: (kvp[0]))

for material, value in ordered_materials:
    print(f"{material}: {value}")
for material, value in ordered_junk:
    print(f"{material}: {value}")




