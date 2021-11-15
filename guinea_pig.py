quantity_food = float(input())
quantity_hay = float(input())
quantity_cover = float(input())
weight = float(input())
for day in range(1, 31):
    quantity_food -= 0.30
    if day % 2 == 0:
        quantity_hay -= quantity_food * 0.05
    if day % 3 == 0:
        quantity_cover -= weight / 3
    if quantity_food < 0 or quantity_hay < 0 or quantity_cover < 0:
        print("Merry must go to the pet store!")
        break
if quantity_food >= 0 and quantity_cover >= 0 and quantity_hay >= 0:
    print(f"Everything is fine! Puppy is happy! Food: {quantity_food:.2f}, Hay: {quantity_hay:.2f}, \n"
          f"Cover: {quantity_cover:.2f}.")
