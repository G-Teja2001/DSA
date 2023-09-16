arr = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

seqIndex = 0
for item in arr:
    if seqIndex == len(sequence):
        break
    if sequence[seqIndex] == item:
        seqIndex += 1

if seqIndex == len(sequence):
    print(True)
else:
    print(False)