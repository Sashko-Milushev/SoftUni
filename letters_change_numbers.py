def letter_position(letter):
    return ord(letter) - 96


def capital_letter_position(letter):
    return ord(letter) - 64


def calculated_string(first_l, second_l, digit):
    if first_l.isupper():
        digit = digit/capital_letter_position(first_l)
    else:
        digit = digit * letter_position(first_l)
    if second_l.isupper():
        digit -= capital_letter_position(second_letter)
    else:
        digit += letter_position(second_letter)
    return digit


sequence = input().split()
total_sum = 0
for text in sequence:
    first_letter = text[0]
    second_letter = text[-1]
    number = int(text[1:-1])
    total_sum += calculated_string(first_letter, second_letter, number)
print(f"{total_sum:.2f}")