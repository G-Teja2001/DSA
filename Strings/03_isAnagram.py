# Naive
def approach1(str1, str2):
    return sorted(str1) == sorted(str2)

# Better
def approach2(s1, s2):
    CHAR = 128
    if len(s1) != len(s2):
        return False

    count1 = [0] * CHAR
    count2 = [0] * CHAR

    for i in range(len(s1)):
        count1[ord(s1[i])] += 1
        count2[ord(s2[i])] += 1
    
    for i in range(CHAR):
        if count1[i] != count2[i]:
            return False
    return True

# Optimal
def approach3(s1, s2):
    # Use 256 if Unicode Encoding
    CHAR = 128
    if len(s1) != len(s2):
        return False
    
    count = [0] * CHAR
    
    for i in range(len(s1)):
        count[ord(s1[i])] += 1
        count[ord(s2[i])] -= 1
    
    for i in count:
        if i != 0:
            return False
    return True

def approach4(s1, s2):
    # If they mention only lower case
    CHAR = 26
    if len(s1) != len(s2):
        return False
    
    count = [0] * CHAR
    
    for i in range(len(s1)):
        count[ord(s1[i]) - ord('a')] += 1
        count[ord(s2[i]) - ord('a')] -= 1
    
    for i in count:
        if i != 0:
            return False
    return True

print(approach1('silent', 'listen'))
print(approach2('aab', 'bab'))
print(approach4('silent', 'listen'))