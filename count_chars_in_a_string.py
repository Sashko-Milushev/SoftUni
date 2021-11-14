string_input = input().split()
given_string = ""
chars = {}
for text in string_input:
    given_string += text
for char in given_string:
    if char not in chars:
        chars[char] = []
    chars[char].append(1)
for char, count in chars.items():
    print(f"{char} -> {len(count)}")
