def symbol_filtering(some_string):
    digits = []
    letters = []
    symbols = []
    for element in some_string:
        if element.isdigit():
            digits.append(element)
        elif element.isalpha():
            letters.append(element)
        else:
            symbols.append(element)
    print("".join(digits))
    print("".join(letters))
    print("".join(symbols))


given_string = input()
symbol_filtering(given_string)



