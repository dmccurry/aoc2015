target = 33100000

presents = {}

for i in range(1, target // 10):
    sum = 0
    for j in range(i, target // 10, i):
        if (j in presents) == False:
            presents[j] = 10
        presents[j] = presents[j] + (i * 10) 

minhouse = target

for i in presents:
    if presents[i] > target and i < minhouse:
        minhouse = i

print(minhouse)