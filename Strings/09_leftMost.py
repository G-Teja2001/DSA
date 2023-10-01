def approach1(string):
    n = len(string)
    for i in range(n):
        for j in range(i, n):
            if string[i] == string[j]:
                return i
    return -1

def approach2(string):
    CHAR= 256
    charCount = [0]*CHAR
    n = len(string)

    for i in range(n):
        charCount[ord(string[i])] += 1
    
    for i in range(len(string)):
        if charCount[ord(string[i])] > 1:
            return i

    return -1

def approach3(string):
    CHAR = 256
    visited = [False] * CHAR
    res = -1
    
    for i in range(len(string) - 1, -1, -1):
        if visited[ord(string[i])]:
            res = i
        else:
            visited[ord(string[i])] = True
    
    return res

str = "geeksforgeeks"
print("Index of leftmost repeating character:")
print(approach3(str))
