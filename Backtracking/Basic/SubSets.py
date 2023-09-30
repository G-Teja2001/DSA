# To find subsets of given string

# O(n*2^n, n)

def findSubsets(string, ans, i):
    # Base Case
    if i == len(string):
        print(ans)
        return
    # Yes Choice
    findSubsets(string, f'{ans}{string[i]}', i+1)
    # No Choice
    findSubsets(string, ans, i+1)

findSubsets('abc', '', 0)