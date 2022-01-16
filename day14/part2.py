input_file = open("input", "r")


def get_distance(reindeer, dur):
    total_time = reindeer[1] + reindeer[2]
    total_cycles = dur // total_time
    distance = total_cycles * reindeer[1] * reindeer[0]
    
    our_time = total_cycles * total_time
    if our_time + reindeer[1] < dur:
        distance = distance + (reindeer[0] * reindeer[1])
    else:
        distance = distance + ((dur - our_time) * reindeer[0])
    
    return distance

reindeer = {}

for line in input_file:
    parts = line.split(" ")
    name = parts[0]
    speed = int(parts[3])
    fly_time = int(parts[6])
    rest_time = int(parts[13])

    reindeer[name] = [speed, fly_time, rest_time, 0]


duration = 2503
distances = []

for i in range(0, duration):
    max_distance = 0
    max_deer = None
    for deer in reindeer:
        distance = get_distance(reindeer[deer], i+1)
        if distance > max_distance:
            max_distance = distance
            max_deer = deer
    reindeer[max_deer][3] = reindeer[max_deer][3] + 1
    
for deer in reindeer:
    print(deer + ": " + str(reindeer[deer][3]))
