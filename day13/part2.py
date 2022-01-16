from itertools import permutations

def get_happiness(table, happiness):
    total_happiness = 0
    for i in range(0, len(table)):
        middle = table[i]
        if i == len(table) - 1:
            right = table[0]
        else:
            right = table[i+1]
        if i == 0:
            left = table[len(table) - 1]
        else:
            left = table[i-1]

        total_happiness = total_happiness + happiness[middle][left] + happiness[middle][right]
    return total_happiness

input_file = open("input", "r")

names = set()
happiness = {}

for line in input_file:
    parts = line.split(" ")
    first = parts[0]
    gain_or_lose = parts[2]
    amount = int(parts[3])
    last = parts[10].replace(".", "").strip()
    gain = 1
    if gain_or_lose == "lose":
        gain = -1

    names.add(first)
    names.add(last)

    if (first in happiness) == False:
        happiness[first] = {}
    happiness[first][last] = gain * amount

happiness["Me"] = {}
for name in names:
    happiness["Me"][name] = 0
    happiness[name]["Me"] = 0

names.add("Me")

max_happiness = 0
for tables in permutations(names):
    this_happiness = get_happiness(tables, happiness)
    if this_happiness > max_happiness:
        max_happiness = this_happiness

print(max_happiness)