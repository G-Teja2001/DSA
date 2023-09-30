def printQueens(board):
    print('---- Chess Board ----')
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=' ')
        print()

def isSafe(board, row, col):
    # Check for upper diag to left
    dupRow = row
    dupCol = col
    while dupRow >= 0 and dupCol >= 0:
        if board[dupRow][dupCol] == 'Q':
            return False
        dupRow -= 1
        dupCol -= 1
    
    # Check for left
    dupRow = row
    dupCol = col
    while dupCol >= 0:
        if board[dupRow][dupCol] == 'Q':
            return False
        dupCol -= 1
    
    # Check for lower diag to left
    dupRow = row
    dupCol = col
    while dupRow < len(board) and dupCol >= 0:
        if board[dupRow][dupCol] == 'Q':
            return False
        dupRow += 1
        dupCol -= 1
    return True

def nQueens(board, col, count):
    # Base Case
    if col == len(board):
        count[0] += 1
        printQueens(board)
        return
    
    # Row Loop
    for row in range(len(board)):
        if isSafe(board, row, col):
            board[row][col] = 'Q'
            nQueens(board, col+1, count)
            board[row][col] = 'x'

def solveNQueens(n):
    count = [0]
    board = [['x'] * n for _ in range(n)]
    nQueens(board, 0, count)
    
    if count[0] == 0:
        print("No solution exists for this board size.")
    else:
        print(f'Total Possible Ways: {count[0]}')

n = int(input('Enter n: '))
solveNQueens(n)
