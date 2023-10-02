# O(n^2) time
def longestDistinct(string):
    n = len(string)
    res = 0

    for i in range(n):
        visited = [False] * 256
        for j in range(i, n):
            if visited[ord(string[j])]:
                break
            else:
                res = max(res, j - i + 1)
                visited[ord(string[j])] = True

    return res

print(longestDistinct("geeksforgeeks"))

# O(n) time | O(min(n, a)) space
def longestDistinct2(string):
    lastSeen = {}
    longest = [0, 1]
    startIdx = 0
    for i, char in enumerate(string):
        if char in lastSeen:
            startIdx = max(startIdx, lastSeen[char] + 1)
        if longest[1] - longest[0] < i + 1 - startIdx:
            longest = [startIdx, i + 1]
        lastSeen[char] = i
    return string[longest[0] : longest[1]]

print(longestDistinct2("geeksforgeeks"))
