import re
input_file = open("input", "r")
[replacements_block, medicine] = input_file.read().split("\n\n")

num = len(re.findall('([A-Z])', medicine))
num_y = len(re.findall('(Y)', medicine))
num_around = len(re.findall('(Ar|Rn)', medicine))

print(num)
print(num_y)
print(num_around)

print(num - num_around - (2 * num_y) - 1)