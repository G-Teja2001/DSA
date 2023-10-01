# O(n^2, n)
def approach1(str1, str2):
    if len(str1) != len(str2):
        return False
    n = len(str1)
    dummyStr = str1

    for i in range(n):
        if dummyStr[i:] + dummyStr[:i] == str2:
            return True
    return False

print(approach1('geeksforgeeks', 'sgeeksforgeek'))

# Can be implemented through kmp algo..
