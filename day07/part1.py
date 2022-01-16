input_file = open("input", "r")
wires = {}

instructions = []
for line in input_file:
    instructions.append(line)


while len(instructions) > 0:
    new_instructions = []
    for instruction in instructions:
        [val, assign] = instruction.split(" -> ")
        assign = assign.strip()
        if (' ' in val) == False:
            if val.isnumeric() == True:
                wires[assign] = int(val)
            elif val in wires:
                wires[assign] = wires[val]
            else: 
                new_instructions.append(instruction)
        else:
            parts = val.split(" ")
            if parts[0] == "NOT":
                if parts[1].isnumeric() == True:
                    wires[assign] = ~parts[1] & 65535
                elif parts[1] in wires:
                    wires[assign] = ~wires[parts[1]] & 65535
                else: 
                    new_instructions.append(instruction)
            elif parts[1] == "AND":
                left = parts[0]
                right = parts[2]
                if left.isnumeric() == False and right.isnumeric() == False and left in wires and right in wires:
                    wires[assign] = wires[parts[0]] & wires[parts[2]]
                elif left.isnumeric() == False and left in wires and right.isnumeric() == True:
                    wires[assign] = wires[parts[0]] & int(right)
                elif right.isnumeric() == False and right in wires and left.isnumeric() == True:
                    wires[assign] = int(left) & wires[parts[2]]
                elif left.isnumeric() == True and right.isnumeric() == True:
                    wires[assign] = int(left) & int(right)
                else:
                    new_instructions.append(instruction)
            elif parts[1] == "OR" and parts[0] in wires and parts[2] in wires:
                left = parts[0]
                right = parts[2]
                if left.isnumeric() == False and right.isnumeric() == False and left in wires and right in wires:
                    wires[assign] = wires[parts[0]] | wires[parts[2]]
                elif left.isnumeric() == False and left in wires and right.isnumeric() == True:
                    wires[assign] = wires[parts[0]] | int(right)
                elif right.isnumeric() == False and right in wires and left.isnumeric() == True:
                    wires[assign] = int(left) | wires[parts[2]]
                elif left.isnumeric() == True and right.isnumeric() == True:
                    wires[assign] = int(left) | int(right)
                else:
                    new_instructions.append(instruction)
            elif parts[1] == "LSHIFT" and parts[0] in wires:
                wires[assign] = wires[parts[0]] << int(parts[2])
            elif parts[1] == "RSHIFT" and parts[0] in wires:
                wires[assign] = wires[parts[0]] >> int(parts[2])
            else:
                new_instructions.append(instruction)
    instructions = new_instructions

print("Solution is: " + str(wires["a"]))