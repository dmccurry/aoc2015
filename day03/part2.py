inputFile = open("input", "r")
data = inputFile.read()
s_x = 0
s_y = 0
r_x = 0
r_y = 0
i = 0
house_map = {}
num_houses = 0

house_map[str(0) + "," + str(0)] = 2
num_houses = num_houses + 1

for c in data:
    if i % 2 == 0:
        if c == "^": 
            s_y = s_y - 1
        if c == "v":
            s_y = s_y + 1
        if c == "<":
            s_x = s_x - 1
        if c == ">":
            s_x = s_x + 1
        x = s_x
        y = s_y
    else:
        if c == "^": 
            r_y = r_y - 1
        if c == "v":
            r_y = r_y + 1
        if c == "<":
            r_x = r_x - 1
        if c == ">":
            r_x = r_x + 1
        x = r_x
        y = r_y

    key = str(x) + "," + str(y)
    if key in house_map:
        house_map[key] = house_map[key] + 1
    else:
        house_map[key] = 1
        num_houses = num_houses + 1
    i = i + 1

print("Solution is " + str(num_houses))