# Find num of subsets which are start and end with 1
# O(n^2)
def approach1(str):
    count = 0
    for i in range(len(str)):
        if str[i] == '0':
            continue
        else:
            for j in range(i+1, len(str)):
                if str[j] == '1':
                    count += 1

    return count

print(approach1('00100101'))

# O(n)
def approach2(s):
    ones_count = 0
    count = 0
    for char in s:
        if char == '1':
            ones_count += 1
            # For each '1', there are ones_count - 1 
            # valid subsets that start and end with '1'
            count += ones_count - 1
    return count

print(approach2('00011'))

# O(n)
def approach3(s):
    count = s.count('1')
    return (count * (count-1))//2

print(approach3('00100101'))
