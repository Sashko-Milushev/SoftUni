n = int(input())
matrix = []
for row_index in range(n):
    matrix.append([x for x in input()])
special_symbol = input()
is_found = False
for row_index in range(n):
    for col_index in range(n):
        if matrix[row_index][col_index] == special_symbol:
            is_found = True
            print(f"({row_index}, {col_index})")
            break
    if is_found:
        break
if not is_found:
    print(f"{special_symbol} does not occur in the matrix")