# O(n^2) time | O(1) space
def approach1(string):
    for idx in range(len(string)):
        foundDuplicate = False
        for idx2 in range(len(string)):
            if string[idx] == string[idx2] and idx != idx2:
                foundDuplicate = True

        if not foundDuplicate:
            return idx

    return -1

print(approach1('hh'))


# O(n) time | O(1)
def approach2(string):
    CHAR = 256
    visited = [0] * CHAR
    
    for i in range(len(string) - 1, -1, -1):
        visited[ord(string[i])] += 1

    for i in range(len(string)):
        if visited[ord(string[i])] == 1:
            return i

    return -1

# O(n) time | O(1) space - where n is the length of the input string
# The constant space is because the input string only has lowercase
# English-alphabet letters; thus, our hash table will never have more
# than 26 character frequencies.

def firstNonRepeatingCharacter(string):
    characterFrequencies = {}

    for character in string:
        characterFrequencies[character] = characterFrequencies.get(character, 0) + 1
    
    for idx in range(len(string)):
        character = string[idx]
        if characterFrequencies[character] == 1:
            return idx

    return -1

# def approach3(string):
#     CHAR = 256
#     visited = [False] * CHAR
#     res = -1
    
#     for i in range(len(string) - 1, -1, -1):
#         if visited[ord(string[i])]:
#             if string[i] == string[res]:
#                 res = -1
#         else:
#             res = i
#             visited[ord(string[i])] = True
    
#     return res

# this approach wont work as we keep assigning the new res
# which wont be keeping track if the chars appear next to it


# because it can incorrectly reset the res value 
# when the non-repeating characters appear next to each other. 

# hha -> 2 this wont be possible