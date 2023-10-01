def isIsomorphic(str1, str2):
    if len(str1) != len(str2):
        return False
    
    charMapStr1 = {}
    charMapStr2 = {}
    
    for i in range(len(str1)):
        if str1[i] in charMapStr1:
            if charMapStr1[str1[i]] != str2[i]:
                return False
        else:
            if str2[i] in charMapStr2:
                return False
            charMapStr1[str1[i]] = str2[i]
            charMapStr2[str2[i]] = str1[i]
    
    return True

print(isIsomorphic('aab', 'bba'))