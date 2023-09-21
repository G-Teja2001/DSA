def generateSubsets(str, curr, index):
    if len(str) == index:
        print(curr)
        return
    """Two cases for every character
    (i) We consider the character
        as part of current subset
    (ii) We do not consider current
        character as part of current
        subset"""
    generateSubsets(str, curr, index+1)
    generateSubsets(str, curr + str[index], index+1)

generateSubsets('abc', '', 0)