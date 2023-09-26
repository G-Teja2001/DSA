heights = [4, 2, 0, 6, 3, 2, 5]

def func(heights):  
    n = len(heights)

    area = 0
    width = 1

    leftMax = [0] * n
    rightMax = [0] * n

    for i in range(n):
        leftMax[i] = max(heights[i], leftMax[i-1])

    i = n - 1
    while i >= 0:
        rightMax[i] = max(heights[i], rightMax[i+1]) if i < n - 1 else heights[i]
        i -= 1

    for i in range(n):
        waterLevel = min(leftMax[i], rightMax[i])
        barHeight = heights[i]

        waterTrapped = waterLevel - barHeight

        if waterTrapped < 0:
            waterTrapped = 0
        
        area += waterTrapped * width
    return area

print(func([2, 3]))