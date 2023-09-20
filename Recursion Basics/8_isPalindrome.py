# O(n, n)
def isPalindrome(str, start, end):
    if start >= end:
        return True
    
    if str[start] != str[end]:
        return False
    
    return isPalindrome(str, start+1, end-1)

str = 'ababa'
print(isPalindrome(str, 0, len(str)-1))
