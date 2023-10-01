def is_subsequence(str1, str2):
    i, j = 0, 0

    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            i += 1
        j += 1
    return i == len(str1)

string1 = "abc"
string2 = "ahbgdc"

if is_subsequence(string1, string2):
    print(f"'{string1}' is a subsequence of '{string2}'")
else:
    print(f"'{string1}' is not a subsequence of '{string2}'")
