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

    reindeer[name] = [speed, fly_time, rest_time]


duration = 2503
distances = []
for deer in reindeer:
    distance = get_distance(reindeer[deer], duration)
    distances.append(distance)
    print(deer + ": " + str(distance))

print(max(distances))