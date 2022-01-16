target = 33100000

presents = {}

for i in range(1, target // 10):
    sum = 0
    visits = 0
    for j in range(i, target // 10, i):
        if visits < 50:
            if (j in presents) == False:
                presents[j] = 11
            presents[j] = presents[j] + (i * 11) 
            visits = visits + 1

minhouse = target

for i in presents:
    if presents[i] > target and i < minhouse:
        minhouse = i

print(minhouse)