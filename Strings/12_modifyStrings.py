def modifyStrings(s1, s2):
    set1 = set(s1)
    set2 = set(s2)

    common_chars = set1.intersection(set2)
    
    uncommon_chars_s1 = ''.join(char for char in s1 if char not in common_chars)
    uncommon_chars_s2 = ''.join(char for char in s2 if char not in common_chars)
    
    if not uncommon_chars_s1 and not uncommon_chars_s2:
        return -1
    
    result = uncommon_chars_s1 + uncommon_chars_s2

    return result

# Example usage:
s1 = "aacdb"
s2 = "gafd"
output = modifyStrings(s1, s2)
print(output)