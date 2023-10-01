# https://practice.geeksforgeeks.org/problems/check-if-a-string-is-isogram-or-not-1587115620/1

def isIsogram(string):
    seen = set()
    for char in string:
        if char in seen:
            return False
        seen.add(char)
    return True

print(isIsogram('geeks'))