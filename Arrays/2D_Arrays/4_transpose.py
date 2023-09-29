def fun(matrix):
    print('Before Transpose')
    printMatrix(matrix)

    transposed = []

    rows = len(matrix)
    cols = len(matrix[0])

    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)

    print('After Transpose')
    printMatrix(transposed)

def printMatrix(matrix):
    for row in matrix:
        print(row)

matrix = [
    [1, 2, 3], 
    [4, 5, 6]
]
fun(matrix)
