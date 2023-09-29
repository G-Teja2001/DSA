# BruteForce / Naive
matrix = [
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [27, 29, 37, 48],
    [32, 33, 39, 50]
]
key = 33

def bruteSearch(matrix, key):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if key == matrix[i][j]:
                return (i, j)
    return -1

print(bruteSearch(matrix, key))

# For sorted
def binarySearch(matrix, key):
    for i in range(len(matrix)):
        left = 0
        right = len(matrix[i]) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if matrix[i][mid] == key:
                return (i, mid)
            elif matrix[i][mid] < key:
                left = mid + 1
            else:
                right = mid - 1
    return -1

print(binarySearch(matrix, key))

# For sorted
def stairCaseSearch(matrix, key):
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Start from the top-right corner of the matrix
    i, j = 0, cols - 1

    while i < rows and j >= 0:
        if key == matrix[i][j]:
            return (i, j)
        elif key < matrix[i][j]:
            j -= 1  # Move left if the key is smaller
        else:
            i += 1  # Move down if the key is larger
    return -1

print(stairCaseSearch(matrix, key))