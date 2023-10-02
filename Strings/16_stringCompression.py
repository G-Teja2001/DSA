# https://leetcode.com/problems/string-compression/

def compress(string):
    s = ''
    i = 0
    while i < len(string):
        count = 1
        while i < len(string) - 1 and string[i] == string[i + 1]:
            i += 1
            count += 1
        s += string[i]
        if count > 1:
            s += str(count)
        i += 1
    return s

print(compress('aaabbaaccd'))