input_file = open("input", "r")
[replacements_block, start] = input_file.read().split("\n\n")
replacements = replacements_block.split('\n')

new_stuff = set()

for replacement in replacements:
    [left, right] = replacement.split(' => ')
    left = left.strip()
    right = right.strip()

    for i in range(0, len(start)):
        new_sub = start[i::]
        if new_sub.startswith(left):
            new_stuff.add(start[0:i:] + start[i::].replace(left, right, 1))
print(len(new_stuff))
