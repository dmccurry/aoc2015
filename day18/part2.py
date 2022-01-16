input_file = open("input", "r")

def count(lights):
    c = 0
    for i in range(0, len(lights)):
        c = c + sum(lights[i])
    return c

def iter(lights):
    new_lights = []

    for i in range(0, len(lights)):
        new_row = []
        for j in range(0, len(lights[i])):
            neighbors = 0 
            if i > 0: 
                if j > 0: 
                    neighbors = neighbors + lights[i-1][j-1]
                neighbors = neighbors + lights[i-1][j]
                if j < len(lights[i]) - 1:
                    neighbors = neighbors + lights[i-1][j+1]
            if j > 0:
                neighbors = neighbors + lights[i][j-1]
            if j < len(lights[i]) - 1:
                neighbors = neighbors + lights[i][j+1]
            if i < len(lights) - 1:
                if j > 0: 
                    neighbors = neighbors + lights[i+1][j-1]
                neighbors = neighbors + lights[i+1][j]
                if j < len(lights[i]) - 1:
                    neighbors = neighbors + lights[i+1][j+1]
        
            if (i == 0 and j == 0) or (i == len(lights) - 1 and j == len(lights[i]) - 1) or (i == 0 and j == len(lights[i]) - 1) or (j == 0 and i == len(lights) - 1):
                new_row.append(1)
            elif lights[i][j] == 1 and (neighbors == 2 or neighbors == 3):
                new_row.append(1)
            elif lights[i][j] == 0 and neighbors == 3:
                new_row.append(1)
            else:
                new_row.append(0)
        new_lights.append(new_row)
    return new_lights

lights = []

for line in input_file:
    line = line.strip()
    row = []
    for char in line:
        if char == '#':
            row.append(1)
        else:
            row.append(0)
    lights.append(row)

n_iterations = 100

for i in range(0, n_iterations):
    lights = iter(lights)

print(count(lights))

