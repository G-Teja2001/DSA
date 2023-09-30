def gridWays(i, j, n, m):
    if i == n-1 and j == m-1:
        return 1
    elif i == n or j == m:
        return 0
    
    way1 = gridWays(i+1, j, n, m)
    way2 = gridWays(i, j+1, n, m)

    return way1 + way2

print(gridWays(0, 0, 100, 3))