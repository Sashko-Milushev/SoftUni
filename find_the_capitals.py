given_string = input()
res = [idx for idx in range(len(given_string)) if given_string[idx].isupper()]
print(str(res))