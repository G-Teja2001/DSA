# O -> Depends on all of these params
# O(3^n)
"""
    Given a rope of length N meters, and the rope can be cut in only 3 sizes A, B and C. 
    The task is to maximizes the number of cuts in rope. 
    If it is impossible to make cut then print the number else print -1.
"""

def maxPieces(n, a, b, c):
    if n == 0:
        return 0
    if n < 0:
        return -1
    
    res = max(
        maxPieces(n-a, a, b, c),
        maxPieces(n-b, a, b, c),
        maxPieces(n-c, a, b, c),
    )

    if res == -1:
        return -1
    
    return res + 1

print(maxPieces(5, 2, 5, 1))