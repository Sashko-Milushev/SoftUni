print("Please make a guess, bokluk!!! 1,2,3,4,5 or 6?")
number = int(input())

import random

n = random.randint(1,6)
print(n)
if number == n: print("You die, bokluk")
else: print("You live, bokluk!!!")

