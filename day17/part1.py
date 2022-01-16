from itertools import combinations
target = 150
num = 0
input_file = open("input", "r")

nums = []
for line in input_file:
    nums.append(int(line.strip()))


for i in range(0, len(nums)):
    for n in combinations(nums, i):
        if sum(n) == target:
            num = num + 1

print(num)