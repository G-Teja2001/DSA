nums = [10, 12, 20, 4]

def secondLargest(nums):
    if len(nums) < 2:
        return None
    _1Max = -float('inf')
    _2Max = -float('inf')

    for i in nums:
        if i > _1Max:
            _2Max = _1Max
            _1Max = i
        elif i > _2Max and i != _1Max:
            _2Max = i
    
    if _2Max == -float('inf'):
        # [1, 1, 1, 1]
        print('There is no second largest.')
    else:
        print(_2Max)

secondLargest(nums)
