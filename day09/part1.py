from itertools import permutations

input_file = open("input", "r")
graph = {}
locations = []
    
allPaths = []
for line in input_file:
    [locs, distance] = line.split(" = ")
    [start, end] = locs.split(" to ")
    distance = int(distance)
    
    if (start in locations) == False:
        locations.append(start)
    if (end in locations) == False:
        locations.append(end)

    if (start in graph) == False:
        graph[start] = {}
    graph[start][end] = distance
        
    if (end in graph) == False:
        graph[end] = {}
    graph[end][start] = distance

shortest = 9999;
for maps in permutations(locations):
    dist = sum(map(lambda x, y: graph[x][y], maps[:-1], maps[1:]))
    if dist < shortest:
        shortest = dist
print("Solution is " + str(shortest))