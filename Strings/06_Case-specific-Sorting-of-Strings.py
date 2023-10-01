# https://practice.geeksforgeeks.org/problems/case-specific-sorting-of-strings4845/

def fun(string):
    upperCase = []
    lowerCase = []

    for i in string:
        if ord(i) >= 97 and ord(i) <= 123:
            lowerCase.append(i)
        else:
            upperCase.append(i)
    
    res = ''

    upperCase.sort()
    lowerCase.sort()
    
    lower_index, upper_index = 0, 0

    for i in string:
        if ord(i) >= 97 and ord(i) <= 123:
            res += lowerCase[lower_index]
            lower_index += 1
        else:
            res += upperCase[upper_index]
            upper_index += 1
    
    return res

print(fun('defRTSersUXI'))
