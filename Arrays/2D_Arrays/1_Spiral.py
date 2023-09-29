matrix = [[i + j * 4 for i in range(1, 5)] for j in range(4)]

num_rows = len(matrix)
num_cols = len(matrix[0])

start_row = 0
end_row = num_cols - 1

start_col = 0
end_col = num_rows - 1

while start_row <= end_row and start_col <= end_col:
    # Print the top row
    for i in range(start_col, end_col + 1):
        print(matrix[start_row][i], end=' ')

    # Print the rightmost column
    for i in range(start_row + 1, end_row + 1):
        print(matrix[i][end_col], end=' ')

    # Print the bottom row (if there are more than one rows left)
    if start_row < end_row:
        for i in range(end_col - 1, start_col - 1, -1):
            print(matrix[end_row][i], end=' ')

    # Print the leftmost column (if there are more than one columns left)
    if start_col < end_col:
        for i in range(end_row - 1, start_row, -1):
            print(matrix[i][start_col], end=' ')

    start_row += 1
    start_col += 1

    end_col -= 1
    end_row -= 1