def approach1(string):
    CHAR = 256
    visited = [0] * CHAR

    for i in range(len(string) - 1, -1, -1):
        visited[ord(string[i])] += 1

    for i in range(len(string)):
        if visited[ord(string[i])] == 1:
            return i

    return -1

print(approach1('hh'))


# def approach2(string):
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