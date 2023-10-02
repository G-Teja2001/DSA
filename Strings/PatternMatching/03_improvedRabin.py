def improvedRabin(string, pattern):
    d = 10
    n = len(string)
    m = len(pattern)
    
    patternHash = 0
    currHash = 0
    for i in range(m):
        patternHash = patternHash * d + ord(pattern[i])
        currHash = currHash * d + ord(string[i])
    
    for i in range(n - m + 1):
        if currHash == patternHash:
            match = True
            for j in range(m):
                if string[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                print(i, end=' ')
        
        if i < n - m:
            currHash = (d * (currHash - ord(string[i]) * (d ** (m - 1)))) + ord(string[i + m])

improvedRabin('ABABABCD', 'AB')

"""
using modulo q in the Rabin-Karp algorithm is essential for maintaining the efficiency and correctness of the algorithm 
while preventing hash value overflow and reducing the likelihood of hash collisions.
without mod we will get higher values which may cause overflow..
"""
def improvedRabinWithMod(string, pattern, q):
    d = 10
    n = len(string)
    m = len(pattern)
    
    h = pow(d, m - 1, q)

    patternHash = 0
    currHash = 0
    for i in range(m):
        patternHash = (patternHash * d + ord(pattern[i])) % q
        currHash = (currHash * d + ord(string[i])) % q
    
    for i in range(n - m + 1):
        if currHash == patternHash:
            match = True
            for j in range(m):
                if string[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                print(i, end=' ')
        
        if i < n - m:
            currHash = ((d * (currHash - ord(string[i]) * h)) + ord(string[i + m])) % q

print()
improvedRabinWithMod('ABABABCD', 'AB', 101)
