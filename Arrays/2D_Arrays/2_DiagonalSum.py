# Even
matrix = [[i + j * 4 for i in range(1, 5)] for j in range(4)]

# Odd
matrix = [[i + j * 3 for i in range(1, 4)] for j in range(3)]

num_rows = len(matrix)
num_cols = len(matrix[0])

if num_rows != num_cols:
    exit('Only for square matrices')

sum = 0
for i in range(num_rows):
    for j in range(num_cols):
        if i == j:
            sum += matrix[i][j]
        elif i + j == num_rows-1:
            sum += matrix[i][j]

print(sum)

sum = 0
for i in range(num_rows):
    # Primary Diag
    sum += matrix[i][i]

    # Secondary Diag
    if i != num_rows-i-1:
        sum += matrix[i][num_rows-i-1]
print(sum)
