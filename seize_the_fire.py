list_of_fires_and_cells = input().split("#")
water = int(input())
effort = 0
total_fire = 0
put_out_cells = []

for fire in list_of_fires_and_cells:
    args = fire.split(" = ")
    type_of_fire = args[0]
    level_of_cell = int(args[1])
    if water < level_of_cell:
        continue

    if type_of_fire == "High":
        if 81 <= level_of_cell <= 125:
            water -= level_of_cell
            effort += level_of_cell *0.25
            total_fire += level_of_cell
            put_out_cells.append(level_of_cell)

    elif type_of_fire == "Medium":
        if 51 <= level_of_cell <= 80:
            water -= level_of_cell
            effort += level_of_cell * 0.25
            total_fire += level_of_cell
            put_out_cells.append(level_of_cell)
    elif type_of_fire == "Low":
        if 1 <= level_of_cell <= 50:
            water -= level_of_cell
            effort += level_of_cell * 0.25
            total_fire += level_of_cell
            put_out_cells.append(level_of_cell)
print("Cells:")
for cell in put_out_cells:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")




