arr = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

def isValidSubsequence(arr, sequence):
    seqIndex = 0
    for value in arr:
        if seqIndex == len(sequence):
            break
        if sequence[seqIndex] == value:
            seqIndex += 1
    return seqIndex == len(sequence)

print(isValidSubsequence(arr, sequence))