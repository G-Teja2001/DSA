def next_permutation(arr):
    n = len(arr)
    index = -1
    # Find the first element from the right that is smaller than the next element
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            index = i
            break

    # If no such element is found, the entire list is in descending order,
    # and it's the last permutation. 
    # We return the first permutation.
    if index == -1:
        arr.reverse()
        return

    # Find the smallest element to the right of index, but greater than arr[index]
    for i in range(n - 1, index, -1):
        if arr[i] > arr[index]:
            arr[index], arr[i] = arr[i], arr[index]
            break

    # Reverse the portion of the list to the right of index
    left = index + 1
    right = n - 1
    reverse(arr, left, right)


def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
arr = [4, 3, 2, 1]
next_permutation(arr)
print(arr)
