# text = input().upper()
# new_text = ""
# for index in range(len(text)):
#     if not text[index].isdigit():
#         new_text += text[index]
#     else:
#         new_text += str(text[index] + ",")
# text_to_calculate = new_text.rstrip(",")
# text_to_calculate = text_to_calculate.split(",")
# repeated_symbols = ""
# for item in text_to_calculate:
#     num = int(item[-1])
#     symbols = item[0:-1]
#     symbols *= num
#     repeated_symbols += symbols
# unique_symbols = len(set(repeated_symbols))
# print(f"Unique symbols used: {unique_symbols}")
# print(repeated_symbols)
import re

text = input().upper()
split_string = re.split('(\D+)', text)
for item in split_string:
    if item == "":
        split_string.remove(item)
new_text = ""
for index in range(0, len(split_string), 2):
    new_text += split_string[index]*int(split_string[index+1])
unique_symbols = set(new_text)
print(f"Unique symbols used: {len(unique_symbols)}")
print(new_text)