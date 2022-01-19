from collections import deque
number_of_guests = int(input())
all_guests = set()
list_of_guests = set()
for guest in range(number_of_guests):
    reservation_code = input()
    all_guests.add(reservation_code)

while True:
    incoming = input()
    if incoming == "END":
        break
    else:
        list_of_guests.add(incoming)
guests_not_arrived = sorted(all_guests - list_of_guests)
print(len(guests_not_arrived))
for guest in guests_not_arrived:
    print(guest)
