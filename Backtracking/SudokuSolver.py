board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                for k in range(1, 10):
                    if isValid(board, i, j, str(k)):
                        board[i][j] = str(k)
                        if solve(board):
                            return True
                        else:
                            board[i][j] = '.'
                return False
    return True

def isValid(board, row, col, char):
    for i in range(9):
        if board[i][col] == char:
            return False
        if board[row][i] == char:
            return False
        if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == char:
            return False
    return True

if solve(board):
    for row in board:
        print(row)
else:
    print('No solution exists for this Sudoku puzzle.')
