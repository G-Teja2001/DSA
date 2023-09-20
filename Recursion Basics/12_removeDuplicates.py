def removeDups(str, i, newStr, charDict):
    if i == len(str):
        print(newStr)
        return
    
    if str[i] not in charDict:
        charDict[str[i]] = True
        newStr += str[i]

    removeDups(str, i + 1, newStr, charDict)

originalStr = 'asaa'
removeDups(originalStr, 0, '', {})
