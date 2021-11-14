def add_user(forces_as_dict, to_side, user_to_be_added):
    for side, users in forces_as_dict.items():
        if user_to_be_added in users:
            return forces_as_dict
    if to_side not in forces_as_dict:
        forces_as_dict[to_side] = [user_to_be_added]
    else:
        forces_as_dict[to_side].append(user_to_be_added)
    return forces_as_dict


def change_side(forces_as_dict, to_side, user_to_be_changed):
    for side, users in forces_as_dict.items():
        if user_to_be_changed in users:
            forces_as_dict[side].remove(user_to_be_changed)
            return add_user(forces_as_dict, to_side, user_to_be_changed)
    return add_user(forces_as_dict, to_side, user_to_be_changed)


command = input()
forces = {}
while command != "Lumpawaroo":
    command_list = command.split(" | ")
    if len(command_list) > 1:
        side, user = command_list
        forces = add_user(forces, side, user)

    else:
        user, side = command.split(" -> ")
        forces = change_side(forces, side, user)
        print(f"{user} joins the {side} side!")

    command = input()
ordered_forces = sorted(forces.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))
for side, users in ordered_forces:
    if users:
        print(f"Side: {side}, Members: {len(users)}")
        for user in sorted(users):
            print(f"! {user}")
