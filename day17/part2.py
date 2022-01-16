from itertools import combinations
target = 150
num = 0
input_file = open("input", "r")

nums = []
for line in input_file:
    nums.append(int(line.strip()))

lens = {}
for i in range(0, len(nums)):
    for n in combinations(nums, i):
        if sum(n) == target:
            name = len(list(n))
            if (name in lens) == False:
                lens[name] = 0
            lens[name] = lens[name] + 1

print(lens)