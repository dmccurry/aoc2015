import re
lights = [[ 0 for x in range(1000)] for y in range(1000)]
num_on = 1000*1000
num_on = 0
input_file = open("input", "r")
for line in input_file:
    instruct = line.replace("\n", "")
    instruct = instruct.replace("turn ", "")
    instruct = instruct.replace("through ", "")
    [direction, start, end] = instruct.split(" ")

    [sX, sY] = start.split(",")
    [eX, eY] = end.split(",")
    sX = int(sX)
    sY = int(sY)
    eX = int(eX)
    eY = int(eY)
    for row in range(sX, eX+1):
        for col in range(sY, eY+1):
            if direction == "on":
                if lights[row][col] == 0:
                    num_on = num_on + 1
                lights[row][col] = 1
            elif direction == "off":
                if lights[row][col] == 1:
                    num_on = num_on - 1
                lights[row][col] = 0
            elif direction == "toggle":
                if lights[row][col] == 0:
                    num_on = num_on + 1
                    lights[row][col] = 1
                else:
                    num_on = num_on - 1
                    lights[row][col] = 0
            

print("Solution is " + str(num_on))