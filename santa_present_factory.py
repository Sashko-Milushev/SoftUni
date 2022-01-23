from collections import deque
materials_stack = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())
crafted = {}
job_done = False
presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}
while magic and materials_stack:
    box = materials_stack[-1]
    cur_magic = magic[0]
    total_magic_level = box * cur_magic
    if total_magic_level in presents:
        materials_stack.pop()
        magic.popleft()
        toy = presents[total_magic_level]
        if toy not in crafted:
            crafted[toy] = 1
        else:
            crafted[toy] += 1
        if "Doll" in crafted and "Wooden train" in crafted:
            job_done = True
        if "Teddy bear" in crafted and "Bicycle" in crafted:
            job_done = True
    else:
        if total_magic_level < 0:
            result = magic.popleft() + materials_stack.pop()
            materials_stack.append(result)
        elif total_magic_level > 0:
            magic.popleft()
            new_value = materials_stack.pop() + 15
            materials_stack.append(new_value)
        elif total_magic_level == 0:
            if box == 0:
                materials_stack.pop()
            if cur_magic == 0:
                magic.popleft()

if job_done:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials_stack:
    print(f"Materials left: {', '.join(str(x) for x in reversed(materials_stack))}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")
for present, value in sorted(crafted.items()):
    print(f"{present}: {value}")