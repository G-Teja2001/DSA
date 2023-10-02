def naiveRabin(string, pattern):
    n = len(string)
    m = len(pattern)

    # Computation of Pattern's Hash Val
    p = 0
    for i in pattern:
        p += ord(i)
    
    # PreCompute hash
    currHash = 0
    for i in range(m):
        currHash += ord(string[i])
    
    for i in range(n - m + 1):
        if currHash == p:
            match = True
            for j in range(m):
                if string[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                print(i, end=' ')
        
        if i < n-m:
            currHash = currHash - ord(string[i]) + ord(string[i + m])

naiveRabin('ABABABCD', 'AB')