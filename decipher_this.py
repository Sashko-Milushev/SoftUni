secret_message = input().split()
deciphered_message = []


def switch_letters(word):
    letters = list(word)
    letters[1], letters[-1] = letters[-1], letters[1]
    return ''.join(letters)


for word in secret_message:
    number = ""
    for char in word:
        if char.isdigit():
            number += char
    word = word.replace(number, chr(int(number)))
    deciphered_message.append(word)
for words in deciphered_message:
    print("".join([switch_letters(words)]), end=' ')



