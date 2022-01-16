input_file = open("input", "r")
a = 1
b = 0
instructions = []

for line in input_file:
    instructions.append(line.strip())


current_instruction = 0

while current_instruction >= 0 and current_instruction < len(instructions):
    i = instructions[current_instruction]
    in_parts = i.split(' ')
    ins = in_parts[0]
    reg = in_parts[1]

    if ins == 'hlf':
        if reg == 'a':
            a = a // 2
        elif reg == 'b':
            b = b // 2
        current_instruction += 1
    elif ins == 'tpl':
        if reg == 'a':
            a = a * 3
        elif reg == 'b':
            b = b * 3
        current_instruction += 1
    elif ins == 'inc':
        if reg == 'a':
            a = a + 1
        elif reg == 'b':
            b = b + 1
        current_instruction += 1
    elif ins == 'jmp':
        current_instruction += int(reg)
    elif ins == 'jie':
        offset = in_parts[2]
        if reg == 'a,' and a % 2 == 0:
            current_instruction += int(offset)
        elif reg == 'b,' and b % 2 == 0:
            current_instruction += int(offset)
        else:
            current_instruction += 1
    elif ins == 'jio':
        offset = in_parts[2]
        if reg == 'a,' and a == 1:
            current_instruction += int(offset)
        elif reg == 'b,' and b == 1:
            current_instruction += int(offset)
        else:
            current_instruction += 1

print (a)
print (b)