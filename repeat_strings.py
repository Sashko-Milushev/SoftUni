sequence_of_strings = input().split()
final_string = ""
for word in sequence_of_strings:
    word_length = len(word)
    final_string += word * word_length
print(final_string)

