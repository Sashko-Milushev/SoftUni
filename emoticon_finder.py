given_string = input()
list_of_emos = []
while given_string:
    emo = ""
    emo_start = given_string.find(":")

    if emo_start == -1:
        break

    emo += given_string[emo_start: emo_start + 2]

    if emo != ": ":
        list_of_emos.append(emo)
        given_string = given_string[emo_start + 2:]

print(*list_of_emos, sep="\n")
