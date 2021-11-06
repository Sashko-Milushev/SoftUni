string = input()
sum = 0

string = string.lower()
sum += string.count("sand")
sum += string.count("fish")
sum += string.count("water")
sum += string.count("sun")
print(sum)