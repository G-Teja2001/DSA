def fun(index, arr, target, dataStructure):
    if index == len(arr):
        if target == 0:
            print(dataStructure)
        return
    
    if arr[index] <= target:
        dataStructure.append(arr[index])
        fun(index, arr, target-arr[index], dataStructure)
        dataStructure.pop()
    
    fun(index+1, arr, target, dataStructure)

fun(0, [2, 3, 6, 7], 7, [])
