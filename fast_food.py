from collections import deque
food_for_the_day = int(input())
queue_of_orders = deque(input().split())
biggest_order = max(int(x) for x in queue_of_orders)
print(biggest_order)
for client in range(len(queue_of_orders)):
    if food_for_the_day >= int(queue_of_orders[0]):
        food_for_the_day -= int(queue_of_orders[0])
        queue_of_orders.popleft()
    else:
        break

if queue_of_orders:
    print(f"Orders left: {' '.join(queue_of_orders)}")
else:
    print("Orders complete")