inputFile = open("input", "r")
data = inputFile.read()
floors = 0

for letter in data:
    if letter == "(":
        floors = floors + 1
    else:
        floors = floors - 1

print("Solution is " + str(floors))