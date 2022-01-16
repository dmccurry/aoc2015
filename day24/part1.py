from itertools import combinations
from sys import maxsize
input_file = open("input", "r")
numbers = []
foundSums = []
for line in input_file:
    numbers.append(int(line.strip()))

target = sum(numbers) // 3

print(target)

for i in range(2, len(numbers)):
    for items in combinations(numbers, i):
        if sum(items) == target:
            foundSums.append(items)

    if len(foundSums) > 0:
        break

minQE = maxsize
for sums in foundSums:
    s_l = list(sums)
    qe = 1
    for i in s_l:
        qe = qe * i
    if qe < minQE:
        minQE = qe

print(minQE)