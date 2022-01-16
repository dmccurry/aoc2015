inputFile = open("input", "r")
data = inputFile.read()
x = 0
y = 0
house_map = {}
num_houses = 0

house_map[str(x) + "," + str(y)] = 1
num_houses = num_houses + 1

for c in data:
    if c == "^": 
        y = y - 1
    if c == "v":
        y = y + 1
    if c == "<":
        x = x - 1
    if c == ">":
        x = x + 1

    key = str(x) + "," + str(y)
    if key in house_map:
        house_map[key] = house_map[key] + 1
    else:
        house_map[key] = 1
        num_houses = num_houses + 1

print("Solution is " + str(num_houses))