input_file = open("input", "r")

matches = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

for line in input_file:
    parts = line.split(" ")
    num = int(parts[1].replace(":", ""))
    keys = []
    values = []
    for i in range(2, len(parts), 2):
        keys.append(parts[i].replace(":", ""))
        values.append(int(parts[i+1].replace(",", "").strip()))
    
    valid = True
    for i in range(0, len(keys)):
        if keys[i] == "cats" or keys[i] == "trees":
            if matches[keys[i]] >= values[i]:
                valid = False
        elif keys[i] == "pomeranians" or keys[i] == "goldfish":
            if matches[keys[i]] <= values[i]:
                valid = False
        elif matches[keys[i]] != values[i]:
            valid = False
    
    if valid == True:
        print(num)
        break