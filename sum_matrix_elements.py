rows, cols = [int(x) for x in input().split(", ")]
matrix = []
sum_of_nums = 0
for row_index in range(rows):
    matrix.append([int(x) for x in input().split(", ")])
for row_index in range(rows):
    sum_of_nums += sum(matrix[row_index])

print(sum_of_nums)
print(matrix)