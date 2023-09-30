# WAP To Which Makes Array [1,2,3,4,5] and While BackTracking
# Decrease Every Item in Array By 2
# O(2n), O(n)
def changeArr(arr, i, val):
    # Base Case
    if i == len(arr):
        print(arr)
        return
    # Recursion
    arr[i] = val
    # Fn Call Step.
    changeArr(arr, i+1, val+1)
    # BackTracking Step.
    arr[i] = arr[i] - 2

arr = [0]*5
changeArr(arr, 0, 1)
print(arr)