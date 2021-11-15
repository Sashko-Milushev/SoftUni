energy = int(input())
distance = input()
won_battles = 0
while distance != "End of battle":
    energy -= int(distance)
    if energy < 0:
        print(f"Not enough energy! Game ends with {won_battles} won battles and 0 energy")
        break

    won_battles += 1
    if won_battles % 3 == 0:
        energy += won_battles

    distance = input()
if energy >= 0:
    print(f"Won battles: {won_battles}. Energy left: {energy}")

