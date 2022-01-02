number_of_persons = int(input())
info = []

for _ in range(number_of_persons):
    information = input().split()
    for word in information:
        if "@" and "|" in word:
            word = word[1:-1]

            info.append(word)
        elif "#" and "*" in word:
            word = word[1:-1]

            info.append(word)

for index in range(0, len(info), 2):
    print(f"{info[index]} is {info[index+1]} years old.")