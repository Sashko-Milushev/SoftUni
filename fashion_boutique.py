clothes_in_the_box = [int(s) for s in input().split()]
rack_capacity = int(input())
rack_count = 1
current_stack_on_rack = []

while clothes_in_the_box:
    if sum(current_stack_on_rack) + clothes_in_the_box[-1] < rack_capacity:
        current_stack_on_rack.append(clothes_in_the_box.pop())
    elif sum(current_stack_on_rack) + clothes_in_the_box[-1] == rack_capacity:
        current_stack_on_rack.append(clothes_in_the_box.pop())
        if clothes_in_the_box:
            rack_count += 1
            current_stack_on_rack.clear()

    else:
        current_stack_on_rack.clear()
        rack_count += 1
        current_stack_on_rack.append(clothes_in_the_box.pop())

print(rack_count)


