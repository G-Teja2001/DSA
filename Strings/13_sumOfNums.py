def sumOfNums(string):
    current_number = ""
    total_sum = 0

    for char in string:
        if char.isdigit():
            current_number += char
        elif current_number:
            total_sum += int(current_number)
            current_number = ""
    
    if current_number:
        total_sum += int(current_number)

    return total_sum

string = "g4g"
result = sumOfNums(string)
print(result)