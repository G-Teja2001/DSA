input_string = "Hello, World!"
# 0 - 127
char_frequency = [0] * 128

for char in input_string:
    if 0 <= ord(char) < 128:
        char_frequency[ord(char)] += 1

for i in range(128):
    if char_frequency[i] > 0:
        print(f"'{chr(i)}' occurs {char_frequency[i]} times")
