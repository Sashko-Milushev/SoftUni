from collections import deque


def convert_seconds_to_str(seconds):
    seconds %= 24 * 60 * 60
    hours = seconds // (60 * 60)
    seconds %= (60 * 60)
    minutes = seconds // 60
    seconds %= 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def time_as_seconds(some_str):
    hours, minutes, seconds = some_str.split(":")
    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)
    return (hours * 60 * 60) + (minutes * 60) + seconds


robo_info = input().split(";")
starting_time = input()

items = deque()
while True:
    line = input()
    if line == "End":
        break
    else:
        items.append(line)
time = time_as_seconds(starting_time)
robo_dict = {}
robo_busy_until = {}
for robot in robo_info:
    data_for_robot = robot.split("-")
    robo_dict[data_for_robot[0]] = int(data_for_robot[1])
    robo_busy_until[data_for_robot[0]] = -1
while items:
    time += 1
    item = items.popleft()
    for name, busy_until in robo_busy_until.items():
        if time >= busy_until:
            print(f"{name} - {item} [{convert_seconds_to_str(time)}]")
            robo_busy_until[name] = time + robo_dict[name]
            break
    else:
        items.append(item)